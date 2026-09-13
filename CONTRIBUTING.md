# Contributing to EAI Standard

EAI Standard is developed as an open candidate standard. Contributions are welcome from teachers, school leaders, researchers, developers, suppliers, architects and other parties working in education.

## Canonical boundary

Before proposing a change, check `standard/public-interface.yaml`. It is the authoritative manifest of canonical EAI Standard artifacts.

Registries, adapters, context overlays, evidence, system profiles, examples, documentation and implementations may support or instantiate the standard, but they do not become normative merely because they are useful or widely used.

## Language and source terminology

English is the default language for canonical semantics, public documentation, registries and implementation guidance.

Original-language terminology must be preserved where it belongs to an external source model, publication, proper name or official framework. A source-preserving adapter therefore keeps the exact source label even when the surrounding EAI documentation and interpretation are in English.

Translations and localised presentation layers are welcome, but they must not silently redefine canonical meaning. A translation is a view of the same semantics, not a separate standard.

## What can be proposed

Contributions may concern:

- clarification of a definition;
- a new or revised normative rule;
- a skill or microstructure;
- an AI action or evidence type;
- a remediation pattern;
- a model adapter;
- a context profile;
- an example or conformance case;
- a schema or validation improvement;
- evidence relevant to a normative choice;
- an identifier, conformance or versioning improvement.

## Before proposing a normative change

A normative proposal should describe:

1. the problem;
2. the concrete use case;
3. the affected actor(s);
4. the current behaviour or definition;
5. the proposed change;
6. examples before and after the change;
7. compatibility impact;
8. impact on existing adapters, registries and schemas;
9. known alternatives;
10. supporting evidence where the proposal makes an empirical claim;
11. whether the proposal changes meaning or only presentation.

A proposal does not need to start with a complete solution. A well-described problem can be opened first for discussion.

## Semantic change versus presentation change

A different grouping, UI, table, diagram, file layout or human-readable view is not by itself a reason to alter canonical semantics.

A canonical change should address at least one real problem such as:

- two implementations could interpret the same field differently;
- a necessary distinction cannot currently be represented;
- a normative rule cannot be tested or exchanged consistently;
- an identifier or version has ambiguous meaning;
- an existing construct produces a demonstrable interoperability problem.

Presentation improvements should normally stay in documentation or implementation layers.

## Open discussion

Substantive design questions should preferably be discussed in public issues before a breaking normative change is merged. This makes assumptions, alternatives and disagreement visible.

Discussion should distinguish between:

- **empirical claims**: claims about learning, behaviour, technology or implementation that require evidence;
- **normative choices**: design decisions about what the standard requires;
- **terminology choices**: decisions about labels and definitions;
- **implementation choices**: choices that belong in a product or adapter rather than the standard;
- **presentation choices**: alternative human-readable views of unchanged semantics.

## Normative language

Canonical `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT` and `MAY` requirements follow BCP 14 as described in `standard/normative-language.md`.

Do not use capitalized requirement keywords casually in canonical artifacts. A `MUST` creates a conformance obligation.

## Decision principles

Changes are assessed on:

- semantic clarity;
- interoperability value;
- usefulness across more than one implementation;
- impact on teachers/professionals and learners;
- model neutrality;
- testability;
- backward compatibility;
- evidence quality for empirical claims;
- feasibility of sustainable maintenance.

Popularity alone is not sufficient reason for a normative change. A technically elegant proposal is also insufficient if it has no clear educational or interoperability use case.

## Stakeholder balance

The standard should not be shaped only by one role. Substantial releases should seek review from more than one stakeholder type, including users and implementers.

Relevant stakeholder roles include:

- teachers and other education professionals;
- learners or learner representatives where appropriate;
- education organisations;
- suppliers and developers;
- educational researchers and domain experts;
- information architects and interoperability experts;
- public-sector or sector organisations where relevant.

## Pull requests

Pull requests should be small enough to review and should identify whether they change:

- documentation/presentation only;
- registries/adapters;
- optional schema fields;
- canonical identifiers or versioning;
- normative semantics;
- conformance behaviour.

Breaking normative candidate changes require a changelog entry and, where existing implementations are affected, migration information and updated conformance fixtures.

## Versioning

`standard_version` is the version of the EAI Standard release. Other version fields such as `source_version`, `profile_version` or `artifact_version` have narrower meanings and must not be used interchangeably.

The repository uses semantic versioning:

- **patch**: clarification without semantic change;
- **minor**: backward-compatible additions;
- **major**: incompatible normative changes.

Before 1.0, breaking changes may occur in minor candidate releases, but they must remain explicit and traceable.

## Identifiers

Canonical identifier rules are defined in `standard/identifiers.yaml`. Do not reuse a canonical ID for a different meaning. Third-party additions should use their own namespace rather than imitate the reserved EAI identifier space.

Conformance outputs use canonical `CP-*` profile identifiers. Human-readable profile labels are descriptive and must not replace the stable identifier in exchanged conformance results.

## Conduct

Contributions should focus on the content of proposals. Different educational models, pedagogical positions and technical approaches may coexist. The standard should only choose between them where interoperability or semantic consistency requires it.
