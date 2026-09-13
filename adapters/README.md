# Model adapters

Model adapters connect an existing didactic, pedagogical or professional process model to the EAI Standard without rewriting that model.

An adapter is not a summary of a model. It is a mapping layer.

## Adapter requirements

Each adapter should provide:

- model name and version or source edition;
- model family, if useful;
- the model's own phase or process terminology;
- the model's original ordering, branching or return paths;
- purpose of each phase where the source model defines one;
- expected teacher/professional action;
- expected learner action;
- candidate core human actions;
- candidate microstructures;
- plausible AI actions in that phase;
- likely displacement points;
- evidence points;
- handback opportunities;
- remediation opportunities.

## What an adapter must not do

An adapter must not:

- replace the source model's terminology with EAI terminology;
- imply that a mapping is part of the source model;
- merge distinct models only because they are commonly grouped together;
- add phases that the source model does not contain without explicitly marking them as an EAI-side interpretation;
- turn a candidate core action into a universal core action.

## Direct and explicit instruction

A first deep adapter will be developed for a well-documented direct/explicit-instruction model. Related models and variants must remain distinguishable. `Direct Instruction`, `direct instruction`, `explicit instruction` and `EDI` should not be treated as synonyms without source support.

The adapter is intended to show how the same standard can describe both teacher and learner action inside a structured instructional process while preserving the original model.
