---
pair_id: CHATPAIR-004
pair_number: 4
prompt_sha256: f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b
response_sha256: 146edcc68715f2076fdc72bdd4186efc10b438f3a55443882d0330e9ed8d6789
generated_at: 2026-03-12T20:08:19.636509Z
---

# CHATPAIR-004 — Unified_Atomic_Knowledge_Substrate_v1___Document-G

## Prompt

Proceed

## Response

Unified Atomic Knowledge Substrate v1


Document-Grade Architecture Specification Package


Document ID: uaks_v1_architecture_spec_20260311
Version: 1.0-draft
Status: Draft for foundational launch
Normative language: The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as requirement levels.



0. Front Matter


0.1 Purpose


This document defines the v1 architecture for a unified atomic substrate that treats textual knowledge and technical logic as first-class, governed, addressable units. It establishes the normative requirements for ontology, schemas, storage, refinement, retrieval, assembly, governance, interfaces, and foundational launch artifacts.


0.2 Scope


This specification covers:

Area
Included
Atom model
Yes
Text atoms
Yes
Code atoms
Yes
Graph relations
Yes
Provenance
Yes
CAS
Yes
Raw source archive
Yes
Vector retrieval
Yes
GraphQL interface
Yes
Governance
Yes
Launch artifact inventory
Yes

This specification does not attempt to standardize distributed peer-to-peer replication, autonomous code rewriting, or universal language support in v1.


0.3 System designation

Field
Value
Canonical name
Unified Atomic Knowledge Substrate
Abbreviation
UAKS
Version
v1
System type
Hybrid semantic-graph, content-addressed, provenance-governed assembly substrate


1. Executive Thesis


UAKS-v1 is a substrate, not a folder tree, not a document library, and not merely a chatbot memory layer.


The substrate MUST store persistent knowledge as atomic units.
It MUST store logical structure as explicit relations.
It MUST store exact state as immutable content-addressed objects.
It MUST preserve raw source artifacts for audit and re-refinement.
It MUST generate human-facing artifacts as assembled outputs or saved recipes rather than treat static documents as the primary truth objects.


The system’s central design claim is:


Text and code belong to one ontology but require different refinery disciplines.



2. Governing Principles

Principle ID
Principle
Normative statement
GP-01
Atom-first persistence
The system MUST treat atoms as the primary active knowledge substrate.
GP-02
Hybrid retrieval
The system MUST combine graph and vector retrieval with governance and temporal constraints.
GP-03
Provenance integrity
Every verified atom MUST retain a precise provenance chain.
GP-04
Immutable content state
Content-addressed payloads MUST be immutable.
GP-05
Logical supersession
Conceptual continuity MUST be represented via explicit supersession relations rather than silent overwrite.
GP-06
Cross-domain traceability
Business or policy text SHOULD be linkable to implementing or affected code.
GP-07
Assembly over static document
Output documents SHOULD be reproducible from recipes and atoms.
GP-08
Resolution elasticity
The same substrate MUST support multiple output scales.
GP-09
Specialized refinement
Text and code MUST have distinct refinement pipelines under one governance model.
GP-10
Auditability
The system MUST support inspection of source, transformation, and assembly lineage.


3. Core Requirements


3.1 Functional requirements

ID
Requirement
FR-01
The system MUST ingest raw text, conversational text, code, scripts, config, and rich source artifacts.
FR-02
The system MUST produce TextAtom and CodeAtom as first-class outputs of refinery pipelines.
FR-03
The system MUST assign stable logical identifiers to atoms.
FR-04
The system MUST assign content hashes to immutable payload states.
FR-05
The system MUST preserve original raw sources in an archive.
FR-06
The system MUST support graph relations among atoms and entities.
FR-07
The system MUST support semantic retrieval via vector indexing where applicable.
FR-08
The system MUST support typed query access through a unified interface.
FR-09
The system MUST support recipe-based assembly of outputs.
FR-10
The system MUST support supersession, contradiction marking, and validation state transitions.

3.2 Nonfunctional requirements

ID
Requirement
NFR-01
Verified atoms MUST have complete provenance.
NFR-02
Hashing MUST be deterministic for equivalent canonical payloads.
NFR-03
Retrieval MUST permit hybrid scoring across graph, vector, temporal, and governance dimensions.
NFR-04
Exact content states MUST be reconstructable from CAS references.
NFR-05
Re-refinement MUST be possible from raw archived sources.
NFR-06
The system SHOULD tolerate partial refinement failure without global data loss.
NFR-07
The system SHOULD support incremental update processing.
NFR-08
The system MUST preserve traceability across text-to-code bridges where established.


4. Logical System Topology


4.1 Core layers

Layer
Mandatory
Role
Source Intake Layer
Yes
Registers and fingerprints incoming sources
Raw Source Archive
Yes
Stores original source artifacts intact
Text Refinery
Yes
Produces text atoms from human-language sources
Code Refinery
Yes
Produces code atoms from technical sources
Graph Layer
Yes
Stores explicit relations and dependency structure
Vector Layer
Yes
Stores embeddings for semantic retrieval
CAS Layer
Yes
Stores immutable content-addressed payloads
Metadata / Governance Layer
Yes
Tracks states, review events, lineage, and policy
Assembly Layer
Yes
Builds outputs from selected atoms
Interface Layer
Yes
Exposes typed query and control surface

4.2 Trust boundaries

Boundary
Authoritative source
Raw source truth
Raw Source Archive
Exact payload state
CAS
Conceptual continuity
Atom logical ID and supersession chain
Explicit relational truth
Graph Layer
Semantic neighborhood
Vector Layer
Human-facing assembled output
Assembly Layer, bounded by source-backed atoms


5. Ontology Overview


5.1 Root object families

Family
Description
Atom
Abstract base type for all atomic units
TextAtom
Atomic textual meaning unit
CodeAtom
Atomic executable or technical logic unit
Entity
Domain object referenced by atoms
Relation
Typed connection between atoms or between atoms and entities
SourceObject
Registered raw source artifact
ProvenanceRecord
Transformation and lineage object
Recipe
Persisted assembly plan
ValidationEvent
Review or state-transition record

5.2 First-class mandate


TextAtom and CodeAtom MUST be modeled as peer first-class types.
Neither MUST be modeled as a lower-trust annotation on the other.
Both MUST inherit from Atom.



6. Abstract Atom Specification


6.1 Base schema

Field
Type
Required
Description
atomId
ULID or UUID
Yes
Stable logical identity
atomType
Enum
Yes
TEXT or CODE
atomClass
Enum
Yes
Functional role
contentHash
Hash
Yes
Immutable payload identity
canonicalPayloadRef
CASRef
Yes
Pointer to exact payload in CAS
sourceRef
ID
Yes
Originating source object
provenanceRef
ID
Yes
Latest provenance record
validationState
Enum
Yes
Lifecycle state
confidenceScore
Float
Yes
Confidence of correctness or extraction integrity
taxonomyTags
Array
Yes
Domain and role tags
scopeTags
Array
No
Project, audience, jurisdiction, domain scope
effectiveFrom
Timestamp
No
Start of validity
effectiveTo
Timestamp
No
End of validity
supersedes
Atom ID
No
Previous logical state
supersededBy
Atom ID
No
Later logical state
createdAt
Timestamp
Yes
Creation time
updatedAt
Timestamp
Yes
Metadata update time
status
Enum
Yes
Active, archived, hidden, blocked

6.2 Base atom classes

atomClass value
Meaning
AXIOM
Foundational invariant or principle
FACT
Verifiable declarative statement
RULE
Business, legal, policy, or system rule
PROCEDURE
Ordered operational instruction
EVIDENCE
Source-backed support unit
INTERPRETATION
Explicit inference or synthesis
INTERFACE
Input-output or contract definition
DEPENDENCY
Structural dependency expression
TEST
Assertion or executable validation
RECIPE
Saved assembly plan as an atomized object if needed

6.3 Atom invariants

Invariant ID
Invariant
AI-01
Every atom MUST have one logical ID and one content hash.
AI-02
Every verified atom MUST resolve to an archived source or a derivation chain terminating in archived sources.
AI-03
Every atom MUST have an explicit type and class.
AI-04
Verified atoms MUST NOT be silently overwritten.
AI-05
Atoms SHOULD be independently interpretable within their subtype rules.


7. TextAtom Specification


7.1 Definition


A TextAtom is the smallest self-contained textual unit that expresses a coherent meaning, claim, rule, instruction, evidence fragment, or interpretation without depending on hidden neighboring prose for basic comprehension.


7.2 TextAtom schema

Field
Type
Required
Description
textKind
Enum
Yes
Note, requirement, policy, transcript-claim, documentation-clause, evidence-fragment
canonicalStatement
Text
Yes
Self-contained textual statement
sourceSpan
Span
Yes
Exact source location
entitiesMentioned
Array
Yes
Referenced entities
claimPolarity
Enum
No
Positive, negative, conditional, comparative
temporalTag
Enum
No
Current, historical, projected, obsolete
evidenceRefs
Array
No
Supporting evidence links
contradictionRefs
Array
No
Conflicting claims
parentTextAtomRefs
Array
No
More abstract atoms
childTextAtomRefs
Array
No
More granular atoms

7.3 TextAtom acceptance rules

Rule ID
Requirement
TA-01
The canonicalStatement MUST be understandable without hidden local context.
TA-02
The atom MUST have exact source span provenance.
TA-03
Key referents MUST be explicit or resolvable through linked entities.
TA-04
Rules, requirements, and policies SHOULD carry scope or temporal qualifiers when necessary.
TA-05
Interpretive atoms MUST be marked as interpretation rather than fact.


8. CodeAtom Specification


8.1 Definition


A CodeAtom is the smallest operationally meaningful technical unit suitable for dependency reasoning, traceability, impact analysis, and state reconstruction.


A CodeAtom MUST NOT be restricted to “pure function” only. The v1 system MUST support multiple code atom categories.


8.2 CodeAtom categories

Category
Meaning
FUNCTION
Standalone callable unit
METHOD
Callable bound to type/object context
CLASS
Type container or behavior container
MODULE
File or package-level semantic unit
CONFIG
Structured configuration definition
QUERY
Database or data-access primitive
SCRIPT_STEP
Shell or workflow step
TEST_CASE
Executable validation unit
SCHEMA_UNIT
Schema, migration, type model, interface model
UI_COMPONENT
Reusable user interface unit
INFRA_UNIT
Deployment or infrastructure logic unit

8.3 CodeAtom schema

Field
Type
Required
Description
codeKind
Enum
Yes
Code category
language
String
Yes
Source language
runtime
String
No
Execution/runtime environment
signature
JSON/Text
No
Inputs, outputs, modifiers, generics
astNodeType
String
Yes
Canonical AST classification
symbolName
String
No
Named symbol
modulePath
String
Yes
Logical projected workspace path
astSpan
Span
Yes
Exact location in source
dependencyRefs
Array
No
Direct dependencies
dependentRefs
Array
No
Reverse dependencies
sideEffectProfile
Enum
No
Pure, read-only, write, network, filesystem, external
complexityScore
Float
No
Static complexity estimate
testRefs
Array
No
Linked tests
buildRefs
Array
No
Linked build outputs or compiled objects
businessRuleRefs
Array
No
Linked policy or rule text atoms
interfaceContractRef
ID
No
Contract object
breakingChangeRisk
Enum
No
Low, medium, high
contentAddressRef
CASRef
Yes
Exact immutable payload pointer

8.4 CodeAtom acceptance rules

Rule ID
Requirement
CA-01
A CodeAtom MUST map to a structurally valid span resolved by the code refinery.
CA-02
A CodeAtom MUST record exact source location.
CA-03
A CodeAtom MUST record language and AST node type.
CA-04
If dependencies are resolvable, they SHOULD be materialized as graph relations.
CA-05
If a code unit enforces a policy or requirement, the system SHOULD permit a trace link to a TextAtom.
CA-06
Content changes MUST yield a new content hash.


9. Entity and Relation Model


9.1 Entity definition


An Entity is a named or canonicalized domain object referenced by atoms. Examples include business concepts, technical services, database tables, interfaces, policies, users, modules, runtime environments, and external systems.


9.2 Entity schema

Field
Type
Required
entityId
ID
Yes
entityType
String
Yes
canonicalName
String
Yes
aliases
Array
No
description
Text
No
status
Enum
Yes
createdAt
Timestamp
Yes

9.3 Relation types

Relation
Source
Target
Meaning
IMPLEMENTS
CodeAtom
TextAtom
Code enforces or realizes text rule
DOCUMENTS
TextAtom
CodeAtom
Text describes code
DEPENDS_ON
CodeAtom
CodeAtom
Technical dependency
TESTS
CodeAtom or TestAtom
CodeAtom
Validation relationship
USES_ENTITY
Atom
Entity
References domain object
SUPPORTED_BY
TextAtom
TextAtom or Evidence
Evidence support
CONTRADICTS
Atom
Atom
Competing states or claims
SUPERSEDES
Atom
Atom
Logical successor
DERIVED_FROM
Atom
SourceObject
Origin linkage
ASSEMBLED_IN
Atom
Recipe
Used in recipe
AFFECTS
TextAtom
CodeAtom
Policy or requirement impacts code
EXPOSES_INTERFACE
CodeAtom
Entity or Contract
Interface definition linkage

9.4 Relation invariants

ID
Requirement
RI-01
Verified relations MUST resolve to existing node identities.
RI-02
SUPERSEDES relations MUST NOT form cycles in normal use.
RI-03
DEPENDS_ON SHOULD be directional.
RI-04
IMPLEMENTS and AFFECTS SHOULD be available for traceability use cases.


10. Source Intake and Raw Archive


10.1 Source intake requirement


Every inbound artifact MUST be registered as a SourceObject before refinement.


10.2 SourceObject schema

Field
Type
Required
sourceId
ID
Yes
sourceType
Enum
Yes
origin
String
Yes
ingestedAt
Timestamp
Yes
checksum
Hash
Yes
mimeType
String
Yes
authorRef
ID
No
rightsClass
Enum
No
rawArchiveRef
ID
Yes

10.3 Archive rules

Rule ID
Requirement
SA-01
The raw archive MUST preserve original source material in an untouched form.
SA-02
Archived objects MUST be referenced by stable archive identifiers.
SA-03
Refinery outputs MUST remain traceable back to archived source objects.
SA-04
Re-refinement MUST be possible from archived sources.


11. Content-Addressable Storage


11.1 CAS function


The CAS layer stores immutable payload objects addressed by content hash rather than human file path.


11.2 CAS rules

Rule ID
Requirement
CAS-01
CAS objects MUST be immutable.
CAS-02
Identical canonical payloads MUST produce the same content hash under the selected hashing standard.
CAS-03
Any content mutation MUST produce a new content object and new hash.
CAS-04
Atoms MUST reference exact CAS payloads for reproducibility.
CAS-05
Human-facing stable names MAY exist as projection-layer constructs, but MUST NOT replace content identity.

11.3 CAS object schema

Field
Type
Required
casRef
ID
Yes
contentHash
Hash
Yes
contentType
String
Yes
canonicalizationVersion
String
Yes
byteSize
Integer
Yes
createdAt
Timestamp
Yes
storageLocation
String
Yes


12. Refinery Architecture


12.1 Shared refinery principle


Text and code MUST use separate refinement pipelines. They MUST share governance, provenance, identity, and publication rules.



13. Text Refinery Specification


13.1 Pipeline stages

Stage
Description
TR-1 Segmentation
Split source based on structure and semantic cues
TR-2 Extraction
Identify entities, claims, temporal markers, evidence fragments
TR-3 Distillation
Rewrite into smallest independent units of value
TR-4 Typing
Assign text kind and atom class
TR-5 Linking
Connect evidence, parent-child structure, contradictions, entities
TR-6 Validation
Check atomicity, provenance, and clarity
TR-7 Publication
Persist payload, graph relations, metadata, and state

13.2 Text refinery rules

Rule ID
Requirement
TRR-01
Distilled textual units MUST preserve source-backed meaning.
TRR-02
Text atoms MUST carry exact source spans.
TRR-03
Interpretive compression SHOULD be marked explicitly where inference occurs.
TRR-04
Deduplication SHOULD merge equivalent claims while preserving provenance multiplicity.


14. Code Refinery Specification


14.1 Pipeline stages

Stage
Description
CR-1 Parse
Build AST or equivalent structural model
CR-2 Symbol extraction
Identify functions, methods, classes, configs, tests, modules
CR-3 Boundary determination
Decide code atom spans
CR-4 Dependency analysis
Resolve calls, imports, interfaces, bindings where possible
CR-5 Technical typing
Assign code kind, runtime, side-effect profile
CR-6 Bridge linking
Link code to tests, docs, rules, schemas, interfaces
CR-7 Validation
Verify parse validity, span integrity, content identity
CR-8 Publication
Persist payload, relations, metadata, and state

14.2 Code refinery rules

Rule ID
Requirement
CRR-01
Code atomization MUST be structurally grounded, not solely text-chunk based.
CRR-02
The code refinery SHOULD use AST-aware parsing for supported languages.
CRR-03
Dependency edges SHOULD be recorded when robustly resolvable.
CRR-04
The system MUST support reprocessing when parser capabilities improve.
CRR-05
Tests, configs, schemas, and infrastructure logic MAY be emitted as CodeAtoms.


15. Provenance Model


15.1 Provenance layers

Layer
Description
Source provenance
Where the atom originated
Transformation provenance
How the atom was extracted, rewritten, merged, or validated
Assembly provenance
Which outputs and recipes used the atom

15.2 ProvenanceRecord schema

Field
Type
Required
provenanceId
ID
Yes
sourceRef
ID
Yes
operationType
Enum
Yes
inputRefs
Array
Yes
outputRefs
Array
Yes
operatorRef
ID
No
toolVersion
String
No
timestamp
Timestamp
Yes
notes
Text
No

15.3 Provenance rules

Rule ID
Requirement
PR-01
Every verified atom MUST have a provenance chain.
PR-02
Merge and deduplication events MUST preserve all underlying source references.
PR-03
Assemblies SHOULD be able to expose provenance for included atoms.


16. Validation and Governance


16.1 Validation states

State
Meaning
DRAFT
Newly created, not yet conformance checked
DISTILLED
Machine-created and schema-valid
REVIEWED
Human or trusted review completed
VERIFIED
Approved for production assembly use
DEPRECATED
Retained but not normally active
DISPUTED
Truth or integrity challenged

16.2 ValidationEvent schema

Field
Type
Required
validationEventId
ID
Yes
targetRef
ID
Yes
previousState
Enum
Yes
newState
Enum
Yes
actorRef
ID
No
timestamp
Timestamp
Yes
reason
Text
No

16.3 Governance rules

Rule ID
Requirement
GOV-01
Verified atoms MUST NOT be overwritten in place.
GOV-02
State transitions MUST be auditable.
GOV-03
Contradictory atoms MAY coexist if clearly marked and scoped.
GOV-04
High-risk rule-linked code SHOULD require review prior to verified status.
GOV-05
Policy, legal, or requirement text SHOULD require review before verified use.


17. Retrieval Architecture


17.1 Retrieval principle


Retrieval MUST be hybrid. No single substrate is sufficient for the required system behavior.


17.2 Retrieval score model


A generic retrieval score MAY be represented as:


$$
R(a, q) = w_sS(a,q) + w_gG(a,q) + w_tT(a,q) + w_vV(a) + w_uU(a) + w_cC(a) - w_dD(a,q)
$$


Where semantic similarity, graph relevance, temporal fit, validation trust, utility, and centrality are combined with penalties for distance, contradiction, or staleness.


17.3 Retrieval rules

Rule ID
Requirement
RET-01
Queries MUST be able to combine graph and vector criteria.
RET-02
Validation state SHOULD affect ranking.
RET-03
Temporal validity SHOULD affect ranking where time matters.
RET-04
Code retrieval SHOULD weight dependency and symbol relations more heavily than prose-only similarity.
RET-05
Text retrieval SHOULD weight evidence and scope coherence strongly.


18. Resolution and Assembly


18.1 Resolution levels

Level
Description
MICRO
Minimal core claim or logic path
COMPACT
Essential support only
STANDARD
Balanced explanatory output
EXTENDED
Detailed exposition or technical walkthrough
DEEP
Evidence-rich, edge-case inclusive, contradiction-aware output

18.2 Recipe schema

Field
Type
Required
recipeId
ID
Yes
recipeType
Enum
Yes
atomSequence
Array
Yes
templateRef
ID
Yes
resolutionLevel
Enum
Yes
generationRules
JSON
No
createdAt
Timestamp
Yes

18.3 Assembly rules

Rule ID
Requirement
ASM-01
Assembled outputs SHOULD be reproducible from saved recipes.
ASM-02
The assembly layer MUST NOT fabricate unsupported factual content as if it were atom-backed truth.
ASM-03
Connective prose MAY be generated to improve readability.
ASM-04
Provenance exposure SHOULD be available for high-trust outputs.


19. GraphQL Interface Specification


19.1 Interface role


The GraphQL layer is the typed access surface over graph, vector, CAS, archive, and governance services.


19.2 GraphQL principles

Rule ID
Requirement
GQL-01
The interface MUST expose Atom, TextAtom, CodeAtom, Entity, SourceObject, ProvenanceRecord, and Recipe types or equivalent queryable structures.
GQL-02
Clients SHOULD be able to request only needed fields.
GQL-03
Resolvers MUST enforce access and validation rules.
GQL-04
The GraphQL layer MUST NOT be treated as the source of truth itself; it is a contract surface.

19.3 Example query families

Query family
Purpose
atom(id)
Retrieve a specific atom
atoms(filter)
Search and filter atom sets
traceRuleToCode(ruleId)
Find linked implementation code
impactAnalysis(codeAtomId)
Return affected dependents and linked rules/docs
assemble(recipeId or querySpec)
Produce output from atoms and template
source(id)
Retrieve source metadata
provenance(id)
Inspect lineage


20. Decision Matrix


Graph + Vector + CAS + Raw Source Archive + GraphQL API


20.1 Decision summary

Component
v1 decision
Reason
Graph
Mandatory
Explicit structure, dependencies, traceability
Vector
Mandatory
Semantic retrieval and approximate recall
CAS
Mandatory
Immutable state, deduplication, exact reconstruction
Raw Source Archive
Mandatory
Audit, provenance, re-refinement
GraphQL API
Mandatory for v1 contract
Typed unified access layer

20.2 Benefit-cost-risk matrix

Component
Benefits
Costs
Risk if absent
Graph
Strong traceability, dependency reasoning, contradiction visibility
Ontology design overhead, edge management complexity
System collapses into loosely related chunks
Vector
Semantic recall, paraphrase matching, discovery
Embedding cost, refresh complexity, drift handling
Retrieval becomes brittle and keyword-bound
CAS
Immutable exact states, deduplication, snapshot reproducibility
Hash and object management complexity
No deterministic content state or exact replay
Raw Source Archive
Audit anchor, re-refinement, source recovery
Storage growth, archival discipline
Provenance breaks; future refinery upgrades blocked
GraphQL API
Unified typed interface, client flexibility, clean contract
Resolver complexity, schema governance
Fragmented interfaces, inconsistent access semantics

20.3 Final judgment


All five components MUST be present in v1 if the system is intended as a serious foundational launch rather than a loose prototype.



21. Failure Modes and Countermeasures

Failure mode
Description
Countermeasure
False atomicity
Units too small or contextless
Enforce acceptance tests and parent-child relations
Semantic drift
Similar but wrong retrieval
Hybrid retrieval with graph and validation weighting
Provenance erosion
Atoms lose exact source trace
Mandatory provenance rules
Redundancy bloom
Near-duplicates multiply
Merge policy plus provenance-preserving deduplication
Stale recall
Old atoms dominate relevant newer state
Temporal weighting and supersession rules
Code/text disconnect
Policy and code drift apart
Cross-domain bridge relations and drift reports
CAS opacity
Human users cannot understand hash-based storage
Projection layer and stable human-facing labels
Schema creep
Ontology becomes unstable
Governance board or change-control process


22. Launch Artifact Manifest


This section defines the foundational artifact inventory required for a solid launch. “Solid launch” here means durable, governable, and extensible, not merely demo-capable.


22.1 Governance artifacts

Artifact ID
Artifact
Mandatory
GA-01
Vision and thesis document
Yes
GA-02
Scope and exclusions charter
Yes
GA-03
Ontology charter
Yes
GA-04
Naming convention standard
Yes
GA-05
Provenance policy
Yes
GA-06
Validation policy
Yes
GA-07
Supersession policy
Yes
GA-08
Contradiction handling policy
Yes
GA-09
Security and rights policy
Yes

22.2 Architecture artifacts

Artifact ID
Artifact
Mandatory
AA-01
V1 architecture specification
Yes
AA-02
Logical data model
Yes
AA-03
Physical storage architecture
Yes
AA-04
Service decomposition spec
Yes
AA-05
Trust boundary map
Yes
AA-06
Nonfunctional requirements spec
Yes
AA-07
Failure mode and resilience analysis
Yes

22.3 Schema artifacts

Artifact ID
Artifact
Mandatory
SA-01
Atom base schema
Yes
SA-02
TextAtom schema
Yes
SA-03
CodeAtom schema
Yes
SA-04
Entity schema catalog
Yes
SA-05
Relation schema catalog
Yes
SA-06
SourceObject schema
Yes
SA-07
ProvenanceRecord schema
Yes
SA-08
Recipe schema
Yes
SA-09
ValidationEvent schema
Yes
SA-10
Telemetry schema
Yes

22.4 Refinery artifacts

Artifact ID
Artifact
Mandatory
RA-01
Text refinery specification
Yes
RA-02
Code refinery specification
Yes
RA-03
Atomicity test suite
Yes
RA-04
Deduplication and merge policy
Yes
RA-05
AST parsing strategy
Yes
RA-06
Entity extraction rules
Yes
RA-07
Relation extraction rules
Yes
RA-08
Re-refinement protocol
Yes
RA-09
QA rubric
Yes

22.5 Retrieval and assembly artifacts

Artifact ID
Artifact
Mandatory
RT-01
Retrieval scoring specification
Yes
RT-02
Resolution model
Yes
RT-03
Template catalog
Yes
RT-04
Assembly engine specification
Yes
RT-05
Recipe persistence specification
Yes
RT-06
Provenance rendering rules
Yes
RT-07
Traceability report format
Yes
RT-08
Impact analysis report format
Yes

22.6 API and interface artifacts

Artifact ID
Artifact
Mandatory
IA-01
GraphQL schema
Yes
IA-02
Resolver contract specification
Yes
IA-03
Query pattern library
Yes
IA-04
Auth and access model
Yes
IA-05
Portal projection specification
Yes
IA-06
Consumer interface contract
Yes

22.7 Storage and infrastructure artifacts

Artifact ID
Artifact
Mandatory
ST-01
CAS object model
Yes
ST-02
Hashing standard
Yes
ST-03
Raw archive storage policy
Yes
ST-04
Graph indexing plan
Yes
ST-05
Vector indexing plan
Yes
ST-06
Backup and recovery plan
Yes
ST-07
Snapshot and restore protocol
Yes
ST-08
Migration strategy
Yes

22.8 Operational artifacts

Artifact ID
Artifact
Mandatory
OP-01
Pilot intake SOP
Yes
OP-02
Review workflow SOP
Yes
OP-03
Dispute handling SOP
Yes
OP-04
Change management SOP
Yes
OP-05
Incident response SOP
Yes
OP-06
Release checklist
Yes
OP-07
Runbook set
Yes
OP-08
Observability dashboard specification
Yes

22.9 Evaluation artifacts

Artifact ID
Artifact
Mandatory
EV-01
Benchmark corpus definition
Yes
EV-02
Gold-standard atom set
Yes
EV-03
Retrieval evaluation harness
Yes
EV-04
Assembly evaluation harness
Yes
EV-05
Traceability coverage report
Yes
EV-06
Drift detection report
Yes
EV-07
Cost and capacity model
Yes
EV-08
Launch readiness scorecard
Yes

22.10 Seed content artifacts

Artifact ID
Artifact
Mandatory
SC-01
Canonical ontology examples
Yes
SC-02
Sample TextAtom corpus
Yes
SC-03
Sample CodeAtom corpus
Yes
SC-04
Rule-to-code bridge examples
Yes
SC-05
Initial template pack
Yes
SC-06
Initial recipe pack
Yes


23. Minimal Foundational Launch Set


The following reduced set is the true minimum for a serious foundation.

Launch tier
Artifact set
Core design
Vision, scope, architecture, ontology, trust boundary map
Core data model
Atom, TextAtom, CodeAtom, Entity, Relation, SourceObject, ProvenanceRecord, Recipe schemas
Core storage
CAS object model, raw archive policy, graph indexing plan, vector indexing plan
Core pipelines
Text refinery spec, code refinery spec, atomicity test suite, AST strategy
Core interface
GraphQL schema, resolver contract
Core governance
Provenance, validation, supersession, contradiction, security policies
Core utility
Retrieval spec, assembly spec, template catalog, traceability report format
Core operation
Intake SOP, review SOP, release checklist, runbooks
Core evaluation
Benchmark corpus, gold-standard atoms, readiness scorecard, cost model


24. Recommended Build Order

Phase
Output
Phase 1
Governance pack and ontology pack
Phase 2
Schema pack and storage decision pack
Phase 3
Text refinery and code refinery specs
Phase 4
GraphQL schema and retrieval spec
Phase 5
Assembly/recipe spec and report formats
Phase 6
Operational SOPs and evaluation harnesses
Phase 7
Seed corpus and pilot validation


25. Final Normative Conclusion


A valid v1 of this system MUST include:


Graph.
Vector retrieval.
Content-addressable storage.
A preserved raw source archive.
A typed GraphQL interface.
TextAtom and CodeAtom as first-class types.
Separate refineries for text and code.
Shared governance, provenance, and recipe logic.
Launch artifacts sufficient to operate, validate, and evolve the system.


Anything less than that may still be a useful prototype, but it is not yet a foundational atomic knowledge substrate in the full sense defined by this specification.


26. Immediate next drafting set


The highest-value next package is this five-document cluster:

Next document
Purpose
Ontology Charter v1
Freeze core types, classes, and relations
Schema Pack v1
Formalize machine-readable schemas
Text Refinery Spec v1
Define textual atomization pipeline
Code Refinery Spec v1
Define AST-aware technical atomization
GraphQL Contract v1
Define the system’s typed access surface

Proceeding directly from here, the cleanest move is to draft the Ontology Charter v1 in the same document-grade style.
