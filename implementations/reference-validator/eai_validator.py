#!/usr/bin/env python3
"""Candidate reference validator for EAI Standard cases.

Status: candidate, not authoritative. See README.md for the gates that remain.

The validator follows the processing contract in docs/validator-core-contract.md:

1. load the canonical manifest and check the declared standard_version;
2. load the canonical vocabularies and schemas listed in that manifest;
3. validate the case against the canonical case schema;
4. resolve canonical identifiers and internal references;
5. evaluate the rules classified as ``machine`` in rule-executability.yaml;
6. report explicit unknowns without resolving them;
7. list the hybrid and human-review rules it did not evaluate;
8. determine conformance and information_state separately;
9. emit a result that validates against conformance-result.schema.json.

It reads only artifacts listed in standard/public-interface.yaml. It contains no
framework, jurisdiction, model-provider or LLM judgement.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

VALIDATOR_VERSION = "0.1.0-candidate"
NAMESPACE = "https://e-ai-model.github.io/EAI-standard/implementations/reference-validator"
DEFAULT_ROOT = Path(__file__).resolve().parents[2]

# Local diagnostic codes. They use this implementation's own namespace because
# the canonical diagnostics have no code for these conditions (see README.md).
LOCAL_SCHEMA_INVALID = "refval:schema_invalid"
LOCAL_UNSUPPORTED_VERSION = "refval:unsupported_standard_version"

# Diagnostics whose presence means a required anchor is missing, so the
# selected profile cannot be fully evaluated (information_state: incomplete).
ANCHOR_DIAGNOSTICS = {"EAI-D001", "EAI-D002", "EAI-D021"}

# Identifier shapes reserved by standard/identifiers.yaml. A failing schema
# pattern or enum on a value of this shape is a canonical identifier problem.
RESERVED_PREFIX = re.compile(r"^(EAI-[RD]|REL|AIA|EV|CP|TSK|LSK|AIS|MS|REM|PRT|POS|ADP)-")


class Canon:
    """Canonical artifacts of one standard version, loaded through the manifest."""

    def __init__(self, root: Path = DEFAULT_ROOT):
        self.root = Path(root)
        std = self.root / "standard"
        self.manifest = self._yaml(std / "public-interface.yaml")
        self.version = self.manifest["standard_version"]
        listed = {name for names in self.manifest["canonical_artifacts"].values() for name in names}

        def canonical(name):
            if name not in listed:
                raise ValueError(f"{name} is not listed in the canonical manifest")
            return self._yaml(std / name)

        self.diagnostics = {d["code"]: d for d in canonical("diagnostics.yaml")["diagnostics"]}
        self.rules = {r["id"] for r in canonical("rules.yaml")["normative_rules"]}
        self.executability = canonical("rule-executability.yaml")["rules"]
        self.profiles = {p["id"] for p in canonical("conformance-profiles.yaml")["profiles"]}
        self.ids = {
            "ai_action": {a["id"] for a in canonical("ai-actions.yaml")["ai_actions"]},
            "evidence_type": {e["id"] for e in canonical("evidence-types.yaml")["evidence_types"]},
            "protection_requirement": {p["id"] for p in canonical("protection.yaml")["requirements"]},
            "concept_position": {p["id"] for p in canonical("concept-positioning.yaml")["positions"]},
            "rule": self.rules,
        }

        schemas = {}
        for name in self.manifest["canonical_artifacts"]["schemas"]:
            schema = json.loads((std / name).resolve().read_text(encoding="utf-8"))
            schemas[schema["$id"]] = schema
        self.registry = Registry().with_resources(
            (sid, Resource.from_contents(s)) for sid, s in schemas.items())
        base = self.manifest_schema_id("case.schema.json")
        self.case_validator = Draft202012Validator(schemas[base], registry=self.registry)
        self.result_validator = Draft202012Validator(
            schemas[self.manifest_schema_id("conformance-result.schema.json")], registry=self.registry)

    def manifest_schema_id(self, filename):
        for name in self.manifest["canonical_artifacts"]["schemas"]:
            if name.endswith("/" + filename):
                schema = json.loads((self.root / "standard" / name).resolve().read_text(encoding="utf-8"))
                return schema["$id"]
        raise ValueError(f"{filename} is not a canonical schema")

    @staticmethod
    def _yaml(path):
        return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def json_path(parts) -> str:
    out = "$"
    for part in parts:
        out += f"[{part}]" if isinstance(part, int) else f".{part}"
    return out


def leaf_errors(error):
    """Expand oneOf/anyOf errors to the branch that applies.

    A ``oneOf: [X, {type: null}]`` failure on a non-null value is reported as
    the failure inside X, so an identifier error inside a protection
    assessment is not hidden behind a generic "not valid under any schema".
    """
    if not error.context:
        return [error]
    branches = {}
    for sub in error.context:
        branches.setdefault(sub.relative_schema_path[0], []).append(sub)
    alternatives = error.validator_value if isinstance(error.validator_value, list) else []
    kept = [subs for index, subs in branches.items()
            if not (index < len(alternatives) and alternatives[index] == {"type": "null"})]
    if len(kept) != 1:
        return [error]
    return [leaf for sub in kept[0] for leaf in leaf_errors(sub)]


def missing_property(error):
    match = re.match(r"^'(.+)' is a required property$", error.message)
    if match:
        return match.group(1)
    absent = [k for k in error.validator_value if isinstance(error.instance, dict) and k not in error.instance]
    return absent[0] if len(absent) == 1 else None


def classify_schema_error(error) -> str:
    """Map one schema failure to the smallest canonical diagnostic for it.

    This table is implementation logic, not canonical semantics: each entry
    names the rule whose representation boundary the schema enforces.
    """
    path = list(error.absolute_path)
    keys = [p for p in path if isinstance(p, str)]
    keyword = error.validator
    instance = error.instance

    if keyword == "required":
        # jsonschema emits one error per missing property but keeps the whole
        # required list in validator_value; classify this error's property only.
        missing = [missing_property(error)]
        if not path:
            if "goal" in missing:
                return "EAI-D001"
            if "process_positions" in missing:
                return "EAI-D002"
            if {"context", "actors"} & set(missing):
                return "EAI-D021"
        if keys[-1:] == ["core_actions"] or "process_position_refs" in missing or "actor" in missing:
            return "EAI-D021"
    # A present but empty or mistyped anchor is the same gap as a missing one.
    if keyword in ("minItems", "minLength", "type"):
        if keys == ["process_positions"]:
            return "EAI-D002"
        if keys == ["goal"]:
            return "EAI-D001"
        if keys in (["context"], ["actors"]) or keys[-1:] in (["core_actions"], ["process_position_refs"]):
            return "EAI-D021"
    if keyword in ("pattern", "enum", "const") and isinstance(instance, str) and RESERVED_PREFIX.match(instance):
        return "EAI-D026"
    if keyword == "additionalProperties" and isinstance(instance, dict) and "microstructures" in instance \
            and keys[-2:] != ["core_actions"] and keys[-1:] != ["core_actions"]:
        return "EAI-D022"
    if "extensions" in keys:
        return "EAI-D018"
    if "protection" in keys:
        return "EAI-D023"
    if keys[-1:] == ["action_kind"] and instance == "core_learning_action":
        return "EAI-D029"
    return LOCAL_SCHEMA_INVALID


class Result:
    def __init__(self, canon: Canon):
        self.canon = canon
        self.diagnostics = []

    def add(self, code, path, details=None, message=None):
        canonical = self.canon.diagnostics.get(code)
        if canonical:
            entry = {"code": code, "severity": canonical["severity"], "effect": canonical["effect"],
                     "message": " ".join(canonical["message"].split()),
                     "related_rule": canonical.get("related_rule")}
        else:
            entry = {"code": code, "severity": "error", "effect": "non_conformance",
                     "message": message or "Local validator diagnostic.", "related_rule": None}
        entry["path"] = path
        entry["details"] = details
        if not any(d["code"] == code and d["path"] == path for d in self.diagnostics):
            self.diagnostics.append(entry)


def check_schema(case, canon, result) -> bool:
    errors = sorted(canon.case_validator.iter_errors(case), key=lambda e: list(e.absolute_path))
    for error in errors:
        for leaf in leaf_errors(error):
            code = classify_schema_error(leaf)
            details = {"schema_keyword": leaf.validator, "schema_message": leaf.message[:300]}
            result.add(code, json_path(leaf.absolute_path), details,
                       message="The case does not validate against the canonical case schema.")
    return not errors


def iter_core_actions(case):
    for a, actor in enumerate(case.get("actors", [])):
        for c, action in enumerate(actor.get("core_actions", [])):
            yield ["actors", a, "core_actions", c], actor, action


def check_identifiers(case, canon, result):
    """EAI-R020: canonical exchange identifiers resolve in the declared version."""
    def resolve(value, cls, path):
        if value is not None and value not in canon.ids[cls]:
            result.add("EAI-D026", json_path(path), {"identifier": value, "identifier_class": cls})

    for path, _, action in iter_core_actions(case):
        for m, micro in enumerate(action.get("microstructures") or []):
            for i, aia in enumerate(micro.get("ai_actions") or []):
                resolve(aia, "ai_action", path + ["microstructures", m, "ai_actions", i])
        for d, dim in enumerate((action.get("protection") or {}).get("dimensions") or []):
            dpath = path + ["protection", "dimensions", d]
            resolve(dim.get("requirement_id"), "protection_requirement", dpath + ["requirement_id"])
            for b, basis in enumerate(dim.get("bases") or []):
                if basis.get("type") == "eai_normative_rule":
                    resolve(basis.get("reference"), "rule", dpath + ["bases", b, "reference"])
    for e, item in enumerate(case.get("evidence_items") or []):
        resolve(item.get("evidence_type"), "evidence_type", ["evidence_items", e, "evidence_type"])
    for m, meaning in enumerate(case.get("concept_meanings") or []):
        resolve(meaning.get("position_ref"), "concept_position", ["concept_meanings", m, "position_ref"])


def check_anchors(case, result):
    """EAI-R027: context, goal, actor and a resolving process position."""
    if not case.get("goal"):
        result.add("EAI-D001", "$.goal")
    if not case.get("process_positions"):
        result.add("EAI-D002", "$.process_positions")
    if not case.get("context"):
        result.add("EAI-D021", "$.context", {"missing_anchor": "context"})
    positions = {p.get("id") for p in case.get("process_positions") or []}
    for path, actor, action in iter_core_actions(case):
        if not actor.get("actor"):
            result.add("EAI-D021", json_path(path[:2] + ["actor"]), {"missing_anchor": "actor"})
        refs = action.get("process_position_refs") or []
        unresolved = [r for r in refs if r not in positions]
        if not refs or unresolved:
            result.add("EAI-D021", json_path(path + ["process_position_refs"]),
                       {"missing_anchor": "process_position", "unresolved_refs": unresolved})


def check_learning_action(case, result):
    """EAI-R034: core_learning_action only under a learner actor."""
    for path, actor, action in iter_core_actions(case):
        if action.get("action_kind") == "core_learning_action" and actor.get("actor") != "learner":
            result.add("EAI-D029", json_path(path + ["action_kind"]), {"actor": actor.get("actor")})


# Canonical enum fields whose value "unknown" is an explicit unknown marker,
# taken from the canonical schemas (case, protection assessment, evidence item,
# human control). Boolean nulls in human_control are not counted, because the
# schema does not define null there as preserved uncertainty.
UNKNOWN_ENUM_FIELDS = {
    "core_action": ("status",),
    "microstructure": ("human_execution",),
    "protection_dimension": ("status",),
    "protection_basis": ("applicability", "bindingness"),
    "evidence_item": ("source_actor", "independence"),
    "human_control": ("responsible_actor", "decision_authority", "information_available", "timing",
                      "effectiveness"),
}


def explicit_unknowns(case):
    """Paths of explicit unknown markers. They are reported, never resolved."""
    found = []

    def enum_unknowns(node, kind, path):
        for key in UNKNOWN_ENUM_FIELDS[kind]:
            if isinstance(node, dict) and node.get(key) == "unknown":
                found.append(json_path(path + [key]))

    found += [json_path(["unknowns", i]) for i, _ in enumerate(case.get("unknowns") or [])]
    for path, _, action in iter_core_actions(case):
        enum_unknowns(action, "core_action", path)
        if "action_kind" in action and action["action_kind"] is None:
            found.append(json_path(path + ["action_kind"]))
        for m, micro in enumerate(action.get("microstructures") or []):
            enum_unknowns(micro, "microstructure", path + ["microstructures", m])
        protection = action.get("protection") or {}
        for d, dim in enumerate(protection.get("dimensions") or []):
            dpath = path + ["protection", "dimensions", d]
            enum_unknowns(dim, "protection_dimension", dpath)
            for b, basis in enumerate(dim.get("bases") or []):
                enum_unknowns(basis, "protection_basis", dpath + ["bases", b])
        found += [json_path(path + ["protection", "unknowns", i])
                  for i, _ in enumerate(protection.get("unknowns") or [])]
    for e, item in enumerate(case.get("evidence_items") or []):
        enum_unknowns(item, "evidence_item", ["evidence_items", e])
    enum_unknowns(case.get("human_control"), "human_control", ["human_control"])
    for m, meaning in enumerate(case.get("concept_meanings") or []):
        for key in ("meaning", "position_ref"):
            if meaning.get(key) is None:
                found.append(json_path(["concept_meanings", m, key]))
    return found


def validate_case(case, profile, canon: Canon):
    if profile not in canon.profiles:
        raise ValueError(f"Unknown conformance profile: {profile}")
    result = Result(canon)
    case = copy.deepcopy(case)

    unknowns = []
    stopped_at = None
    declared = case.get("standard_version") if isinstance(case, dict) else None
    if declared != canon.version:
        result.add(LOCAL_UNSUPPORTED_VERSION, "$.standard_version",
                   {"declared": declared, "supported": canon.version},
                   message="The declared standard_version is not supported by this validator.")
        stopped_at = "standard_version"
    elif not check_schema(case, canon, result):
        stopped_at = "schema_validation"
    else:
        # Referential, machine-rule and unknown checks run only on schema-valid
        # input, so one missing prerequisite does not cascade into further
        # diagnostics (mutation_contract.diagnostic_rule in the fixtures).
        check_identifiers(case, canon, result)
        check_anchors(case, result)
        check_learning_action(case, result)
        unknowns = explicit_unknowns(case)
        if unknowns:
            result.add("EAI-D020", "$", {"explicit_unknowns": unknowns})

    codes = {d["code"] for d in result.diagnostics}
    conformance = "non_conformant" if any(d["effect"] == "non_conformance" for d in result.diagnostics) \
        else "conformant"
    if codes & ANCHOR_DIAGNOSTICS:
        information_state = "incomplete"
    elif any(d["effect"] == "uncertainty" for d in result.diagnostics):
        information_state = "contains_unknowns"
    else:
        information_state = "complete"

    machine = sorted(r for r, c in canon.executability.items() if c == "machine")
    output = {
        "profile": profile,
        "standard_version": canon.version,
        "conformance": conformance,
        "information_state": information_state,
        "diagnostics": result.diagnostics,
        "retained_unknowns": [{"path": p} for p in unknowns],
        "extensions": [{
            "namespace": NAMESPACE,
            "version": VALIDATOR_VERSION,
            "schema": None,
            "data": {
                "status": "candidate_not_authoritative",
                "machine_rules_supported": machine,
                "evaluation_completed": stopped_at is None,
                "stopped_at": stopped_at,
                "hybrid_rules_not_decided": sorted(r for r, c in canon.executability.items() if c == "hybrid"),
                "human_review_rules_not_decided": sorted(
                    r for r, c in canon.executability.items() if c == "human_review"),
                "note": "conformant covers the machine-evaluable part only; hybrid and human-review "
                        "rules need the supplied review input this validator does not create.",
            },
        }],
    }
    errors = list(canon.result_validator.iter_errors(output))
    if errors:
        raise AssertionError(f"validator produced an invalid result: {errors[0].message}")
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("case", help="case file (YAML or JSON)")
    parser.add_argument("--profile", required=True, help="conformance profile, e.g. CP-01")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="EAI Standard repository root")
    args = parser.parse_args(argv)
    canon = Canon(Path(args.root))
    case = yaml.safe_load(Path(args.case).read_text(encoding="utf-8"))
    output = validate_case(case, args.profile, canon)
    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    print()
    return 0 if output["conformance"] == "conformant" else 1


if __name__ == "__main__":
    sys.exit(main())
