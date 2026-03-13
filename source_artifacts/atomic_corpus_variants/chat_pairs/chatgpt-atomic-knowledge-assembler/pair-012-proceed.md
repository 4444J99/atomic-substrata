---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 12
prompt_title: "Proceed"
response_title: "Query Pattern Library v1"
prompt_sha256: "f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b"
response_sha256: "78bced675e1e7cb352074ea9b8c2ffa4276885a1f976c5b1e63eadcd8101a25f"
---

# Pair 012

## Prompt

Proceed

## Response

Query Pattern Library v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_query_pattern_library_20260311
Version: 1.0-draft
Status: Draft normative library


1. Purpose


This library defines canonical query patterns for retrieval, trace, impact, review, assembly, and portal projection. It exists to standardize how clients, resolvers, operators, and evaluation harnesses express common intents against the substrate.


2. Query pattern thesis


A stable knowledge substrate needs stable query archetypes. Free-form querying remains useful, but core workflows SHOULD resolve through repeatable query patterns with known semantics, expected result types, and predictable trust behavior.


3. Query pattern object model

Field
Meaning
patternId
unique pattern identifier
patternName
human-readable label
intentClass
fact, policy, code, trace, impact, research, review, projection
inputShape
expected input fields
defaultFilters
type/state/scope defaults
retrievalProfile
weighting profile to apply
outputTemplate
preferred template if assembled
trustMode
standard, research, exploratory, high-trust
resultShape
expected response structure

4. Canonical query families

Family
Purpose
Direct Lookup
fetch exact object by ID or exact identifier
Concept Retrieval
find governed objects about a topic
Policy Retrieval
find rules, constraints, and implementing logic
Code Retrieval
find symbols, modules, dependencies, tests
Trace Retrieval
explain how one object connects to another
Impact Retrieval
explain likely consequences of a change
Research Retrieval
broad evidence-rich synthesis candidate pool
Review Retrieval
adjudicate disputed or promotable objects
Projection Retrieval
construct workspace or document views

5. Canonical patterns


5.1 Exact Object Lookup

Field
Value
patternId
qp_exact_object_lookup_v1
intentClass
Direct Lookup
inputShape
id
defaultFilters
none beyond access control
retrievalProfile
direct resolution
resultShape
single object

Expected behavior: resolve by canonical object ID, return current or historical object with clear state markers.


5.2 Exact Symbol Lookup

Field
Value
patternId
qp_exact_symbol_lookup_v1
intentClass
Code Retrieval
inputShape
symbolName, optional repositoryId, modulePath
defaultFilters
CodeAtom, active by default
retrievalProfile
code retrieval
resultShape
ranked code atoms plus dependency context

Expected behavior: favor lexical symbol match, then graph expansion for dependencies and tests.


5.3 Topic Concept Retrieval

Field
Value
patternId
qp_topic_concept_retrieval_v1
intentClass
Concept Retrieval
inputShape
queryText, optional scopeDescriptor
defaultFilters
primary atoms, verified/accepted by default
retrievalProfile
balanced
resultShape
ranked atom set

Expected behavior: balanced lexical-semantic retrieval with light graph expansion.


5.4 Policy-to-Code Trace

Field
Value
patternId
qp_policy_to_code_trace_v1
intentClass
Trace Retrieval
inputShape
policyAtomId or queryText resolving to rule-like object
defaultFilters
PolicyAtom, TextAtom, CodeAtom, supporting relations
retrievalProfile
trace and impact
outputTemplate
Trace Report
resultShape
origin, paths, target code, tests, gaps

Expected behavior: traverse AFFECTS, IMPLEMENTS, DOCUMENTS, TESTS.


5.5 Claim-to-Evidence Trace

Field
Value
patternId
qp_claim_to_evidence_trace_v1
intentClass
Trace Retrieval
inputShape
atomId or claim query
defaultFilters
TextAtom, EvidenceAtom, support relations
retrievalProfile
trace
outputTemplate
Trace Report
resultShape
claim, supporting evidence, provenance notes

5.6 Change Impact Query

Field
Value
patternId
qp_change_impact_v1
intentClass
Impact Retrieval
inputShape
triggerRef, optional scopeDescriptor, optional depth
defaultFilters
impacted code, policy, docs, tests
retrievalProfile
trace and impact
outputTemplate
Impact Report
resultShape
affected scope, risk, actions

5.7 Drift Review Query

Field
Value
patternId
qp_drift_review_v1
intentClass
Review Retrieval
inputShape
driftAtomId or analytical query with includeAnalysis
defaultFilters
accepted/reviewed analysis plus linked primary atoms
retrievalProfile
research deep or trace
outputTemplate
Review Packet
resultShape
drift finding, affected objects, recommended review set

5.8 Deep Research Synthesis Query

Field
Value
patternId
qp_deep_research_synthesis_v1
intentClass
Research Retrieval
inputShape
queryText, scopeDescriptor, optional time window
defaultFilters
verified/reviewed primary atoms, accepted/reviewed analysis
retrievalProfile
research deep
outputTemplate
Research Synthesis
resultShape
evidence lattice, interpretations, tensions, synthesis

5.9 Workspace Projection Query

Field
Value
patternId
qp_workspace_projection_v1
intentClass
Projection Retrieval
inputShape
projectId or rootRefs, optional historical state
defaultFilters
active code/text/recipe/entity objects
retrievalProfile
mixed projection profile
outputTemplate
Workspace Projection
resultShape
projection descriptor with grouped nodes

6. Pattern-specific defaults

Pattern
Default trust mode
Include analysis
Historical by default
exact object lookup
inspection
no
yes if ID resolves historical
exact symbol lookup
standard
no
no
topic concept retrieval
standard
no
no
policy-to-code trace
standard
no
no
claim-to-evidence trace
standard
no
no
change impact
standard
accepted only if relevant
no
drift review
research
yes
sometimes
deep research synthesis
research
yes
optional
workspace projection
standard
no
optional

7. Evaluation use


Each pattern SHOULD have corresponding gold queries and expected object sets in the evaluation harness.


8. Final normative judgment


A valid UAKS-v1 query implementation SHOULD route common intents through this library, MUST respect pattern-level trust and scope defaults, and SHOULD expose pattern IDs in logs and evaluation traces.



Auth and Access Model v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_auth_access_model_20260311
Version: 1.0-draft
Status: Draft normative model


1. Purpose


This model defines authentication assumptions, authorization layers, access scopes, and result-filtering behavior for UAKS-v1. It governs who may view, query, assemble, mutate, review, or import across the substrate.


2. Access thesis


Authorization in UAKS-v1 MUST apply at more than one layer. It is not sufficient to secure only the API. Access decisions MUST be compatible with source sensitivity, atom trust state, projection context, and mutation risk.


3. Access layers

Layer
Function
Identity layer
authenticate actor
Role layer
assign functional role
Scope layer
restrict project/repository/domain reach
Object layer
restrict source/atom/entity visibility
Action layer
restrict operations such as import, review, relation creation
Output layer
restrict what may appear in assemblies or projections

4. Actor classes

Actor class
Meaning
Reader
may inspect allowed objects
Researcher
may access broader read-only analytical contexts
Reviewer
may adjudicate trust states and review packets
Editor
may submit structured changes and new relations
Importer
may submit external analysis bundles
Operator
may manage pipelines and release operations
Administrator
may manage policy and access controls
ServiceAccount
non-human system actor with constrained privileges

5. Core permissions

Permission
Meaning
read_object
inspect object by ID
query_collection
run filtered retrieval
assemble_output
generate rendered outputs
view_provenance
inspect lineage details
view_forensic
inspect full forensic provenance
create_relation
create governed relations
import_analysis
submit external analysis envelope
change_validation_state
promote or dispute objects
manage_projection
create and persist projections
manage_policy
update governance rules
operate_pipeline
run refinery or import jobs

6. Scope descriptors for access


Authorization SHOULD operate with scopes such as:

Scope type
Example
project scope
project_alpha
repository scope
repo_refinery
source scope
specific source IDs
domain scope
policy, code, research, operations
sensitivity scope
public, internal, restricted, privileged
environment scope
development, staging, production

7. Object sensitivity classes


Every stored object SHOULD carry a sensitivity class.

Sensitivity class
Meaning
Public
broadly viewable
Internal
authenticated internal readers
Restricted
limited by role and scope
Privileged
limited to reviewers/operators/admins
Sealed
accessible only via special policy or emergency route

8. Access decision model


An access decision SHOULD be computed as:

Factor
Question
authenticated
who is the actor
role fit
does the role allow the requested action
scope fit
does the actor have required project/domain scope
sensitivity fit
is the object too sensitive for this actor
trust fit
may the actor see low-trust or disputed objects
mode fit
is the output mode allowed for this actor

9. Read rules


9.1 Direct object read


A direct object read MAY succeed even for superseded or disputed objects if the actor has inspection rights. Read access and normal assembly eligibility are distinct concepts.


9.2 Collection query read


Collection queries MUST filter inaccessible objects before ranking and return stable semantics for filtered results.


9.3 Provenance read


Forensic provenance SHOULD be more restricted than summary provenance.

Provenance level
Minimum role suggestion
summary
Reader
inline
Reader / Researcher
appendix
Researcher / Reviewer
forensic
Reviewer / Operator / Administrator

10. Mutation rules

Mutation
Minimum role
create relation
Editor or above
import analysis
Importer or above
promote validation state
Reviewer or above
dispute object
Reviewer or above
change governance policy
Administrator
rerun or operate pipeline
Operator or Administrator

11. Analytical lane access


Because the analytical lane is derivative and may contain unstable interpretations, its visibility SHOULD be role- and mode-aware.

Analysis state
Typical visibility
IMPORTED
Importer, Reviewer, Operator
MACHINE_DERIVED
Researcher, Reviewer, Operator
REVIEWED
Researcher, Reviewer, Operator
ACCEPTED
same as primary substrate visibility unless sensitivity says otherwise
EXPERIMENTAL
Researcher, Reviewer, Operator
DISPUTED
Reviewer, Operator, Administrator by default

12. Projection access


A projection MUST NOT reveal objects the actor could not independently access. Projection convenience does not override object-level authorization.


13. Error semantics

Access error
Meaning
unauthorized
not authenticated or invalid identity
forbidden
authenticated but lacks permission
filtered
object exists but removed by policy from this result
redacted
object partially accessible but sensitive fields hidden

14. Final normative judgment


A valid UAKS-v1 access implementation MUST enforce authorization across query, assembly, provenance, mutation, and projection layers, MUST not let projections bypass object restrictions, and SHOULD distinguish clearly between visibility and assembly eligibility.



Portal Projection Data Model v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_portal_projection_data_model_20260311
Version: 1.0-draft
Status: Draft normative data model


1. Purpose


This data model defines the object structures used to create, store, inspect, and reconstruct workspace, document, trace, review, and historical projections over the substrate.


2. Projection thesis


A projection is a structured view, not a source of truth. The model therefore separates projection identity, projection state, projection nodes, and canonical substrate references.


3. Core projection objects

Object
Role
ProjectionDescriptor
root metadata for one projection
ProjectionNode
one visible node within a projection
ProjectionGroup
hierarchical grouping or container
ProjectionEdge
visible relation between projection nodes
ProjectionRecipeBinding
link between projection and recipe
ProjectionStateSnapshot
reconstructable state hash and object refs

4. ProjectionDescriptor

Field
Meaning
projectionId
unique projection identifier
projectionType
workspace, document, code, trace, review, historical
scopeDescriptor
scope constraints used to build it
rootRefs
seed object references
recipeRef
optional driving recipe
projectionStateHash
exact state identifier
createdAt
creation time
createdBy
actor or service
visibilityClass
access label
status
active, archived, superseded

5. ProjectionNode

Field
Meaning
projectionNodeId
unique node within projection
projectionId
parent projection
nodeType
folder, file, symbol, section, report_block, entity_ref
label
displayed name
canonicalRef
underlying atom/entity/CAS/source/recipe ref
parentGroupId
containing group if any
ordinal
ordering index
stateHash
rendered or projected state hash
renderMetadata
display metadata
accessFiltered
whether portions are hidden/redacted

6. ProjectionGroup

Field
Meaning
projectionGroupId
unique group identifier
projectionId
parent projection
groupType
workspace_folder, document_section, trace_segment, review_bucket
label
displayed grouping label
parentGroupId
nesting parent
ordinal
ordering index

7. ProjectionEdge

Field
Meaning
projectionEdgeId
unique projection edge
projectionId
parent projection
sourceNodeId
node origin
targetNodeId
node target
edgeType
visible relation or navigation link
canonicalRelationRef
optional backing relation edge
renderMetadata
display metadata

8. ProjectionRecipeBinding

Field
Meaning
bindingId
unique binding
projectionId
target projection
recipeRef
recipe used
templateRef
template used
resolutionLevel
projection depth
generatedAt
timestamp

9. ProjectionStateSnapshot

Field
Meaning
snapshotId
unique snapshot
projectionId
owning projection
projectionStateHash
exact projection state hash
includedRefs
canonical refs included
generatedAt
timestamp
historicalMode
whether snapshot reflects non-current state
notes
optional generation notes

10. Projection node types

Node type
Meaning
folder
grouping container in workspace view
file
document or code-like projection
symbol
code-level symbol representation
section
document section
report_block
report subsection
entity_ref
conceptual anchor
trace_node
node in a trace path
review_item
item under adjudication

11. Projection generation rules

Rule ID
Requirement
PDM-01
every projection node MUST retain a canonical reference or explicitly declare itself synthetic
PDM-02
synthetic connective nodes MUST be marked as synthetic
PDM-03
historical projections MUST declare historical mode
PDM-04
projection hashes SHOULD change when included refs or render-relevant ordering changes
PDM-05
redacted projections MUST mark filtered nodes or fields

12. Minimal example


{
  "projectionId": "proj_workspace_001",
  "projectionType": "workspace",
  "scopeDescriptor": {
    "projectIds": ["project_uaks"]
  },
  "rootRefs": ["entity_project_uaks"],
  "recipeRef": "recipe_workspace_default_v1",
  "projectionStateHash": "sha256:proj001",
  "createdAt": "2026-03-11T17:00:00Z",
  "createdBy": "svc_projection",
  "visibilityClass": "internal",
  "status": "active"
}


13. Final normative judgment


A valid portal projection model MUST preserve reconstructability, canonical references, access compatibility, and historical visibility, while remaining explicitly secondary to the underlying substrate.



Pilot Intake SOP v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_pilot_intake_sop_20260311
Version: 1.0-draft
Status: Draft standard operating procedure


1. Purpose


This SOP defines the intake process for pilot-phase sources, technical artifacts, and external analytical bundles. It ensures that incoming material enters the system in a controlled, auditable, and reviewable way.


2. Pilot intake objective


The pilot phase is not just ingestion for volume. It is ingestion for learning. Intake therefore MUST preserve traceability, isolate ambiguous cases, and produce useful signals for schema, refinery, and governance tuning.


3. Intake categories

Intake category
Examples
textual source intake
memos, notes, transcripts, specs
technical source intake
code repositories, scripts, config, schemas
external analysis intake
analytical bundles from linguistic or parallel systems
seed corpus intake
curated evaluation or canonical examples

4. Intake roles

Role
Responsibility
Intake operator
registers and stages incoming objects
Reviewer
adjudicates ambiguous or sensitive intake
Pipeline operator
runs refinery or import jobs
Governance reviewer
resolves policy/trust issues

5. Intake phases

Phase
Name
Purpose
PI-01
Submission
receive incoming material
PI-02
Registration
assign source identity and metadata
PI-03
Classification
determine source family, sensitivity, scope
PI-04
Staging
place in pilot intake queue
PI-05
Preflight checks
validate completeness and parseability
PI-06
Refinery/import execution
run text/code/analysis intake path
PI-07
Post-run review
inspect output quality and anomalies
PI-08
Publication or hold
release to pilot substrate or quarantine

6. Submission requirements


Every intake submission SHOULD include, where applicable:

Field
Meaning
source description
what is being submitted
source origin
where it came from
expected category
text, code, analysis, seed corpus
project/repository scope
contextual boundary
sensitivity class
public/internal/restricted/etc.
author or owner
if known
notes on known issues
parse problems, incomplete spans, ambiguity

7. Registration steps


At registration, the intake operator MUST:

Step
Requirement
assign source ID
mandatory
compute checksum
mandatory
assign MIME/type
mandatory
assign raw archive reference
mandatory
record intake timestamp
mandatory
assign initial scope and sensitivity
mandatory

8. Preflight checks


8.1 Textual intake checks

Check
Pass condition
extractable text present
yes
structure preserved enough for segmentation
yes
source metadata recorded
yes
sensitivity assigned
yes

8.2 Technical intake checks

Check
Pass condition
repository or file set accessible
yes
language family detectable
yes
parser tier known or fallback declared
yes
source exactness preserved
yes

8.3 External analysis intake checks

Check
Pass condition
envelope schema valid
yes
analysis run metadata present
yes
source scope present
yes
findings array present
yes
normalization path available
yes

9. Intake decision outcomes

Outcome
Meaning
publish_to_pilot
proceed into substrate
publish_with_review_flag
proceed but require review
quarantine
hold pending missing information or trust concern
reject
malformed or non-conforming submission
defer
out of pilot scope

10. Required logging


Each intake job MUST log:

Field
Meaning
intake job ID
unique intake event
submitted refs
sources included
operator
actor
path chosen
text/code/analysis
preflight result
pass/fail
output counts
objects produced
anomalies
parse failures, trust mismatches, dedup issues
final outcome
publish/quarantine/etc.

11. Pilot metrics


Pilot intake SHOULD measure:

Metric
Meaning
source acceptance rate
submissions that pass
parse success rate
successful refinery start
atom yield
objects produced per source
review flag rate
ambiguity/trust burden
quarantine rate
problematic intake frequency
time to publish
operational throughput

12. Final normative judgment


A valid pilot intake process MUST register every source before processing, MUST log preflight and outcome decisions, MUST support quarantine for ambiguous cases, and SHOULD optimize for auditability over speed.



Review Workflow SOP v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_review_workflow_sop_20260311
Version: 1.0-draft
Status: Draft standard operating procedure


1. Purpose


This SOP defines how atoms, relations, analysis findings, and projections move through review, adjudication, promotion, dispute, and acceptance workflows.


2. Review thesis


The substrate gains trust not from existence but from adjudication. Review is therefore a core system function, not a cosmetic afterthought.


3. Review targets

Review target
Typical trigger
PolicyAtom
normative consequence
CodeAtom
high-risk implementation or unclear dependency
InterpretationAtom
inferential claim
DriftAtom
taxonomy or policy impact
relation edge
contested or high-consequence linkage
projection/report
human-facing artifact used for decision-making

4. Review roles

Role
Responsibility
Reviewer
inspects object and proposes disposition
Senior reviewer
resolves ambiguity or escalations
Operator
supports tooling and workflow state
Administrator
handles policy exceptions

5. Review states

State
Meaning
queued
awaiting review
in_review
actively being inspected
approved
passes review
needs_revision
insufficient as-is
disputed
materially challenged
accepted
approved for normal use in analysis lane
verified
approved for normal use in primary substrate
deferred
postponed pending further evidence

6. Review packet contents


A review packet SHOULD include:

Field
Meaning
target ref
object under review
object summary
concise explanation
provenance packet
source and transformation lineage
trust state
current state
issues list
open concerns
supporting links
evidence, related objects, trace paths
proposed disposition
approve, revise, dispute, defer

7. Review workflow phases

Phase
Name
Purpose
RW-01
Queueing
create review item
RW-02
Triage
prioritize by risk and consequence
RW-03
Inspection
inspect content, provenance, relations, scope
RW-04
Cross-checking
inspect linked evidence, code, or analysis
RW-05
Disposition
approve, revise, dispute, defer
RW-06
State transition
update validation or review state
RW-07
Audit logging
persist decision rationale

8. Triage priorities

Priority
Typical case
Critical
high-trust outputs, policy-code divergence, privileged objects
High
accepted analysis that may trigger maintenance, high-risk code
Medium
ordinary promotion from distilled to reviewed
Low
exploratory or low-impact research objects

9. Approval criteria


9.1 Primary atoms


A primary atom SHOULD be approved only if:

Criterion
Requirement
provenance complete
yes
type assignment valid
yes
scope clear
yes
contradiction handled
yes
wording materially sound
yes

9.2 Analytical atoms


An analytical object SHOULD be accepted only if:

Criterion
Requirement
analysis provenance complete
yes
source scope clear
yes
analytical/object boundary preserved
yes
finding useful and not contaminating canon
yes
review rationale recorded
yes

9.3 Relations


A relation SHOULD be approved only if:

Criterion
Requirement
endpoints valid
yes
relation type semantically correct
yes
provenance or rationale present
yes
no unmarked contradiction introduced
yes

10. Disposition outcomes

Outcome
Effect
approve_primary
promote toward reviewed/verified
approve_analysis
promote toward reviewed/accepted
request_revision
return for refinement or clarification
dispute
mark disputed and exclude from normal assembly
defer
hold for future review
reject_relation
do not publish or remove pending edge

11. Required audit record


Each review decision MUST record:

Field
Meaning
review event ID
unique decision event
target ref
reviewed object
reviewer
actor
old state
prior state
new state
updated state
rationale
explanation
supporting refs
evidence/trace links
timestamp
when decided

12. Review quality metrics

Metric
Meaning
average review turnaround
operational responsiveness
dispute rate
instability or ambiguity level
reversal rate
later overturns
accepted-to-disputed ratio
trust calibration health
missing-provenance rejection rate
intake/refinery weakness indicator

13. Final normative judgment


A valid UAKS-v1 review workflow MUST record explicit dispositions, MUST preserve rationale and audit trails, MUST distinguish primary verification from analytical acceptance, and SHOULD prioritize high-consequence review items first.



Recommended Immediate Next Set


The architecture and operating model are now far enough along that the next highest-value drafting cluster is:

Priority
Artifact
1
Change Management SOP v1
2
Incident Response SOP v1
3
Query Evaluation Harness Spec v1
4
Benchmark Corpus Definition v1
5
Gold-Standard Atom Set Spec v1

The most efficient next move is the evaluation and operational control cluster, because the ontology and workflow layers are already sufficiently mature.