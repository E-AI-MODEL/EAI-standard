# Roadmap

The roadmap follows two tracks at the same time:

1. build a semantically precise and independently implementable standard;
2. build the evidence, governance, architecture and adoption needed for eventual sector-wide registration.

The version headings below describe the current release plan, not a fixed promise that every activity can occur only in one version. Work may start earlier when that reduces later rework.

## 0.1.x-0.3.x — Foundation and reference cases

Completed or substantially implemented:

- model-independent definitions and normative rules;
- teacher/professional and learner as first-class actors;
- core human action and microstructure semantics;
- AI-action vocabulary;
- evidence, handback and remediation semantics;
- actor profiles and reusable microstructure registries;
- source-preserving model adapters;
- scientific evidence layer;
- machine-readable schemas;
- initial diagnostics and conformance fixtures;
- optional technical AI system profiles.

## 0.4.x — Standardisation hardening

Goal: make the existing semantics publishable as a coherent candidate standard without redesigning the substantive model.

Deliverables:

- one authoritative canonical manifest;
- formal normative language;
- explicit standard-version versus artifact/source/profile version semantics;
- stable canonical identifier classes and URI strategy;
- conformance separated from information uncertainty;
- canonical diagnostic effects;
- publication model for specification, machine contracts, conformance and implementation guidance;
- migration guidance for breaking candidate changes;
- documented license/IPR decision before stable open-standard positioning.

Exit condition:

An external implementer can determine from public repository material which artifacts are normative, which standard version they implement, how identifiers behave and how conformance results must be interpreted.

## 0.5.x — Semantic alignment

Goal: align the action-and-evidence standard with the EAI learning semantics before validator behaviour is further fixed.

Deliverables:

- canonical EAI Concept Positioning semantics: Education-native, Education-led, Shared, Technology-led and Technology-native;
- explicit rule that positions apply to meanings or constructs, not merely to words;
- learner-specific `core_learning_action` as a specialization of the broader `core_human_action`;
- canonical semantics for Education in the Loop, Task Density, Support-Replacement Boundary and Evidence-Function Shift where they materially affect interoperability;
- explicit distinction between meaning-making and visible addition or editing;
- design sequence preserving the order process -> process position/stage -> core learning action -> AI contribution -> Task Density;
- vocabulary provenance distinguishing EAI terms, EAI formalisations, EAI-specific meanings and common terms;
- machine-contract and migration design for the accepted semantic additions.

Exit condition:

An external implementer can distinguish human, educational and technical constructs before allocation analysis, can preserve the learner-specific meaning of the core learning action, and can implement the same semantic sequence without treating tool capability or output volume as educational meaning.

## 0.6.x — Executable conformance and reference implementation

Goal: make interpretation differences detectable by machines after semantic alignment.

Deliverables:

- release-versioned conformance suite;
- coverage of structural, allocation, evidence, handback, adapter, extension, uncertainty and semantic-positioning cases;
- automated canonical-reference checks;
- schema validation in CI;
- identifier uniqueness and reference-resolution checks;
- version consistency checks;
- first reference validator after 0.5 semantics are sufficiently fixed;
- implementation guide for developers.

Exit condition:

At least two independent implementations can represent the same cases and obtain compatible conformance outcomes against the published suite.

## 0.7.x — Pilots and adoption evidence

Goal: move from design plausibility to practical experience.

Deliverables:

- pilots in more than one education organisation or implementation context;
- participation from users and suppliers/implementers;
- documented interpretation problems;
- changes resulting from pilot feedback;
- implementation reports;
- public issue history showing how feedback was handled.

Exit condition:

There is evidence of useful application outside the originating project and no dependency on a single implementation.

## 0.8.x — Architecture positioning

Goal: prepare for sector architecture assessment.

Deliverables:

- precise interoperability problem statement;
- information model;
- actor and information-object model;
- architectural scope;
- overlap analysis with existing standards;
- first ROSA crosswalk;
- crosswalks to relevant international standards where they prevent duplication;
- clear distinction between canonical standard, registries, adapters, context profiles, system profiles and implementations.

Exit condition:

Architecture reviewers can determine where EAI Standard sits in the Dutch education information architecture, what existing standards it reuses or complements, and what lies outside its scope.

## 0.9.x — Open maintenance model

Goal: demonstrate sustainable governance.

Deliverables:

- multi-party maintainer/reviewer structure;
- public change procedure;
- lifecycle and deprecation policy;
- release policy;
- compatibility policy;
- explicit license and contribution/IPR arrangements;
- documented stakeholder participation;
- transparent decision records for material normative changes.

Exit condition:

Maintenance can continue independently of one person and new participants have a clear route to influence the standard.

## 0.10.x — Registration candidate

Goal: prepare a complete intake package for Edustandaard.

Deliverables aligned to the five official assessment criteria:

- **Toegevoegde waarde (added value):** business case, problem statement, alternatives and risk analysis;
- **Draagvlak (stakeholder support):** pilot evidence, users, suppliers and implementation experience;
- **Open standaardisatieproces (open standardisation process):** governance, participation and maintenance evidence;
- **Aansluiting op architectuur (architecture alignment):** ROSA positioning and architecture documentation;
- **Toekomstbestendigheid (future readiness):** lifecycle, extensibility, stable identifiers and supplier-neutral implementation.

The Dutch labels are retained because they are the official Edustandaard assessment terms. The English text is explanatory and does not replace those external terms.

Exit condition:

An external reviewer can answer the intake questions using public repository material plus documented pilot evidence.

## 1.0.0 — Stable standard

Version 1.0 requires more than specification completeness. It also requires:

- stable semantics;
- persistent canonical identifiers;
- executable conformance evidence;
- independent implementation experience;
- sustainable governance;
- explicit licensing/IPR conditions;
- a documented compatibility policy;
- sufficient stakeholder review;
- a clear architectural position;
- evidence that the standard solves a real interoperability problem.

Registration and 1.0 do not have to occur on the same date. The sequence will depend on the formal standardisation process and feedback received during intake and assessment.
