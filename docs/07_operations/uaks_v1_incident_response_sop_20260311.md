---
title: "2. Incident Response SOP v1"
artifact_id: uaks_v1_incident_response_sop_20260311
pair_id: CHATPAIR-014
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

2. Incident Response SOP v1


Document ID: uaks_v1_incident_response_sop_20260311


2.1 Purpose


This procedure governs response to system incidents affecting data integrity, trust state, system availability, or operational correctness.



2.2 Incident categories

Category
Description
Data integrity incident
corrupted or incorrect atoms
Trust incident
incorrect validation state or promotion
Pipeline incident
refinery failure or parser regression
Retrieval incident
incorrect ranking behavior
Projection incident
broken workspace views
Security incident
unauthorized access or mutation
Performance incident
degraded system responsiveness


2.3 Incident severity

Level
Meaning
S1
critical integrity or security failure
S2
major operational disruption
S3
moderate issue affecting subset of users
S4
minor anomaly


2.4 Incident response workflow

Phase
Description
IR-01
detection
IR-02
classification
IR-03
containment
IR-04
diagnosis
IR-05
remediation
IR-06
verification
IR-07
incident report


2.5 Example incidents


Pipeline parser failure


Symptoms:


refinery stops producing atoms

AST parse errors spike


Response:


pause pipeline

revert parser build

reprocess failed batch

generate incident report



Incorrect trust promotion


Symptoms:


machine-derived analysis marked accepted


Response:


mark affected atoms disputed

audit review events

correct validation state

patch review logic
