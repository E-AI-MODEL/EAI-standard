# Architecture

The EAI Standard is organised as a layered interoperability specification. The layers are deliberately separated so that educational meaning, source-model mappings, context-specific expectations, technical AI-system description and software presentation do not become entangled.

## 1. Canonical standard

The canonical layer defines the shared semantics that independent implementations must interpret consistently.

It contains:

- canonical terms;
- canonical relations;
- AI action categories;
- evidence semantics;
- normative rules;
- stable identifier rules;
- diagnostics and conformance semantics;
- machine-readable schemas;
- normative-language rules.

The authoritative list is `standard/public-interface.yaml`. No other document maintains a competing canonical-file list.

The canonical layer is intentionally small. It does not contain a curriculum, teaching sequence, user interface, complete skills catalogue or generic AI governance framework.

## 2. Registries

Registries contain reusable educational content that instantiates standard concepts, for example:

- learner skills;
- teacher/professional skills;
- microstructures;
- evidence patterns;
- remediation patterns.

Registry content may grow without changing the meaning of the canonical standard. A registry item is not automatically a core human action. Core status remains contextual.

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

Scientific evidence is stored separately from canonical semantics. Evidence supports, qualifies or challenges bounded claims. A citation does not automatically create a rule, and a normative rule is not described as empirically validated unless direct validation exists.

## 6. Optional technical system profiles

`system-profiles/` describes technical AI-system configuration when that information is useful for audit, comparison or interpretation.

It is deliberately not part of the canonical EAI human-action standard. The bridge is:

```text
technical system configuration
        -> observed AI action
        -> human/AI allocation in the EAI case
```

A system profile can record capability, enabled deployment configuration, observed behaviour and evidence basis without making technical capability determine educational allocation.

## 7. Implementations

Software belongs outside the standard semantics. Implementations may include:

- validators;
- APIs;
- documentation sites;
- AI systems;
- dashboards;
- spreadsheet or document exports;
- learning-platform integrations.

A renderer or application may choose which supported semantics to display. It must not silently discard unsupported canonical or source-model information.

## Publication architecture

The same released meaning is expressed through four coordinated products:

```text
CANONICAL SEMANTICS
        |
  +-----+------+----------------+
  |            |                |
  v            v                v
specification  machine          conformance
               contracts        suite
        |
        v
implementation guidance
```

The specification defines meaning. Machine contracts define representation. Conformance defines correct interpretation. Implementation guidance explains practical use without adding canonical semantics.

See `docs/10-standard-publication-model.md`.

## Conformance and uncertainty

Conformance and information completeness are separate dimensions. A representation can be conformant while explicitly preserving unknown information.

This prevents missing information from being confused with standards failure and prevents a structurally correct representation from being treated as substantive proof.

## Public interoperability surface

`standard/public-interface.yaml` is the authoritative manifest of canonical artifacts that form the public interoperability contract.

Stable identifiers and candidate canonical URI rules are defined in `standard/identifiers.yaml`.

## Design invariants

The architecture follows three invariants:

> preserve meaning before presentation.

> preserve source semantics before mapping.

> do not change the canonical model merely because the same information can be presented more clearly in another view.

The standard describes educational meaning. Registries provide reusable content. Adapters preserve external models. Context overlays refine expectations. System profiles describe optional technical context. Implementations decide how the information is rendered or operationalised.
