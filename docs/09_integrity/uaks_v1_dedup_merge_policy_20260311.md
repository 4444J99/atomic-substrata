---
title: "Deduplication and Merge Policy v1"
artifact_id: uaks_v1_dedup_merge_policy_20260311
pair_id: CHATPAIR-010
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
