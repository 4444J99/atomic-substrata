---
title: "1. Change Management SOP v1"
artifact_id: uaks_v1_change_management_sop_20260311
pair_id: CHATPAIR-014
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

1. Change Management SOP v1


Document ID: uaks_v1_change_management_sop_20260311


1.1 Purpose


Change management governs modifications to:


ontology

schemas

refinery pipelines

relation catalog

templates

trust policies

operational workflows

codebase implementing the system


Without formal change control, atomic substrates quickly drift into inconsistent semantics.



1.2 Change categories

Category
Examples
Risk level
Schema change
atom fields, relation definitions
high
Ontology change
new atom family, new relation type
high
Pipeline change
new refinery logic, parser upgrade
medium-high
Retrieval change
scoring weights or query behavior
medium
Template change
rendering structures
medium
Workflow change
review policy adjustments
medium
Operational change
deployment scripts, environment config
low-medium


1.3 Change request structure


Every change MUST have a Change Request (CR).

Field
Meaning
changeId
unique identifier
changeType
schema, ontology, pipeline, etc
summary
short description
rationale
why the change exists
impactScope
affected components
riskLevel
low / medium / high
rollbackStrategy
how to revert
testPlan
verification procedure
submittedBy
actor
timestamp
submission time


1.4 Change workflow

Phase
Description
CR-01
Change request submitted
CR-02
Triage and classification
CR-03
Technical review
CR-04
Risk evaluation
CR-05
Implementation
CR-06
Validation testing
CR-07
Deployment
CR-08
Post-change monitoring


1.5 Change approval rules

Change type
Minimum approval
ontology
administrator + reviewer
schema
administrator + operator
refinery
operator + reviewer
retrieval
reviewer
template
reviewer
workflow
administrator
operational
operator


1.6 Rollback requirement


All changes MUST have a rollback plan.


Typical rollback methods:

Method
Example
supersession reversal
restore prior schema version
pipeline revert
redeploy previous refinery build
recipe reset
revert assembly behavior
projection rebuild
regenerate projections
