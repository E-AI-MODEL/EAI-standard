# Core concepts

## Context

The concrete educational or professional situation. Context should be specific enough to determine why the action matters.

## Goal

The intended outcome. A goal may concern learning, pedagogy, professional judgement, decision-making or execution.

## Process position

The place of the situation within the process actually being used. EAI does not impose a universal phase model.

Examples:

- an EDI phase;
- hypothesis formation in inquiry learning;
- a feedback cycle;
- a mentoring conversation;
- an assessment decision;
- a design process.

## Core human action

A human action whose execution, judgement, control or evidence matters for the intended purpose in this context.

A core human action is always interpreted through four anchors:

`context + goal + actor + process position -> core human action`

Removing one of those anchors can change the meaning of the action. The same reusable skill may therefore be core in one situation and peripheral in another.

For example, source evaluation may be central when the learner is learning source criticism, but peripheral when verified sources are deliberately provided so that causal reasoning can be practised.

More than one core action may exist in the same situation. Teacher/professional and learner may also have different core actions at the same moment.

## Skill

A skill is a reusable capability in a registry. It may help classify or identify a core human action, but it is not itself globally core.

A concrete core human action can relate to more than one reusable skill, and the same skill can appear in many contexts without being equally important in each of them.

## Microstructure

A microstructure is a reusable description of a smaller human operation.

In a concrete EAI case, selected microstructures are constituent operations **inside the core human action being analysed**:

```text
CORE HUMAN ACTION
        |
        +-- microstructure
        +-- microstructure
        +-- microstructure
```

A microstructure is therefore not a parallel case level beside the core human action. The registry entry can be reused across different skills and cases, but once selected in a case it is interpreted as part of that case's core human action.

Decomposition is needed when the larger action hides a materially different human-AI allocation, evidence requirement, handback requirement or remediation route. It is not required merely to make the taxonomy more detailed.

For example, `argumentation` may involve:

- analysing the issue;
- formulating a position;
- generating arguments;
- judging relevance;
- recognising counterarguments;
- rebutting;
- structuring;
- concluding;
- reflecting on the reasoning process.

AI may perform some of these while leaving others to the learner. This is why task-level labels such as "AI helped with the essay" are insufficient.

## AI action

A descriptive classification of what AI actually does, such as asking a question, giving a hint, generating alternatives, checking work, proposing a decision or performing part of the target operation.

The same AI action may be useful in one context and displacing in another.

## Protection assessment

After a core human action and the actual human-AI allocation are known, EAI can record a **protection assessment**: which dimensions of the human action should remain human, remain directly evidenced, remain under effective human control, or be returned to human execution.

Protection is not a single `protected: true/false` label. Different dimensions can receive different conclusions in the same case. For example:

```text
human execution              delegable
human judgement              required
effective human oversight    required
human authority to intervene required
human evidence               required
```

The conclusion must also state **why**. EAI distinguishes among:

- an EAI normative rule;
- applicable law or regulation;
- scientific evidence;
- a recognised external framework;
- a professional standard;
- an institutional rule.

The authority of those sources is not interchangeable. Strong scientific evidence is not law, and a recognised guideline is not legally binding merely because it is widely used.

The canonical protection vocabulary is in `../standard/protection.yaml`. Jurisdiction-specific and evidence-informed mappings remain outside the canonical semantics, for example `../context/eu-regulatory-protection.yaml` and `../evidence/protection-guidance.yaml`.

## Human evidence

Evidence supports a claim about human action. Product quality is not enough on its own when AI has contributed to the product.

Evidence should match the claim:

- current performance;
- professional judgement;
- independent mastery;
- retention;
- transfer.

## Responsibility

Responsibility concerns accountable interpretation, judgement, approval or action. It must be distinguished from mere presence in the workflow.

A human clicking "approve" after an AI recommendation is not automatically evidence that the human performed the relevant professional judgement.

Responsibility is also distinct from effective control. A protection assessment can therefore record separately whether human judgement is required, whether effective oversight is required and whether the human has meaningful authority to reject, override or stop AI-supported activity.

## Handback

Handback restores the relevant action to the human after AI support or performance. It is needed when the human action must become visible again.

Handback can itself be a protection requirement when a stronger claim about human capability or judgement is needed.

## Remediation

Remediation is targeted repair after the relevant human action was not sufficiently performed or evidenced. It ends with new human evidence, not merely with the provision of extra support.
