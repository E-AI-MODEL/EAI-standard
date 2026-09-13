# Standard publication model

EAI Standard is not a single YAML file, schema or explanatory document. A stable release must publish the same semantics through several coordinated artifacts without allowing those artifacts to drift apart.

## Four publication products

### 1. Specification

The specification defines the meaning of canonical terms, relations, rules, identifiers and conformance behaviour.

The authoritative list of canonical specification artifacts is `standard/public-interface.yaml`.

### 2. Machine contract

Machine contracts define how canonical EAI information is represented and validated in data exchange.

Current machine contracts are JSON Schemas under `schemas/` plus canonical machine-readable vocabularies under `standard/`.

A schema is not the whole standard. Schema-valid data can still violate a semantic rule, and semantically valid EAI information may require profile-specific interpretation that cannot be expressed by structural JSON Schema alone.

### 3. Conformance

Conformance defines whether an artefact or implementation satisfies a selected EAI profile.

Conformance is separate from information completeness. A representation may conform while preserving unknown information. See `docs/03-conformance.md`.

The target publication set includes:

- conformance profiles;
- canonical diagnostics;
- versioned input fixtures;
- expected results;
- an executable test suite;
- later, a reference validator.

The reference validator must implement published semantics. It must not become the undocumented source of those semantics.

### 4. Implementation guidance

Implementation guidance explains practical application in software, education processes, model adapters, context overlays and human-readable interfaces.

Implementation guidance is non-canonical unless explicitly promoted through the governance process. It may offer patterns and examples but must not create new meanings for canonical fields or identifiers.

## One semantic source, multiple representations

The target architecture is:

```text
CANONICAL EAI SEMANTICS
         |
   +-----+------+----------------+
   |            |                |
   v            v                v
machine       human          conformance
contracts    documentation    test suite
   |            |                |
   +------------+----------------+
                |
        same released meaning
```

This does not require all documentation to be generated automatically. It does require release checks that can detect drift between canonical identifiers, referenced rules, schemas, versions and expected conformance results.

## Release consistency requirements

Before a candidate release is considered internally consistent, release tooling should be able to verify at least that:

- every file listed in `standard/public-interface.yaml` exists;
- every canonical artifact declares the intended `standard_version` where applicable;
- canonical identifiers are unique within their identifier class;
- references to canonical rule, diagnostic, evidence and action IDs resolve;
- JSON Schemas are syntactically valid;
- conformance fixtures validate against the published result schema;
- expected diagnostic IDs exist in the canonical diagnostic registry;
- non-canonical layers do not silently reuse reserved canonical namespaces;
- breaking candidate changes are represented in `CHANGELOG.md`.

## Human-readable views

Human-readable presentations may regroup the same information for different audiences. For example, a system profile may be displayed as identity, computation, data, action capability, human control, safety, evidence and change history even when the underlying machine representation uses another stable grouping.

A presentation change is not a semantic change unless information meaning, cardinality, constraints or interoperability behaviour also changes.

## Relationship to external standards

EAI can align or crosswalk with standards such as JSON Schema, OpenAPI, sector standards or AI-system standards without copying their full information models into EAI.

External standards should be reused where they already solve a generic interoperability problem. EAI should remain focused on its own semantic problem: describing and evaluating the distribution of meaningful human and AI action in education.
