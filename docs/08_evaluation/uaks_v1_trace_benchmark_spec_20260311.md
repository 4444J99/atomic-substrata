---
title: "4. Trace Benchmark Specification v1"
artifact_id: uaks_v1_trace_benchmark_spec_20260311
pair_id: CHATPAIR-015
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

4. Trace Benchmark Specification v1


Document ID: uaks_v1_trace_benchmark_spec_20260311


4.1 Purpose


This benchmark tests graph traversal accuracy.



4.2 Trace scenarios

Scenario
Test
rule-to-code
policy implemented by code
claim-to-evidence
claim supported by sources
change impact
dependency graph correctness
analysis-to-review
drift triggers review


4.3 Example scenario


Origin: policy_atom_005
Expected path:
policy_atom_005
  -> AFFECTS
code_atom_validation
  -> TESTS
code_atom_validation_tests



4.4 Evaluation criteria

Criterion
Meaning
path correctness
graph path matches gold set
missing edges
missing relation detection
extra edges
false positives
trace completeness
full path coverage


5. Evaluation Dataset Packaging


The evaluation pack MUST include:

Artifact
Description
corpus snapshot
immutable dataset
gold atom dataset
expected outputs
gold relation dataset
expected graph
query dataset
evaluation queries
trace scenarios
graph traversal tests


6. Evaluation Execution Rules


The evaluation harness MUST:


ingest benchmark corpus

run refinery pipelines

compare produced atoms to gold set

run retrieval queries

compute retrieval metrics

run trace scenarios

produce evaluation report



7. Evaluation Metrics


Refinery metrics

Metric
Meaning
atom precision
correct atoms produced
atom recall
expected atoms captured
relation precision
correct relations extracted
dedup accuracy
duplicate collapse correctness


Retrieval metrics

Metric
Meaning
precision@k
correct objects in top results
recall@k
coverage of gold results
MRR
ranking quality
semantic recall
conceptual retrieval ability


Trace metrics

Metric
Meaning
path accuracy
correct graph traversal
completeness
full path found
error rate
incorrect edges


Evaluation Pack A Completion


With this pack complete, the system now has:


benchmark inputs

gold reference outputs

query evaluation dataset

trace scenarios


This enables objective testing of refinery, retrieval, and graph correctness.



Remaining Packs Until Phase Completion

Pack
Purpose
Evaluation Pack B
evaluation harnesses
Truth Lifecycle Pack
supersession + contradiction rules
Integrity Pack
hashing + atomicity tests
Launch Pack
capacity model + readiness gate


Recommended Next Step


The next pack should be Evaluation Pack B, which defines:


retrieval evaluation harness

assembly evaluation harness

trace coverage report

drift detection report


This completes the measurement layer of the system.
