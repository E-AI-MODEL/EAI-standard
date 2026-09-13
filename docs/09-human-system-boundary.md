# Human-system boundary

The EAI Standard distinguishes between **human constructs**, **technical system functionality** and **observable AI actions**.

This distinction is essential because generative AI systems can increasingly perform tasks that look similar to human educational or professional actions. Similar task output does not mean that the underlying construct is the same.

## Three layers

```text
TECHNICAL SYSTEM
model, inference, orchestration, data, tools, autonomy
                  |
                  v
OBSERVABLE AI ACTION
question, hint, classify, recommend, draft, perform, execute
                  |
                  v
EAI HUMAN-AI ALLOCATION
which human action mattered, who performed it, and what human evidence remains?
```

The system profile describes the first layer. `standard/ai-actions.yaml` describes the second. The EAI case and conformance rules describe the third.

## Functional correspondence is not construct equivalence

| Human-side construct or action | Possible system-side functionality | Same construct? |
| --- | --- | --- |
| knowledge / experience | model parameters, retrieval, context and stored data | no |
| observation | detection, extraction, classification | no |
| reasoning or problem solving | inference, search, planning and tool use | no automatic equivalence |
| professional judgement | classification, scoring, recommendation or proposed decision | no |
| responsibility | permissions, autonomy and execution rights | no |
| learning | successful system task completion | no |
| independent mastery | autonomous system execution | no |
| retention | persistent memory, context storage or retrieval | no |
| transfer | successful performance on a novel system task | no |
| metacognition | self-check, evaluator loop or verification | no automatic equivalence |

The EAI Standard does not need to settle philosophical questions about whether an AI system can in some sense reason, understand or learn. For interoperability and educational analysis, the safer and more useful rule is narrower:

> Describe system functionality functionally, and describe human educational and professional constructs using evidence appropriate to those human constructs.

## Capability is not allocation

A more capable model may make more operations technically substitutable. That fact does not decide whether those operations should be delegated in a given educational situation.

For example, a system may be able to:

- diagnose an error pattern;
- write a complete argument;
- generate feedback;
- recommend a pedagogical intervention;
- choose a next task;
- execute an external action.

The EAI question remains:

1. What was the relevant human action in this situation?
2. Which microstructure did the system actually perform?
3. What human execution remains observable?
4. What claim is being made about the human?
5. Does the available evidence support that claim?
6. Is handback or remediation required?

## Same system, different EAI meaning

The same technical model can participate in two situations with very different EAI interpretations.

### Situation A

The learner must formulate a counterargument. AI asks: “What might someone who disagrees say?”

System action: `ask_question`.

The target human microstructure remains with the learner.

### Situation B

The learner must formulate a counterargument. AI generates the counterargument and the learner pastes it into the answer.

System action: `full_performance` or `partial_performance`, depending on the task decomposition.

The same underlying model may be used in both situations. The EAI allocation is different because the **observable AI action in relation to the target human action** is different.

## Different systems, same EAI meaning

A simple classifier and a sophisticated multi-agent system might both ultimately flag the same learner response as potentially incorrect. If both only produce a flag for teacher inspection, the observable EAI action can still be `detect_or_flag`.

This is why vendor, model size, benchmark rank or orchestration complexity cannot substitute for action-level analysis.

## System memory and human retention

This is a particularly important boundary.

A system can persist information and retrieve it later. A learner can demonstrate retention after a delay. These can look superficially similar because both involve information being available later, but they are different constructs.

For EAI:

- system persistence belongs in the system profile;
- human retention is a human evidence claim;
- one cannot be used as evidence for the other.

The same distinction applies to system novelty performance versus human transfer.

## Professional responsibility

A system may have technical authority to send a message, modify a record or select a learning route. This is a property of system permissions and workflow governance.

Professional responsibility concerns the accountable human or organisation and cannot be inferred from system autonomy. Conversely, a nominal human approval step does not establish that the relevant professional judgement was actually performed by the human.

## Implementation rule

Implementations should therefore preserve the following sequence:

```text
system configuration
       -> observed AI action
       -> relevant human action
       -> human/AI execution allocation
       -> claim
       -> human evidence
       -> handback/remediation if required
```

The optional [`system-profiles/`](../system-profiles/) layer makes the technical configuration auditable without making it part of the normative human-action standard.
