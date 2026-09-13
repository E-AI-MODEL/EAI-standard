# Governance

EAI Standard is developed and maintained as a public, inspectable candidate standard.

The governance model is designed to support open standardisation, balanced stakeholder participation, transparent change management and sustainable maintenance.

## Canonical material

The authoritative list of canonical EAI Standard artifacts is maintained in:

- `standard/public-interface.yaml`

Governance documents, README files and explanatory documentation MUST NOT maintain an independent competing list of normative artifacts. If a discrepancy exists, `standard/public-interface.yaml` is the manifest that identifies the canonical public interface, and the discrepancy itself must be treated as a specification defect.

Documentation explains the standard but does not override canonical definitions, rules, vocabularies, schemas or conformance semantics unless that document is explicitly listed as canonical in the public interface manifest.

Registries, adapters, context overlays, evidence files, system profiles, examples and implementations are non-canonical layers unless a future release explicitly changes their status through the governance process.

## Normative language

Canonical requirement keywords follow BCP 14 as defined by RFC 2119 and RFC 8174. See `standard/normative-language.md`.

A canonical requirement expressed with `MUST` or `MUST NOT` is blocking for the conformance profile to which it applies. `SHOULD` requirements may be departed from only with an explicit rationale that does not conflict with another mandatory requirement.

## Roles

During the candidate phase the following roles are distinguished, even where one person temporarily fulfils more than one role:

- **maintainers**: manage releases, repository quality and merge decisions;
- **editors**: prepare normative text, schemas and documentation;
- **domain reviewers**: review educational, pedagogical and professional semantics;
- **implementation reviewers**: test whether the specification can be implemented consistently;
- **architecture reviewers**: assess interoperability, information modelling and alignment with sector architecture;
- **contributors**: propose issues, examples, adapters, evidence or changes;
- **users**: apply the standard in educational or technical settings and provide implementation feedback.

Before a stable 1.0 release, maintenance must no longer depend on a single individual.

## Open process

Normative development should be observable through the public repository.

Substantive proposals should normally be discussed through public issues and pull requests. A proposal that changes normative semantics should state:

- the problem being solved;
- the relevant use case;
- affected definitions or rules;
- examples before and after the change;
- compatibility impact;
- effect on teacher/professional and learner cases;
- effect on model adapters, registries and schemas;
- alternatives considered;
- evidence where empirical claims are made.

Decisions should be traceable to the proposal or discussion that motivated them.

## Decision making

During the candidate phase maintainers make merge and release decisions after public review where practical.

A normative change should be accepted because it improves semantic clarity, interoperability, implementation quality or educational applicability. It should not be accepted only because one stakeholder prefers a particular instructional model, product or technology.

A different presentation or grouping of existing semantics is not, by itself, sufficient reason to change the canonical information model. Canonical change should address a real semantic ambiguity, interoperability failure, missing distinction or testability problem.

Substantial changes should seek review from more than one stakeholder role. Disagreement should be recorded where it affects interpretation or future compatibility.

Before 1.0, a more formal multi-party decision model must be established and documented.

## Stakeholder balance

Development should actively seek input from both users and implementers. Relevant perspectives include:

- teachers and other education professionals;
- learners or learner representatives where appropriate;
- education organisations;
- suppliers and developers;
- educational researchers and domain experts;
- information architects and interoperability experts;
- public and sector organisations.

Participation does not imply endorsement of every normative choice.

## Versioning

`standard_version` identifies the EAI Standard release against which a canonical artifact is published.

Other version fields have narrower meanings:

- `artifact_version`: optional revision of an independently versioned non-canonical artifact;
- `source_version`: version of an external source represented through an adapter;
- `profile_version`: version of an optional profile format or profile instance.

A generic top-level `version` field is deprecated for canonical artifacts because it is ambiguous.

### Patch

Clarifications, spelling corrections, non-semantic examples and documentation repairs.

### Minor

Backward-compatible additions such as new canonical identifiers, optional fields, registry items, evidence types or adapters.

### Major

Changes to the meaning of canonical terms, required fields, normative rules or conformance behaviour.

Before 1.0, breaking changes may still occur in candidate releases, but they must be explicit, recorded in `CHANGELOG.md` and accompanied by migration information where existing implementations are affected.

## Identifiers

Canonical identifier and URI rules are defined in `standard/identifiers.yaml`.

Stable identifiers identify semantic concepts rather than repository file locations. Before stable 1.0, candidate identifiers may still change, but changes must be explicit. After 1.0, an identifier must not be silently repurposed for incompatible semantics.

## Evidence and normative choices

Scientific or external evidence may inform the standard, but evidence sources and normative design choices remain distinguishable.

A source does not become a rule merely because it is cited. A normative rule must not be presented as empirically validated unless supporting evidence warrants that claim.

## Conformance and uncertainty

Conformance and information completeness are separate result dimensions.

An artifact can conform while explicitly preserving unknown information. Unknown information becomes a conformance problem only when a profile requires information that is structurally absent, or when uncertainty is converted into a stronger unsupported claim or judgement.

See `standard/conformance-profiles.yaml`, `standard/diagnostics.yaml` and `docs/03-conformance.md`.

## Implementations and feedback

The standard should be tested in more than one implementation context before 1.0. Implementation experience should be documented sufficiently to show:

- where interpretation differed;
- which fields or rules were difficult to apply;
- whether independent implementations produced compatible representations;
- what changed as a result of the test.

## Licensing and intellectual property

Public availability of the repository is not, by itself, a complete licensing or intellectual-property policy.

Before EAI Standard is presented as a stable reusable open standard, the project must publish an explicit license and document any relevant intellectual-property contribution policy. No license is selected implicitly by this governance document.

The eventual policy should distinguish, where needed, between:

- normative specification text;
- machine-readable schemas and vocabularies;
- reference software or validators;
- contributed examples and mappings;
- third-party source material referenced by adapters.

## Maintenance and lifecycle

Stable releases require a documented lifecycle covering:

- ownership and maintenance responsibility;
- release cadence;
- backwards compatibility;
- deprecation;
- migration guidance;
- issue handling;
- security or urgent corrections where applicable;
- archival of superseded versions.

The candidate phase may use a lighter process, but the target is sustainable open maintenance rather than repository ownership by a single author.

## Candidate status

Before 1.0, definitions and structures may still change. Candidate releases should prefer semantic clarity over premature stability where the two conflict.

The development process is guided by the five Edustandaard assessment themes: added value, support/adoption, open standardisation, architectural alignment and future sustainability. See `docs/05-edustandaard-readiness.md`.
