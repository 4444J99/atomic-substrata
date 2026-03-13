---
title: "2. Ontology Charter v1"
artifact_id: uaks_v1_ontology_charter_20260311
pair_id: CHATPAIR-007
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

2. Ontology Charter v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_ontology_charter_20260311
Version: 1.0-draft
Status: Draft normative charter


2.1 Purpose


This charter defines the canonical ontology for UAKS-v1. It establishes the first-class object families, the relation vocabulary, the trust model, and the boundary between evidence, interpretation, executable logic, and derivative analysis.


2.2 Ontological Thesis


The system MUST distinguish between:

Layer
Meaning
Source evidence
What existed in the raw corpus
Atomic knowledge
Governed, typed, reusable units extracted from or derived from sources
Derivative analysis
Structured findings produced by analytical systems about sources or atoms
Assemblies
Temporary or persisted renderings composed from atoms

A raw sentence in a source artifact is not ontologically identical to a normalized rule atom. A normalized rule atom is not ontologically identical to an analytical observation about rhetorical drift. These objects MAY be linked, but they MUST NOT be flattened into a single undifferentiated text object.


2.3 Core Object Families

Object Family
Role
First-Class
Atom
Abstract root type for atomic objects
Yes
TextAtom
Atomic textual meaning
Yes
CodeAtom
Atomic executable or technical logic
Yes
EvidenceAtom
Source-backed support or extracted datum
Yes
PolicyAtom
Normative rule or constraint
Yes
RelationAtom
Reified relation when relation itself needs metadata
Yes
RecipeAtom
Assembly plan as atomic object
Yes
AnalysisAtom
Normalized analytical finding
Yes
ObservationAtom
Direct analytical observation
Yes
InterpretationAtom
Inferential analytical conclusion
Yes
MetricAtom
Quantitative analytical output
Yes
TaxonomyProposalAtom
Proposed ontology/classification object
Yes
SignatureAtom
Persistent stylistic or structural pattern
Yes
DriftAtom
Temporal semantic/stylistic change pattern
Yes
AnalysisRunAtom
One analysis execution record
Yes
Entity
Referenced domain object
Yes
SourceObject
Registered source artifact
Yes
ProvenanceRecord
Lineage and transformation object
Yes

2.4 Root Atom Contract


All atom types inherit the same root obligations.

Constraint ID
Requirement
OC-ATOM-01
Every atom MUST have a stable logical identifier.
OC-ATOM-02
Every atom MUST have a content fingerprint or equivalent immutable state identity.
OC-ATOM-03
Every atom MUST have a declared type and class.
OC-ATOM-04
Every verified atom MUST have provenance.
OC-ATOM-05
Every atom SHOULD be independently interpretable within subtype rules.
OC-ATOM-06
Atoms MAY be superseded but MUST NOT be silently overwritten once verified.

2.5 Atom Families


2.5.1 TextAtom


A TextAtom is the smallest governed unit of textual meaning that can stand alone without hidden local context.


Typical uses include requirements, documentation clauses, notes, claims, normalized statements, and descriptive assertions.


2.5.2 CodeAtom


A CodeAtom is the smallest governed unit of executable or technical logic suitable for dependency reasoning, traceability, impact analysis, and reassembly.


CodeAtom categories MUST include at least:

Code Kind
FUNCTION
METHOD
CLASS
MODULE
CONFIG
QUERY
SCRIPT_STEP
TEST_CASE
SCHEMA_UNIT
UI_COMPONENT
INFRA_UNIT

2.5.3 EvidenceAtom


An EvidenceAtom is a source-backed support unit. It anchors claims, observations, or interpretations to extractable evidence.


Examples include measured values, cited statements, source fragments, or exact spans needed for verification.


2.5.4 PolicyAtom


A PolicyAtom is a normative unit expressing what SHOULD, MUST, MAY, MUST NOT, or SHOULD NOT happen in an operational, legal, procedural, or governance context.


2.5.5 RelationAtom


A RelationAtom is used when a relation itself requires additional metadata, provenance, confidence, time scope, or adjudication.


2.5.6 RecipeAtom


A RecipeAtom represents an assembly pattern that can regenerate outputs from ordered atom sets plus template and resolution rules.


2.5.7 Analysis Family


The analytical lane is a first-class derivative domain.

Type
Purpose
AnalysisAtom
General normalized analytical finding
ObservationAtom
Pattern directly observed from corpus or atom set
InterpretationAtom
Inferential conclusion derived from observations
MetricAtom
Numeric or scored output
TaxonomyProposalAtom
Suggested ontology or grouping
SignatureAtom
Stable stylistic pattern
DriftAtom
Temporal change pattern
AnalysisRunAtom
Metadata for a single analytical execution

2.6 Epistemic Tiers


The ontology MUST preserve epistemic distinctions.

Tier
Canonical Types
Description
Tier 1
SourceObject
Raw evidence-bearing artifacts
Tier 2
EvidenceAtom, TextAtom, CodeAtom, PolicyAtom
Governed primary substrate
Tier 3
ObservationAtom, InterpretationAtom, MetricAtom, DriftAtom, SignatureAtom, TaxonomyProposalAtom
Derivative analysis over sources or atoms
Tier 4
RecipeAtom, Assemblies
Rendered or reusable composition layer

This means analytical outputs are neither raw evidence nor equivalent to source-grounded rules by default.


2.7 Entity Ontology


Entities are not atoms. They are referenced domain objects.


A minimum v1 entity lattice SHOULD include:

Entity Class
Meaning
Person
Human actor
Organization
Group, institution, company, team
Project
Named work program
Repository
Technical codebase or knowledge repository
Module
Technical subsystem
Service
Runtime or system service
Interface
Contract surface
PolicyDomain
Normative domain
Concept
Abstract idea
Term
Canonical lexical item
Topic
Thematic grouping
Dataset
Structured data object
Artifact
General produced object
Environment
Runtime or deployment context
TimeWindow
Temporal scope object

2.8 Relation Vocabulary


The relation vocabulary is canonical. Additional relations MAY be added in later versions, but the following set is normative for v1.


2.8.1 Core Relations

Relation
Source
Target
Meaning
DERIVED_FROM
Atom
SourceObject or Atom
Origin linkage
SUPPORTED_BY
Atom
EvidenceAtom or Atom
Support relation
CONTRADICTS
Atom
Atom
Conflict relation
SUPERSEDES
Atom
Atom
Successor relation
USES_ENTITY
Atom
Entity
Entity reference
ASSEMBLED_IN
Atom
RecipeAtom
Recipe membership
REFINES
Atom
Atom
More precise or granular version

2.8.2 Text-Code Bridge Relations

Relation
Source
Target
Meaning
IMPLEMENTS
CodeAtom
TextAtom or PolicyAtom
Code realizes textual rule
DOCUMENTS
TextAtom
CodeAtom
Text describes code
TESTS
CodeAtom or TestAtom-like CodeAtom
CodeAtom
Validation of technical logic
AFFECTS
PolicyAtom or TextAtom
CodeAtom
Rule impacts code behavior
EXPOSES_INTERFACE
CodeAtom
Entity
Code provides interface

2.8.3 Analysis Relations

Relation
Source
Target
Meaning
ANALYZES
AnalysisAtom family
SourceObject or Atom
Analytical object studies target
MAPS_TO
AnalysisAtom family
Entity or Atom
External label aligned to internal concept
CHARACTERIZES
AnalysisAtom family
Entity, Project, Corpus
Structural description
DETECTS_DRIFT_IN
DriftAtom
Entity or Atom
Change-over-time finding
PROPOSES_TAXONOMY_FOR
TaxonomyProposalAtom
Entity, corpus, concept set
Ontology suggestion
REQUIRES_REVIEW_OF
AnalysisAtom family
Atom
Trigger re-evaluation
IS_SUPERSEDED_BY
AnalysisAtom family
AnalysisAtom family
Analytical successor

2.9 Validation and Trust States


The system has a general lifecycle, and analytical imports have an extended trust gradient.


2.9.1 Core Validation States

State
Meaning
DRAFT
Not yet checked
DISTILLED
Machine-generated and schema-valid
REVIEWED
Human or trusted review performed
VERIFIED
Approved for normal assembly
DEPRECATED
Retained but not active
DISPUTED
Challenged

2.9.2 Analysis Import Trust States

State
Meaning
IMPORTED
Received from external analytical producer
MACHINE_DERIVED
Known analysis-generated object
REVIEWED
Checked by human or trusted adjudicator
ACCEPTED
Allowed in standard assemblies
EXPERIMENTAL
Restricted to research/exploratory contexts
DISPUTED
Challenged
DEPRECATED
Superseded or retired

2.10 Provenance Ontology


The ontology adopts a three-layer provenance model for derivative analytical outputs and a two-layer minimum for all other atoms.

Provenance Layer
Requirement
Source provenance
MUST identify original corpus or artifact scope
Analysis provenance
MUST exist for analytical lane objects
Transformation provenance
MUST record normalization/import/refinery actions

2.11 Supersession Semantics


Supersession is a first-class ontological rule.

Rule ID
Requirement
OC-SUP-01
Knowledge evolution MUST be modeled with explicit successor relations.
OC-SUP-02
A new payload state MUST produce a new content identity.
OC-SUP-03
Supersession chains SHOULD remain acyclic under normal operation.

2.12 Resolution Model


The ontology supports multi-scale assembly.

Resolution
Meaning
MICRO
Minimal core claim or logic unit
COMPACT
Essential support only
STANDARD
Balanced explanation
EXTENDED
Detailed exposition
DEEP
Evidence-rich and contradiction-aware

2.13 Ontology Change Policy

Rule ID
Requirement
OC-CHG-01
New atom families MAY be introduced only through ontology revision control.
OC-CHG-02
Existing first-class types MUST NOT be merged casually.
OC-CHG-03
Cross-domain distinctions between evidence, primary atoms, and analytical atoms MUST be preserved.

2.14 Final Charter Judgment


The v1 ontology is therefore a tripartite substrate:

Domain
Ontological Role
Source domain
Evidence-bearing raw reality
Primary atomic domain
Governed knowledge and technical logic
Analytical derivative domain
Structured interpretation and diagnostics

That tripartite distinction is now canonical.



3. GraphQL Schema Draft v1


Unified Atomic Knowledge Substrate API Contract


Below is a document-grade draft schema. It is intentionally concrete enough to implement, but still conservative enough to revise without breaking the ontology.


scalar DateTime
scalar JSON

enum AtomType {
  TEXT
  CODE
  EVIDENCE
  POLICY
  RELATION
  RECIPE
  ANALYSIS
  OBSERVATION
  INTERPRETATION
  METRIC
  TAXONOMY_PROPOSAL
  SIGNATURE
  DRIFT
  ANALYSIS_RUN
}

enum AtomClass {
  AXIOM
  FACT
  RULE
  PROCEDURE
  EVIDENCE
  INTERPRETATION
  INTERFACE
  DEPENDENCY
  TEST
  RECIPE
  ANALYSIS
  METRIC
  SIGNATURE
  DRIFT
  TAXONOMY
}

enum ValidationState {
  DRAFT
  DISTILLED
  REVIEWED
  VERIFIED
  DEPRECATED
  DISPUTED
  IMPORTED
  MACHINE_DERIVED
  ACCEPTED
  EXPERIMENTAL
}

enum ResolutionLevel {
  MICRO
  COMPACT
  STANDARD
  EXTENDED
  DEEP
}

enum TextKind {
  NOTE
  REQUIREMENT
  POLICY
  TRANSCRIPT_CLAIM
  DOCUMENTATION_CLAUSE
  EVIDENCE_FRAGMENT
  SUMMARY_STATEMENT
}

enum CodeKind {
  FUNCTION
  METHOD
  CLASS
  MODULE
  CONFIG
  QUERY
  SCRIPT_STEP
  TEST_CASE
  SCHEMA_UNIT
  UI_COMPONENT
  INFRA_UNIT
}

enum SideEffectProfile {
  PURE
  READ_ONLY
  WRITE
  NETWORK
  FILESYSTEM
  EXTERNAL
}

enum RelationType {
  DERIVED_FROM
  SUPPORTED_BY
  CONTRADICTS
  SUPERSEDES
  USES_ENTITY
  ASSEMBLED_IN
  REFINES
  IMPLEMENTS
  DOCUMENTS
  TESTS
  AFFECTS
  EXPOSES_INTERFACE
  ANALYZES
  MAPS_TO
  CHARACTERIZES
  DETECTS_DRIFT_IN
  PROPOSES_TAXONOMY_FOR
  REQUIRES_REVIEW_OF
  IS_SUPERSEDED_BY
  DEPENDS_ON
}

interface Node {
  id: ID!
}

interface Atom implements Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!
}

type SourceObject implements Node {
  id: ID!
  sourceType: String!
  origin: String!
  checksum: String!
  mimeType: String!
  ingestedAt: DateTime!
  rightsClass: String
  rawArchiveRef: String!
}

type ProvenanceRecord implements Node {
  id: ID!
  operationType: String!
  sourceRef: ID
  inputRefs: [ID!]!
  outputRefs: [ID!]!
  operatorRef: String
  toolVersion: String
  timestamp: DateTime!
  notes: String
}

type Entity implements Node {
  id: ID!
  entityType: String!
  canonicalName: String!
  aliases: [String!]!
  description: String
  status: String!
  createdAt: DateTime!
}

type RelationEdge implements Node {
  id: ID!
  relationType: RelationType!
  sourceId: ID!
  targetId: ID!
  confidenceScore: Float
  createdAt: DateTime!
  metadata: JSON
}

type TextAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  textKind: TextKind!
  canonicalStatement: String!
  sourceSpan: String!
  claimPolarity: String
  temporalTag: String
  entitiesMentioned: [Entity!]!
}

type EvidenceAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  evidenceText: String!
  sourceSpan: String!
}

type PolicyAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  policyStatement: String!
  policyDomain: String
  severity: String
}

type CodeAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  codeKind: CodeKind!
  language: String!
  runtime: String
  signature: JSON
  astNodeType: String!
  symbolName: String
  modulePath: String!
  astSpan: String!
  sideEffectProfile: SideEffectProfile
  complexityScore: Float
}

type RecipeAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  recipeType: String!
  resolutionLevel: ResolutionLevel!
  atomSequence: [ID!]!
  templateRef: String!
  generationRules: JSON
}

type AnalysisRunAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  analysisRunId: String!
  analysisType: String!
  engineName: String!
  engineVersion: String
  method: String
  parameters: JSON
  sourceScope: JSON!
  timestampProduced: DateTime!
}

type AnalysisAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  findingText: String!
  findingKind: String!
  method: String
  evidenceRefs: [ID!]!
}

type ObservationAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  observationText: String!
  evidenceRefs: [ID!]!
}

type InterpretationAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  interpretationText: String!
  evidenceRefs: [ID!]!
  dependsOnFindingRefs: [ID!]!
}

type MetricAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  metricName: String!
  metricValue: Float!
  metricUnit: String
  metricContext: JSON
}

type TaxonomyProposalAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  proposalText: String!
  proposedClasses: [String!]!
}

type SignatureAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  signatureText: String!
  patternFamily: String
}

type DriftAtom implements Atom & Node {
  id: ID!
  atomType: AtomType!
  atomClass: AtomClass!
  contentHash: String!
  title: String
  taxonomyTags: [String!]!
  scopeTags: [String!]!
  validationState: ValidationState!
  confidenceScore: Float
  effectiveFrom: DateTime
  effectiveTo: DateTime
  createdAt: DateTime!
  updatedAt: DateTime!
  source: SourceObject
  provenance: [ProvenanceRecord!]!
  outgoingRelations: [RelationEdge!]!
  incomingRelations: [RelationEdge!]!

  driftText: String!
  timeWindowA: JSON!
  timeWindowB: JSON!
}

union AtomResult =
    TextAtom
  | EvidenceAtom
  | PolicyAtom
  | CodeAtom
  | RecipeAtom
  | AnalysisRunAtom
  | AnalysisAtom
  | ObservationAtom
  | InterpretationAtom
  | MetricAtom
  | TaxonomyProposalAtom
  | SignatureAtom
  | DriftAtom

input AtomFilterInput {
  atomTypes: [AtomType!]
  atomClasses: [AtomClass!]
  validationStates: [ValidationState!]
  tags: [String!]
  scopeTags: [String!]
  textQuery: String
  entityIds: [ID!]
  sourceIds: [ID!]
  createdAfter: DateTime
  createdBefore: DateTime
}

input AssemblyInput {
  query: String
  atomIds: [ID!]
  templateRef: String!
  resolutionLevel: ResolutionLevel!
  includeAnalysis: Boolean = false
  includeExperimental: Boolean = false
}

type AssemblyResult {
  recipeId: ID
  renderedText: String!
  atomIdsUsed: [ID!]!
  provenanceRefs: [ID!]!
}

type TraceResult {
  originAtom: AtomResult!
  relatedAtoms: [AtomResult!]!
  relations: [RelationEdge!]!
}

type Query {
  atom(id: ID!): AtomResult
  atoms(filter: AtomFilterInput, limit: Int = 25, offset: Int = 0): [AtomResult!]!
  source(id: ID!): SourceObject
  entity(id: ID!): Entity
  provenance(id: ID!): ProvenanceRecord
  recipe(id: ID!): RecipeAtom
  traceRuleToCode(ruleAtomId: ID!): TraceResult!
  impactAnalysis(codeAtomId: ID!): TraceResult!
  assemble(input: AssemblyInput!): AssemblyResult!
}

input CreateRelationEdgeInput {
  relationType: RelationType!
  sourceId: ID!
  targetId: ID!
  confidenceScore: Float
  metadata: JSON
}

input ImportAnalysisBundleInput {
  analysisRunId: String!
  analysisType: String!
  engineName: String!
  engineVersion: String
  method: String
  sourceScope: JSON!
  findings: JSON!
}

type Mutation {
  createRelationEdge(input: CreateRelationEdgeInput!): RelationEdge!
  importAnalysisBundle(input: ImportAnalysisBundleInput!): AnalysisRunAtom!
}


3.1 GraphQL Contract Notes

Topic
Decision
Interface style
Strongly typed with Atom interface and AtomResult union
Analysis ingestion
Explicit mutation rather than hidden source adapter
Trust states
Included directly in ValidationState enum
Assembly
Query-driven but returns recipe-aware result
Cross-domain trace
Dedicated query families such as traceRuleToCode and impactAnalysis
