---
title: "Pilot Intake SOP v1"
artifact_id: uaks_v1_pilot_intake_sop_20260311
pair_id: CHATPAIR-012
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Pilot Intake SOP v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_pilot_intake_sop_20260311
Version: 1.0-draft
Status: Draft standard operating procedure


1. Purpose


This SOP defines the intake process for pilot-phase sources, technical artifacts, and external analytical bundles. It ensures that incoming material enters the system in a controlled, auditable, and reviewable way.


2. Pilot intake objective


The pilot phase is not just ingestion for volume. It is ingestion for learning. Intake therefore MUST preserve traceability, isolate ambiguous cases, and produce useful signals for schema, refinery, and governance tuning.


3. Intake categories

Intake category
Examples
textual source intake
memos, notes, transcripts, specs
technical source intake
code repositories, scripts, config, schemas
external analysis intake
analytical bundles from linguistic or parallel systems
seed corpus intake
curated evaluation or canonical examples

4. Intake roles

Role
Responsibility
Intake operator
registers and stages incoming objects
Reviewer
adjudicates ambiguous or sensitive intake
Pipeline operator
runs refinery or import jobs
Governance reviewer
resolves policy/trust issues

5. Intake phases

Phase
Name
Purpose
PI-01
Submission
receive incoming material
PI-02
Registration
assign source identity and metadata
PI-03
Classification
determine source family, sensitivity, scope
PI-04
Staging
place in pilot intake queue
PI-05
Preflight checks
validate completeness and parseability
PI-06
Refinery/import execution
run text/code/analysis intake path
PI-07
Post-run review
inspect output quality and anomalies
PI-08
Publication or hold
release to pilot substrate or quarantine

6. Submission requirements


Every intake submission SHOULD include, where applicable:

Field
Meaning
source description
what is being submitted
source origin
where it came from
expected category
text, code, analysis, seed corpus
project/repository scope
contextual boundary
sensitivity class
public/internal/restricted/etc.
author or owner
if known
notes on known issues
parse problems, incomplete spans, ambiguity

7. Registration steps


At registration, the intake operator MUST:

Step
Requirement
assign source ID
mandatory
compute checksum
mandatory
assign MIME/type
mandatory
assign raw archive reference
mandatory
record intake timestamp
mandatory
assign initial scope and sensitivity
mandatory

8. Preflight checks


8.1 Textual intake checks

Check
Pass condition
extractable text present
yes
structure preserved enough for segmentation
yes
source metadata recorded
yes
sensitivity assigned
yes

8.2 Technical intake checks

Check
Pass condition
repository or file set accessible
yes
language family detectable
yes
parser tier known or fallback declared
yes
source exactness preserved
yes

8.3 External analysis intake checks

Check
Pass condition
envelope schema valid
yes
analysis run metadata present
yes
source scope present
yes
findings array present
yes
normalization path available
yes

9. Intake decision outcomes

Outcome
Meaning
publish_to_pilot
proceed into substrate
publish_with_review_flag
proceed but require review
quarantine
hold pending missing information or trust concern
reject
malformed or non-conforming submission
defer
out of pilot scope

10. Required logging


Each intake job MUST log:

Field
Meaning
intake job ID
unique intake event
submitted refs
sources included
operator
actor
path chosen
text/code/analysis
preflight result
pass/fail
output counts
objects produced
anomalies
parse failures, trust mismatches, dedup issues
final outcome
publish/quarantine/etc.

11. Pilot metrics


Pilot intake SHOULD measure:

Metric
Meaning
source acceptance rate
submissions that pass
parse success rate
successful refinery start
atom yield
objects produced per source
review flag rate
ambiguity/trust burden
quarantine rate
problematic intake frequency
time to publish
operational throughput

12. Final normative judgment


A valid pilot intake process MUST register every source before processing, MUST log preflight and outcome decisions, MUST support quarantine for ambiguous cases, and SHOULD optimize for auditability over speed.
