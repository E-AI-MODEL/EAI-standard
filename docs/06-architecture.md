# Architecture

The EAI Standard is organised as a layered interoperability specification. The layers are deliberately separated so that educational meaning, source-model mappings, context-specific expectations and software presentation do not become entangled.

## 1. Normative standard

The normative layer defines the shared semantics that independent implementations must interpret consistently.

It contains:

- canonical terms;
- canonical relations;
- AI action categories;
- evidence semantics;
- normative rules;
- diagnostics and conformance states;
- machine-readable schemas.

The normative layer is intentionally small. It does not contain a curriculum, teaching sequence, user interface or complete skills catalogue.

## 2. Registries

Registries contain reusable educational content that instantiates standard concepts, for example:

- learner skills;
- teacher/professional skills;
- microstructures;
- evidence patterns;
- remediation patterns.

Registry content may grow without changing the meaning of the normative standard. A registry item is not automatically a core human action. Core status remains contextual.

## 3. Source-preserving adapters

Adapters connect an external didactic, pedagogical or professional model to EAI semantics.

The source representation is retained first. EAI mappings are added separately. An adapter must therefore be able to contain a source element that currently has no EAI mapping.

`source element -> optional EAI mapping`

is preferred over:

`source model -> rewritten EAI model`

This protects the integrity of the external model and makes mappings inspectable.

## 4. Context overlays

Context overlays refine expected complexity, independence or evidence for a particular environment, such as:

- education sector;
- age band;
- level;
- subject;
- curriculum;
- jurisdiction.

A context overlay may refine an expectation but may not redefine a canonical EAI concept.

## 5. Evidence layer

Scientific evidence is stored separately from normative semantics. Evidence supports, qualifies or challenges bounded claims. A citation does not automatically create a rule, and a normative rule is not described as empirically validated unless direct validation exists.

## 6. Implementations

Software belongs outside the standard semantics. Implementations may include:

- validators;
- APIs;
- documentation sites;
- AI systems;
- dashboards;
- spreadsheet or document exports;
- learning-platform integrations.

A renderer or application may choose which supported semantics to display. It must not silently discard unsupported canonical or source-model information.

## Public interoperability surface

`standard/public-interface.yaml` lists the canonical artifacts that form the public interoperability contract.

This separation allows a school, researcher, AI supplier and learning-platform supplier to exchange the same EAI case while presenting it differently.

## Design invariant

The architecture follows one invariant:

> preserve meaning before presentation.

The standard describes educational meaning. Registries provide reusable content. Adapters preserve external models. Context overlays refine expectations. Implementations decide how the information is rendered or operationalised.
