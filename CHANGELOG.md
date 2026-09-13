# Changelog

All notable changes to the EAI Standard are recorded here.

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
- learner retrieval-and-independent-performance microstructure registry;
- EDI conformance examples for `valid`, `unknown` and `invalid` human-AI allocations.

### Changed

- case schema is now strict and only permits non-canonical data through namespaced extensions;
- microstructure schema is strict and extension-aware;
- adapter schema now preserves original source elements before EAI mappings are added;
- conformance documentation now distinguishes structural validity, unknown information and normative violations;
- README now reflects the layered interoperability architecture and implemented adapter family;
- instruction-model evidence is explicitly separated from model identity and source description.

### Design rules

External models, context overlays and implementations may refine or present EAI semantics but may not silently redefine canonical terms or discard unsupported source information.

Model-family overlap does not imply equivalence. Evidence for one instructional model must not be silently transferred to another.

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
