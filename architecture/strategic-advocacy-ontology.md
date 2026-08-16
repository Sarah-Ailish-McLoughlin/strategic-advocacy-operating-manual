# Strategic Advocacy Ontology

> Status: proposed foundation model (v0.1). Structural/canonical implications require human review before merge.

## Purpose

This ontology provides a controlled semantic model for the Strategic Advocacy Operating Manual. It is intended to make core advocacy concepts and relationships explicit while remaining compatible with the repository's human-readable and machine-readable foundation.

It does not replace the lifecycle, governance rules, methods, playbooks, templates, manifests, or schemas. It provides a semantic layer through which those artefacts can be related consistently.

## Namespace

Suggested compact prefix: `SAO`

Suggested term pattern: `SAO:<PascalCaseTerm>`.

Persistent public URI design is deliberately deferred until a human-approved publication namespace exists.

## Core classes

### Actor

An individual, group, organisation, institution, or other participant that has a role in an advocacy context.

Candidate subclasses include Advocate, SelfAdvocate, Stakeholder, DecisionMaker, Organisation, Institution, Coalition, and Community.

### AdvocacyMatter

An issue, barrier, need, concern, rights matter, service matter, policy matter, or systemic condition that motivates or constrains advocacy.

### AdvocacyGoal

A desired change or condition pursued through advocacy. A goal may concern an individual outcome, service outcome, organisational change, policy change, or systemic change.

### AdvocacyEffort

A bounded body of strategic advocacy work with a defined matter, goals, actors, evidence, actions, observations, and outcomes.

### LifecycleStage

A stage in the repository's strategic advocacy lifecycle. The controlled values are Frame, Understand, Strategise, Design, Act, Observe, LearnAndAdapt, and CloseOrRenew.

### Evidence

Information or material used to understand a matter, support a claim, test an assumption, inform a decision, or evaluate an outcome. Evidence may include lived experience, records, data, correspondence, professional evidence, research, and observations.

### System

A social, administrative, organisational, policy, service, legal, educational, disability, health, community, workplace, or government context within which advocacy occurs.

### SystemElement

A component of a system relevant to advocacy, such as a rule, policy, procedure, decision point, accountability mechanism, complaint mechanism, incentive, or escalation pathway.

### Strategy

A reasoned approach for moving from the current situation toward an AdvocacyGoal under stated assumptions, constraints, risks, and uncertainty.

### AdvocacyAction

An authorised intervention or activity undertaken as part of an AdvocacyEffort, including communication, engagement, meeting, submission, negotiation, complaint, escalation, coalition building, or campaign activity.

### Decision

A material choice made by an authorised actor, including decisions about strategy, action, escalation, adaptation, closure, or renewal.

### Resource

A reusable artefact that supports advocacy work, including guidance, method, playbook, template, schema, manifest, checklist, script, or learning resource.

### Observation

A recorded signal, response, change, risk, assumption result, unintended effect, or other information observed during or after advocacy activity.

### Outcome

A resulting state or change associated with an AdvocacyEffort. Outcomes may include resolution, participation, influence, accountability, capability, policy change, organisational change, or systemic change.

### Indicator

A defined measure or observable signal used to assess progress, outcomes, assumptions, risks, or success conditions.

### AccessibilityRequirement

A requirement or format that supports equitable access to advocacy information or participation, including plain language, Easy Read, captioning, transcripts, alternative formats, or communication supports.

## Core relationships

| Property | Domain | Range | Meaning |
| --- | --- | --- | --- |
| `hasMatter` | AdvocacyEffort | AdvocacyMatter | identifies the matter addressed by an effort |
| `pursuesGoal` | AdvocacyEffort | AdvocacyGoal | identifies a desired change |
| `involvesActor` | AdvocacyEffort | Actor | associates an actor with an effort |
| `occursWithin` | AdvocacyMatter or AdvocacyEffort | System | identifies the relevant system context |
| `hasSystemElement` | System | SystemElement | identifies a relevant component of a system |
| `supportedBy` | AdvocacyMatter, Strategy, Decision, Outcome | Evidence | associates evidence with a claim or object |
| `usesEvidence` | Strategy, AdvocacyAction, Decision | Evidence | records evidence used in reasoning or action |
| `usesStrategy` | AdvocacyEffort | Strategy | associates an effort with a strategy |
| `implements` | AdvocacyAction | Strategy | identifies the strategy an action operationalises |
| `targetsActor` | AdvocacyAction | Actor | identifies an intended audience, stakeholder, or decision maker |
| `performedBy` | AdvocacyAction | Actor | identifies the actor undertaking an action |
| `occursAtStage` | AdvocacyAction, Decision, Observation | LifecycleStage | locates an object in the lifecycle |
| `producesObservation` | AdvocacyAction | Observation | associates an action with observed signals or responses |
| `informsDecision` | Evidence or Observation | Decision | identifies information contributing to a decision |
| `resultsIn` | AdvocacyEffort or AdvocacyAction | Outcome | associates work with an observed outcome without asserting sole causation |
| `measuredBy` | AdvocacyGoal or Outcome | Indicator | identifies a measure or success signal |
| `usesResource` | AdvocacyEffort or AdvocacyAction | Resource | associates reusable manual material with work |
| `requiresAccessibility` | AdvocacyEffort, AdvocacyAction, Resource | AccessibilityRequirement | records an accessibility requirement |
| `supersedes` | Resource, Strategy, Decision | same class | records an explicit replacement relationship |

## Semantic backbone

A useful graph pattern for the operating manual is:

`Actor -> participatesIn -> AdvocacyEffort -> hasMatter -> AdvocacyMatter -> occursWithin -> System`

and:

`AdvocacyEffort -> pursuesGoal -> AdvocacyGoal -> measuredBy -> Indicator`

with:

`AdvocacyEffort -> usesStrategy -> Strategy -> implementedBy -> AdvocacyAction -> producesObservation -> Observation -> informsDecision -> Decision`

Evidence can support matters, strategies, decisions, and outcomes throughout this graph.

## Lifecycle alignment

The ontology adopts the repository's existing eight-stage lifecycle rather than introducing a competing Assess/Plan/Activate/Review lifecycle:

1. Frame
2. Understand
3. Strategise
4. Design
5. Act
6. Observe
7. Learn and adapt
8. Close or renew

External or organisational process models may later be mapped to these stages using explicit mapping relationships rather than replacing the canonical repository lifecycle.

## Competency questions

The model should support questions such as:

1. What advocacy matter is this effort addressing, and in which system does it occur?
2. Which actors participate, hold decision authority, or are targeted by an action?
3. What goals and success indicators govern the effort?
4. What evidence supports a matter, strategy, decision, or claimed outcome?
5. Which strategy does an action implement?
6. At which lifecycle stage was an action, observation, or decision recorded?
7. What observations caused a strategy or plan to be adapted?
8. What outcomes were observed, and how were they measured?
9. Which resources and accessibility requirements apply to an action or effort?
10. Which objects have been superseded, and what provenance supports that change?

## Modelling rules

- Do not infer causation merely because an outcome follows an advocacy action; `resultsIn` records association unless stronger evidence is explicitly modelled.
- Distinguish evidence from decisions and observations from outcomes.
- Preserve human authority for canonical definitions and normative rules.
- Keep lifecycle stages controlled and aligned with `architecture/strategic-advocacy-lifecycle.md`.
- Treat accessibility as a cross-cutting requirement, not a specialist afterthought.
- Record provenance for externally mapped concepts and future vocabulary alignments.
- Prefer reuse or mapping to established vocabularies where semantic equivalence is demonstrated; do not assert `owl:equivalentClass` or equivalent identity without review.

## Relationship to the foundation object schema

The existing `schemas/advocacy-object.schema.json` describes repository artefacts and their provenance/status. Ontology classes describe domain meaning. These layers should remain distinct.

A later reviewed change may extend the schema with optional semantic identifiers or mappings, but this proposal intentionally avoids changing the existing foundation schema.

## Future machine-readable candidates

Subject to human review, subsequent increments may add:

- SKOS concept schemes for controlled vocabularies;
- RDF/OWL serialisation for classes and properties;
- JSON-LD context for repository objects;
- SHACL shapes for semantic validation;
- external mappings to schema.org, PROV-O, SKOS, Dublin Core, Wikidata, and domain-specific vocabularies;
- a governed identifier and deprecation policy;
- competency-question tests and example knowledge graphs.

These are candidates, not canonical commitments.