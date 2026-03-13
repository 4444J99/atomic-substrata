---
title: "Query Pattern Library v1"
artifact_id: uaks_v1_query_pattern_library_20260311
pair_id: CHATPAIR-012
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
