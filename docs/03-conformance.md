# Conformance

Conformance means that a case, registry item, model adapter or implementation uses the EAI Standard consistently enough to be exchanged, inspected and compared without silently changing meaning.

Conformance is **profile-specific**. Supporting one profile does not imply support for the full standard. Canonical profiles are defined in `standard/conformance-profiles.yaml`.

## Two separate result dimensions

EAI Standard separates two questions that must not be collapsed.

### 1. Conformance

- `conformant`: the artefact satisfies the structural and normative requirements of the selected profile;
- `non_conformant`: at least one blocking structural or normative requirement is violated.

### 2. Information state

- `complete`: the information required for the selected profile and intended interpretation is present;
- `contains_unknowns`: material uncertainty is explicitly retained;
- `incomplete`: required information is missing in a way that prevents the selected profile from being fully evaluated.

This means an artefact can be **conformant and still contain unknown information**. That is intentional. Preserving uncertainty can be the correct implementation of the standard.

For example, a representation that states that the evidence for a professional judgement is unavailable may still conform when that uncertainty remains visible and no unsupported stronger claim is presented. A representation becomes non-conformant when it silently turns the missing evidence into a substantive conclusion.

## Diagnostics

Validators return structured diagnostics rather than only a Boolean result. Canonical diagnostic codes are defined in `standard/diagnostics.yaml` and exchanged using `schemas/diagnostic.schema.json` and `schemas/conformance-result.schema.json`.

Each diagnostic has:

- a `severity`: `info`, `warning` or `error`;
- an `effect`: `none`, `uncertainty` or `non_conformance`.

These fields answer different questions. Severity communicates the seriousness of a finding to an implementer. Effect determines how the finding changes the conformance or information result.

An uncertainty diagnostic does not by itself make the artefact non-conformant. An error with `effect: non_conformance` blocks conformance for the relevant profile.

Diagnostics may identify, for example:

- a missing goal;
- a missing process position;
- human and AI execution being conflated;
- claim-evidence mismatch;
- required handback not occurring before a stronger human claim;
- an adapter dropping or rewriting source-model content;
- an unnamespaced extension;
- material information that remains explicitly unknown.

## Basic case exchange

A minimally interpretable case states:

- context;
- goal;
- actor;
- process position;
- at least one candidate/confirmed human action or an explicit unknown marker.

Richer profiles add human-AI allocation, evidence, handback, remediation or source-model mapping requirements.

## Conformance does not mean educational quality

A conforming case can still describe an educationally weak or undesirable situation. Conformance only means the situation is represented without collapsing distinctions the standard requires.

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
- missing information and negative judgement;
- information uncertainty and conformance failure.

## Extensions

Non-canonical information is allowed only through namespaced extensions. A conforming implementation may retain an extension it cannot interpret. It must not reinterpret that extension as canonical EAI data.

## Conformance fixtures

`tests/conformance/` contains machine-readable expected outcomes for conformant, conformant-with-unknowns and non-conformant cases. Domain fixtures add expected diagnostics for instructional and pedagogical cases.

The fixtures are candidate release artifacts for the future executable conformance suite. A reference validator should be built against these semantics, not used to define them retrospectively.
