# EAI Standard documentation

This directory contains human-readable documentation for the candidate standard. Unless a document is explicitly listed in `standard/public-interface.yaml`, documentation is explanatory and does not override canonical semantics.

## Read in this order

File names carry no numbers; the reading order is defined here.

1. [`overview.md`](overview.md) — what the standard is for.
2. [`scope.md`](scope.md) — what is inside and outside scope.
3. [`core-concepts.md`](core-concepts.md) — core human action, microstructures, AI action, evidence and protection.
4. [`conformance.md`](conformance.md) — conformance profiles, information state and diagnostics.
5. [`use-cases.md`](use-cases.md) — interoperability use cases.
6. [`actor-profiles-and-skills.md`](actor-profiles-and-skills.md) — registry-derived teacher/professional and learner actor views and skills.
7. [`core-action-analysis.md`](core-action-analysis.md) — analysing human-AI allocation at action level.
8. [`evidence-handback-remediation.md`](evidence-handback-remediation.md) — evidence, handback and renewed human performance.
9. [`human-system-boundary.md`](human-system-boundary.md) — distinction between technical system functionality and human constructs.
10. [`self-regulation-and-metacognition.md`](self-regulation-and-metacognition.md) — why visible task execution is not the same as learner regulation when AI selects routes, strategies or adjustments.
11. [`protection-assessment.md`](protection-assessment.md) — how EAI proposes what should remain human, evidenced or under human control using distinct scientific, legal, framework and institutional bases.

## Semantic alignment

- [`semantic-alignment.md`](semantic-alignment.md) explains the canonical concept positions and learner-specific analysis in 0.5.
- [`migration-0.4-to-0.5.md`](migration-0.4-to-0.5.md) describes the exchange contract and compatibility changes.

The original proposal is preserved for change provenance; the public-interface manifest identifies the current normative artifacts.

## Standardisation and implementation

- [`architecture.md`](architecture.md) — repository and interoperability architecture.
- [`extensions-and-diagnostics.md`](extensions-and-diagnostics.md) — extensions and diagnostic behaviour.
- [`standard-publication-model.md`](standard-publication-model.md) — specification, machine contracts, conformance and implementation guidance.
- [`versioning-and-identifiers.md`](versioning-and-identifiers.md) — version and identifier strategy.
- [`conformance-suite.md`](conformance-suite.md) — requirements for executable conformance testing and the future reference validator.
- [`validator-core-contract.md`](validator-core-contract.md) — framework-agnostic contract for a future validator core.
- [`migration-0.3-to-0.4.md`](migration-0.3-to-0.4.md) — migration of conformance serialization, diagnostics and version metadata.
- [`registry-coverage-audit.md`](registry-coverage-audit.md) — current depth of skill and microstructure coverage and the priority build order.
- [`edustandaard-readiness.md`](edustandaard-readiness.md) — development path toward possible Edustandaard registration.
- [Licence scope](../LICENSE-SCOPE.md) and [Apache-2.0 decision history](licensing-proposal.md).

## Canonical sources

The authoritative public-interface manifest is:

- [`../standard/public-interface.yaml`](../standard/public-interface.yaml)

The main canonical machine-readable artifacts live under `../standard/` and `../schemas/` as listed in that manifest.

## Evidence

Scientific evidence and claim mappings live under `../evidence/`. Evidence informs standard design but is not itself the normative standard. Candidate evidence-informed protection mappings are stored in `../evidence/protection-guidance.yaml` and remain non-binding scientific guidance unless a separate EAI or external binding basis applies.

## Context and jurisdiction overlays

Context overlays live under `../context/`. They may refine expectations or carry jurisdiction-specific requirements without redefining canonical EAI semantics. `../context/eu-regulatory-protection.yaml` provides the first candidate source-preserving mapping for selected EU AI Act and GDPR protection requirements.

## Registries

Reusable skills, microstructures and remediation patterns live under `../registries/`. The presence of a skill does not imply that it already has deep microstructure coverage. The initial audit is stored in `../registries/coverage/skill-microstructure-coverage.yaml`; accepted changes are tracked in `../registries/coverage/resolution-log.yaml`, and the current coverage position is stored in `../registries/coverage/current-status.yaml`.

## Adapters and examples

Source-preserving mappings to educational models live under `../adapters/`. Worked cases live under `../examples/`. Both are intended to test and demonstrate the standard without redefining it.
