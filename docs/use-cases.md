# Use cases

The EAI Standard is intended to make human-AI allocation in education interoperable across tools, organisations and educational models.

The standard does not prescribe a teaching model. It provides shared semantics that different systems and organisations can implement consistently.

## UC-01 Analyse of an AI-supported learning activity

A teacher, school or tool describes:

- the educational goal;
- the learner action that matters;
- the process position according to the model being used;
- the relevant microstructures;
- the AI action at each relevant microstructure;
- the evidence that remains available.

Different tools should be able to exchange or inspect the case without translating the meaning of these fields manually.

## UC-02 AI tutor configuration

A learning application uses the standard to distinguish between:

- asking a question;
- giving a hint;
- generating alternatives;
- partially performing a target action;
- fully performing a target action.

The same configuration can reference a model adapter and a skill or microstructure registry without embedding one fixed teaching model in the AI system.

## UC-03 Teacher professional judgement

An AI system analyses learner work and proposes a diagnosis or intervention. The standard makes visible which operations were performed by AI and which professional judgement must still be performed and evidenced by the teacher.

This supports auditability without reducing professional judgement to nominal human approval.

## UC-04 Learning evidence after AI support

A learning environment distinguishes:

- successful supported performance;
- independent execution;
- delayed reperformance;
- performance in a novel context.

This prevents product quality from being treated automatically as evidence of mastery, retention or transfer.

## UC-05 Handback and remediation

A system detects that AI performed a microstructure intended for the learner or teacher. It can use the remediation registry to return that operation to the human and request renewed evidence.

## UC-06 Model-specific implementation

An organisation works with EDI, inquiry learning, formative assessment or another process model. A model adapter maps that model to the EAI Standard while preserving the source model's own terminology and phase structure.

This allows different educational approaches to use the same human-AI semantics without being forced into one instructional sequence.

## UC-07 Cross-organisation exchange

A school, AI supplier, learning-platform supplier and research partner exchange a machine-readable description of an AI-supported activity. Stable identifiers and schemas reduce local reinterpretation of terms such as `core_human_action`, `microstructure`, `handback` and `human_evidence`.

## UC-08 Evaluation and research

Researchers compare implementations across tools or instructional models using shared semantic units while keeping claims about effectiveness separate from structural conformance.

## Interoperability value

The standard adds value when two or more parties need to describe, configure, inspect or exchange information about human-AI allocation without first inventing a local vocabulary.

This is the principal interoperability target for the candidate standard.
