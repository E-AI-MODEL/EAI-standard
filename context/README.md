# Context overlays

Context overlays refine expectations without redefining the standard.

Planned or supported overlay dimensions include:

- age band;
- education sector;
- education level;
- subject or domain;
- curriculum reference;
- learning objective reference;
- assessment context;
- jurisdiction;
- externally defined legal or policy requirements;
- support needs where relevant to the educational design.

A context overlay may change the expected complexity, independence, evidence threshold, protection basis or examples used for a skill or microstructure.

It must not silently change the meaning of a core term such as `core_human_action`, `microstructure`, `human_evidence`, `protection_assessment`, `handback` or `transfer`.

## Jurisdiction overlays

Law and regulation belong in jurisdiction-specific overlays rather than in the universal semantic core. An overlay may identify a potentially applicable legal requirement and map it to an EAI protection dimension, but it must preserve:

- the original legal source;
- jurisdiction;
- applicability conditions;
- legal bindingness;
- uncertainty where applicability has not been established.

The first candidate jurisdiction overlay is [`eu-regulatory-protection.yaml`](eu-regulatory-protection.yaml), covering selected EAI-relevant mappings for the EU AI Act and GDPR. It is not legal advice and does not make a legal classification merely because an educational use resembles a listed category.

## Example

`recognise_counterargument` can remain the same microstructure across contexts while expected performance differs between an early learner, upper-secondary learner and university student.

The context layer should describe that expected performance rather than cloning the microstructure into unrelated definitions.

Likewise, the canonical protection requirement `PRT-04 effective_human_oversight` keeps the same EAI meaning while a jurisdiction overlay can state when a particular law makes that requirement legally binding in a concrete deployment.
