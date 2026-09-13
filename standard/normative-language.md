# Normative language

This document is part of the canonical EAI Standard public interface.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** in canonical EAI Standard artifacts are to be interpreted as described in BCP 14, RFC 2119 and RFC 8174, when and only when they appear in all capitals.

Ordinary lower-case uses of words such as “must”, “should” or “may” in explanatory documentation do not by themselves create normative requirements.

## Precedence

The authoritative list of canonical artifacts is `standard/public-interface.yaml`.

When two canonical artifacts appear to conflict, the conflict is a specification defect and must be resolved through the governance process. Implementations MUST NOT invent a private precedence rule that silently changes the meaning of the standard.

Non-canonical documentation, examples, evidence files, registries, adapters, system profiles and implementation material may explain or instantiate the standard, but MUST NOT override canonical semantics.

## Conformance language

A requirement expressed with **MUST** or **MUST NOT** is release-blocking for the conformance profile to which that requirement applies.

A **SHOULD** or **SHOULD NOT** requirement may be departed from only when an implementation has a documented reason and the departure does not violate another mandatory requirement. Such a departure may generate a warning without automatically making the implementation non-conformant.

A **MAY** requirement is optional and its absence is not a conformance failure.
