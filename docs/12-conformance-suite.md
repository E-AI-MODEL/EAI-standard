# Conformance suite

The EAI conformance suite is the executable expression of already-published semantics. It is not the source from which semantics are inferred.

## Purpose

The suite should allow independent implementations to determine whether they interpret the same EAI release in compatible ways.

A conformance test case should specify the canonical `CP-*` profile, `standard_version`, input artefact, expected `conformance`, expected `information_state`, expected material diagnostics and the canonical rule being tested.

## Required test families

Before a reference validator is treated as authoritative tooling, the suite should cover at least:

1. required structural fields and canonical identifier references;
2. preservation of explicit unknowns;
3. multiple process positions and explicit core-action process anchors;
4. human and AI execution separation;
5. microstructure decomposition where allocation differs materially;
6. structured human evidence and claim-evidence fit;
7. supported performance versus independent mastery;
8. retention versus transfer;
9. handback and re-demonstration;
10. remediation followed by new evidence;
11. teacher/professional and learner actions in the same case;
12. structured human control, including nominal versus effective intervention authority;
13. source-preserving adapter behaviour and retained unmapped source elements;
14. context overlays that refine without redefining;
15. namespaced extensions;
16. detection/classification versus professional diagnosis;
17. pedagogical and relational judgement cases;
18. optional semantics retained without private reinterpretation;
19. conformance with material unknown information;
20. non-conformance caused by coercing unknowns into stronger claims;
21. dimension-specific protection assessment;
22. legal, scientific, framework and institutional protection bases remaining distinct;
23. protection authority overstatement and unresolved applicability;
24. machine, hybrid and human-review validator boundaries.

## Rule coverage matrix

`tests/conformance/machine-rule-matrix.yaml` is the coverage contract for rules classified as `machine` in `standard/rule-executability.yaml`.

Every machine rule requires an executable positive and negative fixture before a validator may be labelled the authoritative EAI reference validator. An unknown fixture is also required where explicit unknown information can change information state without causing non-conformance.

A `pending` entry is deliberately visible technical debt. It is preferable to an undocumented assumption that a rule has been tested.

## Expected-result rule

Tests should assert the smallest diagnostic set needed to establish the expected result. Validators should not be rewarded for emitting several diagnostics that merely restate the same semantic failure.

Additional non-blocking diagnostics may be permitted when independently true and when they do not change the expected conformance result.

A retained unmapped source element under `CP-04` may produce informational diagnostic `EAI-D015`; that diagnostic is not a conformance failure and does not by itself make the information state incomplete or unknown.

## Reference validator

A reference validator should validate canonical schemas, resolve references, evaluate machine rules, evaluate only the deterministic portion of hybrid rules, surface required human review, emit canonical diagnostics, preserve unresolved information and return conformance and information state separately.

It must not calculate a total EAI quality score, decide educational effectiveness, infer missing evidence, treat an unknown as failed or safe, or turn an example, adapter, scientific claim, legal overlay, LLM judgement or implementation heuristic into a new normative rule.

See `docs/17-validator-core-contract.md` for the implementation boundary.

## Release gate

The release process should execute the conformance suite in CI. A release should be blocked if a change to canonical semantics causes an unexplained change in expected conformance behaviour.

An implementation must not be labelled the authoritative reference validator while the machine-rule coverage matrix contains required `pending` fixtures.

Intentional breaking candidate changes before 1.0 must update expected fixtures, migration guidance and `CHANGELOG.md` together.
