"""Generate a read-only browser index from the actual versioned repository sources."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
import yaml

REPO = "https://github.com/E-AI-MODEL/EAI-standard"
ROOT = Path(__file__).resolve().parent.parent


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def tag_for(version, commit):
    tag = "v" + version
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "refs/tags/" + tag + "^{commit}"],
        cwd=ROOT, text=True, capture_output=True,
    )
    if result.returncode:
        return None
    if result.stdout.strip() != commit:
        raise ValueError(f"Tag {tag} does not match the pinned commit")
    return tag


def version_data(version, commit, pinned, schema_paths):
    paths = set(git("ls-tree", "-r", "--name-only", commit).splitlines()) if pinned else {
        p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
        if p.is_file() and not any(k in p.relative_to(ROOT).parts for k in (".git", "_site", ".venv", "node_modules"))
    }

    def load(path):
        if path not in paths:
            return {}
        raw = git("show", f"{commit}:{path}") if pinned else (ROOT / path).read_text(encoding="utf-8")
        return yaml.safe_load(raw) or {}

    manifest = load("standard/public-interface.yaml")
    if manifest.get("standard_version") != version:
        raise ValueError(f"Portal source version mismatch: {version}")
    vocabulary = load("standard/definitions.yaml")["terms"]
    position_file = "standard/concept-positioning.yaml"
    positions = load(position_file).get("positions", [])
    position_status = "canonical"
    if not positions:
        position_file = "proposals/0.5-semantic-alignment/concept-positioning.yaml"
        positions = load(position_file).get("positions", [])
        position_status = "proposal"
    rules = load("standard/rules.yaml")["normative_rules"]
    dictionary = load("dictionary/terms.yaml")
    adapter_index = load("adapters/index.yaml")
    adapters = []
    for entry in adapter_index.get("adapters", []):
        path = "adapters/" + entry["path"]
        adapter = load(path)
        adapters.append({"index": entry, "path": path, "data": adapter})
    examples = []
    for path in sorted(paths):
        if path.startswith("examples/") and path.endswith(".yaml"):
            examples.append({"path": path, "data": load(path)})
    canonical_schema_paths = {
        str(Path(p).as_posix()).removeprefix("../")
        for p in manifest["canonical_artifacts"]["schemas"]
    }
    tags = tag_for(version, commit) if pinned else None
    return {
        "version": version,
        "commit": commit,
        "date": git("show", "-s", "--format=%cs", commit),
        "pinned": pinned,
        "tag": tags,
        "manifest": manifest,
        "definitions": vocabulary,
        "positions": positions,
        "position_source": position_file,
        "position_status": position_status,
        "relations": load("standard/relations.yaml").get("relations", []),
        "rules": rules,
        "executability": load("standard/rule-executability.yaml").get("rules", {}),
        "diagnostics": load("standard/diagnostics.yaml").get("diagnostics", []),
        "profiles": load("standard/conformance-profiles.yaml").get("profiles", []),
        "ai_actions": load("standard/ai-actions.yaml").get("ai_actions", []),
        "evidence_types": load("standard/evidence-types.yaml").get("evidence_types", []),
        "protection": load("standard/protection.yaml"),
        "dictionary": dictionary.get("entries", []),
        "sector_terms": load("dictionary/sector-terms.yaml").get("terms", []),
        "adapters": adapters,
        "examples": examples,
        "evidence_map": load("evidence/construct-map.yaml"),
        "claims": load("evidence/claims.yaml"),
        "sources": load("evidence/sources.yaml"),
        "fixtures": load("tests/conformance/machine-rule-fixtures.yaml").get("fixtures", []),
        "matrix": load("tests/conformance/machine-rule-matrix.yaml").get("machine_rules", []),
        "schemas": [
            {"path": path, "title": load(path).get("title", Path(path).stem),
             "canonical": path in canonical_schema_paths,
             "url": f"releases/{version}/{path}"}
            for path in sorted(schema_paths)
        ],
        "files": sorted(p for p in paths if not p.startswith(".") and p.endswith((".md", ".yaml", ".json"))),
    }


def build_portal(site, current_version, snapshots, schema_collections):
    """The browser reads one generated index, not a separately maintained database."""
    versions = {}
    for version, schemas in schema_collections.items():
        pinned = version in snapshots
        commit = snapshots.get(version, git("rev-parse", "HEAD"))
        versions[version] = version_data(version, commit, pinned, schemas.keys())
        for schema in versions[version]["schemas"]:
            if not (site / schema["url"]).is_file():
                raise ValueError("Portal schema URL missing: " + schema["url"])
    payload = {"current": current_version, "repository": REPO,
               "build_commit": git("rev-parse", "HEAD"), "versions": versions}
    (site / "portal-data.json").write_text(
        json.dumps(payload, ensure_ascii=False, default=str, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    from shutil import copy2
    for name in ("index.html", "portal.css", "portal.js"):
        copy2(ROOT / "portal" / name, site / name)
    print(f"Built portal for {len(versions)} source versions.")
