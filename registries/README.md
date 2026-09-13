# Registries

Registries contain reusable educational content that instantiates EAI Standard concepts without becoming part of the normative vocabulary itself.

Current registry families include:

- skills;
- microstructures;
- remediation interventions.

The registry index also exposes the cross-cutting AI-interaction skill inventory and candidate coverage audits.

## Registry rule

A registry item describes a reusable human capability, operation or intervention pattern. It does **not** become a core human action merely because it exists in a registry.

Core status remains contextual and depends on:

- actor;
- goal;
- process position;
- concrete educational or professional situation.

## Coverage is not assumed

The existence of a skill in a skill registry does not mean that the skill is already fully decomposed into microstructures.

The current teacher/professional and learner skill inventories are intentionally broader than the current deep microstructure coverage. This is explicit rather than hidden. The machine-readable audit is:

- [`coverage/skill-microstructure-coverage.yaml`](coverage/skill-microstructure-coverage.yaml)

The audit distinguishes:

- `deep`: current microstructures substantially cover the skill at action level;
- `partial`: material operations are represented, but action-level coverage is not yet complete;
- `none`: no current microstructure registry provides sufficient action-level coverage.

These are development states, not quality scores and not conformance states.

## When decomposition is needed

A dedicated microstructure registry is **not** required for every skill. Decomposition is most useful when a larger skill hides materially different:

- human and AI execution;
- evidence conditions;
- support levels;
- handback requirements;
- remediation routes;
- professional or learner regulation.

Where the same smaller operation recurs across skills, reuse is preferred over duplicating a separate decomposition for each parent skill.

## Cross-cutting AI-interaction skills

`skills/ai-interaction.yaml` describes human capabilities that become relevant when AI participates in a task. These skills do not create a separate human actor and do not replace teacher/professional or learner skills.

Their microstructure coverage should therefore reuse existing human-action microstructures wherever possible. A dedicated AI-interaction microstructure should only be added when a genuinely distinct human operation remains after reuse.

## Version metadata

Registries are non-canonical supporting artifacts and may have an artifact lifecycle separate from the EAI Standard release. New or materially revised registry files should prefer:

```yaml
standard_version: 0.4.0-candidate
artifact_version: x.y.z-candidate
```

Some earlier candidate registry files still use a generic top-level `version` field. In those files that value denotes the registry artifact revision, not the EAI Standard release. These files can be migrated when they are substantively revised; their legacy metadata does not redefine canonical version semantics.

## Stability

Registry items should use stable identifiers. Their descriptions may be refined in backward-compatible releases. A semantic change that would cause an existing identifier to mean something materially different should use a new identifier.

## Relations

Registry items may refer to canonical EAI relations, evidence types, AI actions and other registry items. Such links must not create a circular definition that makes the registry redefine the normative standard.

## Extensions

Registry-specific metadata that is not part of the shared schema must use namespaced extensions.

## Scientific support

Where a registry item carries a substantive educational claim, the claim should be linked to the evidence layer rather than presenting the registry entry itself as scientific validation.
