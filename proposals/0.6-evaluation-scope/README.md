# Proposal: evaluation scope in conformance results

Status: **open proposal; three open points decided on 27 November 2026, one new open point (A) pending; awaiting canonisation in 0.6.** Non-canonical. Nothing in this directory changes the 0.5 candidate public interface. An external review recommended adoption with three conditions; see [review summary](review-2026-11-27.md) and [Decisions](#decisions-27-november-2026).

Target: 0.6.x (executable conformance and reference implementation).

## Problem

A conformance result has two dimensions: `conformance` and `information_state` (`docs/conformance.md`). Neither says **which rules were actually decided**.

The validator core contract requires a validator to evaluate `machine` rules, evaluate only the deterministic part of `hybrid` rules, and leave `human_review` judgements to supplied review input (`docs/validator-core-contract.md`, steps 5 to 7). A validator that follows the contract correctly therefore returns `conformant` for a case whose only problems lie in hybrid or human-review rules.

The candidate reference validator shows this on the canonical example cases. For four of the eleven cases in `tests/conformance/*-cases.yaml`, the expected result is `non_conformant` because of hybrid diagnostics (`EAI-D007`, `EAI-D008`, `EAI-D010`, `EAI-D024`). The validator returns `conformant`, which is correct for its scope, but the result object cannot say so:

| Case | Expected | Machine-only result |
|---|---|---|
| `edi-2.0/small-closure-ai-takeover` | non_conformant (D007, D008, D010) | conformant |
| `pedagogical/ai-mediated-judgement-invalid` | non_conformant (D007, D009, D010) | conformant |
| `protection/science-as-law-invalid` | non_conformant (D024) | conformant |
| `protection/ai-product-mastery-invalid` | non_conformant (D007, D008, D010) | conformant |

A consumer that reads only `conformance` can mistake a machine-only `conformant` for a full verdict. That contradicts the boundary the standard draws: a validator "MUST NOT manufacture the substantive judgement" (`standard/rule-executability.yaml`), but the result format currently gives no way to report that a judgement was left open.

A second, smaller gap: there is no canonical diagnostic for a schema failure that belongs to no specific rule (for example an unknown `claim_type` value). Implementations must invent a local code.

## Use cases

- **Learning platform importing cases.** It must know whether `conformant` means "fully checked" or "structurally sound, review pending" before showing a case to teachers as validated.
- **Two independent validators (0.6 exit condition).** Their results can only be compared if both state which rules they decided. Otherwise one validator that decides fewer rules looks more lenient rather than narrower.
- **Teacher/professional review workflow.** A reviewer needs the list of rules that still need human review, instead of re-reading the whole case.
- **Learner cases.** Rules about learner evidence and handback (`EAI-R007`, `EAI-R010`) are hybrid. A learner record marked `conformant` without review must not be read as "the learner's evidence was checked".

## Proposed change

### 1. Optional `evaluation_scope` on the conformance result

Add an optional object to `schemas/conformance-result.schema.json`:

```json
"evaluation_scope": {
  "type": "object",
  "required": ["completed", "rules_decided", "rules_not_decided"],
  "properties": {
    "completed": {"type": "boolean"},
    "stopped_at": {"enum": ["standard_version", "schema_validation", null]},
    "rules_decided": {
      "type": "array", "uniqueItems": true,
      "items": {"type": "string", "pattern": "^EAI-R[0-9]{3}$"}
    },
    "rules_not_decided": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["rule", "reason"],
        "properties": {
          "rule": {"type": "string", "pattern": "^EAI-R[0-9]{3}$"},
          "reason": {"enum": ["hybrid_judgement_not_supplied", "human_review_not_supplied",
                              "evaluation_stopped", "not_supported", "not_applicable"]}
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

Proposed normative text for `standard/conformance-profiles.yaml` (`result_model`):

- A result that reports `conformant` while one or more canonical rules were not decided SHOULD include `evaluation_scope`.
- When `evaluation_scope` is present, `rules_decided` and the rules in `rules_not_decided` MUST together list every rule in `standard/rule-executability.yaml` for the declared standard version, each exactly once.
- A validator MUST NOT list a rule under `rules_decided` when it evaluated only the deterministic part of a hybrid rule.
- A rule that does not apply to the evaluated artifact (for example a case rule such as `EAI-R027` when an adapter is validated under CP-04) is listed under `rules_not_decided` with reason `not_applicable`, not under `rules_decided`. See open point A for how applicability is determined.
- `evaluation_scope` does not change `conformance` or `information_state`. It states their coverage.

Proposed addition to CP-06 (`full_interoperability`) in `standard/conformance-profiles.yaml`:

```yaml
requires:
  - evaluation_scope_reported
```

A CP-06 result therefore MUST include `evaluation_scope`. For every other profile it remains SHOULD.

### 2. Canonical diagnostic for a generic schema failure

Add to `standard/diagnostics.yaml`:

```yaml
- code: EAI-D034
  severity: error
  effect: non_conformance
  label: schema_invalid
  message: The artifact does not validate against its canonical schema, and no more specific canonical diagnostic applies.
```

Like `EAI-D015` and `EAI-D019`, the entry omits `related_rule`; the diagnostic schema also allows an explicit `null`. Validators SHOULD prefer a rule-specific diagnostic when one applies.

## Example before and after

Before (0.5, machine-only validation of `protection/science-as-law-invalid`):

```json
{
  "profile": "CP-07",
  "standard_version": "0.5.0-candidate",
  "conformance": "conformant",
  "information_state": "complete",
  "diagnostics": []
}
```

After:

```json
{
  "profile": "CP-07",
  "standard_version": "0.6.0-candidate",
  "conformance": "conformant",
  "information_state": "complete",
  "diagnostics": [],
  "evaluation_scope": {
    "completed": true,
    "stopped_at": null,
    "rules_decided": ["EAI-R020", "EAI-R027", "EAI-R028", "EAI-R029", "EAI-R034"],
    "rules_not_decided": [
      {"rule": "EAI-R030", "reason": "hybrid_judgement_not_supplied"},
      {"rule": "EAI-R031", "reason": "hybrid_judgement_not_supplied"}
    ]
  }
}
```

`rules_not_decided` is shortened here: a complete result lists all 33 rules that were not decided (31 hybrid, 2 human-review), so that the two lists together cover all 38 rules. The reader now sees that source-authority overstatement (`EAI-R030`, diagnostic `EAI-D024`) was not decided, which is exactly the problem in this case.

## Compatibility

- **Producers:** the field is optional. Existing 0.5 results stay valid in shape; only `standard_version` changes with the release.
- **Consumers:** a consumer that validates results against the 0.5 schema rejects a result containing `evaluation_scope`, because the result schema sets `additionalProperties: false`. This is a minor-version addition in the sense of `GOVERNANCE.md` (optional field), but consumers must update their schema copy. The 0.5 result schema also fixes `standard_version` to `0.5.0-candidate`, so a strict consumer must update for any 0.6 result, with or without this field. Version-pinned schema publication already supports this.
- **CP-06 claims:** an implementation that claims CP-06 must start reporting `evaluation_scope`.
- **Validators:** the candidate reference validator already reports the same information in an extension (`implementations/reference-validator/`). It would move from the extension to the canonical field.
- **Adapters, registries, case schema:** unaffected.

## Migration and communication

On canonisation, the 0.6 release should:

1. State in the CHANGELOG entry and the GitHub release notes that consumers validating results against the 0.5 result schema must switch to the 0.6 schema (published under `releases/0.6.0-candidate/`).
2. Add `docs/migration-0.5-to-0.6.md` with the field, the coverage rule, the CP-06 requirement, `EAI-D034`, and a before-and-after result.
3. Add non-normative implementer guidance to `docs/conformance.md`: when the field is expected (any `conformant` result with undecided rules, and every CP-06 result), how to fill `reason`, and that the field reports coverage, not quality.
4. Move the candidate reference validator from its extension to the canonical field, and use `EAI-D034` instead of its local `refval:schema_invalid`.

## Alternatives considered

1. **A third conformance value** (`not_determined` or `conditionally_conformant`). Rejected: it merges coverage into the conformance verdict and breaks every consumer that switches on two values.
2. **One `uncertainty` diagnostic per undecided rule.** Rejected: it would make every machine-only result `contains_unknowns`, conflating missing review with missing case information, which `information_state` is defined to keep apart.
3. **A boolean `fully_evaluated`.** Simpler, but a reviewer then still has to work out which rules are open. Rejected in favour of listing them.
4. **Keep it in implementation extensions.** Works for one implementation, but two independent validators would not report coverage the same way, which defeats the 0.6 exit condition.

## Decisions (27 November 2026)

The maintainer decided the three open points after the external review (condition 1 of the [review](review-2026-11-27.md)):

| Open point | Decision | Reason |
|---|---|---|
| Limit the lists to rules relevant to the profile? | No. The two lists together cover **all** canonical rules. | No rule-to-profile mapping exists; an ad hoc one would be a second truth next to the profile definitions. A full list is simple and comparable across validators. A mapping can be proposed separately later. |
| May a profile require `evaluation_scope`? | Yes, **CP-06 only**. SHOULD for all other profiles. | An implementation that claims full interoperability must report its coverage; an optional field nobody fills would not solve the problem. |
| Code for a generic schema failure? | **`EAI-D034`** (`schema_invalid`), `related_rule` omitted. | Results stay comparable; implementations no longer need local codes. |

## Open points after the decisions

**A. Which rules apply, and does the selected profile limit what is decided?** Two automated reviews on E-AI-MODEL/EAI-standard#15 showed that covering all rules raises two related questions:

- *Artifact type.* Some rules do not apply to the evaluated artifact, such as case rules when an adapter is validated under CP-04. `not_applicable` above gives them a place, but the standard does not yet state which rules apply to which artifact type, so two validators can classify the same rule differently.
- *Profile.* A rule can apply to the artifact while the selected profile does not require it, for example a profile-specific requirement such as CP-07's rationale-or-basis requirement for a delegable protection status when a case is validated under CP-01. None of the current reasons describes that accurately.

Options:

1. Add an `applies_to` list per rule (artifact types) in `standard/rule-executability.yaml` or `standard/rules.yaml`, and require validators to decide every applicable rule regardless of the selected profile. The profile then only determines which requirements count towards the profile's verdict. One canonical source, consistent with the decision not to create a separate rule-to-profile mapping.
2. Add the reason `not_required_by_profile` and leave applicability to validators. Simpler, but `not_applicable` and `not_required_by_profile` are then not comparable across implementations until a later release.

This needs a maintainer decision before canonisation.

## Related findings from the reference validator

Recorded in `implementations/reference-validator/README.md` and not part of this proposal: whether registry identifiers must resolve under `EAI-R020`, missing rules for dangling internal references, inconsistent use of `EAI-D020` in four example expectations, and whether `conditional` protection needs a basis under CP-07.
