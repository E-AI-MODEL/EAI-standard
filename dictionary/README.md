# EAI Dictionary

*Concepts for AI, learning and professional practice* · Hans Visser / EAI

A bilingual (English/Dutch) vocabulary of 81 concepts that sit between education and technology. Some terms come from EAI. Others are common terms, included because positioning them between education and technology changes how they should be read.

> At this stage, which step must the learner personally give substantive meaning to in order to learn?
>
> *Aan welke stap moet de leerling in deze fase zelf inhoudelijke betekenis geven om tot leren te komen?*

- **Read it:** [English](en.md) · [Nederlands](nl.md)
- **Machine-readable source:** [`terms.yaml`](terms.yaml), validated against [`dictionary.schema.json`](dictionary.schema.json)

## Status

The dictionary is **non-normative**. It does not define the EAI Standard; [`standard/public-interface.yaml`](../standard/public-interface.yaml) does. Where a dictionary entry and a canonical definition differ, the canonical definition applies.

The dictionary is the source vocabulary for the [0.5 semantic alignment proposal](../proposals/0.5-semantic-alignment/). That proposal selects a small number of these concepts for possible canonical status (Core Learning Action, Task Density, Support–Replacement Boundary, Evidence-Function Shift and others). The rest remain reusable explanatory vocabulary unless conformance or interoperability requires canonical semantics.

Source: *EAI Dictionary* (EN) and *EAI Dictionary* (NL), concept editions of 20 September 2026.

## EAI Concept Positioning

Every entry has a position. The position says **where a meaning comes from and which side sets its boundary**. It is not a quality scale: the middle is not better.

| Position | Nederlands | Meaning |
|---|---|---|
| `education_native` | Onderwijs-eigen | Defined from learning and education. Technology is not needed to establish its meaning. |
| `education_led` | Onderwijsgestuurd | Connects education and technology, but the learning goal, learning process or educational intent determines its meaning and boundary. |
| `shared` | Gedeeld | Exists in the relation between human/educational and technical action. Both sides are needed. |
| `technology_led` | Technologiegestuurd | Starts from system behaviour or a technical property and gains educational meaning through its effect on people, thinking or learning. |
| `technology_native` | Technologie-eigen | Primarily describes a technical mechanism. Education is not needed to define it. |

The positions are defined in [`proposals/0.5-semantic-alignment/concept-positioning.yaml`](../proposals/0.5-semantic-alignment/concept-positioning.yaml) (`POS-01` to `POS-05`).

**One word, different constructs.** When one word refers to different human and technical constructs (agency, memory, reasoning, learning …), each meaning gets its own position instead of an average. Such entries have `meanings.human` and `meanings.system` instead of a single `definition`. *Shared* is something else: one construct that only exists in the relation between human and technical action.

## Labels

| Label | Meaning |
|---|---|
| `eai_term` | A term introduced by EAI. |
| `eai_formalisation` | An existing idea that EAI gives a precise, operational form. |
| `eai_meaning` | An existing term used with an EAI-specific meaning. |
| `common_term` | A common term, included because its position adds something. |

## Entry structure

Each entry in `terms.yaml` has:

- `id`: a stable snake_case identifier, used for links and references;
- `term`: the English and Dutch term. The Dutch term is the headword of the Dutch edition, which keeps some EAI terms in English (for example *Justification Mapping*);
- `nl_translation` (optional): the Dutch translation the Dutch edition gives next to such an English headword (for example *Verantwoordingsmapping*);
- `label` and `position`;
- `definition`, or `meanings.human` and `meanings.system` for split constructs;
- `why`: what becomes unclear if the distinction is not made;
- `distinction` (optional): how the term differs from a neighbouring term;
- `practical_use`: what to do with the term in practice;
- `related` (optional): ids of related entries;
- `eai_refs` (optional): pointers into the repository: `proposal_concepts` in the 0.5 proposal, `definitions` in [`standard/definitions.yaml`](../standard/definitions.yaml), and `identifiers` such as `EV-*`, `AIA-*` and `REM-*`.

The `eai_refs` were added when the dictionary was imported. They are navigation aids, not equivalence claims: a pointer from *Process Evidence* to `EV-14` says that the evidence type is where the concept shows up in the standard, not that the two are the same construct. They should be reviewed as part of the 0.5 work.

## Dutch sector terms

[`sector-terms.yaml`](sector-terms.yaml) records 13 terms the Dutch education sector already uses, such as *menselijke regie*, *professioneel oordeel*, *zelfstandige beheersing* and *zorgplicht*, and how each relates to EAI constructs. Each term has a scope:

| Scope | Meaning |
|---|---|
| `equivalent` | Same meaning as the referenced construct. |
| `broader` / `narrower` | Covers more or less than the referenced construct. Not a synonym. |
| `related` | Touches the construct but is not a translation of it. |
| `context_only` | A legal or institutional basis (for example *zorgplicht*, *menselijk toezicht*). It belongs in a context overlay and has no canonical EAI equivalent. |

This makes it possible to write Dutch guidance in the sector's own words without silently changing what the standard means. The table appears at the end of [nl.md](nl.md) and [en.md](en.md). CI checks that every reference exists.

## The EAI design sequence

**Process → Stage → Core Learning Action → AI contribution**

1. **Process**: what must the learner ultimately know or be able to do, and how does the learner get there?
2. **Stage**: where in that learning process is the learner now?
3. **Core Learning Action**: to which step must the learner personally give substantive meaning at this stage?
4. **AI contribution**: what exactly does AI do at that point?

Only then do we ask about Task Density: how much of that core action does AI carry out? The choice of tool, prompt, tutor or agent comes after that.

## Changing the dictionary

Edit `terms.yaml`, then regenerate the views:

```bash
python scripts/render_dictionary.py
```

CI checks that `terms.yaml` validates against the schema, that every `related` id and every `eai_refs` entry exists, that every position is defined in the positioning model, and that `en.md` and `nl.md` are up to date.
