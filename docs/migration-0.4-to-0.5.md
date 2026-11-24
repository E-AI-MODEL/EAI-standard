# Migration from 0.4 to 0.5

Standard version: `0.5.0-candidate`. The previous validated candidate source is pinned in [schema-snapshots.json](../schema-snapshots.json).

| Contract | Migration |
|---|---|
| Canonical case and conformance result | The current schemas require `standard_version: 0.5.0-candidate`. Validate historical 0.4 records against their own pinned schema. Do not relabel an old result as a new executed conformance result. |
| Core human action | Existing IDs, labels, anchors, actor scopes, allocation and evidence fields are retained. Add the optional action kind only when supported by contextual information. Null indicates unresolved specialization; omission is not a learner classification. |
| Concept meanings | Optional array of distinct meanings with case-local IDs, term, meaning, position_ref and rationale. A null position preserves uncertainty. Position identifiers are POS-01 to POS-05. |
| Task density | Use existing observed allocation; do not convert output length or frequency into a score. |
| Profiles | CP-01 to CP-07 remain. CP-08 adds semantic alignment; CP-06 broad support now includes CP-08. Reassess profile support before declaring conformance. |
| Supporting artifacts | Existing artifact and source versions remain independent. A registry or adapter referencing an earlier standard is not automatically certified for the new profile. |
| Dictionary | The six promoted entries now link to canonical definitions. Remaining proposed concepts remain non-canonical. |

For version-only migration of a case that uses no new semantics, preserve all other fields, verify the structural contract, and record the migration. This does not establish new evidence, an action specialization, or a new conformance result. Preserve the original input and support conditions. Re-evaluate any substantive claim using the applicable 0.5 rule set and human review as required.

The publication workflow generates current schemas and version-specific copies from pinned Git sources. Once Pages is configured, archived 0.4 copies can remain available while the current candidate changes. Use the commit-pinned source if the live site is not enabled.

The structural CI tests are not a reference validator. The full rule-execution suite and independent implementation comparison remain the next roadmap stage.
