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


def test_scope_reports_where_evaluation_stopped(canon):
    full = validate_case(case(), "CP-01", canon)["extensions"][0]["data"]
    assert full["evaluation_completed"] is True and full["stopped_at"] is None
    invalid = validate_case(case(claim_type="bogus"), "CP-01", canon)
    data = invalid["extensions"][0]["data"]
    assert data["evaluation_completed"] is False and data["stopped_at"] == "schema_validation"
    assert codes(invalid) == ["refval:schema_invalid"], codes(invalid)
    version = validate_case(case(standard_version="0.4.0-candidate"), "CP-01", canon)["extensions"][0]["data"]
    assert version["stopped_at"] == "standard_version"


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
