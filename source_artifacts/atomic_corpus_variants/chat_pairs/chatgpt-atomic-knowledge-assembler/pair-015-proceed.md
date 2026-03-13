---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 15
prompt_title: "Proceed"
response_title: "Evaluation Pack A v1"
prompt_sha256: "f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b"
response_sha256: "209bb30fdc6a4acb967ddd1ebaabef7c45edecbdc0cc27a057c9970a7bb5ee9f"
---

# Pair 015

## Prompt

Proceed

## Response

Evaluation Pack A v1


Unified Atomic Knowledge Substrate (UAKS)


Document ID: uaks_v1_evaluation_pack_A_20260311
Version: 1.0-draft
Status: Evaluation specification


This pack defines the evaluation inputs required to measure whether the architecture behaves correctly.


It establishes:


the Benchmark Corpus

the Gold-Standard Atom Set

canonical evaluation queries

baseline trace expectations


Without these artifacts the system cannot be objectively evaluated.



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



2. Gold-Standard Atom Set Specification v1


Document ID: uaks_v1_gold_atom_set_spec_20260311


2.1 Purpose


The gold-standard atom set defines the correct atomization output for benchmark sources.


It is used to evaluate:


refinery correctness

atomic boundary decisions

relation extraction

deduplication behavior



2.2 Gold atom design rules


Each gold atom MUST:


represent a single independent claim or function

include exact source span

include correct atom type

include expected relations



2.3 Gold atom schema

Field
Meaning
goldAtomId
canonical atom identifier
sourceRef
original source
atomType
TextAtom / PolicyAtom / CodeAtom / EvidenceAtom
canonicalStatement
distilled meaning
sourceSpan
exact location
expectedRelations
relation edges
validationState
expected trust level


2.4 Gold relation specification


Relations in the gold set define expected graph structure.

Relation
Example
SUPPORTED_BY
claim supported by evidence
IMPLEMENTS
code implements rule
AFFECTS
policy affects code
DERIVED_FROM
atom from source


2.5 Example gold atom


goldAtomId: gold_atom_014
sourceRef: src_policy_002
atomType: PolicyAtom
canonicalStatement: Imported analysis bundles must pass normalization before publication.
sourceSpan: lines 12–15
expectedRelations:
  - AFFECTS: atom_code_import_pipeline
validationState: VERIFIED



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