# Implementations

This directory is reserved for implementation guidance and references. Implementations are not normative and must not redefine the EAI Standard.

Possible implementations include:

- validators;
- APIs;
- AI systems;
- documentation websites;
- dashboards;
- spreadsheet exports;
- learning-platform integrations;
- research tooling.

## Requirements

An implementation should declare:

- supported EAI Standard version;
- supported conformance profile or profiles;
- supported canonical artifacts;
- unsupported optional semantics;
- extension namespaces it understands;
- behaviour for retained unknown information.

An implementation may choose its own user interface and internal technology. Interoperability depends on preservation of canonical meaning, not presentation.

## Rendering

Presentation is intentionally outside the normative standard. A renderer may simplify or hide fields for a user interface, but stored or exchanged canonical data should not be silently altered or discarded.

## Validation

Validators should return structured conformance results using `schemas/conformance-result.schema.json` and the diagnostic codes in `standard/diagnostics.yaml`.
