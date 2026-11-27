# Proposal: evaluation scope in conformance results

Status: **open proposal for maintainer decision.** Non-canonical. Nothing in this directory changes the 0.5 candidate public interface.

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
                              "evaluation_stopped", "not_supported"]}
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```

Proposed normative text for `standard/conformance-profiles.yaml` (`result_model`):

- A result that reports `conformant` while one or more rules relevant to the selected profile were not decided SHOULD include `evaluation_scope`.
- A validator MUST NOT list a rule under `rules_decided` when it evaluated only the deterministic part of a hybrid rule.
- `evaluation_scope` does not change `conformance` or `information_state`. It states their coverage.

### 2. Canonical diagnostic for a generic schema failure

Add to `standard/diagnostics.yaml`:

```yaml
- code: EAI-D034
  severity: error
  effect: non_conformance
  label: schema_invalid
  message: The artifact does not validate against its canonical schema, and no more specific canonical diagnostic applies.
  related_rule: null
```

`related_rule: null` follows the existing pattern of `EAI-D015` and `EAI-D019`. Validators SHOULD prefer a rule-specific diagnostic when one applies.

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

`rules_not_decided` is shortened here: a complete result lists every hybrid and human-review rule that was not decided. The reader now sees that source-authority overstatement (`EAI-R030`, diagnostic `EAI-D024`) was not decided, which is exactly the problem in this case.

## Compatibility

- **Producers:** the field is optional. Existing 0.5 results stay valid in shape; only `standard_version` changes with the release.
- **Consumers:** a consumer that validates results against the 0.5 schema rejects a result containing `evaluation_scope`, because the result schema sets `additionalProperties: false`. This is a minor-version addition in the sense of `GOVERNANCE.md` (optional field), but consumers must update their schema copy. Version-pinned schema publication already supports this.
- **Validators:** the candidate reference validator already reports the same information in an extension (`implementations/reference-validator/`). It would move from the extension to the canonical field.
- **Adapters, registries, case schema:** unaffected.

## Alternatives considered

1. **A third conformance value** (`not_determined` or `conditionally_conformant`). Rejected: it merges coverage into the conformance verdict and breaks every consumer that switches on two values.
2. **One `uncertainty` diagnostic per undecided rule.** Rejected: it would make every machine-only result `contains_unknowns`, conflating missing review with missing case information, which `information_state` is defined to keep apart.
3. **A boolean `fully_evaluated`.** Simpler, but a reviewer then still has to work out which rules are open. Rejected in favour of listing them.
4. **Keep it in implementation extensions.** Works for one implementation, but two independent validators would not report coverage the same way, which defeats the 0.6 exit condition.

## Open points for the decision

- Should `rules_decided` and `rules_not_decided` be limited to rules relevant to the selected profile? That needs a canonical rule-to-profile mapping, which does not exist yet.
- Should a profile be allowed to require `evaluation_scope` (for example CP-06 full interoperability)?
- Is `EAI-D034` the right identifier, or should generic schema failure be expressed without a code?

## Related findings from the reference validator

Recorded in `implementations/reference-validator/README.md` and not part of this proposal: whether registry identifiers must resolve under `EAI-R020`, missing rules for dangling internal references, inconsistent use of `EAI-D020` in four example expectations, and whether `conditional` protection needs a basis under CP-07.
