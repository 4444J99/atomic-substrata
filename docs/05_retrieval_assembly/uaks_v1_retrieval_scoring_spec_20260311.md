---
title: "Retrieval Scoring Specification v1"
artifact_id: uaks_v1_retrieval_scoring_spec_20260311
pair_id: CHATPAIR-010
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
