#!/usr/bin/env python3
"""Regression tests for validator behaviour that the canonical fixtures do not cover.

These tests belong to this implementation, not to the conformance suite. Each
starts from the canonical fixture base artifact.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eai_validator import DEFAULT_ROOT, Canon, validate_case  # noqa: E402

BASE = yaml.safe_load((DEFAULT_ROOT / "tests/conformance/machine-rule-fixtures.yaml")
                      .read_text(encoding="utf-8"))["base_artifact"]


def case(**changes):
    doc = copy.deepcopy(BASE)
    for key, value in changes.items():
        if value is None:
            doc.pop(key, None)
        else:
            doc[key] = value
    return doc


def codes(output):
    return sorted({d["code"] for d in output["diagnostics"]})


def test_each_missing_required_property_is_classified(canon):
    out = validate_case(case(goal=None, process_positions=None, primary_process_position=None), "CP-01", canon)
    assert codes(out) == ["EAI-D001", "EAI-D002"], codes(out)
    assert out["information_state"] == "incomplete"


def test_null_concept_position_is_an_explicit_unknown(canon):
    meanings = [{"id": "CM-1", "term": "memory", "meaning": "Learner later retrieves knowledge.",
                 "position_ref": None, "rationale": "Position not yet established."}]
    out = validate_case(case(concept_meanings=meanings), "CP-08", canon)
    assert codes(out) == ["EAI-D020"], codes(out)
    assert out["information_state"] == "contains_unknowns"
    assert {"path": "$.concept_meanings[0].position_ref"} in out["retained_unknowns"]


def test_null_action_kind_is_an_explicit_unknown(canon):
    doc = case()
    doc["actors"][0]["core_actions"][0]["action_kind"] = None
    out = validate_case(doc, "CP-08", canon)
    assert codes(out) == ["EAI-D020"], codes(out)


def test_empty_anchors_are_anchor_diagnostics(canon):
    cases = {
        "EAI-D001": case(goal=""),
        "EAI-D021": case(context=""),
    }
    no_actors = case()
    no_actors["actors"] = []
    no_actions = case()
    no_actions["actors"][0]["core_actions"] = []
    cases_list = list(cases.items()) + [("EAI-D021", no_actors), ("EAI-D021", no_actions)]
    for expected, doc in cases_list:
        out = validate_case(doc, "CP-01", canon)
        assert codes(out) == [expected], (expected, codes(out))
        assert out["information_state"] == "incomplete", (expected, out["information_state"])


def test_nested_protection_and_evidence_unknowns(canon):
    doc = case(evidence_items=[{"id": "E-1", "evidence_type": "EV-02", "observation": "Observed.",
                                "claim_types": ["none"], "source_actor": "unknown"}])
    doc["actors"][0]["core_actions"][0]["protection"] = {"dimensions": [{
        "requirement_id": "PRT-03", "status": "unknown", "bases": [{
            "type": "eai_normative_rule", "reference": "EAI-R007",
            "applicability": "unknown", "bindingness": "eai_normative"}]}]}
    out = validate_case(doc, "CP-07", canon)
    assert codes(out) == ["EAI-D020"], codes(out)
    assert out["information_state"] == "contains_unknowns"
    paths = {u["path"] for u in out["retained_unknowns"]}
    assert paths == {"$.evidence_items[0].source_actor",
                     "$.actors[0].core_actions[0].protection.dimensions[0].status",
                     "$.actors[0].core_actions[0].protection.dimensions[0].bases[0].applicability"}, paths


def test_malformed_identifiers_are_identifier_diagnostics(canon):
    doc = case(evidence_items=[{"id": "E-1", "evidence_type": "bogus", "observation": "Observed.",
                                "claim_types": ["none"]}])
    assert codes(validate_case(doc, "CP-01", canon)) == ["EAI-D026"]
    doc = case()
    doc["actors"][0]["core_actions"][0]["microstructures"][0]["ai_actions"] = ["bogus"]
    assert codes(validate_case(doc, "CP-02", canon)) == ["EAI-D026"]
    doc = case(concept_meanings=[{"id": "CM-1", "term": "memory", "meaning": "Storage.",
                                  "position_ref": "bogus", "rationale": "x"}])
    assert codes(validate_case(doc, "CP-08", canon)) == ["EAI-D026"]


def test_omitted_core_actions_is_an_anchor_gap(canon):
    doc = case()
    del doc["actors"][0]["core_actions"]
    out = validate_case(doc, "CP-01", canon)
    assert codes(out) == ["EAI-D021"], codes(out)
    assert out["information_state"] == "incomplete"


def test_protection_conclusion_without_basis(canon):
    def with_dimension(status):
        doc = case()
        doc["actors"][0]["core_actions"][0]["protection"] = {
            "dimensions": [{"requirement_id": "PRT-03", "status": status, "bases": []}]}
        return validate_case(doc, "CP-07", canon)
    required = with_dimension("required")
    assert codes(required) == ["EAI-D023"] and required["conformance"] == "non_conformant", codes(required)
    unknown = with_dimension("unknown")
    assert codes(unknown) == ["EAI-D020"] and unknown["conformance"] == "conformant", codes(unknown)
    delegable = with_dimension("delegable")
    assert codes(delegable) == [] and delegable["conformance"] == "conformant", codes(delegable)


def test_invalid_actor_is_an_anchor_gap(canon):
    for value in ("bogus", None):
        doc = case()
        doc["actors"][0]["actor"] = value
        out = validate_case(doc, "CP-01", canon)
        assert codes(out) == ["EAI-D021"], (value, codes(out))
        assert out["information_state"] == "incomplete"


def test_scope_reports_where_evaluation_stopped(canon):
    full = validate_case(case(), "CP-01", canon)["extensions"][0]["data"]
    assert full["evaluation_completed"] is True and full["stopped_at"] is None
    invalid = validate_case(case(claim_type="bogus"), "CP-01", canon)
    data = invalid["extensions"][0]["data"]
    assert data["evaluation_completed"] is False and data["stopped_at"] == "schema_validation"
    assert codes(invalid) == ["refval:schema_invalid"], codes(invalid)
    version = validate_case(case(standard_version="0.4.0-candidate"), "CP-01", canon)["extensions"][0]["data"]
    assert version["stopped_at"] == "standard_version"


def test_example_cases_do_not_contradict_expectations(canon):
    """The validator must not add a diagnostic the canonical example expectations rule out.

    Hybrid diagnostics in the expectations are not produced (the validator does
    not decide hybrid rules). EAI-D020 is tolerated because four expectations
    omit it despite contains_unknowns (README, open question 6).
    """
    for listing in sorted((DEFAULT_ROOT / "tests/conformance").glob("*-cases.yaml")):
        for entry in yaml.safe_load(listing.read_text(encoding="utf-8"))["cases"]:
            path = (listing.parent / entry["case"]).resolve()
            out = validate_case(yaml.safe_load(path.read_text(encoding="utf-8")), "CP-07", canon)
            extra = set(codes(out)) - set(entry["expected_diagnostics"]) - {"EAI-D020"}
            assert not extra, (path.name, sorted(extra))
            assert out["information_state"] == entry["expected_information_state"], (
                path.name, out["information_state"])


def main():
    canon = Canon(DEFAULT_ROOT)
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for test in tests:
        try:
            test(canon)
            print(f"[pass] {test.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"[FAIL] {test.__name__}: {exc}")
    print(f"\n{len(tests) - failed} of {len(tests)} self-tests passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
