# Conformance

Conformance means that a case, registry item or model adapter uses the standard's concepts consistently enough to be inspected and compared.

## Case-level minimum

A conforming case should state:

- context;
- goal;
- actor;
- process position;
- at least one candidate or confirmed core human action;
- relevant microstructures when allocation differs within the action;
- AI action per relevant microstructure;
- human/AI allocation;
- evidence available;
- responsibility where professional judgement is involved;
- handback requirement where relevant;
- remediation route where the intended human action is missing or unevidenced;
- claim type being made.

## Conformance does not mean educational quality

A structurally conforming case can still be educationally weak. Conformance only means the situation has been described without collapsing important distinctions.

The standard does not certify that:

- the chosen teaching model is effective;
- the learning goal is appropriate;
- the AI system is accurate or safe;
- the professional judgement is correct;
- learning has occurred.

Those claims require separate evidence.

## Required distinctions

A conforming case must not collapse:

- teacher action and learner action;
- AI output and human performance;
- current task success and independent mastery;
- mastery and retention;
- retention and transfer;
- execution and responsibility;
- support and remediation;
- model terminology and EAI terminology.

## Unknown values

Unknown values are valid where information is absent or genuinely unclear. They should trigger a request for more information rather than an automatic negative or positive classification.

## Candidate conformance tests

The `tests/conformance/` directory will contain machine-readable cases that should either pass or fail for explicit reasons.
