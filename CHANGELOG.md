# Changelog

All notable changes to the EAI Standard are recorded here.

## 0.3.1-candidate

Non-normative AI system profile add-on and explicit human-system boundary.

### Added

- `system-profiles/` companion layer for technical AI-system description;
- eight-layer capability taxonomy covering model, inference, orchestration, context/data, tools/actions, application, evaluation and governance/control;
- strict JSON Schema for vendor-neutral system profiles;
- machine-readable human-system boundary matrix;
- explicit rule that functional correspondence does not imply construct equivalence;
- many-to-many bridge from system capabilities to observable canonical EAI AI-actions;
- optional namespaced extension schema linking an EAI case to a system profile;
- vendor-neutral agentic LLM system-profile example;
- worked EAI case showing a technical system profile alongside teacher professional judgement;
- human-system boundary documentation covering system memory versus retention, system novelty performance versus transfer, recommendation versus professional judgement and autonomy versus responsibility;
- machine-readable system-profile index;
- cross-cutting `status-evidence-contract.yaml` distinguishing system capability, enabled deployment configuration, observed case behaviour and evidential basis;
- strict `feature-state.schema.json` for machine-readable feature-state records;
- typed `verification-types.yaml` distinguishing internal consistency, model evaluation, tool verification, source verification, independent external verification and human verification;
- strict `verification-event.schema.json` for verification traces.

### Changed

- repository README now explicitly separates system capability, observable AI action and EAI human-AI allocation;
- repository status advanced to `0.3.1-candidate`;
- system-profile schema now accepts optional cross-cutting `feature_states` and `verification_events` while preserving the existing eight-layer structure;
- system-profile taxonomy now states explicitly that a different human-readable grouping of the same information does not require a new semantic structure;
- system-profile example now demonstrates the difference between `supported`, `enabled` and `observed`, including the provenance of those assertions;
- internal system verification is no longer semantically interchangeable with independent verification.

### Normative impact

None. The canonical EAI public interoperability surface remains unchanged. System profiles are optional and non-normative. Basic EAI conformance does not depend on model name, vendor, model size, benchmark score, orchestration complexity or the presence of a system profile.

The system-profile hardening deliberately adds semantic distinctions only where two implementations could otherwise mean materially different things. It does not replace the eight-layer profile with a new information architecture.

### Design rules

Technical capability changes what a system may be able to perform. It does not determine which human action should be delegated or what counts as evidence of human learning, mastery, retention, transfer, professional judgement or responsibility.

A clearer human-readable grouping of the same system information is a presentation view, not by itself a reason to revise the semantic standard.

`Supported`, `enabled` and `observed` are different statements. A provider claim, deployment observation and independent test are also different evidence bases.

## 0.3.0-candidate

Architecture hardening for interoperability and first deep model adapters.

### Added

- canonical public interface manifest;
- canonical relation vocabulary;
- structured diagnostic codes;
- explicit `valid`, `unknown` and `invalid` conformance states;
- profile-specific conformance model;
- namespaced extension schema;
- conformance-result and diagnostic schemas;
- source-preserving adapter schema and template;
- implementation boundary documentation;
- conformance fixtures for valid, unknown and invalid results;
- architecture and extension documentation;
- machine-readable adapter and registry indexes;
- source-preserving Archer & Hughes Explicit Instruction adapter;
- source-preserving EDI 2.0 adapter using current official public model artifacts;
- source-preserving capital-D Direct Instruction adapter based on current NIFDI model descriptions;
- model-family index that keeps Explicit Instruction, EDI and Direct Instruction distinct;
- adapter-specific source files separating model-definition sources from effectiveness evidence;
- teacher diagnostic-judgement microstructure registry;
- teacher scaffolding-and-feedback microstructure registry;
- teacher pedagogical-relational-judgement microstructure registry;
- learner retrieval-and-independent-performance microstructure registry;
- EDI conformance examples for `valid`, `unknown` and `invalid` human-AI allocations;
- pedagogical conformance examples showing valid human judgement, invalid nominal approval of AI judgement and explicitly preserved uncertainty;
- construct-level reverse evidence map linking EAI rules and registries to bounded scientific claims;
- diagnostic `EAI-D020` for claim-relevant information that remains explicitly unknown.

### Changed

- case schema is now strict and only permits non-canonical data through namespaced extensions;
- microstructure schema is strict and extension-aware;
- adapter schema now preserves original source elements before EAI mappings are added;
- conformance documentation now distinguishes structural validity, unknown information and normative violations;
- README now reflects the layered interoperability architecture, implemented adapter family and pedagogical coverage;
- instruction-model evidence is explicitly separated from model identity and source description;
- scientific evidence documentation now supports two-way traceability from source to claim and from EAI construct back to evidence.

### Removed

- superseded synthetic `adapters/explicit-instruction/` family adapter that combined recurring features from multiple instruction sources without preserving a single source model. It was replaced by distinct source-preserving adapters and a non-normative family index.

### Design rules

External models, context overlays and implementations may refine or present EAI semantics but may not silently redefine canonical terms or discard unsupported source information.

Model-family overlap does not imply equivalence. Evidence for one instructional model must not be silently transferred to another.

Pedagogical and relational professional judgement must remain representable without forcing the situation into a lesson-phase model.

## 0.2.x-candidate

Expanded content and scientific evidence layer.

### Added

- learner and teacher/professional skills registries;
- extended argumentation microstructure registry;
- remediation registry;
- recent-first scientific evidence methodology;
- 2025-2026 evidence sources and bounded claim-source mappings;
- interoperability use cases and Edustandaard-readiness guidance.

## 0.1.0-candidate

Initial repository structure and first normative layer.

### Added

- model-overstijgende scope en begrippen;
- docent/professional- en leerlingprofielen;
- normatieve regels voor kernhandelingen, AI-overname, bewijs, handback en remediatie;
- machineleesbare definities, AI-acties en evidence-types;
- eerste microstructure-registry voor argumenteren;
- eerste voorbeeldcase en conformance-structuur;
- adaptercontract voor externe didactische en pedagogische modellen.

### Deliberately not included

- vaste universele lesfasen;
- leeftijds- of niveaunormen;
- curriculumspecifieke doelen;
- totaalscore voor AI-gebruik;
- interne ontwikkelgeschiedenis of verwijzingen naar eerdere interne modellen.
