# Semantic alignment in 0.5

Standard version: `0.5.0-candidate`. Explanatory document; the normative sources are identified in [the manifest](../standard/public-interface.yaml).

## Meaning before allocation

Terms such as memory, reasoning and learning can denote distinct constructs. Human retention and storage of earlier messages by software may both be called memory, but neither similar wording nor output establishes construct equivalence. The [canonical positions](../standard/concept-positioning.yaml) distinguish Education-native, Education-led, Shared, Technology-led and Technology-native meanings. Shared denotes a single relational construct, not the average of two meanings. The positions do not rank quality.

A case may record multiple `concept_meanings` entries for the same term, with a unique local ID, meaning, position reference and rationale. Use null for an unresolved meaning or position; do not substitute a guessed classification.

## The learner action

The contextual core human action remains the analysis unit for all actors. The optional `action_kind: core_learning_action` identifies the learner-only specialization on that very action. Professional judgement remains a core human action. The specialization depends on the goal and process position, not on which step is longest or most visible. For mixed human actors, separate learner actions where a learner-specific designation is required.

The educational process and position, intended human action, observed AI contribution, allocation, protection, evidence and handback form one analysis sequence. Education in the Loop requires educational intent to inform configuration rather than being inferred from technology.

## Task density and evidence

Task density concerns the extent to which AI performs the relevant core learning action. Use the existing microstructure allocation representation, not output length, prompt counts or a new scale. A short AI answer may perform the entire learning-relevant step. A long AI explanation can leave the target learner action to the learner. Suitability remains contextual.

Visible editing is not necessarily substantive meaning-making. When AI materially contributes to a product, assess evidence of the learner's own operation, independence, retention or transfer separately. A final product alone does not settle those claims, nor does material AI contribution prove that no learning occurred.

## Exchange and review

CP-08 represents semantic alignment. CP-06 includes CP-08. A structural test can reject a learner-only action designation under a professional actor and an invalid position identifier. It cannot establish construct equivalence, verify educational intent or determine whether an action carries the learning. See [rule executability](../standard/rule-executability.yaml), [conformance](conformance.md) and [migration](migration-0.4-to-0.5.md).
