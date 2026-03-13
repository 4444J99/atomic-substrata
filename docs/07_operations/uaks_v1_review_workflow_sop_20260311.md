---
title: "Review Workflow SOP v1"
artifact_id: uaks_v1_review_workflow_sop_20260311
pair_id: CHATPAIR-012
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

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
