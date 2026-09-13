# Conformance

Conformance means that a case, registry item, model adapter or implementation uses the EAI Standard consistently enough to be exchanged, inspected and compared without silently changing meaning.

Conformance is **profile-specific**. Supporting one profile does not imply support for the full standard. Canonical profiles are defined in `standard/conformance-profiles.yaml`.

## Conformance states

A result uses one of three states:

- `valid`: required information is present and no blocking rule is violated;
- `unknown`: information needed for a substantive interpretation is absent, ambiguous or unsupported;
- `invalid`: a normative or schema requirement is violated.

`unknown` and `invalid` are deliberately different. Missing evidence is not the same as evidence of failure.

## Diagnostics

Validators should return structured diagnostics rather than only a Boolean result. Canonical diagnostic codes are defined in `standard/diagnostics.yaml` and exchanged using `schemas/diagnostic.schema.json` and `schemas/conformance-result.schema.json`.

Diagnostics may identify, for example:

- a missing goal;
- a missing process position;
- human and AI execution being conflated;
- a mastery claim without matching evidence;
- required handback not occurring;
- an adapter dropping or rewriting source-model content;
- an unnamespaced extension.

## Basic case exchange

A minimally interpretable case states:

- context;
- goal;
- actor;
- process position;
- at least one candidate/confirmed human action or an explicit unknown marker.

Richer profiles add human-AI allocation, evidence, handback, remediation or source-model mapping requirements.

## Conformance does not mean educational quality

A structurally conforming case can still be educationally weak. Conformance only means the situation is represented without collapsing required distinctions.

The standard does not certify that:

- the chosen teaching or pedagogical model is effective;
- the educational goal is appropriate;
- the AI system is accurate, safe or lawful;
- a professional judgement is correct;
- learning has occurred;
- a particular intervention will improve learning.

Those claims require separate evidence.

## Required distinctions

Depending on profile, a conforming representation must not silently collapse:

- teacher/professional action and learner action;
- AI output and human performance;
- current task success and independent mastery;
- mastery, retention and transfer;
- execution and responsibility;
- support, handback and remediation;
- source-model terminology and EAI terminology;
- missing information and negative judgement.

## Extensions

Non-canonical information is allowed only through namespaced extensions. A conforming implementation may retain an extension it cannot interpret. It must not reinterpret that extension as canonical EAI data.

## Test fixtures

`tests/conformance/` contains examples of `valid`, `unknown` and `invalid` results. These fixtures are intended to become part of an executable conformance test suite as the standard matures.
