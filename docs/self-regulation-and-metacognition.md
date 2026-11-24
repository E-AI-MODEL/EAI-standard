# Learner self-regulation and metacognition

The EAI Standard treats learner regulation as a distinct analysis target when the educational goal requires the learner to set direction, plan, monitor, seek help, adjust strategy or evaluate their own process.

This matters because visible task execution can remain human while AI performs much of the regulation around that execution. A learner may still type, calculate or write while an AI system determines the route, selects the strategy, monitors progress, changes difficulty and decides what should happen next.

The current candidate registry is:

- `registries/microstructures/learner-self-regulation-and-metacognition.yaml`

It contains sixteen reusable microstructures grouped around:

1. goal orientation and planning;
2. monitoring and impasse detection;
3. regulation of support and strategy;
4. effort and attention regulation;
5. evaluation, reflection and future adjustment.

## What the registry does not assume

Self-regulation is not globally protected from AI support. Whether a regulatory operation must remain human depends on the goal, process position, actor and evidence claim.

For example, automatic routing may be entirely acceptable when route selection is peripheral to the educational purpose. The same routing becomes consequential when the intended learning is that the learner independently plans, monitors and adjusts their own approach.

## Central distinction

The registry makes the following distinction explicit:

```text
learner executes task steps
        does not imply
learner regulates the learning process
```

A conforming case therefore may need to analyse both task execution and regulatory execution when both matter to the intended claim.

## AI support versus regulatory takeover

AI may support self-regulation through questions, bounded hints, alternatives or prompts while the learner still performs the relevant regulatory operation.

Examples include:

- AI asks what the learner's current goal is, but the learner formulates the goal;
- AI offers two strategies, but the learner compares and selects one;
- AI prompts a checkpoint, but the learner judges progress from their own evidence;
- AI provides a hint after a targeted help request, and the learner resumes the task and decides the next step.

By contrast, regulatory takeover may occur when AI:

- determines the learning goal;
- creates the complete plan;
- selects the strategy;
- detects every impasse before the learner does;
- decides when support must increase or decrease;
- evaluates whether performance is sufficient;
- automatically changes the route or next task.

These actions are not automatically unacceptable. They change what can be claimed about learner self-regulation.

## Handback and remediation

`REM-11 return_regulatory_control` restores learner regulation when an AI system has performed a regulatory operation that matters to the intended claim.

The pattern is:

```text
identify displaced regulatory operation
-> pause or hide AI routing/recommendation
-> restate the learning goal
-> require learner planning, monitoring or adjustment
-> collect process evidence
-> resume only the bounded support that is still needed
```

The remediation is complete only when new human evidence is available.

## Evidence

Useful evidence includes direct explanation, process traces, comparison and selection, targeted probe responses and independent re-performance where relevant.

A polished reflection written by AI is not by itself evidence that the learner monitored or regulated the process. Likewise, successful completion of a system-generated route does not establish that the learner can independently plan or adapt that route.

## Scientific status

The registry is a candidate taxonomy. Recent evidence supports action-level analysis, the relevance of cognitive substitution and task-specific judgement about AI use, but does not directly validate these sixteen EAI microstructure boundaries as a measurement model.

The evidence map therefore records the registry as conceptually aligned with current evidence while keeping direct construct validation open.

## Reference cases

Two examples are included:

- `examples/self-regulation/learner-regulates-ai-supported-task.yaml` shows bounded AI support with human regulatory execution;
- `examples/self-regulation/ai-routes-learner-invalid.yaml` shows successful visible task execution while AI performs the regulatory operations required by an independent self-regulation claim.

Candidate expected outcomes are stored in `tests/conformance/self-regulation-cases.yaml`.
