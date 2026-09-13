# Versioning and identifiers

EAI Standard separates the version of the standard from versions of supporting artifacts and external source material.

## Standard version

`standard_version` identifies the EAI Standard release against which a canonical artifact is published.

Example:

```yaml
standard_version: 0.4.0-candidate
```

A canonical artifact should not use an ambiguous top-level `version` field when that field could be read as either a standard version or an artifact revision.

## Other version fields

Use narrower fields when another object has its own lifecycle:

- `artifact_version`: revision of an independently versioned supporting artifact;
- `source_version`: version of an external source model represented through an adapter;
- `profile_version`: version of an optional profile format or concrete profile;
- model or deployment version fields inside a system profile remain technical system metadata and do not identify the EAI Standard release.

These version numbers may differ legitimately.

## Canonical identifiers

Canonical concepts intended for exchange use stable IDs such as:

- `EAI-R007` for a normative rule;
- `REL-009` for a relation;
- `AIA-09` for an AI action;
- `EV-03` for an evidence type;
- `EAI-D020` for a diagnostic;
- `CP-03` for a conformance profile.

Identifier patterns and the candidate URI namespace are defined in `standard/identifiers.yaml`.

## Canonical URIs

A canonical URI gives an EAI concept a globally scoped identifier independently of the repository file that currently stores it.

Conceptually:

```text
EAI-R007
  -> https://e-ai-model.github.io/EAI-standard/id/rule/EAI-R007
```

A URI identifies the semantic concept. It must not encode a branch name, commit-specific path or transient documentation location.

The presence of canonical URIs does not require JSON-LD, RDF or another semantic-web technology. Implementations may continue to exchange compact canonical IDs where the standard contract permits that.

## Candidate versus stable releases

Before 1.0, semantic learning may still require identifier changes. Such changes must be explicit and documented with migration impact.

After stable 1.0:

- an identifier must not be silently reassigned to incompatible semantics;
- an incompatible replacement receives a new identifier;
- the previous identifier may be deprecated but remains historically interpretable;
- textual clarification that does not change meaning may retain the same identifier.

## Local extensions

Third parties may define their own identifiers, but must use their own namespace and may not create identifiers that appear to be canonical EAI identifiers.

This allows local innovation without creating ambiguity about what belongs to the released standard.
