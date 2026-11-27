#!/usr/bin/env python3
"""Execute the machine-rule fixtures against the candidate reference validator.

For every fixture in tests/conformance/machine-rule-fixtures.yaml this script
materialises the input (base artifact plus RFC 6902-style mutations), runs the
validator and compares schema validity, conformance, information_state and the
set of diagnostic codes with the fixture's expectation. It also enforces the
release gate in tests/conformance/machine-rule-matrix.yaml: every machine rule
must have executed positive and negative fixtures that pass.

Exit status 0 means every fixture passed. Use --report FILE to write a JSON
report of all runs.
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eai_validator import DEFAULT_ROOT, Canon, validate_case  # noqa: E402

FIXTURES = "tests/conformance/machine-rule-fixtures.yaml"
MATRIX = "tests/conformance/machine-rule-matrix.yaml"


def pointer(path: str) -> list[str]:
    if path == "":
        return []
    if not path.startswith("/"):
        raise ValueError(f"not a JSON Pointer: {path!r}")
    return [p.replace("~1", "/").replace("~0", "~") for p in path[1:].split("/")]


def apply(doc, mutation):
    parts = pointer(mutation["path"])
    if not parts:
        raise ValueError("mutating the document root is not supported")
    parent = doc
    for part in parts[:-1]:
        parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    last, op = parts[-1], mutation["op"]
    if isinstance(parent, list):
        index = len(parent) if last == "-" else int(last)
        if op == "add":
            if index > len(parent):
                raise IndexError(mutation["path"])
            parent.insert(index, copy.deepcopy(mutation["value"]))
        elif op == "replace":
            parent[index] = copy.deepcopy(mutation["value"])
        elif op == "remove":
            del parent[index]
        else:
            raise ValueError(f"unknown op {op!r}")
    else:
        if op == "add":
            parent[last] = copy.deepcopy(mutation["value"])
        elif op == "replace":
            if last not in parent:
                raise KeyError(mutation["path"])
            parent[last] = copy.deepcopy(mutation["value"])
        elif op == "remove":
            del parent[last]
        else:
            raise ValueError(f"unknown op {op!r}")


def run(root: Path):
    canon = Canon(root)
    suite = yaml.safe_load((root / FIXTURES).read_text(encoding="utf-8"))
    matrix = yaml.safe_load((root / MATRIX).read_text(encoding="utf-8"))
    runs, failures = [], []
    for fixture in suite["fixtures"]:
        case = copy.deepcopy(suite["base_artifact"])
        for mutation in fixture.get("mutations") or []:
            apply(case, mutation)
        schema_valid = not any(True for _ in canon.case_validator.iter_errors(case))
        output = validate_case(case, fixture["profile"], canon)
        expected = fixture["expected"]
        actual = {
            "schema_valid": schema_valid,
            "conformance": output["conformance"],
            "information_state": output["information_state"],
            "diagnostics": sorted({d["code"] for d in output["diagnostics"]}),
        }
        wanted = dict(expected, diagnostics=sorted(set(expected["diagnostics"])))
        mismatches = {k: {"expected": wanted[k], "actual": actual[k]} for k in wanted if wanted[k] != actual[k]}
        runs.append({"fixture": fixture["id"], "rule": fixture["rule"], "profile": fixture["profile"],
                     "passed": not mismatches, "mismatches": mismatches, "result": output})
        if mismatches:
            failures.append(f"{fixture['id']}: {json.dumps(mismatches)}")

    passed = {r["fixture"] for r in runs if r["passed"]}
    machine = {r for r, c in canon.executability.items() if c == "machine"}
    rows = {row["rule"]: row for row in matrix["machine_rules"]}
    if set(rows) != machine:
        failures.append(f"matrix rules {sorted(rows)} differ from machine rules {sorted(machine)}")
    for rule in sorted(machine & set(rows)):
        for key in ("positive_fixture", "negative_fixture", "unknown_fixture"):
            fid = rows[rule][key]
            if key == "unknown_fixture" and fid == "not_applicable":
                continue
            if fid not in passed:
                failures.append(f"release gate: {rule} {key} {fid} did not pass")
    return runs, failures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", default=str(DEFAULT_ROOT))
    parser.add_argument("--report", help="write a JSON report to this file")
    args = parser.parse_args(argv)
    runs, failures = run(Path(args.root))
    if args.report:
        Path(args.report).write_text(json.dumps({"runs": runs, "failures": failures}, indent=2,
                                                ensure_ascii=False) + "\n", encoding="utf-8")
    for r in runs:
        print(f"[{'pass' if r['passed'] else 'FAIL'}] {r['fixture']:<22} {r['rule']} {r['profile']} "
              f"{r['result']['conformance']}/{r['result']['information_state']} "
              f"{','.join(d['code'] for d in r['result']['diagnostics']) or '-'}")
    if failures:
        print(f"\n{len(failures)} problem(s):")
        for f in failures:
            print("  - " + f)
        return 1
    print(f"\nReference validator: {len(runs)} fixtures passed; machine-rule release gate satisfied.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
