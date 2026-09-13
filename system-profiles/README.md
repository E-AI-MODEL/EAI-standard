# EAI System Profile add-on

**Status:** candidate, non-normative companion layer  
**Purpose:** describe the technical AI system that participates in an EAI case without confusing system functionality with human learning, judgement or responsibility.

The EAI Standard analyses what a human is intended to do, what AI actually does in the situation, and what human evidence remains. A system profile answers a different question: **what technical system configuration is capable of producing those AI actions?**

The two layers are deliberately separated.

```text
SYSTEM PROFILE
what is the technical configuration?
        |
        v
OBSERVABLE AI ACTION
what does the system actually do in this task?
        |
        v
EAI STANDARD
what does that action mean for the intended human action and evidence?
```

## Three questions that must not be collapsed

1. **System capability**: what can the configured system potentially do?
2. **Observed AI action**: what does it actually do in the concrete workflow?
3. **Human-AI allocation**: what does that action mean for the learner or professional action that matters here?

A more capable model does not automatically justify more delegation. It only changes which operations may be technically substitutable. Whether substitution is educationally or professionally acceptable is analysed at the EAI layer.

## Functional similarity is not construct equivalence

A system may produce a convincing explanation, classify learner work, recommend an intervention, retain persistent data or solve a novel task. These functions do not by themselves establish human constructs such as:

- understanding;
- learning;
- professional judgement;
- responsibility;
- mastery;
- retention;
- transfer;
- metacognition.

The add-on therefore uses the rule:

> **Functional correspondence does not imply construct equivalence.**

For example, persistent system memory is not the same construct as human retention, and a model-generated recommendation is not the same construct as accountable professional judgement.

## Architecture

The system profile uses eight technical layers:

1. **Model**: model identity, version, modalities and base capabilities.
2. **Inference**: inference configuration, effort/compute settings, sampling and verification mechanisms.
3. **Orchestration**: routing, multiple models, agent loops and fallback behaviour.
4. **Context & data**: prompt context, retrieval, knowledge sources, memory and user/task context.
5. **Tools & actions**: search, code, external systems and permitted external actions.
6. **Application**: use case, workflow, interface, autonomy and human decision points.
7. **Evaluation**: task quality, reliability, robustness, cost, latency, safety and version behaviour.
8. **Governance & control**: authorisation, audit, override, escalation, accountable ownership and change control.

The machine-readable taxonomy is in [`capability-taxonomy.yaml`](capability-taxonomy.yaml).

## Relationship to canonical AI actions

The system profile does not replace [`standard/ai-actions.yaml`](../standard/ai-actions.yaml).

A system stack can be complex while producing a simple observable action such as `ask_question` or `retrieve`. Conversely, the same observable action can be produced by very different model, retrieval, tool and orchestration stacks.

Canonical AI actions therefore remain the bridge into an EAI case.

```text
model + inference + orchestration + context + tools
                         |
                         v
                observable AI action
                         |
                         v
         human microstructure / core action
```

## Optional integration

System profiles are an add-on, not part of the normative public interface. An EAI case can reference a system profile through the existing namespaced extension mechanism. This keeps interoperability around human-AI allocation possible even when a system profile is absent.

See:

- [`system-profile.schema.json`](system-profile.schema.json)
- [`human-system-boundary.yaml`](human-system-boundary.yaml)
- [`eai-system-profile-extension.schema.json`](eai-system-profile-extension.schema.json)
- [`examples/generic-agentic-llm.yaml`](examples/generic-agentic-llm.yaml)
- [`examples/eai-extension-example.yaml`](examples/eai-extension-example.yaml)

## Non-goals

This add-on does not:

- rank language models;
- define intelligence or consciousness;
- equate inference with human reasoning;
- infer human-like understanding from task performance;
- turn vendor-specific implementation details into EAI normative concepts;
- make system capability a substitute for analysing the concrete AI action.
