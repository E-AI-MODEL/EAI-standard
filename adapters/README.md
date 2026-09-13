# Model adapters

Model adapters connect an existing didactic, pedagogical or professional process model to the EAI Standard without rewriting that model.

An adapter is not a summary of a model and not an EAI version of that model. It is a **source-preserving mapping layer**.

## Source first

The adapter stores the source model elements before adding EAI mappings. At minimum, it should retain:

- source-model name and reference;
- source version or edition where available;
- original source labels;
- source definitions where available;
- original ordering, branching or relations;
- source element type;
- source metadata needed to understand the element.

A source element may remain unmapped. Unmapped content must be retained and reported rather than removed.

## Mapping second

Mappings are separate records. Each mapping states:

- the source element being mapped;
- the EAI target or targets;
- mapping type;
- rationale;
- optional confidence.

Supported candidate mapping types are:

- `equivalent`;
- `partial_overlap`;
- `broader_than`;
- `narrower_than`;
- `related`;
- `none`.

A mapping is an EAI interpretation. It is never presented as if it were part of the source model itself.

## Adapter requirements

A conforming adapter should:

- preserve source terminology;
- preserve source structure and internal ordering;
- retain unmapped source elements;
- distinguish teacher/professional and learner mappings when relevant;
- map to stable EAI identifiers where possible;
- document interpretive mappings;
- use namespaced extensions for non-standard metadata.

## What an adapter must not do

An adapter must not:

- replace the source model's terminology with EAI terminology;
- silently drop source elements that have no EAI equivalent;
- imply that an EAI mapping is part of the source model;
- merge distinct models only because they are commonly grouped together;
- add source phases that the model itself does not define;
- turn a candidate core action into a universal core action.

## Direct and explicit instruction

The first deep adapters will focus on well-documented direct and explicit instruction models. Related models and variants remain distinguishable. `Direct Instruction`, `direct instruction`, `explicit instruction` and `EDI` are not treated as synonyms without source support.

These adapters will test whether the same EAI semantics can describe teacher and learner action inside structured instructional processes while preserving the original model intact.
