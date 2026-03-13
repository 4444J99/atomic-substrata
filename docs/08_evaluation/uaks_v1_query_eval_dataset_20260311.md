---
title: "3. Evaluation Query Dataset v1"
artifact_id: uaks_v1_query_eval_dataset_20260311
pair_id: CHATPAIR-015
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

3. Evaluation Query Dataset v1


Document ID: uaks_v1_query_eval_dataset_20260311


3.1 Purpose


The query dataset evaluates whether retrieval produces the correct objects.


Queries simulate real use.



3.2 Query categories

Category
Example
concept query
“analysis normalization rules”
code query
“function that parses analysis bundles”
policy query
“rules for accepting analysis findings”
trace query
“what code implements the validation policy”
impact query
“what changes if normalization rule changes”
research query
“analysis techniques used in corpus”


3.3 Dataset size

Query type
Minimum count
concept queries
100
code queries
100
trace queries
50
impact queries
50
research queries
50

Total minimum: 350 queries



3.4 Query schema

Field
Meaning
queryId
unique identifier
queryText
natural language query
intentClass
concept/code/policy/etc
expectedObjects
gold results
acceptableAlternatives
secondary acceptable answers
