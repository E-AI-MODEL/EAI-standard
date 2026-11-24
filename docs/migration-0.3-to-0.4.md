# Migration from 0.3.x to 0.4.0-candidate

EAI Standard 0.4.0-candidate hardens standardisation mechanics. The substantive human-action model is not redesigned, but conformance serialization, canonical version metadata and the case exchange contract change.

## 1. Conformance result

### 0.3.x

```json
{
  "profile": "assessment_evidence",
  "state": "unknown",
  "supported_version": "0.3.0-candidate",
  "diagnostics": []
}
```

### 0.4.0

```json
{
  "profile": "CP-03",
  "standard_version": "0.4.0-candidate",
  "conformance": "conformant",
  "information_state": "contains_unknowns",
  "diagnostics": []
}
```

The old `state` field is removed from the canonical conformance-result schema. Conformance outputs now use the canonical `CP-*` profile identifier rather than the human-readable profile label.

Mapping guidance:

- old `valid` usually becomes `conformant` + `complete`;
- old `unknown` must be reviewed: it usually becomes `conformant` + `contains_unknowns` when uncertainty was correctly preserved, but may become `non_conformant` if an unsupported stronger claim was actually made;
- old `invalid` usually becomes `non_conformant`; information state must be determined separately.

Do not migrate `unknown` mechanically without reviewing what the old result meant.

## 2. Diagnostics

0.4 uses `effect: none | uncertainty | non_conformance` rather than an overloaded diagnostic state. This keeps diagnostic severity, information uncertainty and standards failure separate.

## 3. Canonical version metadata

Canonical YAML artifacts use `standard_version: 0.4.0-candidate`. `artifact_version`, `source_version` and `profile_version` remain available for narrower lifecycle meanings where appropriate.

## 4. Canonical manifest

`standard/public-interface.yaml` is the authoritative list of canonical artifacts. Consumers should stop hard-coding an independent canonical-file list and use the release manifest as the publication contract.

## 5. Identifiers and conformance profiles

Existing canonical IDs are retained unless separately documented. 0.4 adds a candidate URI strategy in `standard/identifiers.yaml`; implementations are not required to adopt JSON-LD or RDF.

Conformance result objects use stable `CP-*` identifiers. `CP-07` is the protection-assessment profile. Human-readable labels remain descriptive metadata rather than exchanged identifiers.

## 6. Hardened case contract

The validator-readiness hardening changes the canonical case shape. This is an explicit breaking candidate change before 1.0.

### Process positions

Replace singular `process_position` with `process_positions[]`. Give each position a case-local `id`. A core human action now records `process_position_refs[]`, making its process anchor explicit even when a case occupies several positions. `primary_process_position` is optional and does not erase the other positions.

### AI actions

Replace singular free-text or canonical `ai_action` with `ai_actions[]`. Values use canonical `AIA-*` identifiers. Multiple actions may be recorded when they are materially relevant.

### Evidence

Replace microstructure `evidence: [EV-*]` with `evidence_refs[]` pointing to structured case-level `evidence_items[]`. Each evidence item records its canonical evidence type, observation and target claim, with optional independence and support conditions.

An `EV-*` code describes an evidence type. It is not itself evidence that the human performed the action.

### Human control

Replace free-text `responsibility` with structured `human_control`. The structure distinguishes responsible actor, decision authority, information availability, timing, intervention capabilities and evidence of whether control is effective rather than nominal.

### Core human actions

Each core human action has a case-local `id` and `process_position_refs[]`. Optional `skill_refs[]` classify the action; they do not become parents of the core action. Microstructures remain constituent operations when decomposition is needed.

## 7. Rule executability

`standard/rule-executability.yaml` classifies rules as `machine`, `hybrid` or `human_review`. This classification constrains validator behaviour but does not change rule meaning or importance.

A validator must not use hidden LLM or heuristic judgements to convert a hybrid or human-review rule into a deterministic standard rule.

## 8. Test fixtures

Use the 0.4 result fixtures and domain fixtures exposing both `expected_conformance` and `expected_information_state`. `tests/conformance/machine-rule-matrix.yaml` tracks executable coverage required before a validator is labelled an authoritative reference implementation.

## What did not change

The hardened representation does not redefine context, goal, actor, core human action, microstructure, AI-action semantics, evidence claim types, handback, remediation, source-preserving adapters or the optional system-profile boundary. It makes their relations explicit enough for independent validation.
