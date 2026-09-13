# Migration from 0.3.x to 0.4.0-candidate

EAI Standard 0.4.0-candidate hardens standardisation mechanics. The substantive human-action model is not redesigned, but conformance serialization and canonical version metadata change.

## 1. Conformance result

### 0.3.x

```json
{
  "profile": "assessment_evidence",
  "state": "unknown",
  "supported_version": "0.3.0-candidate",
  "diagnostics": []
}
```

### 0.4.0

```json
{
  "profile": "CP-03",
  "standard_version": "0.4.0-candidate",
  "conformance": "conformant",
  "information_state": "contains_unknowns",
  "diagnostics": []
}
```

The old `state` field is removed from the canonical conformance-result schema. Conformance outputs now use the canonical `CP-*` profile identifier rather than the human-readable profile label.

Mapping guidance:

- old `valid` usually becomes `conformant` + `complete`;
- old `unknown` must be reviewed: it usually becomes `conformant` + `contains_unknowns` when uncertainty was correctly preserved, but may become `non_conformant` if an unsupported stronger claim was actually made;
- old `invalid` usually becomes `non_conformant`; information state must be determined separately.

Do not migrate `unknown` mechanically without reviewing what the old result meant.

## 2. Diagnostics

### 0.3.x

```json
{
  "code": "EAI-D020",
  "severity": "info",
  "state": "unknown",
  "message": "..."
}
```

### 0.4.0

```json
{
  "code": "EAI-D020",
  "severity": "info",
  "effect": "uncertainty",
  "message": "..."
}
```

`effect` now has three values:

- `none`;
- `uncertainty`;
- `non_conformance`.

This prevents warning severity, information uncertainty and standards failure from being encoded as one overloaded state.

## 3. Canonical version metadata

Canonical YAML artifacts now use:

```yaml
standard_version: 0.4.0-candidate
```

rather than an ambiguous generic:

```yaml
version: ...
```

`artifact_version`, `source_version` and `profile_version` remain available for narrower lifecycle meanings where appropriate.

## 4. Canonical manifest

`standard/public-interface.yaml` is the authoritative list of canonical artifacts.

Consumers should stop hard-coding an independent canonical-file list and use the release manifest as the publication contract.

## 5. Identifiers

Existing canonical IDs are retained unless separately documented. 0.4.0 adds a candidate URI strategy in `standard/identifiers.yaml`; implementations are not required to adopt JSON-LD or RDF.

Conformance result objects use the stable conformance-profile identifiers `CP-01` through `CP-06`. Human-readable labels such as `assessment_evidence` remain descriptive metadata in `standard/conformance-profiles.yaml`, not the exchanged profile identifier.

## 6. Normative language

Canonical all-capital requirement keywords now explicitly follow BCP 14 / RFC 2119 / RFC 8174.

Implementations should treat a violated applicable `MUST` or `MUST NOT` as non-conformance for the relevant profile.

## 7. Test fixtures

Replace assumptions based on:

- `valid-result.json`;
- `unknown-result.json`;
- `invalid-result.json`.

Use the 0.4 fixtures:

- `conformant-result.json`;
- `conformant-with-unknowns-result.json`;
- `non-conformant-result.json`.

Domain test fixtures now expose both `expected_conformance` and `expected_information_state`.

## What did not change

0.4.0 does not redefine:

- context;
- goal;
- actor;
- core human action;
- microstructure;
- AI-action semantics;
- evidence claim types;
- handback;
- remediation;
- source-preserving adapters;
- the optional system-profile boundary.

The release is intended to make those semantics more stable and independently implementable, not to replace them.
