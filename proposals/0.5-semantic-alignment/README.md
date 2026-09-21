# EAI 0.5 semantic alignment proposal

Status: proposal for the next semantic release. This directory is intentionally non-canonical until the proposal is accepted and the public interface, schemas, conformance profiles, diagnostics and migration notes are updated together.

## Why this proposal exists

The 0.4 candidate is strong once a relevant human action has already been identified. It can represent human-AI allocation, protection, evidence, handback and remediation with considerable precision.

The next semantic step is earlier in the reasoning process.

Educational and technical discourse often use the same words for different constructs: agency, autonomy, memory, reasoning, learning, judgement, feedback and others. At the same time, a technical capability does not by itself determine the educational meaning of using that capability in a learning process.

The proposed 0.5 alignment therefore adds two things before allocation analysis:

1. **concept positioning**: identify where the meaning of a concept comes from and which domain sets its boundary;
2. **learning-action specialization**: preserve the learner-specific EAI question inside the broader `core_human_action` construct.

The intended design order becomes:

```text
concept meaning and boundary
        ->
process
        ->
process position / stage
        ->
core human action
        ->
learner-specific core learning action where applicable
        ->
observable AI contribution
        ->
task density / allocation
        ->
protection
        ->
human evidence
        ->
handback / remediation / re-demonstration
```

## Source concepts

This proposal aligns the repository with the current EAI publications and dictionary drafts:

- *De vraag die we vergeten in het AI-debat*
- *EAI Dictionary* (English edition, concept)
- *EAI Dictionary* (Dutch edition, concept)

The proposal does not import every dictionary entry into the canonical standard. It first formalises the semantic distinctions that change how the standard itself should be read.

## What should become canonical after review

The proposal recommends canonical status for:

- the five concept-positioning positions;
- the rule that one word may represent multiple constructs and those constructs must be positioned separately;
- the distinction between `core_human_action` and learner-specific `core_learning_action`;
- Education in the Loop as an EAI design principle;
- Task Density as a relation between AI execution and the contextual core learning action, not as a measure of AI volume;
- the Support-Replacement Boundary;
- the Evidence-Function Shift;
- the rule that functional correspondence never establishes construct equivalence.

Other dictionary concepts may remain reusable EAI vocabulary or explanatory terms unless conformance or interoperability requires canonical semantics.

## Release rule

Do not merge this proposal into the canonical public interface piecemeal.

Promotion to canonical 0.5 semantics should update together:

- `standard/public-interface.yaml`;
- canonical definitions and relations;
- identifiers;
- case and evidence schemas where required;
- conformance profiles;
- rule executability and diagnostics;
- migration guidance;
- conformance fixtures.

This avoids creating a second semantic truth between the dictionary, documentation and machine contract.
