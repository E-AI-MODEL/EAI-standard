# Scientific evidence layer

Scientific grounding is a first-order requirement of the EAI Standard.

The evidence layer is deliberately separate from the normative standard. Research can support, constrain or challenge a design choice, but a cited source does not automatically become a normative rule. Likewise, a normative rule must not be presented as empirically validated unless the relevant evidence supports that claim.

## Recency policy

For AI-specific claims, the primary evidence spine prioritises research from 2025-2026. Older sources are used only when they provide foundational learning-science theory, a uniquely relevant earlier experiment, model-definition evidence, or historical context that has not been superseded.

The current order of preference is:

1. recent peer-reviewed systematic reviews and meta-analyses;
2. recent peer-reviewed experiments and field studies;
3. recent peer-reviewed teacher/professional-practice research and measurement studies;
4. large-scale current datasets, with observational status made explicit;
5. recent preprints and working papers when they add evidence not yet available in peer-reviewed form;
6. older foundational or model-specific literature where no newer equivalent source exists.

Internal literature maps, prior reviews and project documents may be used for **source discovery**, but the public evidence files should cite the original scientific publication whenever possible.

## Three linked files

The scientific layer uses three complementary views:

- `sources.yaml` records source identity, design, publication status, scope, findings and limitations;
- `claims.yaml` expresses bounded scientific claims and identifies which sources support or qualify them;
- `construct-map.yaml` works in the opposite direction and shows which scientific claims support, bound or merely align with EAI rules, terms and registry families.

This prevents a bibliography from becoming a decorative appendix. A reviewer can move in either direction:

`source -> claim -> EAI implication`

or

`EAI construct -> evidence claim -> original source`.

## Claim-first structure

A bibliography alone is insufficient. `claims.yaml` contains bounded evidence statements and links each claim to the sources that support or qualify it. This makes it possible to inspect whether the evidence actually bears on the claim.

Each claim receives a candidate strength label:

- `A`: convergent support from multiple strong recent sources, normally including synthesis or complementary designs;
- `B`: strong but still bounded support, often from one or more peer-reviewed studies plus convergent evidence;
- `C`: promising or context-specific evidence, observational evidence, psychometric evidence or a narrower empirical base;
- `D`: early, indirect or predominantly conceptual evidence;
- `N`: normative design choice, not an empirical claim.

Strength belongs to the **claim**, not permanently to a source.

## Direct support versus alignment

`construct-map.yaml` distinguishes several relationships:

- `direct_support`: the evidence directly supports the distinction or constraint;
- `conceptual_alignment`: findings point in the same direction but do not validate the EAI construct itself;
- `boundary_support`: evidence supports a caution or non-inference rule;
- `context_support`: evidence is relevant only to a narrower model or implementation context.

This distinction is important for candidate concepts such as `core_human_action`, `microstructure` and `handback`. Current research can strongly motivate those distinctions without yet proving that the EAI operationalisation is the only or best measurement model.

## Mixed findings are required

The repository must not be constructed as a confirmation archive. Recent evidence includes both positive and negative results. For example, designed AI tutoring can improve learning in some contexts, while unrestricted answer provision or task outsourcing can improve immediate performance yet weaken later unaided performance in others.

The purpose of the evidence layer is therefore not to prove that AI is beneficial or harmful. It is to identify which distinctions are needed to describe conditions under which human-AI allocation changes learning, professional judgement or evidence quality.

## Model evidence and AI evidence are different

Model adapters have their own `sources.yaml` and, where useful, `evidence-links.yaml`.

A model-definition source answers a question such as: **what does EDI, Explicit Instruction or Direct Instruction actually specify?**

Scientific effect evidence answers a different question: **what evidence supports the effectiveness of a practice, mechanism or human-AI distinction?**

These are never silently merged. In particular, evidence for capital-D Direct Instruction is not treated as evidence for every form of direct or explicit instruction.

## Status distinctions

Every source is labelled by design and publication status. Peer-reviewed meta-analysis, field experiment, psychometric validation, policy dataset, preprint and working paper are not treated as interchangeable evidence.

Current examples include:

- 2026 meta-analytic evidence on GenAI and cognitive learning outcomes;
- 2026 longitudinal secondary-school evidence distinguishing homework performance from closed-book learning outcomes;
- 2026 international PISA evidence showing different associations for different forms of AI use;
- 2026 teacher research on epistemic agency, pedagogical judgement and professional agency;
- 2026 assessment-literacy research on task-boundary judgement and verification;
- 2025 field experiments on guarded versus unguarded AI support and designed AI tutoring.

## What the evidence does not yet validate

The scientific literature can support the distinctions used by the EAI Standard, but it does not by itself validate the standard as a measurement or interoperability instrument.

Before a stable 1.0 release, the standard still requires direct validation of at least:

- construct clarity of `core_human_action` and `microstructure`;
- inter-rater agreement when independent users classify the same case;
- discriminability between AI action categories;
- validity of handback and re-demonstration rules for the claims they are intended to support;
- usability across didactic, pedagogical and professional contexts;
- applicability across subjects, age groups and education sectors;
- interoperability across independent implementations.

That distinction is deliberate: **scientifically aligned** is not the same as **scientifically validated**.
