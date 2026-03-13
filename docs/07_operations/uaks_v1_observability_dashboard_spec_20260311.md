---
title: "4. Observability Dashboard Spec v1"
artifact_id: uaks_v1_observability_dashboard_spec_20260311
pair_id: CHATPAIR-014
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

4. Observability Dashboard Spec v1


Document ID: uaks_v1_observability_dashboard_spec_20260311


Observability ensures operational visibility.



4.1 Core dashboard sections

Section
Purpose
ingestion metrics
intake throughput
refinery metrics
atomization success
trust metrics
validation and review state
retrieval metrics
ranking performance
projection metrics
portal health
system metrics
infrastructure health


4.2 Intake metrics

Metric
Meaning
sources ingested
intake volume
intake success rate
successful registration
quarantine rate
problematic sources
processing latency
time to publish


4.3 Refinery metrics

Metric
Meaning
parse success rate
AST/parser reliability
atoms produced per source
yield
deduplication rate
redundancy control
anomaly rate
parse or classification failures


4.4 Trust metrics

Metric
Meaning
objects by validation state
trust distribution
review backlog
review workload
dispute rate
conflict frequency
promotion rate
acceptance throughput


4.5 Retrieval metrics

Metric
Meaning
query latency
performance
precision@k
ranking quality
recall@k
coverage
trace accuracy
graph correctness


4.6 Projection metrics

Metric
Meaning
projection generation latency
portal responsiveness
projection error rate
rendering failures
cache hit rate
projection reuse


4.7 System metrics

Metric
Meaning
CAS storage growth
storage health
graph DB latency
graph performance
vector index health
semantic retrieval health
API throughput
resolver load
