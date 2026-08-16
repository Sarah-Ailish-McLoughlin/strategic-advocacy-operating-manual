# Semantic Authority Boundary

> Status: proposed architecture decision for human review.

## Decision

The Strategic Advocacy Operating Manual owns the semantics required to describe **strategic advocacy practice**. It does not become the canonical ontology for lived experience, semantic sovereignty, generic provenance, generic evidence, participation theory, human rights, or human-impact judgement.

The repository therefore uses a three-layer semantic architecture:

1. **Strategic Advocacy Core** — advocacy-specific concepts owned and governed here.
2. **Boundary mappings and bridge relationships** — conservative links from advocacy concepts to externally governed concepts.
3. **External semantic authorities** — vocabularies, standards, and governed company knowledge that retain authority for their own domains.

This boundary supports the manual's human purpose while reducing semantic duplication and preventing machine validation from being mistaken for ethical, legal, community, or publication authority.

## Strategic Advocacy Core: owned here

The ontology may define and govern concepts whose meaning is specific to the operating manual, including:

- `AdvocacyMatter`
- `AdvocacyEffort`
- `AdvocacyGoal`
- strategic advocacy lifecycle stages
- advocacy strategy and tactic/action concepts
- stakeholder and power-analysis roles needed by the manual
- advocacy engagement
- advocacy-specific observations and review relationships
- advocacy outcomes as records of resulting states or changes
- accessibility requirements as they apply to advocacy practice

These concepts answer questions such as: what change is sought, in which system, with which actors, through what strategy and authorised action, with what observations and outcomes?

## Concepts that require external authority or conservative projection

Generic concepts such as `Agent`, `Evidence`, `Decision`, `Observation`, provenance, validation status, adoption status, participation frameworks, rights, and impact assessment should not silently acquire new universal meanings in this repository.

Where the manual needs them it may:

- use a version-pinned external vocabulary directly;
- define a narrow local projection for advocacy use;
- record a candidate mapping in `ontology/external-mappings.csv`; or
- defer the mapping where equivalence has not been established.

Label similarity is not sufficient evidence for `owl:equivalentClass`, `owl:equivalentProperty`, or other identity-strength mappings.

## McLoughlin.world boundary

Company knowledge currently describes the proposed McLoughlin.world information architecture as focusing on **semantic sovereignty, pattern recognition tools, and lived-experience-informed frameworks**, including proposed areas for a Splaining Taxonomy, lived-experience terminology, linguistic laundering, visual-language rules, systemic patterns, historical injustice, and safety signals.

That evidence makes McLoughlin.world a **candidate semantic authority** for those authored/lived-experience domains, rather than a reason to move them into this advocacy manual.

This is an authority-boundary decision, not an equivalence assertion. The currently identified McLoughlin.world source is a proposed site map; publication status, stable identifiers, versioning, and canonical term definitions must be verified before operational ontology mappings are promoted.

Accordingly:

- this repository may describe that an advocacy matter is informed by lived experience or concerns a systemic pattern;
- it must not reproduce or redefine McLoughlin.world taxonomies merely to make the advocacy graph self-contained;
- any future mappings to McLoughlin.world terms remain `candidate` until stable identifiers and human-reviewed semantics exist.

## Human rights, participation, and impact

A successful advocacy outcome is not intrinsically a human benefit and must not be typed as such merely because the advocacy objective was achieved.

The preferred pattern is to keep the observed `Outcome` distinct from a later **human-reviewed assessment** of effects, rights implications, benefit, harm, uncertainty, and participation.

A future bridge may need to express relationships such as:

- an advocacy matter `concernsRight` an externally governed rights reference;
- an engagement records a participation level or participation evidence;
- an outcome `hasImpactAssessment` an externally aligned assessment object;
- an assessment identifies affected people/groups, evidence, assessor/provenance, findings, uncertainty, and review status.

These relationships should be introduced only after competency questions and authority sources are approved. The repository must not create a broad `HumanBenefit` class that allows conformance or inference to stand in for human judgement.

## Participation before automated impact claims

Before introducing strong rights-impact semantics, the model should be able to answer:

1. Who was affected or potentially affected?
2. Who participated in framing, strategy, engagement, review, or assessment?
3. What accessibility or communication requirements applied?
4. What evidence records affected people's views or lived experience?
5. How did participation influence a decision or assessment?
6. Who made the final assessment and under what authority?
7. What evidence and provenance support the assessment?
8. Is the finding positive, negative, mixed, uncertain, disputed, or not yet reviewed?

These are competency questions, not assertions that every advocacy effort has satisfied them.

## External-authority policy

Candidate external authorities include established standards such as PROV-O and SKOS and, where fit-for-purpose and human-reviewed, rights/participation/impact vocabularies or normative references.

External bindings must record at minimum:

- local term or relationship;
- external vocabulary and stable identifier;
- mapping relation;
- mapping status;
- review note or rationale;
- version or retrieval reference when the external meaning may change.

Operational dependencies must fail closed when a required mapping is unresolved. A proposed or candidate mapping must not be treated as approved equivalence.

## Validation and authority

SHACL, parser, JSON-LD, schema, manifest, or other deterministic validation may establish only the conformance conditions explicitly tested.

Validation must not imply:

- advocacy quality;
- legal correctness;
- ethical justification;
- human-rights benefit;
- consent or community endorsement;
- authority to act for another person or group;
- publication approval; or
- permission to contact stakeholders or execute advocacy actions.

Humans retain authority over canonical semantic changes, strong mappings, consequential advocacy decisions, rights/impact judgements, stakeholder engagement, and publication.

## Promotion criteria for a separate shared ontology

Do **not** create a separate human-impact, participation, or semantic-sovereignty ontology repository merely because multiple concepts are related.

Consider extraction only when there is evidence of repeated cross-repository reuse and all of the following are available:

1. a clearly bounded domain not already governed by an existing authority;
2. multiple real consumers with compatible competency questions;
3. stable identifiers and versioning requirements;
4. an identified human governance owner;
5. mapping and deprecation policy;
6. executable conformance tests;
7. evidence that extraction reduces duplication rather than creating another semantic authority conflict.

Until those conditions exist, use narrow local bridge relationships and governed external mappings.

## Immediate implementation sequence

1. Keep the current advocacy ontology narrow.
2. Extend competency questions before adding rights/impact classes.
3. Review generic `Actor`, `Evidence`, `Decision`, and `Observation` projections against governed external owners.
4. Record external mappings conservatively and include version/retrieval provenance before making them operational dependencies.
5. Add validation fixtures that prove unresolved required mappings fail closed.
6. Add fixtures proving structural validation cannot create or infer human approval.
7. Add a machine-readable validation receipt that distinguishes conformance from quality, approval, and authority.
8. Introduce a small human-impact/participation bridge only when approved competency questions require it.

## Non-goals

This decision does not create an execution engine, a universal human-rights ontology, a universal evidence ontology, or a canonical McLoughlin.world ontology. It does not grant machines authority to determine human benefit, represent community consent, or make consequential advocacy decisions.
