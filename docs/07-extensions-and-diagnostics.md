# Extensions and diagnostics

## Why extensions exist

Implementations often need local or vendor-specific data that does not belong in the shared standard. The EAI Standard therefore permits extensions only when they are explicitly namespaced.

An extension must not change the meaning of a canonical field.

Example:

```json
{
  "namespace": "https://example.org/eai/extensions/runtime",
  "version": "1.0",
  "data": {
    "interaction_id": "abc-123",
    "confidence": 0.81
  }
}
```

The namespace identifies the party responsible for the extension semantics. Implementations that do not understand the extension may retain it without interpreting it.

Unnamespaced extra fields are not part of the interoperability contract.

## Conformance and information state

From 0.4.0 onward, the standard does not use one `valid / unknown / invalid` axis for both standards compliance and substantive uncertainty.

Instead it reports two dimensions.

### Conformance

- `conformant`: the selected profile's structural and normative requirements are satisfied;
- `non_conformant`: at least one blocking requirement is violated.

### Information state

- `complete`: required information is available at the level needed for the intended interpretation;
- `contains_unknowns`: relevant uncertainty is explicitly preserved;
- `incomplete`: information needed to evaluate the selected profile is structurally missing.

This distinction is important. Not knowing whether a human judgement is supported is different from falsely presenting that judgement as established.

## Diagnostics

Conformance returns diagnostics rather than only `true` or `false`.

A diagnostic contains:

- a stable code;
- `severity`;
- `effect`;
- message;
- optional path to the affected data;
- optional reference to the related normative rule.

`severity` is one of:

- `info`;
- `warning`;
- `error`.

`effect` is one of:

- `none`;
- `uncertainty`;
- `non_conformance`.

Severity and effect must not be conflated. A warning may expose material uncertainty without blocking conformance. A canonical `MUST` violation should normally produce an error with `effect: non_conformance`.

Canonical diagnostics use the `EAI-D` namespace defined in `standard/diagnostics.yaml`.

Implementations may add their own diagnostics, but must use a separate namespace.

## Retain unsupported information

An implementation may support only a subset of optional semantics. Unsupported information should be retained where technically possible and reported without inventing another meaning.

An unsupported optional concept can therefore produce an uncertainty diagnostic while the surrounding artifact remains conformant.

Adapters apply the same principle to external models: an unmapped source element remains part of the adapter.

## Extension identifiers

Canonical EAI identifiers are reserved for the released standard. Local and third-party extensions use their own namespaces and must not mimic canonical identifiers in a way that makes local semantics appear standardized.

See `standard/identifiers.yaml`.

## Conformance is profile-specific

A validator must report which conformance profile and which `standard_version` it evaluated.

Current profiles include:

- basic case exchange;
- human-AI allocation;
- assessment evidence;
- source-preserving model adapters;
- registry items;
- full interoperability.

Passing one profile does not imply support for all EAI Standard semantics.

See `docs/03-conformance.md` for the full result model.
