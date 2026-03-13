---
title: "Traceability Report Format v1"
artifact_id: uaks_v1_traceability_report_format_20260311
pair_id: CHATPAIR-011
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Traceability Report Format v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_traceability_report_format_20260311
Version: 1.0-draft
Status: Draft normative format


1. Purpose


This format standardizes reports that explain how one object or claim is connected to others across the substrate. It is used for rule-to-code trace, source-to-claim trace, claim-to-evidence trace, and analysis-to-review trace.


2. Report thesis


A trace report is not merely a list of links. It is a structured explanation of path, support, state, and consequence.


3. Core report schema

Field
Meaning
reportId
unique report identifier
reportType
rule_to_code, source_to_claim, claim_to_evidence, analysis_to_review, historical_trace
originRef
starting object
targetRefs
reached objects
pathRefs
relation edges and intermediate nodes
stateSummary
current trust/supersession status
provenanceMode
hidden/summary/inline/appendix/forensic
generatedAt
timestamp
recipeRef
if persisted

4. Canonical sections

Order
Section
Required
1
Trace objective
Yes
2
Origin object summary
Yes
3
Path narrative
Yes
4
Target object summaries
Yes
5
Support and provenance
Yes
6
Exceptions, ambiguity, or conflict
Conditional
7
Historical notes
Conditional

5. Trace types


5.1 Rule-to-code trace

Element
Required content
Origin
PolicyAtom or TextAtom
Path
AFFECTS / IMPLEMENTS / DOCUMENTS / TESTS edges
Targets
CodeAtom(s), test atoms, supporting docs
Notes
missing implementations, disputed links, stale code states

5.2 Source-to-claim trace

Element
Required content
Origin
SourceObject or EvidenceAtom
Path
DERIVED_FROM / SUPPORTED_BY / REFINES
Targets
TextAtom, PolicyAtom, InterpretationAtom
Notes
scope and transformation history

5.3 Claim-to-evidence trace

Element
Required content
Origin
TextAtom or PolicyAtom
Path
SUPPORTED_BY
Targets
EvidenceAtom(s), source spans
Notes
evidence sufficiency and gaps

5.4 Analysis-to-review trace

Element
Required content
Origin
DriftAtom, InterpretationAtom, AnalysisAtom
Path
REQUIRES_REVIEW_OF / MAPS_TO / ANALYZES
Targets
objects flagged for review
Notes
trust status, run provenance, scope

6. Trace quality rules

Rule ID
Requirement
TRF-01
a trace report MUST distinguish direct edges from inferred narrative explanation
TRF-02
a trace report MUST surface missing links if the chain is incomplete
TRF-03
a trace report SHOULD mark whether targets are current, superseded, disputed, or accepted
TRF-04
a trace report MUST not collapse contradictory branches without flagging them

7. Minimal trace result example

Field
Example
Origin
atom_policy_005
Path
AFFECTS -> atom_code_021, TESTS -> atom_code_test_003
Targets
implementation function, linked test
Notes
one dependent code path lacks reviewed test coverage

8. Final normative judgment


A valid traceability report MUST be path-aware, state-aware, and provenance-aware. It SHOULD be readable both as a structured table and as narrative explanation.
