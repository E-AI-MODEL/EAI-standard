# Conformance suite

The EAI conformance suite is the executable expression of already-published semantics. It is not the source from which semantics are inferred.

## Purpose

The suite should allow independent implementations to determine whether they interpret the same EAI release in compatible ways.

A conformance test case should therefore specify:

- the selected canonical conformance profile identifier (`CP-*`);
- the `standard_version`;
- the input artefact or case;
- expected `conformance`;
- expected `information_state`;
- expected blocking diagnostics;
- expected uncertainty diagnostics where material;
- a short rationale identifying the canonical rule being tested.

## Required test families

Before a reference validator is treated as authoritative tooling, the suite should cover at least:

1. required structural fields;
2. preservation of explicit unknowns;
3. human and AI execution separation;
4. microstructure decomposition where allocation differs materially;
5. claim-evidence fit;
6. supported performance versus independent mastery;
7. retention versus transfer;
8. handback and re-demonstration;
9. remediation followed by new evidence;
10. teacher/professional and learner actions in the same case;
11. source-preserving adapter behaviour;
12. retained unmapped source elements;
13. context overlays that refine without redefining;
14. namespaced extensions;
15. detection/classification versus professional diagnosis;
16. pedagogical and relational judgement cases;
17. optional semantics retained without private reinterpretation;
18. conformance with material unknown information;
19. non-conformance caused by coercing unknowns into stronger claims.

## Expected-result rule

Tests should assert the smallest diagnostic set needed to establish the expected result. Validators should not be rewarded for emitting several diagnostics that merely restate the same semantic failure.

Additional non-blocking diagnostics may be permitted when they are independently true and do not change the expected conformance result.

A retained unmapped source element under `CP-04` may produce informational diagnostic `EAI-D015`; that diagnostic is not a conformance failure and does not by itself make the information state incomplete or unknown.

## Reference validator

A future reference validator should:

- validate structural JSON Schema constraints;
- apply canonical semantic rules that can be evaluated from the supplied data;
- emit canonical diagnostics;
- preserve unresolved information as unknown;
- return conformance and information state separately;
- identify the standard version and canonical conformance profile it evaluated;
- avoid hidden implementation rules that do not exist in canonical artifacts.

The validator should not:

- calculate a total EAI quality score;
- decide educational effectiveness;
- infer missing evidence;
- treat an `unknown` as a failed or safe state;
- turn an example, adapter or evidence claim into a new normative rule.

## Release gate

A future release process should execute the conformance suite in CI. A release should be blocked if a change to canonical semantics causes an unexplained change in expected conformance behaviour.

Intentional breaking candidate changes before 1.0 must update the expected fixtures and `CHANGELOG.md` together.
