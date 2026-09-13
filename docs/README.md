# EAI Standard documentation

This directory contains human-readable documentation for the candidate standard. Unless a document is explicitly listed in `standard/public-interface.yaml`, documentation is explanatory and does not override canonical semantics.

## Read in this order

1. [`00-overview.md`](00-overview.md) — what the standard is for.
2. [`01-scope.md`](01-scope.md) — what is inside and outside scope.
3. [`02-core-concepts.md`](02-core-concepts.md) — core human action, microstructures, AI action, evidence and related concepts.
4. [`03-conformance.md`](03-conformance.md) — conformance profiles, information state and diagnostics.
5. [`04-use-cases.md`](04-use-cases.md) — interoperability use cases.
6. [`06-actor-profiles-and-skills.md`](06-actor-profiles-and-skills.md) — teacher/professional and learner action registries.
7. [`07-core-action-analysis.md`](07-core-action-analysis.md) — analysing human-AI allocation at action level.
8. [`08-evidence-handback-remediation.md`](08-evidence-handback-remediation.md) — evidence, handback and renewed human performance.
9. [`09-human-system-boundary.md`](09-human-system-boundary.md) — distinction between technical system functionality and human constructs.

## Standardisation and implementation

- [`06-architecture.md`](06-architecture.md) — repository and interoperability architecture.
- [`07-extensions-and-diagnostics.md`](07-extensions-and-diagnostics.md) — extensions and diagnostic behaviour.
- [`10-standard-publication-model.md`](10-standard-publication-model.md) — specification, machine contracts, conformance and implementation guidance.
- [`11-versioning-and-identifiers.md`](11-versioning-and-identifiers.md) — version and identifier strategy.
- [`12-conformance-suite.md`](12-conformance-suite.md) — requirements for executable conformance testing and the future reference validator.
- [`05-edustandaard-readiness.md`](05-edustandaard-readiness.md) — development path toward possible Edustandaard registration.

## Canonical sources

The authoritative public-interface manifest is:

- [`../standard/public-interface.yaml`](../standard/public-interface.yaml)

The main canonical machine-readable artifacts live under `../standard/` and `../schemas/` as listed in that manifest.

## Evidence

Scientific evidence and claim mappings live under `../evidence/`. Evidence informs standard design but is not itself the normative standard.

## Adapters and examples

Source-preserving mappings to educational models live under `../adapters/`. Worked cases live under `../examples/`. Both are intended to test and demonstrate the standard without redefining it.
