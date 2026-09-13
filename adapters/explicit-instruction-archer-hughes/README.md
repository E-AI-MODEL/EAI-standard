# Explicit Instruction adapter: Archer & Hughes

Status: candidate

This adapter maps **Explicit Instruction: Effective and Efficient Teaching** by Anita L. Archer and Charles A. Hughes to the EAI Standard while preserving the source model's own structure.

The adapter is not a claim that Explicit Instruction is the preferred teaching model. It exists because the model is widely used, sufficiently specified, and useful for testing whether the EAI Standard can represent a structured instructional approach without rewriting it.

## Source model

Primary model source:

- Archer, A. L., & Hughes, C. A. (2011). *Explicit Instruction: Effective and Efficient Teaching*. Guilford Press.
- Public sample chapter: https://explicitinstruction.org/download/sample-chapter.pdf
- Companion site: https://explicitinstruction.org/

The source describes explicit instruction as structured, systematic and scaffolded. It contains sixteen instructional elements and also presents six higher-level teaching functions that group those elements:

1. Review
2. Presentation
3. Guided practice
4. Corrections and feedback
5. Independent practice
6. Weekly and monthly reviews

The adapter uses these six source functions as the primary process positions because they are compact, explicit in the source and sufficiently stable for interoperability.

## Why this adapter is useful for EAI

The model contains several transitions that are especially relevant to human-AI allocation:

- activation and review before new instruction;
- teacher modelling before learner performance;
- high-response guided practice;
- close monitoring and immediate feedback;
- systematic reduction of support;
- movement toward independent performance;
- distributed and cumulative practice.

These make it possible to distinguish, for example, AI that supplies an example from AI that performs the learner's target operation, or AI that flags an error from AI that makes the teacher's diagnostic and instructional decision.

## Mapping rule

Source terminology remains canonical for the adapter. EAI mappings are added alongside the source representation. A source element that does not map cleanly is retained with `mapping_status: unmapped` or `mapping_status: partial`.

## Evidence status

The adapter describes the model. It does not by itself establish the model's effectiveness in every context. Model-definition sources and effectiveness evidence are therefore kept separate in `sources.yaml`.
