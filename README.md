# EAI Standard

**Status:** Candidate 0.4.0  
**Scope:** model-independent description of human action when AI participates in educational processes.

The EAI Standard does not prescribe a didactic or pedagogical model. It makes visible which human actions are intended in a concrete educational or learning situation, what role AI takes, what human evidence still matters, which human dimensions should remain protected, and what happens when AI performs an intended human action.

The same grammar applies to two primary actors:

- **teacher/professional**: didactic action, pedagogical action and professional judgement;
- **learner**: cognitive, metacognitive, social and self-regulatory action.

## Basic unit

Each description follows the same chain:

`context -> goal -> actor -> process position -> core human action -> microstructures -> AI action/allocation -> protection assessment -> human evidence -> handback -> remediation -> re-demonstration`

A **core human action** is context-dependent and is always interpreted through four anchors: context, goal, actor and process position. An action is not inherently protected or unprotected merely because of its name.

A **microstructure** is a smaller constituent human operation inside the selected core human action when decomposition is needed. Registry microstructures can be reused across skills and cases, but they do not form a parallel case level beside the core human action.

## Design rules

1. The standard does not define universal educational phases. An existing educational model keeps its own phases and terminology through an adapter.
2. A core human action is interpreted through context, goal, actor and process position.
3. A core human action may contain multiple microstructures.
4. In a concrete case, selected microstructures are constituent operations of the selected core human action.
5. Human execution and AI execution are recorded separately.
6. The amount of AI output is not a measure of task takeover. The relevant question is which intended human action AI performs.
7. AI output is not automatically evidence of human action or learning.
8. Current performance, independent mastery, retention and transfer are different evidence claims.
9. Unknown information remains `unknown`; missing information is not silently filled in.
10. When AI performs a core human action and a claim about human mastery or professional judgement is required, the action must be returned to the human and made visible again unless equivalent direct human evidence already exists.
11. Protection is assessed per human dimension and with an explicit basis. Scientific evidence, law, recognised frameworks and local rules are not interchangeable sources of authority.
12. An educational model may refine the standard but may not change the meaning of canonical concepts.
13. A different presentation of the same semantics is not a reason to change the canonical information model.

## Canonical standard and supporting layers

The repository is deliberately layered:

- [`standard/`](standard/) contains the canonical public interface: definitions, relations, rules, AI actions, evidence semantics, protection semantics, identifiers, diagnostics, conformance profiles and normative language;
- [`schemas/`](schemas/) contains machine-readable contracts associated with that interface;
- [`registries/`](registries/) contains extensible skills, microstructures and interventions;
- [`adapters/`](adapters/) contains **source-preserving** mappings to existing didactic, pedagogical and professional models;
- [`context/`](context/) contains overlays such as age, level, subject, curriculum, jurisdiction and externally defined requirements;
- [`evidence/`](evidence/) contains scientific grounding, claim-source mappings and evidence-informed protection guidance;
- [`system-profiles/`](system-profiles/) is a **non-normative technical companion layer** for the system configuration around an observable AI action;
- [`examples/`](examples/) contains worked cases;
- [`tests/`](tests/) contains conformance fixtures;
- [`implementations/`](implementations/) contains non-normative implementation material.

The **only authoritative list** of canonical artifacts is [`standard/public-interface.yaml`](standard/public-interface.yaml). Other documents refer to that manifest and do not maintain competing lists.

## Publication model

EAI distinguishes four publication products that must preserve the same semantics:

1. **Specification**: what the concepts and rules mean;
2. **Machine contract**: how that meaning is exchanged in machine-readable form;
3. **Conformance**: when an artifact or implementation applies the standard consistently;
4. **Implementation guidance**: how the standard can be used in concrete systems and educational contexts without introducing new canonical semantics.

See [`docs/10-standard-publication-model.md`](docs/10-standard-publication-model.md).

## Human and system are different analysis layers

The standard separates three questions:

1. **What can the technical system do and how is it configured?** This may optionally be described in a system profile.
2. **What does the system actually do in this task?** This is described with canonical AI actions.
3. **What does that AI action mean for the intended human action, required protection and available human evidence?** This is the EAI analysis.

```text
SYSTEM PROFILE
model + inference + orchestration + context + tools + autonomy
                         |
                         v
OBSERVABLE AI ACTION
question / hint / classify / recommend / perform / execute
                         |
                         v
EAI STANDARD
human action / allocation / protection / evidence / handback / remediation
```

The central boundary rule is:

> **Functional correspondence does not imply construct equivalence.**

A system may, for example, persist information, solve a novel task or recommend an intervention. That does not make system memory the same construct as human retention, novel system task performance the same as human transfer, or an AI recommendation the same as professional judgement.

See [`docs/09-human-system-boundary.md`](docs/09-human-system-boundary.md) and [`system-profiles/human-system-boundary.yaml`](system-profiles/human-system-boundary.yaml).

## Source-preserving adapters

An adapter does not rewrite an existing educational model into EAI terminology. The original source structure is preserved first. EAI mappings are added separately. A source element without a defensible mapping remains present and is explicitly marked as unmapped.

This prevents models such as Expliciete Directe Instructie 2.0 (EDI), Direct Instruction or Explicit Instruction from being simplified merely to fit the standard.

The first instruction adapters are candidates:

- [`adapters/explicit-instruction-archer-hughes/`](adapters/explicit-instruction-archer-hughes/): Archer & Hughes Explicit Instruction;
- [`adapters/edi-2.0/`](adapters/edi-2.0/): Expliciete Directe Instructie 2.0;
- [`adapters/direct-instruction-engelmann/`](adapters/direct-instruction-engelmann/): capital-D Direct Instruction in the Engelmann tradition.

The models are deliberately not merged. The family index in [`adapters/direct-explicit-instruction-family/`](adapters/direct-explicit-instruction-family/) makes overlap and structural differences visible without claiming equivalence.

## Human action and microstructures

In addition to broad teacher/professional and learner skills, deeper reusable registries currently cover areas including:

- argumentation;
- professional diagnosis and interpretation of learner evidence;
- scaffolding, feedback and fading support;
- pedagogical and relational professional judgement;
- retrieval, independent reperformance, retention and transfer;
- learner self-regulation and metacognition.

The registry index is in [`registries/index.yaml`](registries/index.yaml).

## Protection assessment

EAI can propose what should remain human, evidenced or under meaningful human control once the contextual core human action and actual human-AI allocation are known.

Protection is deliberately multi-dimensional. The standard separately represents:

- human execution;
- human judgement;
- human evidence;
- effective human oversight;
- human authority to intervene;
- handback;
- re-demonstration;
- direct human interaction.

Each dimension can be `required`, `strongly_recommended`, `recommended`, `conditional`, `delegable` or `unknown`. A single blanket `protected: true/false` flag is not conformant because it hides what is actually being preserved.

Protection conclusions are also source-qualified. EAI distinguishes an EAI normative rule, applicable law or regulation, scientific evidence, a recognised framework, a professional standard and an institutional rule. Their authority and bindingness must not be conflated.

The canonical vocabulary is [`standard/protection.yaml`](standard/protection.yaml) and the machine contract is [`schemas/protection-assessment.schema.json`](schemas/protection-assessment.schema.json). Evidence-informed candidate guidance is in [`evidence/protection-guidance.yaml`](evidence/protection-guidance.yaml). Jurisdiction-specific mappings, such as selected EU AI Act and GDPR requirements, remain in context overlays such as [`context/eu-regulatory-protection.yaml`](context/eu-regulatory-protection.yaml).

See [`docs/16-protection-assessment.md`](docs/16-protection-assessment.md).

## System profile companion layer

[`system-profiles/`](system-profiles/) can describe a concrete AI configuration without pulling technical system properties into normative EAI human-action semantics.

The existing eight-layer technical structure remains deliberately stable. Alternative human-readable groupings are treated as projections of the same information, not as reasons to redesign the semantic model.

The companion layer distinguishes:

- what a system **supports**;
- what is **enabled** in a deployment;
- what is actually **observed** in a concrete case;
- the **evidence basis** for a technical assertion.

It also distinguishes internal model checks, source verification, independent external verification and human verification.

## Conformance

From 0.4.0 onward, conformance and information uncertainty are separate result dimensions.

**Conformance:**

- `conformant`;
- `non_conformant`.

**Information state:**

- `complete`;
- `contains_unknowns`;
- `incomplete`.

An artifact can therefore be correctly represented according to the standard while still containing explicitly unknown information. Preserving uncertainty is not a failure. Silently turning that uncertainty into a stronger conclusion may be.

Conformance results use canonical profile identifiers such as `CP-01` and `CP-03`. Validators return structured diagnostics with a `severity` and a separate `effect`. See [`docs/03-conformance.md`](docs/03-conformance.md), [`standard/diagnostics.yaml`](standard/diagnostics.yaml) and [`standard/conformance-profiles.yaml`](standard/conformance-profiles.yaml).

## Identifiers and versions

Canonical concepts use stable identifiers such as `EAI-R007`, `EV-03`, `AIA-09`, `PRT-04`, `TSK-035`, `LSK-071` and `AIS-001`. [`standard/identifiers.yaml`](standard/identifiers.yaml) also defines a candidate strategy for globally identifiable HTTP URIs without requiring JSON-LD or RDF.

`standard_version` identifies the EAI Standard release. `artifact_version`, `source_version` and `profile_version` have narrower lifecycle meanings where needed. Generic top-level `version` is deprecated for canonical artifacts.

Normative terms such as `MUST`, `SHOULD` and `MAY` follow BCP 14. See [`standard/normative-language.md`](standard/normative-language.md).

## Language policy

English is the default language for canonical semantics, public documentation, registries and implementation guidance. Original-language terminology is preserved where it belongs to a source model, publication, proper name or external official framework. A translation or localised presentation may be added, but it must not silently replace or redefine canonical meaning.

For source-preserving adapters this means, for example, that official EDI source labels such as `Voorkennis`, `Begeleide inoefening` and `Kleine lesafsluiting` remain in their original Dutch form even though the adapter documentation and EAI interpretation are in English.

## Extensions

Local or vendor-specific data may be added only through explicitly namespaced extensions. An extension may not redefine a canonical concept. Implementations that do not understand an extension may preserve it without interpreting it.

## What the standard does not do

The EAI Standard:

- does not select a preferred didactic approach;
- does not prescribe a pedagogical theory;
- does not determine which tool or language model must be used;
- does not use a total score for "good" or "bad" AI use;
- does not bind the base standard to one age group, education level, subject, curriculum or jurisdiction;
- does not treat a produced final artifact as automatic evidence of learning;
- does not present structural conformance as evidence of educational quality or effectiveness;
- does not equate technical AI capability with human knowledge, learning, judgement or responsibility;
- does not convert scientific findings, external frameworks or legal sources into interchangeable forms of authority;
- does not provide legal advice or replace competent legal assessment;
- does not attempt to replace general AI risk, governance, security or system standards.

Level, age, subject, curriculum, jurisdiction and specific educational models are added as extensible context or source-preserving adapters.

## Scientific grounding

The evidence layer is separate from the normative standard. AI-specific claims prioritise recent research from 2025-2026. Claims are explicitly linked to sources and receive a provisional evidence-strength rating. A source does not automatically create a normative rule, and scientific alignment is not the same as direct validation of the standard itself.

Model adapters distinguish **model-definition sources** from **effectiveness evidence**. [`evidence/construct-map.yaml`](evidence/construct-map.yaml) provides the reverse view by showing which scientific claims support, constrain or merely align with an EAI rule, construct or registry. [`evidence/protection-guidance.yaml`](evidence/protection-guidance.yaml) uses those bounded claims to propose candidate protection patterns without presenting evidence as law.

## Governance and open-standard status

The repository is public and the change process is being developed for open standardisation. An explicit license and intellectual-property policy is still required before the standard can be positioned as a stable reusable open standard. No license is implied merely by public repository availability.

See [`GOVERNANCE.md`](GOVERNANCE.md) and [`docs/05-edustandaard-readiness.md`](docs/05-edustandaard-readiness.md).

## Version

The repository uses semantic versioning. Before 1.0, breaking candidate changes may still occur when they are explicit and documented.

Current version: **0.4.0-candidate**.
