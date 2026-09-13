# Explicit instruction family adapter

**Status:** candidate 0.2

This adapter demonstrates how the EAI Standard can be applied to a family of explicit/direct instructional approaches without treating those approaches as one identical model.

It is intentionally a **family adapter**. It does not claim that all approaches called direct instruction, explicit instruction or EDI use the same terminology, sequence or implementation rules.

The adapter identifies recurring process positions that are well represented in evidence-informed explicit instruction literature: review or activation of relevant prior knowledge, explicit presentation in manageable steps, modelling, checks for understanding, guided practice, movement toward independent practice, and later review or reflection.

A branded or locally defined instructional model should receive its own adapter when its terminology, phases or rules need to be preserved exactly.

## Why this adapter exists

The EAI Standard itself does not prescribe instructional phases. This adapter tests whether an instructional approach can supply its own process structure while retaining the same EAI semantics:

`goal -> actor -> process position -> core human action -> microstructures -> AI action -> human evidence -> handback/remediation`

## Interpretation rule

The `candidate_core_actions` listed per process position are **not automatically protected actions**. They are plausible human actions for that process position. The concrete lesson goal and situation determine which actions actually become core human actions.

## AI rule

The adapter does not classify an AI tool as suitable or unsuitable for a whole phase. AI participation is described per action. The same AI feature may support one target action while displacing another.

## Source basis

This family adapter is a synthesis, not a reproduction of one proprietary model. It draws on recurring features described in:

- Barak Rosenshine, *Principles of Instruction: Research-Based Strategies That All Teachers Should Know* (American Educator, 2012).
- Education Endowment Foundation guidance on explicit instruction, modelling, guided practice and movement toward independent learning.

Sources inform the adapter. They are not themselves normative rules of the EAI Standard.
