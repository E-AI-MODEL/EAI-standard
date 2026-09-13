# Protection assessment

A central EAI question is not merely **what AI does**, but **which aspects of a human action should remain human, remain directly evidenced, remain under effective human control, or be returned to the human after AI support**.

The EAI Standard represents this through a source-qualified protection assessment attached to a contextual core human action.

## Why protection comes after the core human action

Protection cannot be decided from a skill name or AI feature alone.

The same operation may need to remain human in one situation and be fully delegable in another. EAI therefore resolves protection only after the following are known:

```text
context
+ goal
+ actor
+ process position
        |
        v
core human action
        |
        v
microstructures when needed
        |
        v
actual human-AI allocation
        |
        v
claim and evidence requirement
        |
        v
protection assessment
```

For example, spelling correction may be delegable in a history task but may need human execution and evidence in a spelling-learning task. The action label is the same; the educational meaning is not.

## Protection is not one binary flag

`protected: true` would be too coarse because different dimensions can have different requirements.

The canonical protection dimensions are:

| ID | Dimension | Question |
| --- | --- | --- |
| `PRT-01` | human execution | Must the human personally perform the operation? |
| `PRT-02` | human judgement | Must the substantive interpretation or decision remain human? |
| `PRT-03` | human evidence | Must direct evidence of human performance or judgement remain available? |
| `PRT-04` | effective human oversight | Must a human meaningfully monitor and oversee the AI-supported process? |
| `PRT-05` | human authority to intervene | Must a human be able to reject, change, override, stop or otherwise intervene? |
| `PRT-06` | handback | Must an AI-supported or AI-performed action be returned to the human? |
| `PRT-07` | re-demonstration | Must new human execution be observed before a stronger claim is made? |
| `PRT-08` | direct human interaction | Must direct human interaction remain part of the process? |

A single case may therefore conclude:

```text
human execution              delegable
human judgement              required
human evidence               required
effective human oversight    required
human authority to intervene required
```

This is more precise than saying that "AI may support but not replace".

## Protection status

Each dimension receives its own status:

- `required`: an applicable EAI normative, legal or other binding basis requires it;
- `strongly_recommended`: strong, directly relevant evidence or recognised non-binding guidance supports it;
- `recommended`: relevant evidence or guidance supports it;
- `conditional`: the conclusion depends on an explicit condition;
- `delegable`: no protection requirement has been identified for that dimension within the recorded scope and bases;
- `unknown`: the available information is insufficient.

`delegable` is deliberately narrow. It does not mean universally safe, lawful or educationally effective. It means that the recorded assessment did not identify a reason to protect that dimension in the stated case.

## The basis must remain visible

Protection conclusions can come from materially different sources. EAI records the source type, applicability and bindingness separately.

The canonical basis types are:

- `eai_normative_rule`;
- `law_or_regulation`;
- `scientific_evidence`;
- `recognised_framework`;
- `professional_standard`;
- `institutional_rule`.

This distinction prevents three common category errors:

1. treating a scientific finding as if it were a legal obligation;
2. treating a non-binding framework as if it were mandatory law;
3. treating a legal requirement for human oversight as if it required the human to perform every underlying educational operation personally.

## Scientific protection proposals

The scientific evidence layer can support a recommendation about human execution, evidence, handback or re-demonstration without turning that recommendation into law.

Current candidate evidence patterns include:

### Independent mastery after AI support

Recent evidence supports the distinction between successful AI-supported performance and later unaided capability. When AI has materially performed a target cognitive operation and independent mastery is the claim of interest, EAI therefore recommends preserving direct human evidence and returning the operation to the learner before a stronger mastery claim is made.

The relevant bounded evidence claims are stored in `evidence/claims.yaml`, including `CLM-002`, `CLM-003`, `CLM-005` and `CLM-009`. The candidate protection mappings are in `evidence/protection-guidance.yaml`.

### Professional judgement

Recent teacher-AI research supports distinguishing professional judgement from tool operation, AI recommendation and nominal approval. Where the claim concerns human professional judgement, EAI can therefore recommend or require, depending on the applicable EAI rule and case, that substantive human judgement and evidence of that judgement remain visible.

### Retention and transfer

Retention and transfer are stronger claims than immediate supported task success. The protection assessment can therefore require or recommend later human evidence rather than treating the AI-supported product as sufficient.

## EU AI Act example

EU law is represented as a jurisdiction-specific context overlay rather than being embedded into the universal EAI semantics.

Regulation (EU) 2024/1689 lists several education and vocational-training uses in Annex III, including AI systems intended to determine access or admission, evaluate learning outcomes, assess the appropriate level of education a person will receive or can access, and monitor prohibited behaviour during tests.

That does **not** mean every educational AI system is automatically high-risk. Article 6(3) contains a derogation for specified Annex III systems that do not pose a significant risk of harm, including by not materially influencing the outcome of decision-making, when the stated conditions are met. Profiling within an Annex III use remains high-risk under that paragraph. Legal classification therefore has to be established separately.

Where a system/use is legally classified as high-risk and Article 14 applies, the AI Act requires effective human oversight. The assigned natural persons must, as appropriate and proportionate, be enabled to understand relevant capabilities and limitations, monitor system operation, remain aware of automation bias, interpret output, decide not to use or to disregard/override/reverse output, and intervene in or interrupt operation.

Article 26 also requires deployers of high-risk AI systems to assign human oversight to natural persons with the necessary competence, training and authority, as well as necessary support.

EAI maps those obligations primarily to:

- `PRT-04 effective_human_oversight`;
- `PRT-05 human_authority_to_intervene`.

It does **not** infer from those articles that every learning or professional microstructure must be executed personally by the human.

The source-preserving candidate mapping is in `context/eu-regulatory-protection.yaml`.

Official source: Regulation (EU) 2024/1689, ELI `https://eur-lex.europa.eu/eli/reg/2024/1689/oj`.

## GDPR example

Article 22 GDPR concerns decisions based solely on automated processing, including profiling, that produce legal or similarly significant effects. The article contains exceptions and safeguards; in specified cases those safeguards include at least the right to obtain human intervention, express a point of view and contest the decision.

EAI can record this as a potentially applicable legal basis for human intervention or authority, but applicability must be established separately. GDPR Article 22 and AI Act human-oversight requirements are not interchangeable legal rules.

Official source: Regulation (EU) 2016/679, ELI `https://eur-lex.europa.eu/eli/reg/2016/679/oj`.

## Recognised frameworks, professional standards and institutional rules

The same structure can represent other external requirements or evidence-informed frameworks, but EAI deliberately does not assign them a stronger status than their source warrants.

For example:

```yaml
requirement_id: PRT-02
status: recommended
bases:
  - type: recognised_framework
    reference: framework.example.section_4
    authority: Example authority
    applicability: applicable
    bindingness: non_binding
```

A school policy can also create a locally binding rule without being presented as national or European law.

## Example machine-readable assessment

```yaml
protection:
  dimensions:
    - requirement_id: PRT-02
      status: required
      rationale: The case requires accountable human professional judgement.
      bases:
        - type: eai_normative_rule
          reference: EAI-R009
          applicability: applicable
          bindingness: eai_normative

    - requirement_id: PRT-04
      status: required
      rationale: The deployed system is legally classified as high-risk and Article 14 applies.
      bases:
        - type: law_or_regulation
          reference: EU_AI_ACT_ARTICLE_14
          authority: European Union
          jurisdiction: European_Union
          source_uri: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
          applicability: applicable
          bindingness: legally_binding

    - requirement_id: PRT-01
      status: delegable
      rationale: Personal execution of the technical preprocessing step is not part of the intended professional judgement or evidence claim.
      bases: []
```

The schema permits an empty basis list for `delegable` or `unknown`, but a `required` conclusion must have an applicable binding or EAI-normative basis under the canonical interpretation rules.

## Protection and conformance are different

A protection assessment can be structurally conformant while concluding `unknown` because legal applicability or evidence remains unresolved.

Conversely, a protection assessment is non-conformant if it labels something `required by law` while its only basis is a non-binding framework or scientific study.

The standard therefore validates the **meaning and traceability of the assessment**, not whether every educational or legal conclusion is substantively correct in the real world.

## Boundary

EAI protection assessment is a standards mechanism for traceable human-AI allocation decisions. It is not legal advice, does not replace competent legal assessment, and does not make an educational intervention effective merely because the recommended protection pattern is followed.
