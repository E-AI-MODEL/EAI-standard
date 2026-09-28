# Human Action Map

**Status:** candidate, non-normative registry and implementation input
**Language:** Dutch source layer (nl)

The Human Action Map helps an educator identify and formulate the human action that carries substantive meaning at a particular point in learning.

For learner cases, it is intended as a precision instrument for the EAI sequence:

process -> process position -> core learning action -> observed AI contribution

The map does **not** add a fifth step to that sequence. It is used while identifying and formulating the core learning action.

## What it contains

The current Dutch candidate contains 103 independently defined action verbs. Each entry contains the verb, a concise definition, nearby words, and a short distinction from those nearby words.

The relations form a semantic neighbourhood network. They are not levels, ranks or a cognitive hierarchy.

## Important boundaries

- A verb is not automatically a core learning action.
- Core status depends on the concrete process, process position, goal and context.
- A precise formulation normally adds the substantive object and contextual precision.
- Nearby words are navigation aids, not parent/child relations.
- Some related words are intentionally not independent entries.
- The Dutch definitions are candidate synthesis. Scientific and framework grounding is maintained separately in the evidence layer.
- This registry does not redefine canonical EAI vocabulary and is not part of standard/public-interface.yaml.

## Data

The candidate dataset is split into four JSON files under nl/. Splitting is a repository convenience only and has no semantic meaning.

The implementation under implementations/human-action-map/ loads these files and presents search, a local semantic neighbourhood and a simple formulation aid.

## Relation to existing learner skills

The existing learner skill registry remains intact. Skills such as LSK-020 analyse, LSK-026 evaluate, LSK-027 decide and LSK-048 reflect_on_process describe reusable capabilities. The Human Action Map is a finer-grained language and navigation layer for selecting and formulating the action in a concrete case. It must not silently replace existing skill identifiers or families.

## Language

Dutch is preserved here because this candidate was developed as a Dutch educational language instrument. If promoted beyond a localised registry, canonical English semantics and stable identifiers must be designed in line with the repository language and identifier policies.
