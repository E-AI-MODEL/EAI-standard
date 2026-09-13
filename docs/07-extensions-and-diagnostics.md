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

## Conformance states

The standard distinguishes three states:

### valid

The required information is present and the selected conformance profile has no blocking violation.

### unknown

Information required for a substantive interpretation is absent, ambiguous or unsupported. `unknown` is not a negative score and not a schema failure by itself.

### invalid

A normative or schema requirement is violated.

The distinction is important. For example, not knowing whether independent re-demonstration occurred is different from knowing that a mastery claim was made without required re-demonstration.

## Diagnostics

Conformance should return diagnostics rather than only `true` or `false`.

A diagnostic contains:

- a stable code;
- severity;
- state;
- message;
- optional path to the affected data;
- optional reference to the related normative rule.

Canonical diagnostics use the `EAI-D` namespace defined in `standard/diagnostics.yaml`.

Implementations may add their own diagnostics, but must use a separate namespace.

## Retain unsupported information

An implementation may support only a subset of optional semantics. Unsupported information should be retained where technically possible and reported as `unknown` rather than discarded or converted into another meaning.

Adapters apply the same rule to external models: an unmapped source element remains part of the adapter.

## Conformance is profile-specific

A validator should report which profile it evaluated. Future profiles may include, for example:

- basic case exchange;
- full human-AI allocation;
- assessment evidence;
- model-adapter conformance;
- registry conformance.

Passing one profile does not imply support for all EAI Standard semantics.
