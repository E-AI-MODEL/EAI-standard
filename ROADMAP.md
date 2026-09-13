# Roadmap

The roadmap follows two tracks at the same time:

1. build a semantically precise and implementable standard;
2. build the evidence, governance and adoption needed for eventual sector-wide registration.

The second track is not postponed until the specification is finished. The development process should continuously produce the material needed to assess added value, support, openness, architectural fit and future sustainability.

## 0.1.x — Semantic foundation

Goal: stabilise the model-independent language of the standard.

Deliverables:

- scope and problem statement;
- core definitions;
- normative rules;
- teacher/professional and learner as first-class actors;
- process position without prescribing a universal instructional sequence;
- core human action and microstructure semantics;
- AI action vocabulary;
- evidence vocabulary;
- handback and remediation semantics;
- initial conformance rules.

Exit condition:

Two reviewers can describe the same simple case without major disagreement about the meaning of the core fields.

## 0.2.x — Actor profiles

Goal: develop the generic human-action layer for teachers/professionals and learners.

Deliverables:

- teacher/professional skill families;
- learner skill families;
- microstructure model for both actors;
- distinction between pedagogical, didactic, cognitive, metacognitive, social and professional actions where relevant;
- initial remediation patterns.

Exit condition:

The actor profiles remain usable without referring to one age group, subject, curriculum or teaching model.

## 0.3.x — First full model adapter

Goal: prove that an existing instructional model can connect to the standard without being rewritten by it.

Deliverables:

- selection and source documentation for a widely used direct/explicit instruction model;
- preservation of the model's own phase names and ordering;
- mapping of teacher and learner actions per phase;
- candidate core human actions per phase;
- allowed AI action descriptions;
- handback and evidence examples;
- adapter conformance tests.

Exit condition:

The adapter adds model-specific depth while the normative core remains unchanged.

## 0.4.x — Skills and microstructures registry

Goal: create reusable semantic registers for human actions.

First reference case: argumentation.

Deliverables:

- stable identifiers;
- family/skill/subskill/microstructure hierarchy;
- actor field;
- definitions and observable behaviour;
- AI-overwrite risk description where relevant;
- diagnostic signal;
- prevention;
- remediation;
- renewed human evidence;
- relation model without forcing a single hierarchy.

Exit condition:

The same microstructure can be referenced from more than one model adapter or educational context without duplication.

## 0.5.x — Machine-readable implementation

Goal: make the standard independently implementable.

Deliverables:

- JSON Schemas;
- validation fixtures;
- canonical identifiers;
- version metadata;
- conformance examples;
- valid and invalid test cases;
- generated human-readable exports where useful.

Exit condition:

At least two independent implementations can create and validate compatible representations of the same cases.

## 0.6.x — Pilots and adoption evidence

Goal: move from design plausibility to practical experience.

Deliverables:

- pilots in more than one education organisation or implementation context;
- participation from both users and suppliers/implementers;
- documented interpretation problems;
- changes resulting from pilot feedback;
- implementation reports;
- public issue history showing how feedback was handled.

Exit condition:

There is evidence of useful application outside the originating project and no dependency on a single implementation.

## 0.7.x — Architecture positioning

Goal: prepare for sector architecture assessment.

Deliverables:

- precise interoperability problem statement;
- information model;
- actor and information-object model;
- architectural scope;
- overlap analysis with existing standards;
- first ROSA crosswalk;
- distinction between normative core, adapters, profiles and implementations.

Exit condition:

Architecture reviewers can determine where the standard sits in the Dutch education information architecture and where it does not.

## 0.8.x — Open maintenance model

Goal: demonstrate sustainable governance.

Deliverables:

- multi-party maintainer/reviewer structure;
- public change procedure;
- lifecycle and deprecation policy;
- release policy;
- compatibility policy;
- documented stakeholder participation;
- transparent decision records for material normative changes.

Exit condition:

Maintenance can continue independently of one person and new participants have a clear route to influence the standard.

## 0.9.x — Registration candidate

Goal: prepare a complete intake package for Edustandaard.

Deliverables aligned to the five assessment criteria:

- **Toegevoegde waarde:** business case, problem statement, alternatives and risk analysis;
- **Draagvlak:** pilot evidence, users, suppliers and implementation experience;
- **Open standaardisatieproces:** governance, participation and maintenance evidence;
- **Aansluiting op architectuur:** ROSA positioning and architecture documentation;
- **Toekomstbestendigheid:** lifecycle, extensibility, stable identifiers and supplier-neutral implementation.

Exit condition:

An external reviewer can answer the intake questions using public repository material plus documented pilot evidence.

## 1.0.0 — Stable standard

Version 1.0 is not defined only by specification completeness. It also requires:

- stable semantics;
- independent implementation experience;
- sustainable governance;
- a documented compatibility policy;
- sufficient stakeholder review;
- a clear architectural position;
- evidence that the standard solves a real interoperability problem.

Registration and 1.0 do not have to occur on the same date. The sequence will depend on the formal standardisation process and feedback received during intake and assessment.
