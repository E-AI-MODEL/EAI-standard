#!/usr/bin/env python3
"""Regression test of the pinned 0.4 -> 0.5 example migration, not a reference validator."""
import json

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

from build_schema_site import ROOT, git, source_schemas


def validator(schemas):
    registry = Registry().with_resources(
        (s["$id"], Resource.from_contents(s)) for s in schemas.values()
    )
    return Draft202012Validator(schemas["schemas/case.schema.json"], registry=registry)


def main():
    snapshots = json.loads((ROOT / "schema-snapshots.json").read_text(encoding="utf-8"))
    commit = snapshots["0.4.0-candidate"]
    before = validator(source_schemas(commit))
    after = validator(source_schemas())
    paths = [p for p in git("ls-tree", "-r", "--name-only", commit).splitlines()
             if (p.startswith("examples/") and p.endswith(".yaml"))
             or p == "system-profiles/examples/eai-extension-example.yaml"]
    if not paths:
        raise ValueError("Missing predecessor examples")
    for path in paths:
        old = yaml.safe_load(git("show", f"{commit}:{path}"))
        new = yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))
        before.validate(old)
        after.validate(new)
        if new != dict(old, standard_version="0.5.0-candidate"):
            raise ValueError(f"Migration altered content other than standard_version: {path}")
        if after.is_valid(old):
            raise ValueError(f"0.5 schema unexpectedly accepts old version: {path}")
    print(f"[migration] {len(paths)} examples validated against both versions; only version changed")
    semantic = yaml.safe_load((ROOT / "examples/semantic-alignment/meaning-split-valid.yaml").read_text(encoding="utf-8"))
    after.validate(semantic)
    if before.is_valid(dict(semantic, standard_version="0.4.0-candidate")):
        raise ValueError("0.4 schema unexpectedly accepts 0.5 semantic fields")
    print("[migration] new 0.5 semantic fields are rejected by the pinned 0.4 schema")


if __name__ == "__main__":
    main()
