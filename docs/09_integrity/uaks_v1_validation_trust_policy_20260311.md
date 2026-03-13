---
title: "Validation and Trust Policy v1"
artifact_id: uaks_v1_validation_trust_policy_20260311
pair_id: CHATPAIR-009
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Validation and Trust Policy v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_validation_trust_policy_20260311
Version: 1.0-draft
Status: Draft normative policy


1. Purpose


This policy governs lifecycle states, review thresholds, trust gradients, and assembly eligibility for all atom families.


2. Core validation states

State
Meaning
Standard assembly eligibility
DRAFT
created but not conformance-checked
No
DISTILLED
machine-produced and schema-valid
No
REVIEWED
human or trusted review applied
Conditional
VERIFIED
approved for normal assembly
Yes
DEPRECATED
retained, not active
No
DISPUTED
challenged or conflicting
No

3. Analysis trust states

State
Meaning
Standard assembly eligibility
IMPORTED
raw accepted external import
No
MACHINE_DERIVED
normalized machine analysis
No by default
ACCEPTED
approved for standard use
Yes
EXPERIMENTAL
exploratory research lane only
No by default

4. Promotion rules

From
To
Minimum requirement
DRAFT
DISTILLED
schema-valid and provenance present
DISTILLED
REVIEWED
reviewer check or trusted adjudicator
REVIEWED
VERIFIED
passes domain-specific trust threshold
IMPORTED
MACHINE_DERIVED
normalization membrane completed
MACHINE_DERIVED
REVIEWED
review performed
REVIEWED
ACCEPTED
approved for standard analytical inclusion

5. Mandatory review cases


The following SHOULD require human or high-trust review before standard assembly:

Atom family
Trigger
PolicyAtom
operational, legal, or governance consequence
CodeAtom
external side effects, high breaking-change risk
InterpretationAtom
inferential claims influencing decisions
TaxonomyProposalAtom
ontology-changing suggestion
DriftAtom
triggers taxonomy or policy review
any atom
contradiction or low-confidence ambiguity

6. Assembly inclusion policy

Output mode
Allowed states
Standard operational output
VERIFIED, ACCEPTED
Research output
REVIEWED, VERIFIED, ACCEPTED, optional EXPERIMENTAL
Exploratory output
may include DISTILLED and MACHINE_DERIVED if explicitly requested
High-trust/compliance output
VERIFIED only unless policy exception exists

7. Dispute handling


A disputed atom MUST remain traceable, MUST retain provenance, and SHOULD remain queryable in forensic contexts while excluded from normal assembly.


8. Supersession handling


Superseded atoms MUST NOT be deleted merely because newer atoms exist. They SHOULD remain accessible for history, lineage, and comparison.
