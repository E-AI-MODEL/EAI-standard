# Core human action analysis

A central purpose of the EAI Standard is to avoid coarse statements such as "AI supports the task" or "the human remains in control". Those statements are too broad to show what happened to the human action that actually matters.

## Analysis sequence

A conforming analysis proceeds in this order:

1. identify the concrete context;
2. state the goal;
3. identify the human actor whose action or capability is being examined;
4. locate the situation in the process or model actually being used;
5. identify one or more candidate core human actions;
6. decompose each core human action far enough to expose relevant microstructures;
7. record what the human does and what AI does at those microstructures;
8. identify the evidence that remains available;
9. compare the evidence to the claim that is being made;
10. use handback or remediation where a needed human action is missing, displaced or insufficiently evidenced.

## Core human action

A core human action is not simply an important skill. It is the human action whose execution is necessary for the intended learning, professional judgement, pedagogical purpose or decision in the specific situation.

Three consequences follow.

### Core status is contextual

A skill cannot be permanently labelled core. The same action can move between central and peripheral roles depending on the goal and process position.

### Multiple core actions may coexist

A situation may contain several relevant core human actions. For example, in guided practice the learner may need to execute a reasoning step while the teacher must interpret the learner response and select a support level. Neither actor's action should be collapsed into the other.

### Core actions may require decomposition

A high-level action such as `argue`, `diagnose`, `design` or `assess` can conceal materially different operations. Decomposition is required when AI performs only some of those operations or when different operations require different evidence.

## Sufficient decomposition

Microstructure analysis should stop when the allocation and evidence question becomes clear enough to act on. The standard does not require endless atomisation.

Decomposition is probably too coarse when:

- AI and human both appear to perform the same high-level skill but their contributions cannot be distinguished;
- a claim about learning depends on one hidden sub-operation;
- a remediation cannot target the missing action precisely;
- two reviewers interpret the same allocation differently because the action label is too broad.

Decomposition is probably too fine when:

- the additional split does not change allocation, evidence, handback or remediation;
- the operations cannot be meaningfully distinguished in observable practice;
- the split creates implementation burden without improving interpretation.

## Allocation

Allocation is recorded at the smallest level needed for the case. At minimum, an implementation should be able to distinguish:

- human execution;
- AI execution;
- shared or partial execution;
- unknown execution.

The standard does not define a universal percentage of acceptable AI involvement.

A one-sentence AI output may fully perform the relevant human action. A long AI output may be peripheral to it. Output volume is therefore not a proxy for displacement.

## Process position

The standard requires a process position because the role of an action changes with the process. The source model supplies the process structure. EAI does not replace it.

For an instructional model, a process position might be guided practice. In an inquiry model it might be hypothesis formation. In a mentoring process it might be problem exploration. In a formal assessment process it might be evidence interpretation.

## Teacher and learner in one case

Cases should include both actors when both actions materially matter.

Example:

- learner core action: formulate and test an argument;
- teacher core action: interpret the learner's reasoning and decide what support is warranted;
- AI action: generate a counterargument and cluster learner responses.

The learner and teacher allocations are analysed separately. A case is not considered human-led merely because one of the two actors still makes a final click or approval.

## Unknown

Insufficient information must remain `unknown`. Reviewers should not infer human execution from a polished product, nor infer AI execution solely from the presence of AI in the workflow.

Unknown is a valid result and may trigger a request for better trace, direct observation or a fresh performance opportunity.
