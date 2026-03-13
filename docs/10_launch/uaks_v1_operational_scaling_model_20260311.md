---
title: "3 Operational Scaling Model"
artifact_id: uaks_v1_operational_scaling_model_20260311
pair_id: CHATPAIR-019
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

3 Operational Scaling Model


Document ID: uaks_v1_operational_scaling_model_20260311


3.1 Pipeline throughput


Estimated refinery throughput:

Operation
Rate
text refinery
1000 paragraphs / hour
code refinery
200 files / hour
analysis ingestion
50 bundles / hour


3.2 Retrieval performance


Expected retrieval performance:

Query Type
Latency
lexical search
<50 ms
vector search
<100 ms
hybrid retrieval
<150 ms
graph traversal
<200 ms


3.3 Assembly performance

Output Size
Assembly Time
short answer
<1 sec
memo
<2 sec
technical report
<5 sec


4 Operational Staffing Model


Pilot operation can run with minimal staffing.

Role
Responsibility
operator
system operation
reviewer
trust validation
administrator
governance

Minimum pilot team:


2–3 people
