---
title: "Federated Analytical Producer Contract"
artifact_id: uaks_v1_external_analysis_integration_spec_20260311
pair_id: CHATPAIR-007
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

4. External Analysis Integration Spec v1


Federated Analytical Producer Contract


Document ID: uaks_v1_external_analysis_integration_spec_20260311
Version: 1.0-draft


4.1 Purpose


This specification defines how external analytical systems, especially linguistic-analysis systems, publish structured outputs into UAKS-v1 without collapsing the boundary between evidence and derivative interpretation.


The external system is a parallel producer, not a raw source adapter and not a canonical truth authority.


4.2 Core Design Rule


The integration model MUST be:

Stage
Role
Publish
External system emits structured analytical envelope
Normalize
UAKS translation membrane maps foreign schema to local ontology
Ingest
Normalized analysis objects become governed atoms and relations

4.3 Exchange Envelope


The external system MUST publish machine-readable result bundles.


4.3.1 Required Envelope Fields

Field
Type
Meaning
analysis_run_id
String
Unique run identifier
analysis_type
String
Discourse, semantic drift, syntax, rhetoric, etc.
engine_name
String
External system identity
engine_version
String
Version
method
String
Algorithm/model/process
timestamp
DateTime
Time produced
source_scope
Object
Corpus slice analyzed
parameters
Object
Run parameters
findings
Array
Analytical findings
relations
Array
Proposed cross-object edges
ontology_version
String
External ontology version if any
schema_version
String
Exchange schema version

4.3.2 Finding Object Fields

Field
Type
Meaning
finding_id
String
Stable ID within run or across runs
finding_kind
String
observation, interpretation, metric, taxonomy_proposal, signature, drift
finding_text
String
Human-readable normalized statement
confidence
Float/String
Confidence score or category
evidence_refs
Array
Source spans or internal IDs
tags
Array
External tags
supersedes
String
Prior finding ID if relevant
metrics
Object
Numeric details if applicable
cluster_id
String
External grouping ID if applicable
time_window_a
Object
For drift or comparative runs
time_window_b
Object
For drift or comparative runs
suggested_relations
Array
Proposed edges to atoms/entities

4.4 Source Scope Contract


The external system MUST define the analyzed corpus precisely enough for reproducibility.

Scope Field
Meaning
source_ids
Source objects or external source identifiers
conversation_ids
Conversational units analyzed
document_ids
Documents analyzed
project_scope
Project boundary
author_scope
Author or actor filter
time_window
Temporal slice
selection_filters
Any additional filtering logic

4.5 Normalization Membrane


The normalization membrane is mandatory. It MUST insulate UAKS from foreign assumptions.


4.5.1 Membrane Functions

Function
Description
Identifier resolution
Map external references to internal source/atom/entity IDs
Ontology mapping
Convert external categories to local atom types
Trust assignment
Apply imported/machine-derived states
Evidence binding
Link findings to source spans or evidence atoms
Deduplication
Merge equivalent findings while preserving lineage
Provenance generation
Record analysis and transformation provenance
Relation generation
Convert suggested relations into typed graph edges

4.5.2 Membrane Output Types

External Finding Kind
Internal Type
observation
ObservationAtom
interpretation
InterpretationAtom
metric
MetricAtom
taxonomy_proposal
TaxonomyProposalAtom
signature
SignatureAtom
drift
DriftAtom
run_metadata
AnalysisRunAtom

4.6 Provenance Requirements


Analytical imports require a three-layer provenance model.


4.6.1 Source Provenance

Field
Requirement
corpus scope
MUST be recorded
source references
MUST be recorded if available
time scope
SHOULD be recorded if relevant

4.6.2 Analysis Provenance

Field
Requirement
engine name
MUST be recorded
engine version
SHOULD be recorded
method
MUST be recorded
parameters
SHOULD be recorded
ontology/dictionary version
SHOULD be recorded
timestamp
MUST be recorded

4.6.3 Transformation Provenance

Field
Requirement
import job ID
MUST be recorded
normalization schema version
MUST be recorded
conflict-resolution logic
SHOULD be recorded
deduplication outcome
SHOULD be recorded

4.7 Trust and Validation Policy


Imported analysis MUST NOT silently become canonical truth.

State
Meaning
Assembly Eligibility
IMPORTED
Raw accepted bundle
No normal assembly
MACHINE_DERIVED
Parsed and normalized
Exploratory only by default
REVIEWED
Human/trusted review completed
Conditional
ACCEPTED
Approved for normal assembly
Yes
EXPERIMENTAL
Research lane only
No standard assembly
DISPUTED
Challenged
No
DEPRECATED
Retired
No

4.8 Relation Mapping


The integration layer SHOULD map useful external edges into the internal relation vocabulary.

External Intent
Internal Relation
analyzed corpus
ANALYZES
aligns to concept
MAPS_TO
proposes category
PROPOSES_TAXONOMY_FOR
detects change
DETECTS_DRIFT_IN
structurally describes
CHARACTERIZES
flags re-evaluation
REQUIRES_REVIEW_OF
replaces prior analysis
IS_SUPERSEDED_BY

4.9 Deduplication and Conflict Rules

Rule ID
Requirement
EAI-DEDUP-01
Equivalent findings MAY be merged if provenance multiplicity is preserved.
EAI-DEDUP-02
Conflicting findings MUST remain separately representable.
EAI-DEDUP-03
New findings that replace old findings SHOULD use supersession edges.

4.10 Synchronous vs Asynchronous Integration


The systems SHOULD be operationally asynchronous and logically composable.

Mode
Decision
External run execution
Asynchronous
Bundle publishing
Asynchronous
Ingestion into UAKS
Controlled pipeline
Query-time retrieval
Federated or pre-ingested
Assembly-time inclusion
Policy-gated

4.11 Assembly Policy for Analysis Objects


Analysis objects MAY be included differently based on output mode.

Output Mode
Analysis Inclusion Policy
Standard operational output
Only ACCEPTED analysis atoms
Research output
ACCEPTED, REVIEWED, optionally EXPERIMENTAL
Exploratory output
MACHINE_DERIVED allowed if explicitly requested
Compliance / high-trust output
Analysis lane excluded unless specifically approved

4.12 Initial Minimal Import JSON Shape


{
  "analysis_run_id": "run_20260311_001",
  "analysis_type": "semantic_drift",
  "engine_name": "external_linguistic_engine",
  "engine_version": "1.2.0",
  "method": "embedding_drift_plus_topic_alignment",
  "timestamp": "2026-03-11T12:00:00Z",
  "source_scope": {
    "project_scope": "project_alpha",
    "source_ids": ["src_001", "src_002"],
    "time_window": {
      "start": "2025-01-01T00:00:00Z",
      "end": "2026-03-01T00:00:00Z"
    }
  },
  "parameters": {
    "cluster_count": 12,
    "similarity_threshold": 0.82
  },
  "findings": [
    {
      "finding_id": "finding_001",
      "finding_kind": "drift",
      "finding_text": "The concept 'validation' shifted from schema conformance toward policy enforcement across the corpus.",
      "confidence": 0.91,
      "evidence_refs": ["src_001#L10-L20", "src_002#L33-L44"],
      "tags": ["semantic_drift", "validation", "policy"],
      "time_window_a": {
        "start": "2025-01-01T00:00:00Z",
        "end": "2025-06-30T23:59:59Z"
      },
      "time_window_b": {
        "start": "2025-07-01T00:00:00Z",
        "end": "2026-03-01T00:00:00Z"
      },
      "suggested_relations": [
        {
          "relation_type": "REQUIRES_REVIEW_OF",
          "target_id": "atom_policy_123"
        }
      ]
    }
  ],
  "relations": []
}


4.13 Final Integration Judgment


The external analytical system is now formally modeled as:

Role
Status
Raw source adapter
No
Canonical truth authority
No
Parallel analytical producer
Yes
First-class integration lane
Yes

That is the correct abstraction boundary.



5. Recommended Immediate Next Build Set


With all four documents now established, the highest-value next construction set is:

Priority
Artifact
1
Schema Pack v1 in machine-readable JSON Schema or TypeScript types
2
Text Refinery Specification v1
3
Code Refinery Specification v1
4
Graph Relation Catalog v1
5
Validation and Trust Policy v1

The cleanest continuation is to draft the Schema Pack v1 next so the ontology and GraphQL contract can be locked into implementation form.
