# Overview

The EAI Standard provides a common way to describe human action when AI participates in education.

It does not decide which teaching model, pedagogical approach, curriculum or AI system should be used. Its purpose is narrower and more precise: make the division between human and AI action explicit enough to judge whether the intended human learning, professional judgement or pedagogical action is still present and evidenced.

## Why this is needed

Statements such as "AI may support but not replace" are too vague to guide practice. Replacement can only be judged after the intended human action is known.

The standard therefore starts from the situation itself:

1. What is the goal?
2. Who is the relevant human actor?
3. Where are we in the process or educational model being used?
4. Which human action matters here?
5. Which smaller operations make up that action?
6. What does AI actually do in relation to those operations?
7. What human evidence remains visible?
8. Who remains responsible for interpretation and decisions?
9. Does the action need to be handed back to the human?
10. Is renewed performance, retention or transfer evidence required?

## Two human profiles

The same standard is used for:

- **teacher/professional** action, including didactic, pedagogical and professional judgement;
- **learner** action, including cognitive, metacognitive, social and self-regulatory activity.

A single situation may contain core actions for both actors. These are analysed separately.

## Model-independent by design

The standard has no fixed teaching sequence. An EDI phase, an inquiry-learning phase, a mentoring conversation or an assessment process may all be described using the same EAI concepts while keeping their own terminology and internal logic.

Model-specific depth belongs in `adapters/`, not in the core.

## Registries

Skills and microstructures are reusable human-action descriptions. They do not automatically become core actions. Their role depends on the concrete goal and process position.

The first reference registry is `argumentation`, because it clearly shows why task-level labels are too coarse: AI may formulate language while the learner still selects and reasons, or AI may generate the actual arguments and thereby perform the operation that was intended for the learner.
