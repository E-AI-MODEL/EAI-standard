# Conformance test: CASE-ARG-EI-001

This test checks whether an implementation preserves the distinction between supported argumentation and evidence of independent argumentation.

## Input

Use [`examples/argumentation/explicit-guided-practice.yaml`](../../examples/argumentation/explicit-guided-practice.yaml).

## Required conclusions

A conforming implementation must preserve all of the following conclusions:

- The learner's thesis formulation is human-executed in this case.
- The learner's initial main argument is human-executed in this case.
- The AI-generated counterargument means this attempt does **not** establish independent learner capability to generate counterarguments.
- The learner's interpretation of what the counterargument challenges remains separate from the AI generation step.
- The rebuttal is human-executed and may be used as current-performance evidence for rebuttal formulation, subject to the evidence recorded.
- A handback is required for `MS-ARG-15 recognise_counterargument` before a stronger claim about independent counterargument generation is made.
- The teacher's use of AI to organise responses or generate possible hints does not by itself establish or invalidate professional judgement. The implementation must inspect who interpreted learner evidence and who selected support.
- Retention remains `unknown` or unclaimed.
- Transfer remains `unknown` or unclaimed.

## Non-conforming interpretations

The following outputs are non-conforming:

- `The learner mastered argumentation because the final argument was strong.`
- `The learner can generate counterarguments independently.`
- `AI was used, therefore the learner did not perform the task.`
- `The teacher remained in control because the teacher clicked approve.`
- `The activity proves retention.`
- `The activity proves transfer.`

## Purpose

The case tests a central property of the standard: allocation is resolved at action or microstructure level. A single interaction can contain fully human, partially human and AI-performed operations at the same time.
