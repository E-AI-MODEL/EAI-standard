# Actor profiles and skills

The EAI Standard uses the same semantic structure for two primary human actors: the learner and the teacher/professional. Their responsibilities and typical actions differ, but the standard does not create two unrelated models.

## Profile versus registry

An **actor profile** describes broad families of human action that are relevant to that actor.

A **skills registry** contains reusable capabilities that can occur across many models, subjects and contexts.

A **core human action** is not stored as a permanent property of a skill. Core status arises only in a concrete situation.

A **microstructure** is a smaller operation that contributes to a skill or core human action.

The relation is therefore:

`actor profile -> skill family -> skill -> microstructures`

and at runtime or case level:

`goal + process position + context + actor -> selected core human action(s)`

## Teacher/professional profile

The teacher/professional profile currently distinguishes eight families:

- educational design;
- instruction and modelling;
- observation and diagnosis;
- guidance, feedback and remediation;
- assessment and professional decision-making;
- pedagogical and relational action;
- professional communication and collaboration;
- professional self-regulation and improvement.

This separation matters because AI can affect these actions differently. Generating examples is not the same as diagnosing a misconception. Clustering learner responses is not the same as deciding what those responses mean. Drafting possible feedback is not the same as making a pedagogical judgement.

## Learner profile

The learner registry currently distinguishes eight families:

- orientation and task representation;
- knowledge building and understanding;
- reasoning and problem solving;
- creation and production;
- self-regulation and metacognition;
- social learning and communication;
- inquiry and research;
- demonstration, retention and transfer.

These are not stages. A learner can move among them repeatedly within one task.

## Shared AI-interaction skills

Some capabilities concern the interaction with AI itself rather than a subject or instructional model. Examples include:

- defining the intended AI role;
- inspecting and verifying AI output;
- recognising when AI displaces a target human action;
- selecting a handback point;
- distinguishing AI-supported product quality from human evidence;
- calibrating reliance;
- documenting material AI contribution where required.

These are stored separately in `registries/skills/ai-interaction.yaml` so that they do not distort the general teacher and learner skill structures.

## Why skills are not globally protected

The same skill can be core in one situation and peripheral in another.

Spelling correction may be peripheral in a history task and central in a spelling task. Source evaluation may be central in research instruction and secondary in a task that provides verified source material so that causal reasoning can be practised.

The standard therefore prohibits a global list of skills that AI may never perform.

## Shared microstructures

Microstructures may belong to more than one skill. For example, `compare alternatives` may contribute to decision-making, argumentation, problem solving and professional design. Registries should reuse or relate such operations rather than duplicate them purely because they occur in different subjects.

## Candidate status

The current skill sets are intentionally broad and model-independent. They should be refined through implementation, inter-rater testing and comparison with external curricula or competence frameworks. Such mappings belong in context or crosswalk layers and must not silently change the meaning of a skill in the base registry.
