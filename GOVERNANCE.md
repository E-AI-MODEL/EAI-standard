# Governance

EAI Standard is developed and maintained as a public, inspectable candidate standard.

The governance model is designed to support open standardisation, balanced stakeholder participation, transparent change management and sustainable maintenance.

## Canonical material

The canonical normative layer lives in:

- `standard/definitions.yaml`
- `standard/rules.yaml`
- normative JSON Schemas under `schemas/`

Documentation explains the standard but does not override normative definitions or rules.

Registries and adapters are versioned extensions. They may grow without changing the meaning of the core standard.

## Roles

During the candidate phase the following roles are distinguished, even where one person temporarily fulfils more than one role:

- **maintainers**: manage releases, repository quality and merge decisions;
- **editors**: prepare normative text, schemas and documentation;
- **domain reviewers**: review educational, pedagogical and professional semantics;
- **implementation reviewers**: test whether the specification can be implemented consistently;
- **architecture reviewers**: assess interoperability, information modelling and alignment with sector architecture;
- **contributors**: propose issues, examples, adapters, evidence or changes;
- **users**: apply the standard in educational or technical settings and provide implementation feedback.

Before a stable 1.0 release, maintenance must no longer depend on a single individual.

## Open process

Normative development should be observable through the public repository.

Substantive proposals should normally be discussed through public issues and pull requests. A proposal that changes normative semantics should state:

- the problem being solved;
- the relevant use case;
- affected definitions or rules;
- examples before and after the change;
- compatibility impact;
- effect on teacher/professional and learner cases;
- effect on model adapters, registries and schemas;
- alternatives considered;
- evidence where empirical claims are made.

Decisions should be traceable to the proposal or discussion that motivated them.

## Decision making

During the candidate phase maintainers make merge and release decisions after public review where practical.

A normative change should be accepted because it improves semantic clarity, interoperability, implementation quality or educational applicability. It should not be accepted only because one stakeholder prefers a particular instructional model, product or technology.

Substantial changes should seek review from more than one stakeholder role. Disagreement should be recorded where it affects interpretation or future compatibility.

Before 1.0, a more formal multi-party decision model must be established and documented.

## Stakeholder balance

Development should actively seek input from both users and implementers. Relevant perspectives include:

- teachers and other education professionals;
- learners or learner representatives where appropriate;
- education organisations;
- suppliers and developers;
- educational researchers and domain experts;
- information architects and interoperability experts;
- public and sector organisations.

Participation does not imply endorsement of every normative choice.

## Change classes

### Patch

Clarifications, spelling corrections, non-semantic examples and documentation repairs.

### Minor

Backward-compatible additions such as new registry items, evidence types, adapters or optional fields.

### Major

Changes to the meaning of core terms, required fields, normative rules or conformance behaviour.

Before 1.0, breaking changes may still occur in candidate releases, but they must be explicit and recorded in `CHANGELOG.md`.

## Evidence and normative choices

Scientific or external evidence may inform the standard, but evidence sources and normative design choices remain distinguishable.

A source does not become a rule merely because it is cited. A normative rule must not be presented as empirically validated unless supporting evidence warrants that claim.

## Implementations and feedback

The standard should be tested in more than one implementation context before 1.0. Implementation experience should be documented sufficiently to show:

- where interpretation differed;
- which fields or rules were difficult to apply;
- whether independent implementations produced compatible representations;
- what changed as a result of the test.

## Maintenance and lifecycle

Stable releases require a documented lifecycle covering:

- ownership and maintenance responsibility;
- release cadence;
- backwards compatibility;
- deprecation;
- migration guidance;
- issue handling;
- security or urgent corrections where applicable;
- archival of superseded versions.

The candidate phase may use a lighter process, but the target is sustainable open maintenance rather than repository ownership by a single author.

## Candidate status

Before 1.0, definitions and structures may still change. Candidate releases should prefer semantic clarity over premature stability where the two conflict.

The development process is guided by the five Edustandaard assessment themes: added value, support/adoption, open standardisation, architectural alignment and future sustainability. See `docs/05-edustandaard-readiness.md`.
