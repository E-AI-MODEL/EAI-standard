# Evidence, handback and remediation

The EAI Standard separates successful task completion from evidence about human capability or professional judgement.

## Evidence claims

The standard distinguishes at least four claim levels:

- **current performance**: the human contributed successfully in the present task under the recorded support conditions;
- **independent mastery**: the human can execute the relevant action with support reduced to the level required by the claim;
- **retention**: the human can execute the relevant action after a meaningful delay;
- **transfer**: the human can execute the relevant action in a meaningfully different context, task or representation.

Professional judgement is treated as a separate claim type because an AI-generated recommendation and a human professional decision are not interchangeable evidence.

## Evidence is claim-relative

A piece of evidence is not strong or weak in the abstract. It is useful only in relation to a claim.

A polished essay may be strong evidence that a human-AI system produced a good essay. It may be weak evidence that the learner can independently formulate arguments if AI performed those operations.

A teacher approving an AI-generated diagnosis may show that a recommendation was accepted. It does not by itself show that the teacher independently interpreted the learner evidence.

## Support conditions are part of the evidence

Any claim about independence should preserve enough information to know what support was available during the attempt.

Relevant support information may include:

- whether prior AI output remained visible;
- whether hints were available proactively or only on request;
- whether AI supplied substantive reasoning steps;
- whether the teacher or learner could request verification or examples;
- whether the fresh attempt reused the same answer structure.

## Handback

Handback is the planned return of an action from AI-supported or AI-performed execution to human execution.

Handback is required when all three conditions hold:

1. the action is relevant to the intended claim;
2. AI has materially performed or obscured that action;
3. human evidence is still required.

Handback is not a punishment for using AI. It is an evidence and learning mechanism.

## Remediation

Remediation is narrower than repeating the whole task. It targets the missing, displaced or unevidenced human operation.

A remediation sequence normally contains:

`identify -> isolate -> return -> reperform -> collect new evidence -> reconnect`

Examples include:

- removing answer access and requiring a fresh human attempt;
- reducing one support layer;
- returning to one microstructure instead of repeating an entire assignment;
- comparing AI and human alternatives before reconstructing the response;
- requiring explanation before further AI support is made available;
- using a fresh item that preserves the same underlying operation;
- delayed reperformance;
- a transfer task;
- professional reassessment without the AI interpretation in view;
- renewed direct pedagogical interaction.

The canonical candidate patterns are stored in `registries/remediation/interventions.yaml`.

## Remediation endpoint

Remediation is incomplete if it ends only with additional explanation or another AI-generated answer. It must end with new human evidence relevant to the original claim.

The new evidence may show that the human action is now sufficient, still insufficient or still unknown. The standard does not require a positive result.

## Productive AI support

AI support can deliberately perform operations that are not the target of the current learning or professional judgement.

For example, AI may correct spelling during a history reasoning task, provide a fresh practice item, organise large numbers of responses, or translate instructions. Such support should not be treated as displacement merely because AI did work.

The relevant question is whether the performed AI action removes, hides or materially changes the human action required by the current goal.

## Evidence after AI support

A strong design often uses AI in one attempt and deliberately changes the allocation later.

Example:

- attempt 1: AI generates a counterargument and the learner formulates the rebuttal;
- handback: on a fresh issue, the learner must generate the counterargument;
- later check: the learner repeats the operation after delay;
- transfer: the learner uses the same argumentative operation in a different subject or representation.

These are different evidence events and should not be collapsed into one score.
