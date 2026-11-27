# Candidate reference validator

Status: **candidate, not authoritative.** Version `0.1.0-candidate`, implementing EAI Standard `0.5.0-candidate`.

This is a first executable implementation of the [validator core contract](../../docs/validator-core-contract.md). It evaluates the machine-evaluable part of an EAI case and returns a result that validates against `schemas/conformance-result.schema.json`. Like everything under `implementations/`, it is not normative and does not redefine the standard.

## Usage

```bash
pip install -r scripts/requirements.txt
python implementations/reference-validator/eai_validator.py examples/edi-2.0/guided-practice-valid.yaml --profile CP-01
python implementations/reference-validator/run_fixtures.py
```

`eai_validator.py` prints the conformance result as JSON and exits with 0 for `conformant`, 1 for `non_conformant`. `run_fixtures.py` executes every fixture in `tests/conformance/machine-rule-fixtures.yaml` and the release gate in `tests/conformance/machine-rule-matrix.yaml`; `--report FILE` writes all results as JSON. CI runs the fixture suite on every pull request.

## What it does

The steps follow the processing contract:

1. Loads `standard/public-interface.yaml` and reads only the canonical artifacts it lists. A case that declares another `standard_version` is rejected with a local diagnostic.
2. Validates the case against `schemas/case.schema.json`. Each schema failure is mapped to the smallest canonical diagnostic for the rule whose representation boundary the schema enforces (for example a free-standing `microstructures` list → `EAI-D022`, a bare protection flag → `EAI-D023`).
3. On schema-valid input only, so one missing prerequisite does not cascade:
   - `EAI-R020`: AI actions, evidence types, protection requirements, concept positions and `eai_normative_rule` protection bases must resolve in the canonical vocabularies (`EAI-D026`);
   - `EAI-R027`: context, goal, actor and resolving `process_position_refs` (`EAI-D001`, `EAI-D002`, `EAI-D021`);
   - `EAI-R034`: `core_learning_action` only under a learner (`EAI-D029`);
   - explicit unknown markers are reported once as `EAI-D020` and listed in `retained_unknowns`, never resolved.
4. `conformance` is `non_conformant` when any diagnostic has effect `non_conformance`. `information_state` is `incomplete` when an anchor diagnostic is present, `contains_unknowns` when an uncertainty diagnostic is present, and `complete` otherwise.
5. The result carries an extension in this implementation's namespace that lists which rules were evaluated and which hybrid and human-review rules were **not decided**.

The validator contains no framework, jurisdiction, model-provider or LLM judgement. `EAI-R028` and `EAI-R029` are decided by the canonical schema; the validator only maps those failures to their diagnostics.

## Gate status

Against the six conditions in *Reference implementation gate* in the validator core contract:

| Condition | Status |
|---|---|
| 1. Loads the canonical manifest and declared standard version | done |
| 2. Executes every fixture in the green machine-rule matrix | done: 17 of 17 fixtures, including the hybrid structural fixtures |
| 3. Produces the expected schema result, conformance, information state and diagnostics | done for all fixtures |
| 4. Proves that referenced canonical identifiers and diagnostics resolve | done (in `scripts/validate.py` and in this validator) |
| 5. Runs the suite automatically in CI | added in this change |
| 6. No hidden framework, jurisdiction, provider or LLM judgement | by design; open to review |

Before this can be called authoritative it needs review by maintainers, and the open questions below need decisions in the standard.

## Open questions for the standard

These came up while implementing the contract. They are questions about the canonical artifacts, not bugs in this validator.

1. **"Conformant" for machine-only checks.** On the example cases in `tests/conformance/*-cases.yaml`, the validator returns `conformant` for four cases whose expected result is `non_conformant` because of hybrid rules (`EAI-D007`, `EAI-D008`, `EAI-D010`, `EAI-D024`). The validator is right not to decide those rules, but the result model has no field that says "hybrid rules not decided", so a bare `conformant` can be read as a full verdict. This implementation uses an extension for now. A canonical field (for example `evaluation_scope` or `rules_not_decided`) would make this interoperable.
2. **No canonical diagnostic for a generic schema failure.** A schema failure that does not belong to a specific rule (for example a wrong `claim_type` value) has no canonical code. This implementation emits `refval:schema_invalid`.
3. **Unclear whether registry identifiers must resolve.** `EAI-R020` covers skills, microstructures and remediation patterns, but their registries are non-canonical layers in the manifest. This implementation checks their syntax (through the schema) but does not resolve them.
4. **Dangling internal references have no rule.** A microstructure `evidence_refs` entry that names no `evidence_items[].id` is not tied to a canonical diagnostic. Not checked yet.
5. **Inconsistent use of `EAI-D020` in example expectations.** Four example cases expect `contains_unknowns` without `EAI-D020`, while `incomplete-context-unknown` and `teacher-routing-unknown` expect `EAI-D020`. This validator emits `EAI-D020` whenever explicit unknowns are present.
6. **Profiles do not yet change machine behaviour.** All profiles get the same structural checks. Profile-specific requirements (for example claim-matched evidence in CP-03) are hybrid.
