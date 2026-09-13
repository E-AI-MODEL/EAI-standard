# Edustandaard readiness

This document is **not a normative part** of the EAI Standard. It describes the development path toward a possible future submission to Edustandaard.

Development uses the five Edustandaard assessment areas as an ongoing quality check: **Toegevoegde waarde** (added value), **Draagvlak** (stakeholder support), **Open standaardisatieproces** (open standardisation process), **Aansluiting op architectuur** (architecture alignment) and **Toekomstbestendigheid** (future readiness).

## 1. Toegevoegde waarde (added value)

Goal: demonstrate that using the standard creates value compared with local, non-interoperable agreements and that the benefits outweigh possible disadvantages.

For EAI Standard this means demonstrating that multiple parties need shared semantics for describing human and AI action in educational processes.

Evidence required:

- concrete use cases involving multiple parties;
- a description of the problem without a standard;
- demonstrable reduction of local interpretation differences;
- comparison with existing standards and frameworks;
- explicit analysis of risks and disadvantages;
- examples in which the same description can be read or applied by different systems.

Current relevant artifacts:

- `docs/04-use-cases.md`;
- `docs/10-standard-publication-model.md`;
- `standard/public-interface.yaml`;
- source-preserving adapters and conformance cases.

Still required:

- an explicit problem statement;
- an alternatives analysis;
- practical evidence that multiple parties experience the same interoperability problem.

## 2. Draagvlak (stakeholder support)

Goal: demonstrate that providers and users have sufficient practical experience and that the standard is not supported only by its originating project.

For EAI Standard this means validation involving at least:

- education professionals;
- education organisations;
- AI or learning-technology suppliers;
- didactic and pedagogical experts;
- education architecture and interoperability experts;
- where appropriate, researchers and public-sector or sector organisations.

Stakeholder support does not mean agreement with every design decision. It means demonstrable participation, use experience, feedback and transparent handling of that feedback.

Evidence required:

- public issues and change proposals;
- pilot implementations;
- implementation reports;
- participating organisations or roles where they can be made public;
- documented decisions about received feedback;
- multiple independent implementations before a 1.0 candidate.

This remains a major open area.

## 3. Open standaardisatieproces (open standardisation process)

Goal: organise development and maintenance in an open, fair, clear, sustainable and accessible way.

The repository currently provides:

- an authoritative canonical manifest in `standard/public-interface.yaml`;
- formal normative language through BCP 14;
- public governance and contribution guidance;
- explicit version and identifier rules;
- separation between canonical standard, evidence, adapters, registries and implementations;
- traceable breaking candidate changes in `CHANGELOG.md`.

Still required before stable positioning as an open standard:

- an explicit license and IPR/contribution policy;
- formal multi-party decision-making;
- demonstrable external participation;
- documented lifecycle and deprecation procedures that are also used in practice.

Publicly readable on GitHub is not the same as legally reusable under an open license. That distinction must be resolved before 1.0.

## 4. Aansluiting op architectuur (architecture alignment)

Edustandaard evaluates alignment with the Dutch education sector architecture through a ROSA scan.

EAI Standard therefore needs to position clearly:

- which interoperability problem it solves;
- on which architecture layers it operates;
- which actors and information objects are involved;
- which existing standards or concepts are reused;
- where overlap with existing agreements exists;
- which elements are semantic, technical or organisational;
- what is explicitly outside scope.

The candidate standard now has a clearer publication and layering model, but formal architecture positioning is not yet complete.

Future artifacts required:

- `architecture/positioning.md`;
- `architecture/information-model.md`;
- `architecture/rosa-crosswalk.md`;
- targeted crosswalks to relevant international standards where they prevent duplication.

Important design principle: EAI should not reinvent generic AI system, risk, governance or identity standards where existing standards already solve those interoperability problems.

## 5. Toekomstbestendigheid (future readiness)

Goal: prevent the standard from becoming dependent on one product, model provider, AI generation, instructional model or temporary policy term.

Current design choices support this by:

- describing AI actions functionally rather than by brand or product;
- linking educational models through source-preserving adapters;
- treating age, level, subject and curriculum as context layers;
- keeping technical system profiles outside canonical human-action semantics;
- separating identifiers from repository file paths;
- namespacing extensions;
- separating conformance from information uncertainty;
- using one canonical manifest for the public interface.

Still required:

- persistent URI resolution before 1.0;
- automated version and reference checks;
- an executable conformance suite;
- independent implementations;
- compatibility and deprecation policy demonstrated across releases.

## Current readiness for candidate 0.4.0

**Semantic foundation:** advanced, still candidate.  
**Machine readability:** present, further consistency checks still required.  
**Conformance:** semantically hardened; executable suite and reference validator still to be built.  
**Identifiers/versioning:** contract present; persistent publication and automation still required.  
**Scientific grounding:** present as a separate evidence layer; direct validation of EAI constructs remains required.  
**Stakeholder support/pilots:** insufficient for registration.  
**Architecture/ROSA:** still to be developed.  
**Governance:** public foundation present; multi-party maintenance still required.  
**License/IPR:** unresolved and therefore a blocker for stable open-standard positioning and registration.

## When is an Edustandaard intake sensible?

Not when the specification is merely conceptually attractive. An intake becomes sensible once at least the following exist:

- stable scope and problem definition;
- a working machine-readable specification;
- an executable conformance suite;
- at least two independent implementation or pilot contexts;
- demonstrable user and supplier participation;
- a public change and maintenance process;
- explicit license/IPR conditions;
- initial architecture positioning and ROSA exploration;
- a concrete business case for sector-wide interoperability;
- a clear distinction between canonical standard, implementation guidance, adapters, registries and context profiles.

## Development principle

Edustandaard readiness is not a final documentation exercise. The assessment criteria are used as continuous design checks, but they must not drive additions that do not serve EAI Standard's own interoperability problem.
