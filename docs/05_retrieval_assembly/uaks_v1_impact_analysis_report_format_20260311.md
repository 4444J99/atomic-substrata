---
title: "Impact Analysis Report Format v1"
artifact_id: uaks_v1_impact_analysis_report_format_20260311
pair_id: CHATPAIR-011
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Impact Analysis Report Format v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_impact_analysis_report_format_20260311
Version: 1.0-draft
Status: Draft normative format


1. Purpose


This format standardizes reports that explain likely downstream consequences of a change in policy, code, ontology, analysis findings, or other substrate objects.


2. Report thesis


Impact analysis is not simply dependency listing. It is structured consequence analysis combining direct dependency paths, risk, trust state, and recommended action.


3. Core report schema

Field
Meaning
reportId
unique report identifier
triggerRef
changed or proposed-to-change object
affectedRefs
impacted objects
impactPaths
graph paths supporting impact claims
riskSummary
severity and uncertainty
recommendedActions
next steps
generatedAt
timestamp
recipeRef
persisted recipe if any

4. Canonical sections

Order
Section
Required
1
Trigger summary
Yes
2
Affected scope
Yes
3
Path-based impact explanation
Yes
4
Risk classification
Yes
5
Recommended actions
Yes
6
Supporting provenance
Yes
7
Historical / supersession context
Conditional

5. Impact trigger classes

Trigger class
Typical impact targets
PolicyAtom change
CodeAtom, docs, tests, workflows
CodeAtom change
dependents, tests, interfaces, docs
DriftAtom accepted finding
taxonomy, policy, reclassification targets
TaxonomyProposalAtom adoption
entity classes, retrieval behavior, templates
Recipe/template change
portal views, rendered outputs, downstream clients

6. Risk model

Risk level
Meaning
Low
localized, low uncertainty
Medium
multiple dependents or unclear edge effects
High
broad dependency spread, policy/compliance implications, or high-trust outputs affected

Risk SHOULD consider:

Factor
Influence
dependency breadth
upward
trust criticality
upward
missing test/support coverage
upward
accepted historical stability
downward
clear rollback path
downward

7. Recommended action classes

Action
Use
review
human adjudication needed
update_code
implementing logic must change
update_policy
normative rule must change
reclassify
ontology or trust state must change
rerun_analysis
analytical confirmation needed
add_test
insufficient validation coverage
no_action
impact determined minimal

8. Quality rules

Rule ID
Requirement
IAF-01
an impact report MUST distinguish direct from indirect impact
IAF-02
an impact report SHOULD include uncertainty notes where graph paths are incomplete
IAF-03
an impact report MUST surface high-trust affected objects clearly
IAF-04
an impact report SHOULD name missing evidence or missing test coverage where relevant

9. Minimal example

Section
Example content
Trigger
accepted semantic drift finding about “validation”
Affected scope
taxonomy node, policy atom, two implementing code atoms
Risk
medium-high because policy-code semantics may have diverged
Recommended actions
taxonomy review, policy review, code trace audit, add targeted tests

10. Final normative judgment


A valid impact report MUST be consequence-aware, path-aware, and action-oriented. It SHOULD explain not only what is affected, but why and what should happen next.
