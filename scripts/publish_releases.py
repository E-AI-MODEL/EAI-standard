"""Publish immutable candidate tags from the same pin map as the schema site.

Run only in the main-branch release job after validation. Never move a tag.
"""
import json
import os
import re
import subprocess
from build_schema_site import ROOT, VERSION, SHA
from build_portal import git, tag_for
import yaml


def run(*args):
    subprocess.run(args, cwd=ROOT, check=True)


def main():
    if os.environ.get("GITHUB_REF") != "refs/heads/main":
        raise ValueError("Release publication is restricted to main")
    pins = json.loads((ROOT / "schema-snapshots.json").read_text())
    run("git", "fetch", "--tags", "origin")
    run("git", "config", "user.name", "github-actions[bot]")
    run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    for version, commit in sorted(pins.items()):
        if not VERSION.fullmatch(version) or not SHA.fullmatch(commit):
            raise ValueError(f"Invalid release pin: {version}")
        run("git", "merge-base", "--is-ancestor", commit, "HEAD")
        if yaml.safe_load(git("show", f"{commit}:standard/public-interface.yaml"))["standard_version"] != version:
            raise ValueError(f"Incorrect source version: {version}")
        tag = "v" + version
        if not tag_for(version, commit):
            run("git", "tag", "-a", tag, commit, "-m", "EAI Standard " + version)
            run("git", "push", "origin", "refs/tags/" + tag)
        # Fetch again and verify the actual remote tag after any creation.
        run("git", "fetch", "--tags", "origin")
        if tag_for(version, commit) != tag:
            raise ValueError(f"Release tag missing: {tag}")
        repo = os.environ["GITHUB_REPOSITORY"]
        existing = subprocess.run(["gh", "release", "view", tag, "--repo", repo, "--json", "tagName,isPrerelease,isDraft"], capture_output=True, text=True)
        if existing.returncode:
            match = re.search(r"^## " + re.escape(version) + r"[^\n]*\n([\s\S]*?)(?=^## |\Z)", changelog, re.M)
            notes = f"Candidate specification (pre-1.0). Source commit: {commit}. This release does not certify implementations or educational effectiveness.\n\n"
            if match:
                notes += match.group(1).strip()
            run("gh", "release", "create", tag, "--repo", repo, "--verify-tag", "--prerelease",
                "--title", "EAI Standard " + version, "--notes", notes)
        info = json.loads(subprocess.check_output(["gh", "release", "view", tag, "--repo", repo, "--json", "tagName,isPrerelease,isDraft"], text=True))
        if info != {"tagName": tag, "isPrerelease": True, "isDraft": False}:
            raise ValueError(f"Unexpected release metadata: {info}")
        print(f"Verified release {tag} at {commit}")


if __name__ == "__main__":
    main()
