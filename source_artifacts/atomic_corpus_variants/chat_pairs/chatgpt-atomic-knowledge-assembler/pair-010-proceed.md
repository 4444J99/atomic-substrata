---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 10
prompt_title: "Proceed"
response_title: "Retrieval Scoring Specification v1"
prompt_sha256: "f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b"
response_sha256: "da419a0cb374ffcb2a59b176a5427004b78224cb16db959e9edaf621fdb2b5ad"
---

# Pair 010

## Prompt

Proceed

## Response

Retrieval Scoring Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_retrieval_scoring_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


This specification defines how UAKS-v1 retrieves candidate atoms, entities, relations, sources, and recipes from the substrate. Retrieval in UAKS-v1 is hybrid by design. It combines lexical precision, semantic similarity, graph structure, provenance quality, temporal validity, trust state, and assembly fitness.


The retrieval layer exists to answer one question correctly:


Which governed objects should be considered for this request, in what priority order, and under what trust constraints?


2. Retrieval thesis


UAKS-v1 retrieval MUST NOT be reduced to any one of the following alone:

Single-mode strategy
Why insufficient
Full-text search only
brittle to paraphrase, synonymy, and concept drift
Vector similarity only
weak on explicit logic, exact identifiers, and trust constraints
Graph traversal only
weak on latent semantic similarity and fuzzy recall
Latest-first only
weak on foundational centrality and long-lived axioms
Highest-confidence only
can suppress useful but novel or scoped findings

The correct model is a weighted hybrid retrieval system with policy-aware filtering.


3. Retrieval objects


The retrieval layer MAY return the following object families:

Object family
Retrieval role
TextAtom
primary textual knowledge
CodeAtom
executable or technical logic
EvidenceAtom
support and grounding
PolicyAtom
governance and normative rules
AnalysisAtom family
derivative analytical findings
Entity
concept and object anchors
RelationEdge
structural context
RecipeAtom / Recipe
prior useful assembly patterns
SourceObject
forensic source anchor

4. Retrieval stages

Stage
Name
Purpose
RS-01
Query normalization
interpret query, constraints, mode, and scope
RS-02
Candidate generation
collect broad candidate pool from hybrid channels
RS-03
Policy gating
remove ineligible objects based on trust and access
RS-04
Scoring
compute final ranking scores
RS-05
Diversification
avoid over-concentration in redundant near-duplicates
RS-06
Expansion
pull support, parents, children, or dependencies if requested
RS-07
Final selection
emit ranked set for assembly or inspection

5. Query normalization


The retrieval system MUST normalize the incoming request into a formal query context.


5.1 QueryContext fields

Field
Meaning
queryText
natural-language or structured query
requestedObjectTypes
atom families or objects requested
resolutionLevel
micro, compact, standard, extended, deep
outputMode
operational, research, exploratory, high-trust
scopeDescriptor
project/repository/entity/time constraints
includeAnalysis
whether analysis lane is eligible
includeExperimental
whether experimental objects may appear
traceMode
whether lineage/impact/trace relations are primary
userSpecifiedIds
explicit object anchors if any

5.2 Query intent categories

Intent
Typical use
fact retrieval
find direct governed claims
policy retrieval
find rules and constraints
code retrieval
find logic units and dependencies
trace retrieval
rule-to-code, source-to-claim, claim-to-evidence
impact retrieval
what changes if X changes
ontology retrieval
find entities, concepts, taxonomy
research synthesis
broad multi-source candidate pool
exploratory analysis
include machine-derived analytical objects

6. Candidate generation channels


The system MUST support multiple candidate generation channels.


6.1 Lexical channel


Uses full-text or token-index search for exact or near-exact terms, identifiers, symbol names, tag matches, and constrained spans.


Best for:

Best-case lexical targets
exact terminology
code symbol names
policy phrases
quoted text
tags
identifiers

6.2 Semantic channel


Uses embedding-space similarity against atoms, entity descriptions, code summaries, and normalized analytical findings.


Best for:

Best-case semantic targets
paraphrase
conceptual similarity
cross-domain topic recall
latent theme match
synonym and drift-tolerant discovery

6.3 Graph channel


Uses structural traversal from anchored atoms or entities.


Best for:

Best-case graph targets
dependency lookup
support chains
contradiction chains
supersession chains
rule-to-code mapping
analysis-triggered review paths

6.4 Recipe prior channel


Uses prior recipe usage and successful assembly patterns to seed likely candidates.


Best for:

Best-case recipe targets
recurring report structures
known documentation bundles
stable technical explanations
repeated trace workflows

6.5 Recency and activity channel


Uses time-aware boosting from creation, validation, supersession, or recent successful use.


Best for:

Best-case time-sensitive targets
current policy
latest accepted analysis
recent code state
recent ontology changes

7. Hard filters before scoring


The following SHOULD be applied before final ranking when relevant.

Filter class
Effect
access control
remove unauthorized objects
validation threshold
exclude states not permitted by output mode
scope filter
restrict by project/repository/time/entity
type filter
restrict to requested object families
supersession policy
suppress superseded objects unless historical mode requested
analysis policy
exclude analytical lane if not requested or not allowed

8. Core scoring model


The retrieval score for an object o under query context q SHOULD be modeled as:


$$
R(o,q) = w_lL(o,q) + w_sS(o,q) + w_gG(o,q) + w_tT(o,q) + w_vV(o,q) + w_cC(o) + w_uU(o) + w_aA(o,q) - w_dD(o,q)
$$


Where:

Component
Meaning
$L(o,q)$
lexical relevance
$S(o,q)$
semantic similarity
$G(o,q)$
graph relevance
$T(o,q)$
temporal relevance
$V(o,q)$
validation/trust fit
$C(o)$
structural centrality
$U(o)$
utility from prior successful use
$A(o,q)$
assembly fitness for the requested template/resolution
$D(o,q)$
penalties for staleness, contradiction mismatch, redundancy, or scope mismatch

9. Score component definitions


9.1 Lexical relevance  $L$


Lexical relevance SHOULD combine term overlap, exact identifier hits, field-specific matches, and tag matches.


$$
L(o,q) = \alpha_1 \cdot exact_match + \alpha_2 \cdot bm25 + \alpha_3 \cdot tag_match + \alpha_4 \cdot identifier_match
$$


Lexical relevance SHOULD receive extra weight for:

Case
Reason
code symbol match
often exact-intent
policy clause phrase match
precision critical
explicit atom or entity name
user intent likely narrow
quoted span
likely exact retrieval desired

9.2 Semantic similarity  $S$


Semantic similarity SHOULD be computed using cosine or equivalent similarity over embeddings of the query and candidate objects.


It SHOULD be available for:

Object family
Embedding basis
TextAtom
canonical statement
PolicyAtom
policy statement
EvidenceAtom
normalized evidence text
CodeAtom
code summary, docstring, symbol context, linked descriptions
AnalysisAtom family
finding text

9.3 Graph relevance  $G$


Graph relevance SHOULD reflect how structurally close or important an object is relative to query anchors.


Possible subcomponents:

Graph subcomponent
Meaning
path proximity
shortest or weighted path from anchored objects
relation-type relevance
preferred edge types by query intent
dependency reachability
downstream or upstream relevance
support depth
closeness to evidence or claim anchors
supersession priority
latest valid object in a lineage

9.4 Temporal relevance  $T$


Temporal relevance MUST respect effective validity and SHOULD boost recency only where the query or object type warrants it.


$$
T(o,q) = \beta_1 \cdot current_validity + \beta_2 \cdot recency_fit + \beta_3 \cdot time_window_overlap
$$


Temporal weight SHOULD be high for policy, code state, and analysis findings, and lower for axioms or foundational concepts.


9.5 Validation/trust fit  $V$


Validation fit measures whether the object’s trust state is appropriate to the output mode.

Output mode
Preferred states
standard operational
VERIFIED, ACCEPTED
research
REVIEWED, VERIFIED, ACCEPTED
exploratory
may include DISTILLED, MACHINE_DERIVED, EXPERIMENTAL
high-trust
VERIFIED only unless exception exists

Objects outside allowed states SHOULD receive infinite negative gating or severe penalty rather than minor downgrade.


9.6 Centrality  $C$


Centrality reflects how foundational an object is in the substrate.


Candidate methods:

Centrality method
Use
in-degree / out-degree
rough importance
eigenvector centrality
hub-like importance
dependency centrality
technical criticality
support centrality
evidentiary structural importance

Centrality SHOULD be used carefully so that foundational hubs do not swamp query-specific relevance.


9.7 Utility  $U$


Utility reflects how often an object has been used successfully in prior assemblies or workflows.


Candidate factors:

Utility factor
Meaning
recipe frequency
used in successful recipes
selection persistence
retained through review
user acceptance
historically useful outputs
low-revision stability
fewer later corrections

9.8 Assembly fitness  $A$


Assembly fitness scores whether an object fits the requested template and resolution.


Example:

Template / resolution
Preferred candidates
summary / micro
central, high-density atoms
technical spec / extended
procedure, dependency, interface, policy, code
trace report
support, derived_from, implements, tests
research synthesis / deep
evidence, contradictions, analysis lane, provenance-rich objects

9.9 Penalty term  $D$


Penalty SHOULD combine negative factors.

Penalty source
Meaning
redundancy
near-duplicate candidate already selected
stale state
superseded or out-of-window object
scope mismatch
wrong project/time/jurisdiction
trust mismatch
insufficient validation for output mode
contradiction mismatch
candidate conflicts with required stance and lacks surfacing policy

10. Default weight profiles


The system SHOULD support mode-specific weighting profiles.


10.1 General balanced profile

Component
Default weight
lexical
0.18
semantic
0.22
graph
0.18
temporal
0.08
validation
0.14
centrality
0.07
utility
0.05
assembly fitness
0.08

10.2 Policy retrieval profile

Component
Default weight
lexical
0.24
semantic
0.16
graph
0.14
temporal
0.10
validation
0.18
centrality
0.05
utility
0.03
assembly fitness
0.10

10.3 Code retrieval profile

Component
Default weight
lexical
0.20
semantic
0.12
graph
0.26
temporal
0.08
validation
0.12
centrality
0.08
utility
0.04
assembly fitness
0.10

10.4 Trace and impact profile

Component
Default weight
lexical
0.10
semantic
0.08
graph
0.38
temporal
0.10
validation
0.12
centrality
0.06
utility
0.04
assembly fitness
0.12

10.5 Research deep profile

Component
Default weight
lexical
0.12
semantic
0.22
graph
0.18
temporal
0.08
validation
0.10
centrality
0.06
utility
0.04
assembly fitness
0.20

These values are initial defaults only and SHOULD be tuned against the evaluation harness.


11. Type-specific scoring adjustments


11.1 TextAtom adjustments


TextAtom scoring SHOULD emphasize semantic and lexical fit, plus support availability.


Boost conditions:

Condition
Boost
exact policy phrase or concept match
high
linked supporting evidence present
medium
directly refined from requested parent
medium
active and not superseded
medium

11.2 CodeAtom adjustments


CodeAtom scoring SHOULD emphasize graph relevance, identifier match, dependency location, and linked policy/docs.


Boost conditions:

Condition
Boost
symbol or module name exact match
high
direct dependency path from anchored code
high
linked IMPLEMENTS relation to relevant policy
medium-high
linked TESTS coverage
medium

11.3 EvidenceAtom adjustments


EvidenceAtom SHOULD be weakly retrieved on its own unless the query requests support, audit, compliance, or deep explanation.


11.4 AnalysisAtom family adjustments


Analytical lane objects MUST obey trust policy gating. When included, they SHOULD score strongly for research, exploratory, drift, ontology, and discourse-oriented queries.


Boost conditions:

Condition
Boost
accepted/reviewed state
medium-high
recent relevant analysis run
medium
direct REQUIRES_REVIEW_OF or DETECTS_DRIFT_IN link
high for maintenance queries
explicit include-analysis flag
high

12. Diversification policy


The retrieval layer SHOULD avoid returning ten near-identical objects when three representative ones plus support objects would serve better.


Diversification MAY use:

Method
Function
max marginal relevance
balance relevance and novelty
lineage collapsing
suppress superseded siblings
family quotas
avoid single-family dominance
source spread
represent multiple sources where useful

Diversification SHOULD be relaxed for forensic or exact trace modes.


13. Expansion policy


After ranking the top core candidates, the system MAY pull structured expansion objects.


13.1 Expansion modes

Expansion mode
Pulled objects
support expansion
evidence and supporting claims
dependency expansion
upstream/downstream code dependencies
parent-child expansion
refined or abstracted neighbors
provenance expansion
source and transformation records
contradiction expansion
scoped competing objects
recipe expansion
prior assembly neighbors

Expansion MUST remain policy-aware and SHOULD preserve clear distinction between primary hits and context expansions.


14. Historical and supersession handling


14.1 Default behavior


Default retrieval SHOULD prefer active, non-superseded objects.


14.2 Historical mode


When the query requests history, comparison, drift, or lineage, superseded objects MUST remain retrievable and SHOULD be grouped by supersession chain.


14.3 Lineage grouping


The UI or assembly layer SHOULD be able to present:

Grouping
Meaning
current state
preferred active object
historical predecessors
prior superseded objects
successor chain
later replacements
scoped divergence
valid alternatives under different scopes

15. Analytical lane inclusion policy


The retrieval layer MUST treat the analytical lane as derivative, policy-gated material.


15.1 Inclusion rules

Output mode
Analytical inclusion
standard operational
ACCEPTED only, if relevant
research
REVIEWED and ACCEPTED, optionally EXPERIMENTAL
exploratory
may include MACHINE_DERIVED and EXPERIMENTAL if explicitly requested
high-trust
exclude unless explicitly authorized

15.2 Rank dampening


Even when eligible, analytical objects SHOULD receive dampened ranking against direct primary substrate objects unless the query intent clearly favors derivative analysis.


16. Example scoring interpretation


Assume query: “Which code implements the validation policy for imported analysis bundles?”


Likely score priorities:

Component
Importance
lexical
high for “validation”, “analysis bundles”, symbol names
graph
very high for IMPLEMENTS, AFFECTS, DEPENDS_ON
semantic
medium for paraphrased technical matches
temporal
medium if policies recently changed
validation
high, because implementation answers should be trustworthy
assembly fitness
high for trace report or technical spec mode

Top likely objects:

Rank band
Object type
1
PolicyAtom about validation policy
2
linked CodeAtom via IMPLEMENTS
3
linked CodeAtom test cases via TESTS
4
supporting TextAtom documentation
5
accepted AnalysisAtom only if query explicitly asks about analysis behavior

17. Retrieval output contract


The retrieval layer SHOULD emit structured results, not only ranked IDs.


17.1 RetrievalResult schema

Field
Meaning
objectId
retrieved object
objectType
object family
finalScore
combined score
scoreBreakdown
per-component contributions
rank
output rank
matchReasons
human-readable reasons
expansionRole
primary, support, dependency, provenance, contradiction
warnings
trust, staleness, ambiguity flags

18. Evaluation hooks


The retrieval system MUST be measurable.


18.1 Primary evaluation measures

Measure
Meaning
precision@k
relevance of top results
recall@k
coverage of gold objects
mrr
mean reciprocal rank
support coverage
whether support/evidence included when needed
trust compliance
whether disallowed states are excluded
lineage correctness
whether current vs historical state is handled correctly
cross-domain trace accuracy
correctness of rule-to-code and analysis-to-source paths

19. Required tuning artifacts


This retrieval specification depends on these companion artifacts:

Companion artifact
Role
benchmark corpus definition
ground truth input set
gold-standard atom set
expected retrieval targets
query pattern library
canonical test queries
evaluation harness
automated scoring
validation/trust policy
gating rules
graph relation catalog
graph path semantics

20. Final normative judgment


A valid UAKS-v1 retrieval implementation MUST:

Requirement
Status
support lexical retrieval
mandatory
support semantic retrieval
mandatory
support graph-aware retrieval
mandatory
apply trust-aware policy gating
mandatory
respect supersession and historical mode
mandatory
support type-specific weighting
mandatory
produce explainable ranked results
strongly recommended
support expansion modes
strongly recommended


Deduplication and Merge Policy v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_dedup_merge_policy_20260311
Version: 1.0-draft
Status: Draft normative policy


1. Purpose


This policy defines when objects in the substrate may be merged, coalesced, clustered, or explicitly kept separate. The goal is to prevent redundancy bloom without collapsing meaningful distinctions in scope, provenance, trust, or semantics.


2. Deduplication thesis


UAKS-v1 MUST prefer meaning-preserving consolidation over raw object-count growth, but MUST NOT erase distinctions that matter to truth, scope, or auditability.


The system therefore distinguishes:

Condition
Action
exact duplicate state
consolidate aggressively
semantic duplicate with same scope
merge with provenance multiplicity
near-duplicate with meaningful scope difference
keep distinct, relate
contradiction or contested meaning
keep distinct, mark conflict
supersession
keep both, link lineage

3. Duplicate categories

Category
Definition
exact duplicate
same canonical payload, same effective scope, same type
semantic duplicate
materially same meaning after normalization
structural duplicate
same relation or entity binding repeated
scoped variant
same core meaning but different project/time/jurisdiction/speaker scope
contradictory variant
incompatible or opposing meaning
superseded variant
older state replaced by later state
analytical echo
derivative analysis restating already stored accepted finding

4. Merge eligibility rules


4.1 Exact duplicates


Exact duplicates SHOULD be merged into a single active object with preserved provenance multiplicity.


4.2 Semantic duplicates


Semantic duplicates MAY be merged only if all of the following hold:

Requirement
Meaning
same object family
no cross-family flattening
materially equivalent meaning
no loss of meaning
same effective scope
same domain/time/project/jurisdiction
compatible trust state
no unsafe upgrade by merge
provenance preserved
all sources retained

4.3 Non-merge cases


Objects MUST NOT be merged when any of the following apply:

Non-merge trigger
Reason
different scopes
truth differs by context
contradiction exists
conflict must remain visible
different epistemic tier
evidence vs interpretation vs analysis must remain distinct
supersession relation exists
lineage must remain explicit
different atom family with only superficial lexical similarity
ontology boundary preservation

5. Canonical merge actions

Action
Use
collapse-to-one
exact duplicates
merge-with-provenance
semantic duplicates
relate-as-refines
one is more precise
relate-as-supersedes
newer state replaces older
relate-as-contradicts
conflicting claims
cluster-only
similar objects grouped for retrieval but not merged

6. Family-specific rules


6.1 TextAtom


TextAtoms MAY be merged when normalized meaning is materially identical and scope is aligned.


They MUST NOT be merged across:

Boundary
Reason
project scope
context may differ
temporal state
policy or meaning may have changed
normative vs descriptive role
role changes truth-function

6.2 EvidenceAtom


EvidenceAtoms SHOULD usually remain distinct unless they are byte-for-byte or span-for-span identical. Multiple independent evidence spans that support the same claim are better stored as multiple evidence atoms linked to a common claim.


6.3 PolicyAtom


PolicyAtoms SHOULD be merged conservatively. Even subtle wording changes MAY carry normative consequences. If two policies differ in modal force, exception structure, or applicability, they MUST remain distinct.


6.4 CodeAtom


CodeAtoms MUST NOT be merged merely because they are similar in behavior. Exact payload identity and stable content-addressed equivalence are required for hard merge. Otherwise they MAY be clustered as similar implementations or linked through refinement or supersession.


6.5 AnalysisAtom family


Analytical objects SHOULD be merged only when the same analysis type, scope, method, and finding meaning coincide closely. Findings from different analysis runs SHOULD typically remain distinct but MAY be linked or superseded.


7. Provenance preservation


Every merge action MUST preserve provenance multiplicity.


7.1 Provenance rule


When multiple candidates merge into one canonical object, the canonical object MUST retain references to all source and transformation lineages that contributed to the merge.


7.2 Merge event recording


Each merge SHOULD create a provenance or governance event with:

Field
Meaning
merge event ID
unique event
input object refs
objects considered
canonical output ref
retained object
merge rationale
why merge occurred
method/version
rules or model used
operator
human or automated actor

8. Similarity thresholds


The implementation SHOULD use family-specific thresholds.

Family
Exact threshold
Semantic merge threshold
Cluster threshold
TextAtom
exact hash match
high
medium
EvidenceAtom
exact span+payload
very high
low-medium
PolicyAtom
exact or near-exact wording
very high
medium
CodeAtom
exact content identity
not recommended for semantic merge
medium-high
AnalysisAtom family
exact run+finding identity
high if same method/scope
medium

Exact numerical values SHOULD be tuned via evaluation harness, not hardcoded in this policy.


9. Conflict with trust states


Lower-trust objects MUST NOT silently upgrade higher-trust objects through merge.


Example:

Case
Required behavior
machine-derived analysis matches accepted analysis
attach as supporting provenance or cluster candidate, not overwrite
distilled text matches verified text
may attach provenance after review, not downgrade verified status
imported external finding matches verified policy atom
never flatten cross-tier objects

10. Merge outputs


The deduplication layer SHOULD emit one of the following decisions for each candidate pair or cluster:

Decision
Meaning
MERGE_EXACT
collapse into canonical object
MERGE_SEMANTIC
merge with provenance preservation
KEEP_SEPARATE_SCOPE
same meaning, different scope
KEEP_SEPARATE_CONFLICT
contradiction preserved
LINK_REFINES
more/less specific
LINK_SUPERSEDES
historical succession
CLUSTER_SIMILAR
retrieval grouping only
NO_ACTION
unrelated or insufficient confidence

11. Final normative judgment


A valid UAKS-v1 deduplication implementation MUST:

Requirement
Status
preserve provenance on merge
mandatory
preserve epistemic tier boundaries
mandatory
keep contradictions separate
mandatory
keep superseded states separate
mandatory
treat policy and code merges conservatively
mandatory
support similarity clustering without forced merge
strongly recommended


AST Parsing Strategy v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_ast_parsing_strategy_20260311
Version: 1.0-draft
Status: Draft normative strategy


1. Purpose


This strategy defines how UAKS-v1 structurally parses code and technical artifacts to produce CodeAtoms and dependency relations. The aim is parser-grounded technical atomization with exact spans, stable symbol extraction, and language-aware boundaries.


2. Strategy thesis


The code refinery MUST be structurally grounded. It MUST prefer AST or equivalent parse-tree representations for supported languages and structured grammars for supported non-code artifacts.


Regex-only or arbitrary chunking approaches MAY serve as fallback for unsupported inputs, but outputs from those paths SHOULD remain lower-trust until upgraded by parser-grade support.


3. Parser tiers

Tier
Description
Trust
Tier 1
full AST parser with stable grammar
highest
Tier 2
structured parser or schema-aware parser
high
Tier 3
fallback structural parser
medium-low
Tier 4
text chunk heuristic
low

4. Language support model


The implementation SHOULD maintain a language support registry.


4.1 Example support registry

Family
Preferred parsing mode
Python
full AST
TypeScript / JavaScript
full AST
Rust
full AST
SQL
grammar-aware structured parse
YAML / TOML / JSON
structured parse
shell
structured parse where feasible, fallback otherwise
Dockerfile / workflow YAML
structured parse
Markdown with code fences
mixed-mode parse

5. Parser outputs required for publication


For a supported code object to be published as a normal CodeAtom, the parser path SHOULD emit:

Output
Meaning
symbol identity
name or anonymous stable boundary
node type
AST classification
source span
exact location
container path
file/module/package location
child relationships
contained members if applicable
dependency indicators
imports, calls, references where possible

6. Boundary rules


6.1 Functional boundaries


A function or method SHOULD usually become one CodeAtom.


6.2 Type boundaries


A class, interface, schema, or migration unit MAY become one CodeAtom if operationally meaningful.


6.3 Module boundaries


A module MAY become a CodeAtom when file-level logic or configuration has meaning beyond contained symbols.


6.4 Composite handling


A file MAY produce:

Result
Example
one module atom only
small config file
module atom plus child function atoms
utility source file
class atom plus method atoms
object-oriented source file
schema atom plus migration-step atoms
database migration

7. Dependency extraction priorities


The parser strategy SHOULD prioritize these dependency classes:

Priority
Dependency class
1
imports / requires / use statements
2
function/method calls
3
inheritance / interface implementation
4
query/model/schema usage
5
config/environment dependency
6
workflow step dependency

8. Fallback mode rules


When a language lacks Tier 1 or Tier 2 support:

Rule
Requirement
FP-01
fallback outputs MUST be marked as lower trust
FP-02
spans MUST still be exact where possible
FP-03
semantic merge of fallback code atoms SHOULD be conservative
FP-04
reprocessing SHOULD be possible when parser support improves

9. Mixed artifact parsing


Some source files contain multiple modalities.


Examples:

Artifact
Parsing approach
markdown with code fences
document parse + embedded code parse
notebooks
cell-aware parse
workflow YAML with shell fragments
structured parse + embedded shell segments
template files
container parse + extracted logic blocks

The parsing strategy SHOULD support multimodal boundary extraction where practical.


10. Final normative judgment


A valid UAKS-v1 AST strategy MUST:

Requirement
Status
support parser tiers
mandatory
record parser provenance
mandatory
preserve exact spans
mandatory
distinguish parser-grade from fallback-grade outputs
mandatory
support reprocessing on parser improvement
mandatory


Portal Projection Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_portal_projection_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


The portal projection layer provides human-usable and tool-usable views over the atomic substrate without treating those views as primary storage truth. It materializes stable, intelligible workspace views from content-addressed objects, graph relations, and recipes.


2. Projection thesis


The substrate stores atoms and immutable content objects. Users and tools often need familiar workspace projections: project trees, file-like structures, documentation bundles, trace reports, code views, and assembled artifacts.


The portal projection layer therefore MUST provide ergonomic structure while preserving the deeper truth that these are projected states, not primary containers.


3. Projection objects

Projection type
Purpose
workspace projection
project/repository-shaped view
document projection
rendered text or spec
code projection
file/module/function-oriented view
trace projection
lineage and relation inspection
review projection
validation and dispute workflow view
historical projection
time-sliced state view

4. Core projection inputs

Input
Role
CAS objects
exact payload states
atoms
semantic and technical units
entities
conceptual anchors
relations
structural map
recipes
reusable assembly/projection patterns
scope descriptor
project/time/user constraints

5. Projection rules


5.1 Identity rule


Projected paths, names, and folders MAY be stable human-facing aliases, but MUST NOT replace content identity or logical atom identity.


5.2 Reproducibility rule


A projection SHOULD be reconstructable from its recipe, object references, and scope context.


5.3 Non-destructive rule


Edits in a projection layer MUST be mediated back into refinery/governance flows rather than silently mutating canonical substrate truth.


6. Projection schema


6.1 ProjectionDescriptor

Field
Meaning
projectionId
unique projection object
projectionType
workspace, document, code, trace, review, historical
scopeDescriptor
project/repository/time constraints
rootRefs
seed atom/entity/CAS refs
recipeRef
generation recipe if any
createdAt
creation time
projectionStateHash
exact projected state identifier

7. Workspace projection behavior


A workspace projection SHOULD provide a familiar hierarchy built from substrate objects.


Possible mapping:

Projected path concept
Backing substrate
folder
entity cluster, repo, module, or recipe grouping
file
assembled document or code CAS object
symbol view
code atom
spec section
ordered atom sequence
trace panel
graph traversal

8. Historical projection behavior


Historical projections MUST support viewing prior superseded states, prior recipes, and prior code payloads without collapsing them into the current state.


9. Final normative judgment


A valid UAKS-v1 projection layer MUST:

Requirement
Status
separate projection identity from canonical identity
mandatory
support reproducible projections
mandatory
preserve historical state views
mandatory
avoid silent truth mutation through projection edits
mandatory


Release Checklist v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_release_checklist_20260311
Version: 1.0-draft
Status: Draft release gate


A v1 foundational launch SHOULD NOT proceed until the following conditions are satisfied.


1. Governance readiness

Check
Status required
ontology charter approved
pass
validation/trust policy approved
pass
provenance policy approved
pass
supersession policy approved
pass
contradiction handling defined
pass

2. Architecture readiness

Check
Status required
architecture spec frozen for v1
pass
trust boundary map reviewed
pass
storage decisions frozen
pass
migration approach defined
pass

3. Schema readiness

Check
Status required
schema pack frozen
pass
GraphQL contract validated
pass
relation catalog approved
pass
CAS model validated
pass

4. Pipeline readiness

Check
Status required
text refinery operational
pass
code refinery operational
pass
analysis import path operational or intentionally deferred
pass
deduplication policy implemented
pass
parser tier registry defined
pass

5. Retrieval and assembly readiness

Check
Status required
retrieval scoring implemented
pass
template catalog available
pass
assembly engine passes basic evaluation
pass
provenance rendering works
pass
trace report works
pass

6. Operational readiness

Check
Status required
intake SOP defined
pass
review workflow defined
pass
release runbook present
pass
incident response defined
pass
observability minimum viable dashboard present
pass

7. Evaluation readiness

Check
Status required
benchmark corpus exists
pass
gold-standard atoms exist
pass
retrieval evaluation run completed
pass
assembly evaluation run completed
pass
readiness scorecard above threshold
pass


Launch Readiness Scorecard v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_launch_readiness_scorecard_20260311
Version: 1.0-draft
Status: Draft scorecard


1. Purpose


This scorecard provides a go / no-go framework for foundational launch.


2. Scoring categories

Category
Weight
governance
0.15
architecture
0.10
schemas
0.15
pipelines
0.20
retrieval
0.15
assembly
0.10
operations
0.10
evaluation
0.05

3. Category criteria


3.1 Governance

Criterion
Score range
ontology clarity
0–5
policy completeness
0–5
trust model operationality
0–5

3.2 Architecture

Criterion
Score range
boundary clarity
0–5
storage fit
0–5
migration feasibility
0–5

3.3 Schemas

Criterion
Score range
completeness
0–5
consistency
0–5
implementation readiness
0–5

3.4 Pipelines

Criterion
Score range
text refinery maturity
0–5
code refinery maturity
0–5
external analysis import maturity
0–5
deduplication behavior
0–5

3.5 Retrieval

Criterion
Score range
hybrid retrieval effectiveness
0–5
trust compliance
0–5
trace accuracy
0–5

3.6 Assembly

Criterion
Score range
output coherence
0–5
recipe persistence
0–5
provenance visibility
0–5

3.7 Operations

Criterion
Score range
SOP completeness
0–5
monitoring readiness
0–5
release discipline
0–5

3.8 Evaluation

Criterion
Score range
benchmark quality
0–5
harness coverage
0–5
regression detectability
0–5

4. Thresholds

Final score
Decision
4.5–5.0
launch-ready
3.8–4.49
conditional launch
3.0–3.79
pilot-only
below 3.0
no-launch

5. Final recommendation


The strongest next drafting cluster after this set is:

Priority
Artifact
1
Template Catalog v1
2
Provenance Rendering Rules v1
3
Traceability Report Format v1
4
Impact Analysis Report Format v1
5
Resolver Contract Specification v1

The cleanest continuation is the Template Catalog v1 cluster, because it closes the gap between retrieval, assembly, and portal projection.