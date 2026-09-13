# Governance

The EAI Standard is versioned as a public, inspectable specification.

## Canonical material

The canonical normative layer lives in:

- `standard/definitions.yaml`
- `standard/rules.yaml`
- normative JSON Schemas under `schemas/`

Documentation explains the standard but does not override normative definitions or rules.

Registries and adapters are versioned extensions. They may grow without changing the meaning of the core standard.

## Change classes

### Patch

Clarifications, spelling corrections, non-semantic examples and documentation repairs.

### Minor

Backward-compatible additions such as new registry items, evidence types, adapters or optional fields.

### Major

Changes to the meaning of core terms, required fields, normative rules or conformance behaviour.

## Proposed changes

A proposal that changes normative semantics should state:

- the problem being solved;
- affected definitions or rules;
- examples before and after the change;
- compatibility impact;
- effect on teacher/professional and learner cases;
- effect on model adapters and registries.

## Evidence and normative choices

Scientific or external evidence may inform the standard, but evidence sources and normative design choices should remain distinguishable. A source does not become a rule merely because it is cited, and a normative rule should not be presented as empirically validated without evidence supporting that claim.

## Candidate status

Before 1.0, definitions and structures may still change. Candidate releases should prefer semantic clarity over backward compatibility where the two conflict, with all breaking changes recorded in `CHANGELOG.md`.
