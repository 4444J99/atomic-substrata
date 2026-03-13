---
title: "Assembly Engine Specification v1"
artifact_id: uaks_v1_assembly_engine_spec_20260311
pair_id: CHATPAIR-009
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Assembly Engine Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_assembly_engine_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


The Assembly Engine converts governed atoms into human-facing outputs or saved recipes. It does not originate truth. It selects, sequences, and renders truth-bearing substrate objects subject to trust, scope, and template rules.


2. Inputs

Input
Description
query
user or system request
atom set
explicit list of atoms
recipe
prior assembly plan
template
output mold
resolution level
micro to deep
policy
trust and inclusion constraints

3. Outputs

Output
Description
rendered text
assembled human-readable output
recipe
reusable ordered atom plan
provenance refs
lineage exposure
warnings
ambiguity, missing support, low-trust inclusion

4. Assembly stages

Stage
Name
Purpose
AE-01
scope resolution
determine topic, audience, trust mode, depth
AE-02
candidate retrieval
fetch atoms through hybrid retrieval
AE-03
policy filtering
exclude ineligible states
AE-04
structural grouping
group atoms by role and template needs
AE-05
sequencing
order atoms logically
AE-06
connective synthesis
generate transitions and framing
AE-07
provenance packaging
attach source references if needed
AE-08
recipe persistence
save reusable assembly plan

5. Resolution model

Resolution
Inclusion logic
MICRO
highest-centrality core atoms only
COMPACT
core atoms plus minimal support
STANDARD
balanced claim, support, and context
EXTENDED
detailed support and operational structure
DEEP
evidence lattice, edge cases, contradictions, and lineage

6. Template classes

Template class
Purpose
Summary
concise overview
Technical Spec
formal structured explanation
Trace Report
rule-code or source-claim lineage
Impact Report
downstream effect analysis
Decision Memo
rationale, options, recommendation
Research Synthesis
multi-layer evidence-rich exposition

7. Engine rules

Rule ID
Requirement
AE-R-01
the engine MUST honor validation/trust policy
AE-R-02
the engine MUST NOT present unsupported generated claims as substrate truth
AE-R-03
connective prose MAY be generated
AE-R-04
recipe capture SHOULD store atom order, template, and resolution
AE-R-05
contradiction-aware outputs SHOULD surface scoped conflicts rather than flatten them

8. Minimal recipe object


{
  "recipeId": "recipe_101",
  "recipeType": "technical_spec",
  "resolutionLevel": "STANDARD",
  "atomSequence": ["atom_text_014", "atom_policy_005", "atom_code_021"],
  "templateRef": "template_technical_spec_v1",
  "generationRules": {
    "includeProvenance": true,
    "includeAnalysis": false
  },
  "createdAt": "2026-03-11T16:30:00Z"
}


9. Minimal assembly result


{
  "resultId": "assembly_101",
  "recipeRef": "recipe_101",
  "renderedText": "The system stores knowledge as atoms and renders documents as assemblies. Policy logic is enforced by linked code paths.",
  "atomIdsUsed": ["atom_text_014", "atom_policy_005", "atom_code_021"],
  "provenanceRefs": ["prov_014", "prov_005", "prov_021"],
  "warnings": []
}



Foundational Launch Artifact Set


Consolidated Launch Inventory


Below is the launch-ready foundational set, normalized from the prior architecture work into operational categories.


1. Governance ring

Artifact
Required
Vision and Thesis Document
Yes
Scope and Exclusions Charter
Yes
Ontology Charter v1
Yes
Naming Convention Standard
Yes
Provenance Policy
Yes
Validation and Trust Policy v1
Yes
Supersession Policy
Yes
Contradiction Handling Policy
Yes
Security and Rights Policy
Yes

2. Architecture ring

Artifact
Required
Architecture Specification v1
Yes
Visual Architecture Diagram
Yes
Logical Data Model
Yes
Physical Storage Architecture
Yes
Service Decomposition Spec
Yes
Trust Boundary Map
Yes
Failure Mode and Resilience Analysis
Yes
Nonfunctional Requirements Spec
Yes

3. Schema ring

Artifact
Required
Schema Pack v1
Yes
GraphQL Schema Draft v1
Yes
Graph Relation Catalog v1
Yes
CAS Object Model
Yes
Hashing Standard
Yes

4. Pipeline ring

Artifact
Required
Text Refinery Specification v1
Yes
Code Refinery Specification v1
Yes
External Analysis Integration Spec v1
Yes
Atomicity Test Suite
Yes
AST Parsing Strategy
Yes
Deduplication and Merge Policy
Yes
Re-refinement Protocol
Yes
QA Rubric
Yes

5. Retrieval and assembly ring

Artifact
Required
Retrieval Scoring Specification
Yes
Template Catalog
Yes
Assembly Engine Specification v1
Yes
Recipe Persistence Spec
Yes
Provenance Rendering Rules
Yes
Traceability Report Format
Yes
Impact Analysis Report Format
Yes

6. Interface and operations ring

Artifact
Required
Resolver Contract Specification
Yes
Query Pattern Library
Yes
Portal Projection Specification
Yes
Auth and Access Model
Yes
Pilot Intake SOP
Yes
Review Workflow SOP
Yes
Change Management SOP
Yes
Incident Response SOP
Yes
Release Checklist
Yes
Runbook Set
Yes
Observability Dashboard Spec
Yes

7. Evaluation ring

Artifact
Required
Benchmark Corpus Definition
Yes
Gold-Standard Atom Set
Yes
Retrieval Evaluation Harness
Yes
Assembly Evaluation Harness
Yes
Traceability Coverage Report
Yes
Drift Detection Report
Yes
Cost and Capacity Model
Yes
Launch Readiness Scorecard
Yes

8. Seed ring

Artifact
Required
Canonical Ontology Examples
Yes
Sample TextAtom Corpus
Yes
Sample CodeAtom Corpus
Yes
Rule-to-Code Bridge Examples
Yes
Initial Template Pack
Yes
Initial Recipe Pack
Yes


Recommended Build Order


Execution Sequence

Phase
Deliverables
Phase 1
governance pack, ontology charter, naming, provenance, trust
Phase 2
architecture spec, diagram, trust boundary map, storage decisions
Phase 3
schema pack, relation catalog, GraphQL contract
Phase 4
text refinery, code refinery, analysis integration, parsing strategy
Phase 5
retrieval scoring, templates, assembly engine, provenance rendering
Phase 6
SOPs, runbooks, auth, portal projection, release checklist
Phase 7
benchmarks, evaluation harnesses, readiness scorecard, seed corpora


Practical Recommendation


At this point, the highest-value next drafting cluster is:

Priority
Next artifact
1
Retrieval Scoring Specification
2
Deduplication and Merge Policy
3
AST Parsing Strategy
4
Portal Projection Specification
5
Release Checklist + Launch Readiness Scorecard

If you want the most implementation-useful continuation, the next correct move is the Retrieval Scoring Specification v1 pack.
