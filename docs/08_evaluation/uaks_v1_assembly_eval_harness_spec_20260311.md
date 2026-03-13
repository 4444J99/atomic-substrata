---
title: "2 Assembly Evaluation Harness Specification"
artifact_id: uaks_v1_assembly_eval_harness_spec_20260311
pair_id: CHATPAIR-016
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

2 Assembly Evaluation Harness Specification


Document ID: uaks_v1_assembly_eval_harness_spec_20260311


Purpose


Tests whether assembled outputs are faithful to the underlying atoms.


It evaluates:


correctness

coverage

hallucination avoidance

provenance traceability



Harness workflow

Step
Description
AH-01
retrieve atoms for evaluation query
AH-02
run assembly engine
AH-03
generate output using template
AH-04
compare output to gold narrative
AH-05
check provenance references
AH-06
compute evaluation metrics


Assembly metrics

Metric
Meaning
factual correctness
statements match substrate atoms
atom coverage
key atoms included
unsupported claims
hallucination detection
provenance completeness
traceability present
template compliance
output structure valid


Failure example


Example failure:


Output claim appears in assembled text but does not exist in substrate atoms.


Result:


Hallucination score increases.
