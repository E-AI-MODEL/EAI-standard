# EAI Human Action Map

This is a non-normative, browser-based reference implementation of the Dutch Human Action Map candidate.

## Purpose

The interface helps an educator move from a broad verb to a more precise formulation of a possible learner action. It does not decide which action is the core learning action. That remains a contextual educational judgement.

## Interaction

1. Search or choose a verb.
2. Read its definition.
3. Explore nearby words and their distinctions.
4. Add the substantive object.
5. Add contextual precision.
6. Copy the resulting formulation into an EAI case at the core learning action step.

Example: wegen + de bruikbaarheid van twee bronnen + voor een historische vraag becomes: de bruikbaarheid van twee bronnen wegen voor een historische vraag.

## Run locally

Serve the repository root over HTTP and open implementations/human-action-map/index.html.

The implementation loads the four JSON data parts from registries/human-actions/nl/. It uses no external JavaScript libraries.

## Standard boundary

This implementation does not add canonical concepts, identifiers or conformance rules. It is a presentation and navigation layer over candidate registry content.
