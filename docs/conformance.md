# Conformance

Conformance means that a case, registry item, model adapter or implementation uses the EAI Standard consistently enough to be exchanged, inspected and compared without silently changing meaning.

Conformance is **profile-specific**. Supporting one profile does not imply support for the full standard. Canonical profiles are defined in `standard/conformance-profiles.yaml`. Machine-readable conformance results identify the selected profile by its canonical `CP-*` identifier, for example `CP-03`, rather than by the descriptive profile label.

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

The same rule applies to protection assessment. A case may conform while legal applicability or another protection basis remains `unknown` or `potentially_applicable`, provided the implementation does not upgrade that uncertainty into an unsupported `required` or `delegable` conclusion.

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
- a core human action that cannot be interpreted through context, goal, actor and process position;
- a microstructure represented as a parallel case action rather than a constituent operation of its core human action;
- human and AI execution being conflated;
- claim-evidence mismatch;
- required handback not occurring before a stronger human claim;
- a protection conclusion with no stated dimension or basis;
- a scientific or framework source being misrepresented as legally binding;
- protection status being copied across dimensions without separate assessment;
- an adapter dropping or rewriting source-model content;
- an unnamespaced extension;
- material information that remains explicitly unknown.

A retained source-model element without an EAI mapping is permitted under `CP-04`. `EAI-D015` may report that condition informationally, but it does not by itself create uncertainty or non-conformance.

## Basic case exchange

A minimally interpretable case states:

- context;
- goal;
- actor;
- process position;
- at least one candidate/confirmed human action or an explicit unknown marker.

A core human action must be interpretable through all four anchors even when some anchors are inherited from the enclosing case structure.

Richer profiles add human-AI allocation, protection assessment, evidence, handback, remediation or source-model mapping requirements.

A protection assessment is optional in a basic case. When reported, however, it must use the canonical dimensions and preserve the type, applicability and bindingness of its bases.

## Conformance does not mean educational quality, legal compliance or correctness

A conforming case can still describe an educationally weak or undesirable situation. Conformance only means the situation is represented without collapsing distinctions the standard requires.

The standard does not certify that:

- the chosen teaching or pedagogical model is effective;
- the educational goal is appropriate;
- the AI system is accurate, safe or lawful;
- a professional judgement is correct;
- learning has occurred;
- a protection recommendation is legally correct for the real-world deployment;
- a particular intervention will improve learning.

Those claims require separate evidence or competent assessment.

## Required distinctions

Depending on profile, a conforming representation must not silently collapse:

- teacher/professional action and learner action;
- core human action and reusable skill;
- core human action and its constituent microstructures;
- AI output and human performance;
- current task success and independent mastery;
- mastery, retention and transfer;
- execution and responsibility;
- human execution, human judgement, human evidence, oversight and intervention authority;
- scientific evidence, law, recognised frameworks, professional standards and institutional rules;
- support, handback and remediation;
- source-model terminology and EAI terminology;
- missing information and negative judgement;
- information uncertainty and conformance failure.

## Extensions

Non-canonical information is allowed only through namespaced extensions. A conforming implementation may retain an extension it cannot interpret. It must not reinterpret that extension as canonical EAI data.

## Conformance fixtures

`tests/conformance/` contains machine-readable expected outcomes for conformant, conformant-with-unknowns and non-conformant cases. Domain fixtures add expected diagnostics for instructional and pedagogical cases.

The fixtures are candidate release artifacts for the future executable conformance suite. A reference validator should be built against these semantics, not used to define them retrospectively.
