#!/usr/bin/env python3
"""Generate current and pinned version-specific schema views; validate all refs locally."""
from __future__ import annotations
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://e-ai-model.github.io/EAI-standard/"
VERSION = re.compile(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9.-]+)?")
SHA = re.compile(r"[0-9a-f]{40}")
FOLDERS = ("schemas", "system-profiles", "dictionary")


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def source_schemas(commit=None):
    if commit:
        paths = git("ls-tree", "-r", "--name-only", commit).splitlines()
        read = lambda p: git("show", f"{commit}:{p}")
    else:
        paths = [p.relative_to(ROOT).as_posix() for folder in FOLDERS
                 for p in (ROOT / folder).glob("*.schema.json")]
        read = lambda p: (ROOT / p).read_text(encoding="utf-8")
    schemas = {p: json.loads(read(p)) for p in sorted(paths)
               if len(Path(p).parts) == 2 and Path(p).parts[0] in FOLDERS
               and p.endswith(".schema.json")}
    if "schemas/case.schema.json" not in schemas:
        raise ValueError("Required schema source missing")
    for p, schema in schemas.items():
        if schema.get("$id") != BASE + p:
            raise ValueError(f"{p}: expected $id {BASE + p}")
    return schemas


def references(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("$ref", "$dynamicRef") and isinstance(value, str):
                yield value
            else:
                yield from references(value)
    elif isinstance(node, list):
        for value in node:
            yield from references(value)


def rewrite(node, prefix):
    if isinstance(node, dict):
        return {k: (prefix + v[len(BASE):]
                    if k in ("$id", "$ref", "$dynamicRef") and isinstance(v, str) and v.startswith(BASE)
                    else rewrite(v, prefix)) for k, v in node.items()}
    if isinstance(node, list):
        return [rewrite(v, prefix) for v in node]
    return node


def emit(site, schemas, subdir=""):
    prefix = BASE + subdir
    generated = {p: rewrite(s, prefix) for p, s in schemas.items()}
    registry = Registry()
    ids = set()
    for p, s in generated.items():
        Draft202012Validator.check_schema(s)
        sid = s.get("$id")
        if sid != prefix + p or sid in ids:
            raise ValueError(f"Duplicate or incorrect publication identifier: {sid}")
        ids.add(sid)
        registry = registry.with_resource(sid, Resource.from_contents(s))
    for p, s in generated.items():
        resolver = registry.resolver(base_uri=s["$id"])
        for ref in references(s):
            resolver.lookup(ref)
        target = site / subdir / p
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Validated {len(generated)} schemas at {prefix}")
    return [subdir + p for p in generated]


def main():
    manifest = yaml.safe_load((ROOT / "standard/public-interface.yaml").read_text(encoding="utf-8"))
    version = manifest["standard_version"]
    if not VERSION.fullmatch(version):
        raise ValueError(f"Invalid standard version: {version}")
    snapshots = json.loads((ROOT / "schema-snapshots.json").read_text(encoding="utf-8"))
    if not isinstance(snapshots, dict):
        raise ValueError("Snapshots must map versions to pinned commits")
    site = ROOT / "_site"
    if site.exists():
        shutil.rmtree(site)
    site.mkdir()
    notice_files = ("LICENSE", "NOTICE", "LICENSE-SCOPE.md")
    for name in notice_files:
        if not (ROOT / name).is_file():
            raise ValueError(f"Missing distribution notice: {name}")
        shutil.copy2(ROOT / name, site / name)
    current = source_schemas()
    links = emit(site, current)
    collections = {version: current}
    for release_version, commit in sorted(snapshots.items()):
        if not VERSION.fullmatch(release_version) or not isinstance(commit, str) or not SHA.fullmatch(commit):
            raise ValueError(f"Invalid snapshot entry: {release_version}")
        old_manifest = yaml.safe_load(git("show", f"{commit}:standard/public-interface.yaml"))
        if old_manifest.get("standard_version") != release_version:
            raise ValueError(f"Snapshot version mismatch: {release_version}")
        archived = source_schemas(commit)
        if release_version == version:
            if archived != current:
                raise ValueError("Pinned current schemas changed. Use a new standard version.")
            # Protect the released normative material, not the presentation code.
            for paths in manifest["canonical_artifacts"].values():
                for name in paths:
                    path = (ROOT / "standard" / name).resolve().relative_to(ROOT).as_posix()
                    if (ROOT / path).read_text(encoding="utf-8") != git("show", f"{commit}:{path}"):
                        raise ValueError(f"Pinned canonical artifact changed: {path}")
            old_public = git("show", f"{commit}:standard/public-interface.yaml")
            if (ROOT / "standard/public-interface.yaml").read_text(encoding="utf-8") != old_public:
                raise ValueError("Pinned canonical manifest changed")
        collections[release_version] = archived
    for release_version, schemas in collections.items():
        links += emit(site, schemas, f"releases/{release_version}/")
        release = site / "releases" / release_version
        for name in notice_files:
            shutil.copy2(ROOT / name, release / name)
    print(f"Included {len(notice_files)} licence and attribution files in each schema distribution.")
    # Preserve a plain index for tools and browsers without JavaScript.
    (site / "schema-index.html").write_text(
        '<!doctype html><html lang="en"><meta charset="utf-8"><title>EAI Standard schemas</title>'
        '<h1>EAI Standard schemas</h1><p>Current candidate: ' + html.escape(version) +
        '</p><p><a href="LICENSE">Apache-2.0</a> (<a href="LICENSE-SCOPE.md">scope</a>)</p><ul>' +
        "".join(f'<li><a href="{html.escape(p)}">{html.escape(p)}</a></li>' for p in links) +
        '</ul></html>', encoding="utf-8")
    from build_portal import build_portal
    build_portal(site, version, snapshots, collections)
    print(f"Built {len(links)} schema publication files.")


if __name__ == "__main__":
    main()
