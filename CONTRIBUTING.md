# Contributing to EAI Standard

EAI Standard is developed as an open candidate standard. Contributions are welcome from teachers, school leaders, researchers, developers, suppliers, architects and other parties working in education.

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
- evidence relevant to a normative choice.

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
10. supporting evidence where the proposal makes an empirical claim.

A proposal does not need to start with a complete solution. A well-described problem can be opened first for discussion.

## Open discussion

Substantive design questions should preferably be discussed in public issues before a breaking normative change is merged. This makes assumptions, alternatives and disagreement visible.

Discussion should distinguish between:

- **empirical claims**: claims about learning, behaviour, technology or implementation that require evidence;
- **normative choices**: design decisions about what the standard requires;
- **terminology choices**: decisions about labels and definitions;
- **implementation choices**: choices that belong in a product or adapter rather than the standard.

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

- documentation only;
- registries/adapters;
- optional schema fields;
- normative semantics;
- conformance behaviour.

Breaking normative changes require a changelog entry.

## Versioning

The repository uses semantic versioning:

- **patch**: clarification without semantic change;
- **minor**: backward-compatible additions;
- **major**: incompatible normative changes.

Before 1.0, breaking changes may occur in minor candidate releases, but they must remain explicit and traceable.

## Conduct

Contributions should focus on the content of proposals. Different educational models, pedagogical positions and technical approaches may coexist. The standard should only choose between them where interoperability or semantic consistency requires it.
