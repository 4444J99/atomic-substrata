---
title: "UAKS v1 GraphQL Schema Draft"
artifact_id: docs::03_schemas::uaks_v1_graphql_schema_draft.md
pair_id: CHATPAIR-007
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
