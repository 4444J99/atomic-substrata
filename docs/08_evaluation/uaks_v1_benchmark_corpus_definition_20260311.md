---
title: "1. Benchmark Corpus Definition v1"
artifact_id: uaks_v1_benchmark_corpus_definition_20260311
pair_id: CHATPAIR-015
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

1. Benchmark Corpus Definition v1


Document ID: uaks_v1_benchmark_corpus_definition_20260311


1.1 Purpose


The benchmark corpus is a controlled dataset used to test:


text refinery correctness

code refinery correctness

atomization behavior

deduplication behavior

relation extraction

retrieval ranking

trace accuracy


It must represent the variety of real-world inputs the system will face.



1.2 Corpus design principles

Principle
Meaning
coverage
represent multiple source types
complexity
include both simple and multi-claim sources
ambiguity
include ambiguous cases to test refinery discipline
scale
large enough to test retrieval
traceability
every source must have expected atom outputs


1.3 Corpus categories


The benchmark corpus SHOULD include these source families.

Category
Examples
conversational
transcripts, meeting notes
documentation
specifications, memos
policy
rules and normative statements
technical
code repositories and scripts
configuration
YAML, JSON, schema definitions
analytical
external analysis bundles


1.4 Minimum corpus composition

Source type
Minimum count
textual documents
100
policy documents
20
code repositories
10
code files
500
configuration files
50
analysis bundles
30

This scale allows meaningful retrieval testing.



1.5 Corpus structure


Each corpus item MUST contain metadata.

Field
Meaning
sourceId
unique identifier
sourceType
document, code, config, analysis
origin
where it came from
scope
project/domain
timestamp
when captured
expectedAtoms
approximate expected yield
notes
special features


1.6 Corpus storage


The benchmark corpus SHOULD be stored as:


immutable CAS objects

registered SourceObjects

reproducible dataset snapshot
