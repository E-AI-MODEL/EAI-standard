# Registry coverage audit

The EAI Standard separates the breadth of its reusable skill inventories from the depth of its current microstructure coverage. A skill entry is therefore not treated as proof that the skill has already been decomposed sufficiently for action-level human-AI allocation.

The initial machine-readable audit is maintained in:

- `registries/coverage/skill-microstructure-coverage.yaml`

Accepted corrections and additions are tracked in:

- `registries/coverage/resolution-log.yaml`

The current coverage position is maintained in:

- `registries/coverage/current-status.yaml`

## Current scope

The inventory currently covers:

- 57 teacher/professional skills;
- 56 learner skills;
- 24 cross-cutting AI-interaction skills;
- 6 deep microstructure registries containing 93 microstructures.

Teacher/professional deep candidate coverage currently spans 24 skills. Learner deep candidate coverage spans 13 skills after adding the self-regulation and metacognition registry. Cross-cutting AI-interaction skills continue to reuse human-action microstructures where possible instead of creating a separate parallel decomposition.

The purpose of the audit is not to maximise the number of microstructures. It is to identify where a missing decomposition would cause two implementations to represent materially different human-AI allocations as if they were the same.

## Coverage states

The audit uses three development states:

- **deep**: a current registry substantially covers the skill at action level;
- **partial**: current microstructures cover material parts of the skill but not enough for reliable action-level reuse across cases;
- **none**: no current microstructure registry provides sufficient coverage.

These states are not conformance judgements, educational quality scores or evidence-strength ratings.

## Decision rule for adding microstructures

A skill should be decomposed when doing so helps distinguish materially different:

1. human and AI execution;
2. support conditions;
3. evidence claims;
4. handback requirements;
5. remediation routes;
6. learner or professional regulation.

A skill should not receive a dedicated microstructure registry merely for symmetry or completeness. Where the same smaller operation occurs in several skills, reuse is preferred.

## Resolved high-priority gap: learner self-regulation and metacognition

The first audit identified learner self-regulation as the highest-priority gap because AI can leave visible task production with the learner while taking over goal setting, route selection, monitoring, evaluation or adjustment.

That gap now has a dedicated candidate registry:

- `registries/microstructures/learner-self-regulation-and-metacognition.yaml`

It covers `LSK-040` through `LSK-048` with sixteen reusable microstructures for goal orientation, planning, strategy choice, monitoring, impasse detection, help regulation, resumption of regulatory control, strategy adjustment, effort regulation, self-evaluation and reflection.

The new registry does not make self-regulation globally protected. It makes the allocation visible when self-regulation is part of the goal or evidence claim.

## Highest-priority remaining gaps

### 1. Teacher assessment and evidence judgement

The standard already has strong normative evidence semantics, but several professional assessment skills are not yet deeply decomposed. The most important are:

- `TSK-050` define_assessment_claim;
- `TSK-051` interpret_evidence;
- `TSK-052` weigh_multiple_sources;
- `TSK-053` judge_quality;
- `TSK-054` determine_mastery.

This gap matters because AI may contribute to scoring, classification, feedback or evidence aggregation without those actions being equivalent to the final professional judgement.

### 2. Learner reasoning and problem solving

Argumentation is already deeply represented, but it should not be used as a proxy for all reasoning. General analysis, inference, causal reasoning, problem solving, evaluation and decision-making require broader reusable operations.

Priority skills include:

- `LSK-020` analyse;
- `LSK-021` infer;
- `LSK-022` reason_causally;
- `LSK-023` think_critically;
- `LSK-024` solve_problem;
- `LSK-026` evaluate;
- `LSK-027` decide.

### 3. Teacher design and task architecture

AI can change the educational task before execution begins. Goal selection, task choice, practice design, support design, independence and evidence opportunities therefore require action-level analysis where allocation differs materially.

### 4. Learner inquiry and source evaluation

Search, source selection, method choice, evidence collection, analysis and conclusion are common AI-assisted operations. Current argumentation coverage captures only part of this process.

## Lower-priority gaps

Instruction/modelling, knowledge building, creation, social collaboration and professional reflection also contain uncovered skills. They remain part of the inventory, but candidate-stage work should prioritise gaps that most directly affect allocation, evidence and regulatory control.

## AI-interaction skills

The AI-interaction registry is cross-cutting. It should not automatically receive its own parallel microstructure tree.

For example:

- `AIS-007 preserve_human_action` can reuse scaffolding, regulatory-control and independent-reperformance operations;
- `AIS-008 choose_handback_point` can reuse support-fading, regulatory handback and reperformance operations;
- `AIS-005 verify_ai_claim` can reuse future source-evaluation operations;
- `AIS-022 formulate_targeted_help_request` now directly reuses learner self-regulation microstructures;
- `AIS-024 reconstruct_after_ai_support` overlaps with learner reperformance and regulatory handback.

A new AI-specific microstructure is justified only if the human operation remains distinct after such reuse.

## Structural findings

The audit also identified registry-format inconsistencies that should be resolved before executable registry validation:

- the older argumentation registry lacks some metadata present in newer deep registries;
- several deep registry files use a top-level focus identifier rather than a direct skill-registry ID;
- a strict schema for complete skill-registry entries is not yet present;
- registry version metadata still needs migration to the 0.4 publication policy.

The pedagogical-judgement relation gap found in the first audit has already been repaired. The self-regulation gap has now been addressed with a candidate registry, remediation pattern, examples and conformance fixtures.

## Build order

The current recommended sequence is:

1. teacher assessment and evidence judgement;
2. learner reasoning and problem solving;
3. teacher design and task architecture;
4. learner research and source evaluation;
5. teacher instruction and modelling;
6. learner knowledge building and orientation;
7. creation, social collaboration and professional reflection where implementation experience shows recurring allocation differences.

This order is a development priority, not a claim that later domains are less educationally important.
