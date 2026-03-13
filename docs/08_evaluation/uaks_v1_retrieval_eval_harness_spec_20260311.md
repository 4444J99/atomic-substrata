---
title: "1 Retrieval Evaluation Harness Specification"
artifact_id: uaks_v1_retrieval_eval_harness_spec_20260311
pair_id: CHATPAIR-016
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

1 Retrieval Evaluation Harness Specification


Document ID: uaks_v1_retrieval_eval_harness_spec_20260311


Purpose


Measures whether the retrieval layer returns the correct atoms and objects for evaluation queries.


This harness evaluates:


lexical retrieval

semantic retrieval

graph retrieval

hybrid scoring



Harness inputs

Input
Source
benchmark corpus
evaluation pack A
gold atom set
evaluation pack A
query dataset
evaluation pack A
scoring profiles
retrieval spec
system index
substrate database


Harness workflow

Step
Description
RH-01
load evaluation queries
RH-02
execute retrieval pipeline
RH-03
capture ranked results
RH-04
compare results to gold objects
RH-05
compute ranking metrics
RH-06
produce evaluation report


Retrieval metrics

Metric
Meaning
Precision@5
percent of correct objects in top 5
Precision@10
percent of correct objects in top 10
Recall@10
percent of gold objects retrieved
Mean Reciprocal Rank
ranking quality
Semantic Recall
conceptual retrieval success
Graph Recall
ability to follow relations


Example result

Query
Expected
Retrieved
Score
normalization rule
3 atoms
3 atoms
correct
code parser function
1 atom
1 atom
correct
policy validation
2 atoms
1 atom
partial
