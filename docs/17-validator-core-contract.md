# Framework-agnostic validator core contract

The EAI validator core evaluates EAI artefacts against a declared EAI Standard version and conformance profile. It is deliberately independent of instructional frameworks, AI providers, jurisdictions, user interfaces and storage systems.

## Boundary

The core answers a bounded question: does the supplied representation satisfy the machine-evaluable and explicitly represented requirements of the selected EAI conformance profile, and what material information remains unknown?

It does not decide whether an instructional framework is good, whether an intervention is effective, whether a legal regime applies when applicability requires legal interpretation, or whether a professional educational judgement is substantively correct.

Frameworks such as EDI or Explicit Instruction enter through source-preserving adapters. Jurisdiction-specific material enters through context overlays. Scientific findings enter through the evidence layer. None of these may add hidden rules to the validator engine.

## Processing contract

A conforming validator implementation should process an artefact in this order:

1. load the declared `standard_version` and canonical manifest;
2. load the selected `CP-*` conformance profile;
3. validate the artefact against its canonical JSON Schema;
4. resolve and validate canonical identifiers and internal references;
5. evaluate rules classified as `machine` in `standard/rule-executability.yaml`;
6. evaluate the machine-detectable portion of `hybrid` rules without manufacturing the unresolved judgement;
7. mark `human_review` requirements when their substantive conclusion is necessary for the requested interpretation;
8. determine `conformance` and `information_state` separately;
9. emit canonical diagnostics using `schemas/conformance-result.schema.json`.

## No hidden semantics

A validator MUST NOT create normative meaning that is absent from canonical EAI artefacts. In particular, an LLM, classifier, heuristic or implementation-specific policy MUST NOT silently convert a `hybrid` or `human_review` rule into a deterministic EAI rule.

An implementation may use AI to assist a reviewer, but the resulting judgement must be represented as supplied review input or evidence rather than as authority of the validator itself.

## Hardened case representation

The 0.4 candidate case contract uses:

- `process_positions[]` so a case can occupy more than one relevant process position;
- `primary_process_position` only as an optional presentation/routing aid;
- `process_position_refs[]` on each core human action so the four required anchors remain explicit;
- canonical `AIA-*` identifiers in `ai_actions[]`;
- structured `evidence_items[]` and microstructure `evidence_refs[]`;
- structured `human_control` instead of free-text responsibility;
- optional dimension-specific `protection` under a core human action.

The model does not require every core human action to be decomposed. Microstructures are required only when finer decomposition is necessary to distinguish materially different allocation, evidence, handback, remediation or protection states.

## Protection

`CP-07` validates the representation of a protection assessment. It can deterministically check dimensions, statuses and basis presence. It cannot by itself determine disputed legal applicability, scientific sufficiency for a new context or a professional judgement that has not been supplied as evidence or review input.

A legal source, scientific claim, recognised framework and institutional rule therefore remain distinguishable throughout validation. Authority overstatement remains hybrid because correctness of the external authority may require source or legal interpretation.

## Conformance versus review

The validator returns only what the supplied representation and canonical rules justify. A structurally conformant case can still contain unknowns. A case that requires unresolved human review may remain `contains_unknowns` or `incomplete` depending on the selected profile and intended claim. The validator must never fill the gap merely to produce a binary answer.

## Framework agnosticism test

The validator core fails its architectural purpose if adding a new instructional model, jurisdiction or scientific evidence source requires changing core validation code solely because of that model's vocabulary. Such additions should normally be representable through adapters, overlays, evidence mappings or data-driven canonical registries.

## Machine-rule fixture gate

The machine-rule coverage matrix is green at the specification level. `tests/conformance/machine-rule-matrix.yaml` contains no pending machine-rule fixtures. Every rule whose **complete normative meaning** is currently classified as `machine` has a deterministic positive and negative fixture in `tests/conformance/machine-rule-fixtures.yaml`.

The fixture work deliberately tightened the executability boundary. A rule is `machine` only when the complete rule can be decided from canonical structured data. A rule remains `hybrid` when a validator can check one structural fragment but cannot decide the complete normative meaning without contextual interpretation.

The current machine set is:

- `EAI-R020` stable canonical identifiers;
- `EAI-R027` four core-action anchors;
- `EAI-R028` constituent microstructure representation;
- `EAI-R029` source-qualified dimensional protection representation.

For example, `EAI-R002` is hybrid: presence of a process position is structurally checkable, but whether its terminology truly preserves the process or model actually being used is not. `EAI-R021` is also hybrid: namespace syntax is checkable, but whether local semantics are being passed off as canonical EAI semantics cannot be inferred from namespace syntax alone.

No separate unknown fixture is required for the four machine rules. Their machine-evaluable question is structural, referential or representational. Substantive uncertainty belongs to hybrid rules and to the separate `information_state` result rather than being forced into a false third outcome for these checks.

## Reference implementation gate

The specification-side fixture gate is now satisfied. This does **not** yet mean an authoritative reference validator exists.

The next gate is executable implementation verification. A validator may be labelled an authoritative reference validator only after software:

1. loads the canonical manifest and declared standard version;
2. executes every fixture in the green machine-rule matrix;
3. produces the expected schema result, conformance result, information state and canonical diagnostics;
4. proves that all referenced canonical identifiers and diagnostics resolve;
5. runs the same suite automatically in CI;
6. introduces no hidden framework, jurisdiction, model-provider or LLM judgement into machine validation.

A green matrix therefore means the validator core can now be implemented against a bounded test contract. It is not a substitute for passing that contract.
