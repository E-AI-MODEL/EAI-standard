#!/usr/bin/env python3
"""Render dictionary/terms.yaml and dictionary/sector-terms.yaml into readable Markdown views (EN and NL).

Usage:
  python scripts/render_dictionary.py          # write dictionary/en.md and dictionary/nl.md
  python scripts/render_dictionary.py --check  # fail if the views are out of date

Non-normative tooling. terms.yaml is the source; the .md files are generated.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "dictionary" / "terms.yaml"
SECTOR_SOURCE = ROOT / "dictionary" / "sector-terms.yaml"
SCOPE = {
    "en": {"equivalent": "equivalent", "broader": "broader", "narrower": "narrower", "related": "related",
           "context_only": "context only (legal or institutional basis)"},
    "nl": {"equivalent": "gelijk", "broader": "breder", "narrower": "smaller", "related": "verwant",
           "context_only": "alleen context (juridische of institutionele grondslag)"},
}

POSITION = {
    "en": {
        "education_native": "Education-native", "education_led": "Education-led", "shared": "Shared",
        "technology_led": "Technology-led", "technology_native": "Technology-native",
    },
    "nl": {
        "education_native": "Onderwijs-eigen", "education_led": "Onderwijsgestuurd", "shared": "Gedeeld",
        "technology_led": "Technologiegestuurd", "technology_native": "Technologie-eigen",
    },
}
LABEL = {
    "en": {"eai_term": "EAI term", "eai_formalisation": "EAI formalisation", "eai_meaning": "EAI meaning", "common_term": "common term"},
    "nl": {"eai_term": "EAI-term", "eai_formalisation": "EAI-formalisering", "eai_meaning": "EAI-betekenis", "common_term": "algemeen begrip"},
}
TEXT = {
    "en": dict(
        title="EAI Dictionary",
        subtitle="Concepts for AI, learning and professional practice",
        other="Nederlandse versie: [nl.md](nl.md)",
        human="Human", system="System", why="Why", distinction="Distinction", use="Practical use",
        related="Related", refs="EAI references", overview="Overview", term="Term", label="Label",
        position="Position", entries="Entries",
        sector="Dutch sector terms", sector_term="Dutch term", scope="Scope", refers="Refers to", note="Note",
        sector_intro=(
            "Terms the Dutch education sector already uses, and how they relate to EAI constructs. Source: "
            "[`sector-terms.yaml`](sector-terms.yaml). A broader or narrower term is not a synonym; see rule 6 of "
            "*Language versions* in [`GOVERNANCE.md`](../GOVERNANCE.md)."
        ),
        intro=(
            "This is a generated view of [`terms.yaml`](terms.yaml). It is **non-normative**: the canonical "
            "EAI Standard is defined by [`standard/public-interface.yaml`](../standard/public-interface.yaml). "
            "See [README.md](README.md) for status, positioning model and how the dictionary relates to the standard."
        ),
        question="At this stage, which step must the learner personally give substantive meaning to in order to learn?",
    ),
    "nl": dict(
        title="EAI Dictionary",
        subtitle="Begrippen voor AI, leren en professioneel handelen",
        other="English version: [en.md](en.md)",
        human="Mens", system="Systeem", why="Waarom", distinction="Onderscheid", use="Praktisch gebruik",
        related="Verwant", refs="EAI-verwijzingen", overview="Overzicht", term="Begrip", label="Label",
        position="Positie", entries="Begrippen",
        sector="Sectortermen", sector_term="Sectorterm", scope="Reikwijdte", refers="Verwijst naar", note="Toelichting",
        sector_intro=(
            "Woorden die het Nederlandse onderwijsveld al gebruikt, en hoe ze zich verhouden tot EAI-begrippen. Bron: "
            "[`sector-terms.yaml`](sector-terms.yaml). Een bredere of smallere term is geen synoniem; zie regel 6 van "
            "*Language versions* in [`GOVERNANCE.md`](../GOVERNANCE.md)."
        ),
        intro=(
            "Dit is een gegenereerde weergave van [`terms.yaml`](terms.yaml). De dictionary is **niet normatief**: "
            "de canonieke EAI Standard wordt bepaald door [`standard/public-interface.yaml`](../standard/public-interface.yaml). "
            "Zie [README.md](README.md) voor status, positioneringsmodel en de relatie met de standaard."
        ),
        question="Aan welke stap moet de leerling in deze fase zelf inhoudelijke betekenis geven om tot leren te komen?",
    ),
}


def position_text(pos, lang):
    if isinstance(pos, dict):
        t = TEXT[lang]
        return f"{t['human']}: {POSITION[lang][pos['human']]} · {t['system']}: {POSITION[lang][pos['system']]}"
    return POSITION[lang][pos]


def render_sector_terms(sector, by_id, lang):
    t = TEXT[lang]
    out = [f"## {t['sector']}", "", t["sector_intro"], "",
           f"| {t['sector_term']} | {t['scope']} | {t['refers']} | {t['note']} |", "|---|---|---|---|"]
    for term in sorted(sector["terms"], key=lambda x: x["term_nl"].lower()):
        refs = []
        for kind, values in term["refs"].items():
            for v in values:
                if kind == "dictionary" and v in by_id:
                    refs.append(f"[{by_id[v]['term'][lang]}](#{v})")
                elif kind == "files":
                    refs.append(f"[`{v}`](../{v})")
                else:
                    refs.append(f"`{v}`")
        name = term["term_nl"] if lang == "nl" else f"{term['term_nl']} *({term['gloss_en']})*"
        note = term["note"][lang].replace("|", "\\|")
        out.append(f"| {name} | {SCOPE[lang][term['scope']]} | {'<br>'.join(refs)} | {note} |")
    return out + [""]


def render(data, lang, sector=None):
    t = TEXT[lang]
    entries = sorted(data["entries"], key=lambda e: e["term"][lang].lower())
    by_id = {e["id"]: e for e in data["entries"]}
    out = [
        f"<!-- Generated by scripts/render_dictionary.py from dictionary/terms.yaml. Do not edit by hand. -->",
        "",
        f"# {t['title']}",
        "",
        f"*{t['subtitle']}* · {data['author']}",
        "",
        f"Standard version: `{data['standard_version']}`",
        "",
        t["other"],
        "",
        t["intro"],
        "",
        f"> {t['question']}",
        "",
        f"## {t['overview']}",
        "",
        f"| {t['term']} | {t['label']} | {t['position']} |",
        "|---|---|---|",
    ]
    for e in entries:
        out.append(f"| [{e['term'][lang]}](#{e['id']}) | {LABEL[lang][e['label']]} | {position_text(e['position'], lang)} |")
    out += ["", f"## {t['entries']}", ""]
    for e in entries:
        heading = e["term"][lang]
        secondary = [e["term"]["en"] if lang == "nl" else e["term"]["nl"]]
        if e.get("nl_translation"):
            secondary.append(e["nl_translation"])
        secondary = [s for s in dict.fromkeys(secondary) if s != heading]
        if secondary:
            heading += " · " + " · ".join(f"*{s}*" for s in secondary)
        out += [f'<a id="{e["id"]}"></a>', f"### {heading}", "",
                f"**{position_text(e['position'], lang)}** · {LABEL[lang][e['label']]}", ""]
        if "definition" in e:
            out += [e["definition"][lang], ""]
        else:
            out += [f"- **{t['human']}:** {e['meanings']['human'][lang]}",
                    f"- **{t['system']}:** {e['meanings']['system'][lang]}", ""]
        out += [f"**{t['why']}.** {e['why'][lang]}", ""]
        if "distinction" in e:
            out += [f"**{t['distinction']}.** {e['distinction'][lang]}", ""]
        out += [f"**{t['use']}.** {e['practical_use'][lang]}", ""]
        if e.get("related"):
            links = " · ".join(
                f"[{by_id[r]['term'][lang]}](#{r})" if r in by_id else f"`{r}` (unknown)" for r in e["related"]
            )
            out += [f"{t['related']}: {links}", ""]
        refs = e.get("eai_refs") or {}
        flat = [f"`{x}`" for key in ("proposal_concepts", "definitions", "identifiers") for x in refs.get(key, [])]
        if flat:
            out += [f"{t['refs']}: {', '.join(flat)}", ""]
    if sector:
        out += render_sector_terms(sector, by_id, lang)
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    check = "--check" in sys.argv[1:]
    data = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    sector = yaml.safe_load(SECTOR_SOURCE.read_text(encoding="utf-8")) if SECTOR_SOURCE.exists() else None
    stale = []
    for lang in ("en", "nl"):
        target = ROOT / "dictionary" / f"{lang}.md"
        content = render(data, lang, sector)
        if check:
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                stale.append(target.relative_to(ROOT).as_posix())
        else:
            target.write_text(content, encoding="utf-8")
    if stale:
        print("Out of date: " + ", ".join(stale) + ". Run: python scripts/render_dictionary.py")
        return 1
    print("Dictionary views are up to date." if check else "Dictionary views written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
