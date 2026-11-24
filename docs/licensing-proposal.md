# Licensing proposal

Status: **proposed, not adopted**. This document does not grant a licence or change the rights of contributors or third parties.

## Recommendation

Adopt the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0) for the EAI Standard's original material over which the relevant rights holders can grant that licence: the specification, machine-readable definitions and schemas, original examples, documentation, dictionary material and repository tooling.

Use one licence for that material so a school, researcher, developer or supplier can read the specification, reuse its schemas and build an implementation without having to reconcile separate software and documentation licences. The [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/main/LICENSE) is an example of a public specification using Apache-2.0.

## What this would permit

Apache-2.0 is permissive. Subject to its terms, recipients may use, reproduce, modify and distribute covered material, including in commercial and proprietary implementations. It includes a patent licence within the scope defined in the licence. Redistribution requires a copy of the licence, preservation of applicable notices, and prominent notices of changes to modified files. Where a NOTICE file applies, its attribution requirements also apply.

The licence does not require downstream implementations to publish their own source code merely because they use covered material. It does not grant general trademark rights or imply endorsement, registration or conformance to EAI.

## Third-party material and contributions

- External educational models, research articles, quotations, source labels, software dependencies and other third-party material are not relicensed merely because this repository contains or refers to them. Check their rights and preserve their source notices; remove or replace material where permission is missing.
- Original EAI mappings can be covered only to the extent that the relevant rights holders can license them. Identify material with separate terms explicitly.
- The name and any logos or trademarks are separate from the copyright and patent licence. Do not represent a modified specification or product as an official or certified EAI release without a documented basis.
- Establish who owns the original material and whether earlier contributions can be included. Do not assume that public visibility or a merged contribution gives the project all necessary rights.
- For future contributions, document the contribution terms in CONTRIBUTING.md. A Developer Certificate of Origin sign-off is an optional way to record the contributor's right to submit material; it is not proof that a third-party source can be relicensed.

## Alternatives considered

| Alternative | Reason not preferred for the combined repository |
|---|---|
| MIT | Simple, but does not contain the same explicit patent grant as Apache-2.0. |
| CC BY 4.0 for text and Apache-2.0 for code | Useful where content and software have clearly separate lifecycles, but creates an avoidable boundary for YAML/JSON specifications, examples and derived representations. |
| No general licence | Preserves current restrictions but leaves prospective adopters without clear general reuse permission. |

## Decision and implementation

Before adoption, the rights holders or authorized maintainer must approve the licence and review existing material and contributions. Then:

- Add the unmodified Apache-2.0 licence text as LICENSE.
- Identify the actual copyright holder(s) and any required attribution notices; add NOTICE and third-party notices where appropriate.
- Update README.md, GOVERNANCE.md, CONTRIBUTING.md and the release record to identify the adopted licence and exceptions.
- Check the repository and generated schema distribution for accurate notices. Make the publication version and licence scope clear.

The decision remains open until explicitly approved. No rights are granted by this proposal.
