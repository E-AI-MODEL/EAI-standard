#!/usr/bin/env python3
"""Repository consistency checks for the EAI Standard.

Non-normative tooling. This script is not a reference validator: it does not
evaluate EAI rules. It only checks that the machine-readable layer of the
repository is internally consistent:

1. every YAML and JSON file parses;
2. every JSON Schema is a valid Draft 2020-12 schema and its $refs resolve
   against the local schema files (no network access is used);
3. conformance result fixtures validate against conformance-result.schema.json;
4. machine-rule fixtures produce the expected schema validity after their
   JSON-Pointer mutations are applied to the base artifact;
5. example cases validate against case.schema.json;
6. the non-normative dictionary validates against its schema, and its
   related terms and EAI references point to things that exist.

Example cases that are known not to validate yet are listed in
tests/schema-migration-pending.txt. The check fails when an unlisted case is
invalid, and also when a listed case has become valid (so the list can only
shrink).

Usage: python scripts/validate.py
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError
from referencing import Registry, Resource
from referencing.exceptions import Unresolvable

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv"}
PENDING_FILE = ROOT / "tests" / "schema-migration-pending.txt"

# (glob, schema file) pairs for documents that must validate.
CASE_SCHEMA = "schemas/case.schema.json"
DOCUMENT_TARGETS = [
    ("examples/**/*.yaml", CASE_SCHEMA),
    ("system-profiles/examples/eai-extension-example.yaml", CASE_SCHEMA),
    ("system-profiles/examples/generic-agentic-llm.yaml", "system-profiles/system-profile.schema.json"),
    ("tests/conformance/*-result.json", "schemas/conformance-result.schema.json"),
    ("dictionary/terms.yaml", "dictionary/dictionary.schema.json"),
]
DICTIONARY_FILE = "dictionary/terms.yaml"
FIXTURES_FILE = "tests/conformance/machine-rule-fixtures.yaml"

errors: list[str] = []


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def iter_files(*suffixes: str):
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path.suffix in suffixes and not SKIP_DIRS.intersection(path.parts):
            yield path


def load(path: Path):
    text = path.read_text(encoding="utf-8")
    return json.loads(text) if path.suffix == ".json" else yaml.safe_load(text)


# ---------------------------------------------------------------- 1. parsing

def check_parsing() -> dict[Path, object]:
    docs: dict[Path, object] = {}
    for path in iter_files(".yaml", ".yml", ".json"):
        try:
            docs[path] = load(path)
        except (yaml.YAMLError, json.JSONDecodeError) as exc:
            first = str(exc).strip().splitlines()
            errors.append(f"parse: {rel(path)}: {' / '.join(first[:3])}")
    print(f"[parse] {len(docs)} files parsed")
    return docs


# ---------------------------------------------------------------- 2. schemas

def build_registry(docs: dict[Path, object]) -> tuple[Registry, dict[str, dict]]:
    registry = Registry()
    schemas: dict[str, dict] = {}
    for path, doc in docs.items():
        if path.suffix != ".json" or not path.name.endswith(".schema.json"):
            continue
        schemas[rel(path)] = doc
        try:
            Draft202012Validator.check_schema(doc)
        except SchemaError as exc:
            errors.append(f"schema: {rel(path)} is not a valid Draft 2020-12 schema: {exc.message}")
        if "$id" not in doc:
            errors.append(f"schema: {rel(path)} has no $id")
            continue
        registry = registry.with_resource(doc["$id"], Resource.from_contents(doc))
    return registry, schemas


def iter_refs(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "$ref" and isinstance(value, str):
                yield value
            else:
                yield from iter_refs(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_refs(item)


def check_refs(registry: Registry, schemas: dict[str, dict]) -> None:
    count = 0
    for name, schema in schemas.items():
        resolver = registry.resolver(base_uri=schema.get("$id", ""))
        for ref in iter_refs(schema):
            count += 1
            try:
                resolver.lookup(ref)
            except Unresolvable:
                errors.append(f"schema: {name}: $ref {ref!r} does not resolve to a local schema")
    print(f"[schemas] {len(schemas)} schemas checked, {count} $refs resolved locally")


def validator_for(schema_file: str, registry: Registry, schemas: dict[str, dict]) -> Draft202012Validator:
    return Draft202012Validator(schemas[schema_file], registry=registry)


def first_error(validator: Draft202012Validator, instance) -> str | None:
    errs = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    if not errs:
        return None
    err = errs[0]
    where = "/" + "/".join(str(p) for p in err.absolute_path)
    more = f" (+{len(errs) - 1} more)" if len(errs) > 1 else ""
    return f"{where}: {err.message}{more}"


# ---------------------------------------------------------- 3/5. documents

def load_pending() -> set[str]:
    if not PENDING_FILE.exists():
        return set()
    lines = PENDING_FILE.read_text(encoding="utf-8").splitlines()
    return {line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")}


def check_documents(docs, registry, schemas) -> None:
    pending = load_pending()
    seen_pending: set[str] = set()
    valid = invalid_pending = 0
    for pattern, schema_file in DOCUMENT_TARGETS:
        validator = validator_for(schema_file, registry, schemas)
        for path in sorted(ROOT.glob(pattern)):
            if path not in docs:
                continue  # parse error already reported
            name = rel(path)
            problem = first_error(validator, docs[path])
            if name in pending:
                seen_pending.add(name)
                if problem is None:
                    errors.append(
                        f"documents: {name} now validates against {schema_file}; "
                        f"remove it from {rel(PENDING_FILE)}"
                    )
                else:
                    invalid_pending += 1
            elif problem is None:
                valid += 1
            else:
                errors.append(f"documents: {name} does not validate against {schema_file}: {problem}")
    for name in sorted(pending - seen_pending):
        errors.append(f"documents: {rel(PENDING_FILE)} lists {name}, which is not a checked document")
    print(f"[documents] {valid} valid, {invalid_pending} known invalid pending migration")


# ---------------------------------------------------------------- 4. fixtures

def _pointer_parts(pointer: str) -> list[str]:
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ValueError(f"invalid JSON Pointer {pointer!r}")
    return [p.replace("~1", "/").replace("~0", "~") for p in pointer[1:].split("/")]


def _apply(doc, mutation):
    op, parts = mutation["op"], _pointer_parts(mutation["path"])
    if not parts:
        raise ValueError("mutations on the document root are not supported")
    parent = doc
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    last = parts[-1]
    if isinstance(parent, list):
        index = len(parent) if last == "-" else int(last)
        if op == "add":
            parent.insert(index, mutation["value"])
        elif op == "replace":
            parent[index] = mutation["value"]
        elif op == "remove":
            del parent[index]
        else:
            raise ValueError(f"unknown op {op!r}")
    else:
        if op in ("add", "replace"):
            if op == "replace" and last not in parent:
                raise KeyError(last)
            parent[last] = mutation["value"]
        elif op == "remove":
            del parent[last]
        else:
            raise ValueError(f"unknown op {op!r}")


def check_fixtures(docs, registry, schemas) -> None:
    path = ROOT / FIXTURES_FILE
    data = docs.get(path)
    if data is None:
        return
    validator = validator_for(CASE_SCHEMA, registry, schemas)
    checked = 0
    for fixture in data.get("fixtures", []):
        fid = fixture.get("id", "<no id>")
        artifact = copy.deepcopy(data["base_artifact"])
        try:
            for mutation in fixture.get("mutations") or []:
                _apply(artifact, mutation)
        except (KeyError, IndexError, ValueError, TypeError) as exc:
            errors.append(f"fixtures: {fid}: mutation cannot be applied: {exc!r}")
            continue
        expected = (fixture.get("expected") or {}).get("schema_valid")
        if expected is None:
            continue
        problem = first_error(validator, artifact)
        actual = problem is None
        checked += 1
        if actual != expected:
            detail = f" ({problem})" if problem else ""
            errors.append(f"fixtures: {fid}: expected schema_valid={expected}, got {actual}{detail}")
    print(f"[fixtures] {checked} machine-rule fixtures checked for schema validity")


# ---------------------------------------------------------------- 6. dictionary

def collect_ids(node, found: set[str]) -> None:
    if isinstance(node, dict):
        value = node.get("id")
        if isinstance(value, str):
            found.add(value)
        for child in node.values():
            collect_ids(child, found)
    elif isinstance(node, list):
        for child in node:
            collect_ids(child, found)


def check_dictionary(docs) -> None:
    data = docs.get(ROOT / DICTIONARY_FILE)
    if not isinstance(data, dict):
        return
    entries = data.get("entries") or []
    term_ids = [e.get("id") for e in entries]
    for dup in sorted({i for i in term_ids if term_ids.count(i) > 1}):
        errors.append(f"dictionary: duplicate id {dup}")
    known_terms = set(term_ids)

    known_ids: set[str] = set()
    for path, doc in docs.items():
        if rel(path).startswith(("standard/", "registries/")):
            collect_ids(doc, known_ids)
    definitions = set((docs.get(ROOT / "standard/definitions.yaml") or {}).get("terms", {}))
    proposal = docs.get(ROOT / "proposals/0.5-semantic-alignment/core-semantics.yaml") or {}
    proposal_concepts = set(proposal.get("concepts", {}))
    positioning = docs.get(ROOT / str(data.get("positioning_model", ""))) or {}
    positions = {p.get("label") for p in positioning.get("positions", [])}

    checked = 0
    for entry in entries:
        eid = entry.get("id")
        pos = entry.get("position")
        for value in (pos.values() if isinstance(pos, dict) else [pos]):
            if value not in positions:
                errors.append(f"dictionary: {eid}: position {value!r} is not defined in {data.get('positioning_model')}")
        for ref in entry.get("related", []):
            checked += 1
            if ref not in known_terms:
                errors.append(f"dictionary: {eid}: related term {ref!r} does not exist")
        refs = entry.get("eai_refs") or {}
        for kind, known in (("proposal_concepts", proposal_concepts), ("definitions", definitions), ("identifiers", known_ids)):
            for ref in refs.get(kind, []):
                checked += 1
                if ref not in known:
                    errors.append(f"dictionary: {eid}: {kind} reference {ref!r} does not exist")
    print(f"[dictionary] {len(entries)} entries, {checked} references checked")


def main() -> int:
    docs = check_parsing()
    registry, schemas = build_registry(docs)
    check_refs(registry, schemas)
    check_documents(docs, registry, schemas)
    check_fixtures(docs, registry, schemas)
    check_dictionary(docs)
    if errors:
        print(f"\n{len(errors)} problem(s) found:")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
