---
title: "Resolver Contract Specification v1"
artifact_id: uaks_v1_resolver_contract_spec_20260311
pair_id: CHATPAIR-011
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Resolver Contract Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_resolver_contract_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


This specification defines the behavior of GraphQL resolvers and adjacent query handlers over the UAKS-v1 substrate. It exists to ensure that API behavior remains consistent with ontology, trust policy, provenance rules, and storage boundaries.


2. Resolver thesis


Resolvers are contract surfaces, not truth sources. They orchestrate retrieval, filtering, joining, projection, and rendering over authoritative substrate layers.


3. Resolver responsibilities

Responsibility
Meaning
object resolution
map IDs to canonical objects
policy enforcement
apply validation/access/trust gates
hybrid retrieval orchestration
invoke lexical, semantic, graph channels
projection
shape results into API contract
provenance attachment
expose lineage according to mode
error signaling
distinguish not found, unauthorized, filtered, ambiguous

4. Resolver classes

Resolver class
Purpose
direct object resolver
fetch one object by ID
collection resolver
search/filter paginated object sets
trace resolver
produce path-aware trace results
impact resolver
produce consequence-aware results
assembly resolver
produce rendered text and recipe-aware outputs
import mutation resolver
ingest external analysis bundles
relation mutation resolver
create governed relations

5. Core contract rules

Rule ID
Requirement
RCS-01
resolvers MUST not bypass validation/trust policy
RCS-02
resolvers MUST not invent substrate objects absent from authoritative storage
RCS-03
resolvers SHOULD return score breakdowns or match reasons where practical for ranked retrieval
RCS-04
resolvers MUST distinguish current from superseded/historical objects when relevant
RCS-05
resolvers MUST preserve ontology distinctions across evidence, primary atoms, and analysis atoms

6. Query resolver behavior


6.1 atom(id)

Requirement
Behavior
direct ID resolution
fetch canonical object by ID
trust handling
enforce access, not assembly eligibility
historical behavior
return object even if superseded, clearly marked

6.2 atoms(filter, limit, offset)

Requirement
Behavior
candidate generation
hybrid retrieval if textQuery present
filter application
type, state, scope, source, entity filters
pagination
deterministic and stable
explanation
SHOULD include match reasons in debug/inspection modes

6.3 traceRuleToCode(ruleAtomId)

Requirement
Behavior
origin validation
confirm origin is rule-like object
path traversal
prioritize AFFECTS, IMPLEMENTS, DOCUMENTS, TESTS
result shape
path-aware and target-aware trace result
missing links
return explicit warnings, not silent omission

6.4 impactAnalysis(codeAtomId)

Requirement
Behavior
dependency traversal
downstream and linked rule/doc/test paths
risk shaping
classify risk and uncertainty
result shape
structured consequence result

6.5 assemble(input)

Requirement
Behavior
retrieval
invoke scoring specification if query-driven
policy filtering
enforce output-mode trust rules
template application
honor requested template
provenance mode
attach according to template and mode
output
return rendered text plus atom/provenance references

7. Mutation resolver behavior


7.1 createRelationEdge

Requirement
Behavior
ontology validation
relation type must be canonical or approved
endpoint validation
source and target must exist
provenance capture
mutation should record actor/time/provenance
policy enforcement
restricted by access and trust rules

7.2 importAnalysisBundle

Requirement
Behavior
schema validation
envelope must satisfy import contract
normalization membrane
MUST be applied
output
return AnalysisRunAtom and imported object references
trust state
imported objects enter with imported/machine-derived states, not accepted automatically

8. Error contract


Resolvers SHOULD classify errors into stable categories.

Error class
Meaning
NOT_FOUND
no such object exists
UNAUTHORIZED
caller lacks access
FILTERED_BY_POLICY
object exists but is not eligible under requested mode
INVALID_INPUT
malformed request
AMBIGUOUS_QUERY
request resolves to multiple incompatible anchors
INCOMPLETE_TRACE
result exists but graph path is incomplete
IMPORT_REJECTED
analysis bundle failed schema or trust checks

9. Performance and batching rules

Rule ID
Requirement
RCS-P-01
resolvers SHOULD batch related object fetches
RCS-P-02
resolvers SHOULD avoid N+1 graph traversals where possible
RCS-P-03
ranked collection queries SHOULD cap candidate pools before expensive deep expansion
RCS-P-04
provenance expansion SHOULD be lazy unless requested or required by mode

10. Final normative judgment


A valid resolver implementation MUST behave as a disciplined orchestration layer over the authoritative substrate. It MUST respect ontology, trust, provenance, and history semantics, and SHOULD expose enough explanation to make ranked retrieval and trace behavior auditable.



Recommended Immediate Next Set


The highest-value next drafting cluster is now:

Priority
Artifact
1
Query Pattern Library v1
2
Auth and Access Model v1
3
Portal Projection Data Model v1
4
Pilot Intake SOP v1
5
Review Workflow SOP v1

At this point, the architecture stack is coherent enough that the next phase is less about ontology invention and more about operationalizing query behavior, access control, and workflow discipline.
