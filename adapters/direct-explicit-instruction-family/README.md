# Direct / explicit instruction model family

Status: candidate family index

This directory documents relationships among instructional models that are often grouped under labels such as direct instruction, explicit instruction or explicit direct instruction. It is **not** itself a model adapter and does not merge those models.

## Why the distinction matters

Several traditions share features such as clear goals, modelling, guided practice, checking understanding, feedback and movement toward independent performance. Shared features do not make the models identical.

The EAI Standard therefore treats model-family membership as an organisational relation only. Each model receives its own source-preserving adapter.

## Candidate family members

| Model | Adapter status | Notes |
| --- | --- | --- |
| Archer & Hughes Explicit Instruction | implemented | Six source teaching functions, sixteen instructional elements and model principles are retained through source pointers and a schema-conformant adapter. |
| Expliciete Directe Instructie 2.0 (Hollingsworth & Ybarra, Dutch adaptation Schmeier) | implemented as candidate | Uses the current book-edition metadata and official public Pica phase artifact; unavailable book detail remains explicitly unknown. |
| Direct Instruction (Engelmann tradition) | implemented as candidate | Represents capital-DI as a curricular/instructional system rather than forcing it into a generic phase sequence. |
| ADI / IGDI and other Dutch variants | not yet implemented | Separate adapters required if included. |

## Family-level commonalities

The following are useful comparison dimensions, not universal definitions:

- explicitness of goals and instructional target;
- modelling or demonstration;
- granularity of instructional steps;
- frequency of learner responding;
- checking for understanding;
- feedback and correction;
- guided practice;
- fading or transfer of responsibility;
- independent practice;
- cumulative or distributed review.

## Structural differences already visible

The adapters show why a family index is useful but cannot replace model-specific mappings:

- **Archer & Hughes Explicit Instruction** can be represented through six teaching functions plus instructional elements and principles.
- **EDI 2.0** exposes a nine-phase lesson model with cross-cutting techniques and an explicit decision point before independent work.
- **Direct Instruction** in the Engelmann tradition is more appropriately represented through curricular design, placement, grouping, scripted presentation, response systems, error correction, mastery and progress relations.

These structures overlap at points but are not interchangeable.

## EAI rule

No family-level commonality becomes a normative EAI rule merely because several models share it. A concrete adapter maps only what its own source supports.
