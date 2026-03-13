---
source_export: "ChatGPT-Atomic Knowledge Assembler.json"
pair_number: 21
prompt_title: "produce updates of final extremely useful artifacts"
response_title: "Updated Final Artifacts"
prompt_sha256: "e5a4cd64ac85222ec1764e0f559c1ef2b512b183667530e8e971a474640bb207"
response_sha256: "34261eab8555e87dcf73e6d7aefa545db20d1c598d5694005d4d0311778ea05e"
---

# Pair 021

## Prompt

produce updates of final extremely useful artifacts:


the automated repository generator script (so this entire system can be created locally with one command).


provide complete list of remaining artifacts; provide manifest covering length of this entire chat providing a unique ID and title for each prompt and response pairing and provide a completion matrix checklist covering all that needs to be done to take this chat and break it into a fully realized directory locally and provide an AI handoff prompt to do so


Finally:
It's a simple, one-paragraph prompt to be able to give to an AI engineer to execute perfectly what we need and ensure that everything's been preserved.

## Response

Thought for 1m 6s


Updated Final Artifacts


1. Automated Repository Generator Script


One-command local scaffold for the entire system


Save this as scripts/bootstrap_uaks_repo.sh, then run it with environment variables.


#!/usr/bin/env bash
set -euo pipefail

: "${PROJECT_SLUG:=uaks}"
: "${REPO_ROOT:=$PWD/${PROJECT_SLUG}}"
: "${AUTHOR_NAME:=unknown}"
: "${DATE_STAMP:=$(date +%Y%m%d)}"
: "${DEFAULT_BRANCH:=main}"
: "${PYTHON_BIN:=python3}"

mkdir -p "${REPO_ROOT}"
cd "${REPO_ROOT}"

mkdir -p \
  docs/00_meta \
  docs/01_governance \
  docs/02_architecture \
  docs/03_schemas \
  docs/04_refinery \
  docs/05_retrieval_assembly \
  docs/06_interface_portal \
  docs/07_operations \
  docs/08_evaluation \
  docs/09_integrity \
  docs/10_launch \
  docs/11_implementation \
  docs/12_seed_content \
  manifests \
  prompts \
  scripts \
  src \
  tests \
  data/benchmark \
  data/gold \
  data/import_samples \
  data/projections \
  .github/workflows

cat > README.md <<EOF
# ${PROJECT_SLUG}

Unified Atomic Knowledge Substrate repository scaffold.

Generated on: ${DATE_STAMP}
Author: ${AUTHOR_NAME}

## Quick start

\`\`\`bash
export PROJECT_SLUG="${PROJECT_SLUG}"
export REPO_ROOT="${REPO_ROOT}"
bash scripts/bootstrap_uaks_repo.sh
\`\`\`

## Repository intent

This repository holds the full architecture, governance, schema, refinery, retrieval, assembly, portal, operations, evaluation, integrity, and launch artifacts for the UAKS program.
EOF

cat > .gitignore <<'EOF'
__pycache__/
*.pyc
.venv/
.env
.DS_Store
coverage/
dist/
build/
*.log
EOF

cat > docs/00_meta/repository_charter.md <<EOF
# Repository Charter

Project: ${PROJECT_SLUG}
Generated: ${DATE_STAMP}
Author: ${AUTHOR_NAME}

This repository is the local realization of the UAKS design program.
EOF

create_doc () {
  local path="$1"
  local title="$2"
  cat > "$path" <<EOF
# ${title}

Status: draft
Owner: ${AUTHOR_NAME}
Created: ${DATE_STAMP}

## Purpose

TODO

## Source lineage

Derived from the UAKS architecture conversation artifact set.

## Notes

TODO
EOF
}

completed_docs=(
  "docs/02_architecture/uaks_v1_architecture_spec.md|UAKS v1 Architecture Specification"
  "docs/02_architecture/uaks_v1_visual_architecture.md|UAKS v1 Visual Architecture"
  "docs/02_architecture/uaks_v1_ontology_charter.md|UAKS v1 Ontology Charter"
  "docs/02_architecture/uaks_v1_external_analysis_integration_spec.md|UAKS v1 External Analysis Integration Specification"
  "docs/03_schemas/uaks_v1_schema_pack.md|UAKS v1 Schema Pack"
  "docs/03_schemas/uaks_v1_graphql_schema_draft.md|UAKS v1 GraphQL Schema Draft"
  "docs/04_refinery/uaks_v1_text_refinery_spec.md|UAKS v1 Text Refinery Specification"
  "docs/04_refinery/uaks_v1_code_refinery_spec.md|UAKS v1 Code Refinery Specification"
  "docs/05_retrieval_assembly/uaks_v1_retrieval_scoring_spec.md|UAKS v1 Retrieval Scoring Specification"
  "docs/05_retrieval_assembly/uaks_v1_template_catalog.md|UAKS v1 Template Catalog"
  "docs/05_retrieval_assembly/uaks_v1_provenance_rendering_rules.md|UAKS v1 Provenance Rendering Rules"
  "docs/05_retrieval_assembly/uaks_v1_traceability_report_format.md|UAKS v1 Traceability Report Format"
  "docs/05_retrieval_assembly/uaks_v1_impact_analysis_report_format.md|UAKS v1 Impact Analysis Report Format"
  "docs/05_retrieval_assembly/uaks_v1_assembly_engine_spec.md|UAKS v1 Assembly Engine Specification"
  "docs/06_interface_portal/uaks_v1_resolver_contract_spec.md|UAKS v1 Resolver Contract Specification"
  "docs/06_interface_portal/uaks_v1_query_pattern_library.md|UAKS v1 Query Pattern Library"
  "docs/06_interface_portal/uaks_v1_auth_access_model.md|UAKS v1 Auth and Access Model"
  "docs/06_interface_portal/uaks_v1_portal_projection_spec.md|UAKS v1 Portal Projection Specification"
  "docs/06_interface_portal/uaks_v1_portal_projection_data_model.md|UAKS v1 Portal Projection Data Model"
  "docs/07_operations/uaks_v1_change_management_sop.md|UAKS v1 Change Management SOP"
  "docs/07_operations/uaks_v1_incident_response_sop.md|UAKS v1 Incident Response SOP"
  "docs/07_operations/uaks_v1_runbook_set.md|UAKS v1 Runbook Set"
  "docs/07_operations/uaks_v1_observability_dashboard_spec.md|UAKS v1 Observability Dashboard Specification"
  "docs/07_operations/uaks_v1_release_gate_procedure.md|UAKS v1 Release Gate Procedure"
  "docs/07_operations/uaks_v1_pilot_intake_sop.md|UAKS v1 Pilot Intake SOP"
  "docs/07_operations/uaks_v1_review_workflow_sop.md|UAKS v1 Review Workflow SOP"
  "docs/08_evaluation/uaks_v1_benchmark_corpus_definition.md|UAKS v1 Benchmark Corpus Definition"
  "docs/08_evaluation/uaks_v1_gold_atom_set_spec.md|UAKS v1 Gold-Standard Atom Set Specification"
  "docs/08_evaluation/uaks_v1_query_eval_dataset.md|UAKS v1 Query Evaluation Dataset"
  "docs/08_evaluation/uaks_v1_trace_benchmark_spec.md|UAKS v1 Trace Benchmark Specification"
  "docs/08_evaluation/uaks_v1_retrieval_eval_harness_spec.md|UAKS v1 Retrieval Evaluation Harness Specification"
  "docs/08_evaluation/uaks_v1_assembly_eval_harness_spec.md|UAKS v1 Assembly Evaluation Harness Specification"
  "docs/08_evaluation/uaks_v1_trace_coverage_report_spec.md|UAKS v1 Traceability Coverage Report Specification"
  "docs/08_evaluation/uaks_v1_drift_detection_report_spec.md|UAKS v1 Drift Detection Report Specification"
  "docs/09_integrity/uaks_v1_supersession_policy.md|UAKS v1 Supersession Policy"
  "docs/09_integrity/uaks_v1_contradiction_policy.md|UAKS v1 Contradiction Handling Policy"
  "docs/09_integrity/uaks_v1_provenance_policy.md|UAKS v1 Provenance Policy"
  "docs/09_integrity/uaks_v1_hashing_standard.md|UAKS v1 Hashing Standard"
  "docs/09_integrity/uaks_v1_canonicalization_spec.md|UAKS v1 Canonicalization Specification"
  "docs/09_integrity/uaks_v1_atomicity_test_suite.md|UAKS v1 Atomicity Test Suite"
  "docs/09_integrity/uaks_v1_deduplication_protocol.md|UAKS v1 Deduplication Protocol"
  "docs/09_integrity/uaks_v1_integrity_verification_procedure.md|UAKS v1 Integrity Verification Procedure"
  "docs/10_launch/uaks_v1_capacity_model.md|UAKS v1 Capacity Model"
  "docs/10_launch/uaks_v1_storage_model.md|UAKS v1 Storage Model"
  "docs/10_launch/uaks_v1_operational_scaling_model.md|UAKS v1 Operational Scaling Model"
  "docs/10_launch/uaks_v1_launch_readiness_assessment.md|UAKS v1 Launch Readiness Assessment"
  "docs/10_launch/uaks_v1_launch_pack.md|UAKS v1 Launch Pack"
)

remaining_docs=(
  "docs/01_governance/vision_and_thesis.md|Vision and Thesis Document"
  "docs/01_governance/scope_and_exclusions_charter.md|Scope and Exclusions Charter"
  "docs/01_governance/naming_convention_standard.md|Naming Convention Standard"
  "docs/01_governance/security_and_rights_policy.md|Security and Rights Policy"
  "docs/02_architecture/logical_data_model.md|Logical Data Model"
  "docs/02_architecture/physical_storage_architecture.md|Physical Storage Architecture"
  "docs/02_architecture/service_decomposition_spec.md|Service Decomposition Specification"
  "docs/02_architecture/trust_boundary_map.md|Trust Boundary Map"
  "docs/02_architecture/failure_mode_and_resilience_analysis.md|Failure Mode and Resilience Analysis"
  "docs/02_architecture/nonfunctional_requirements_spec.md|Nonfunctional Requirements Specification"
  "docs/03_schemas/cas_object_model.md|CAS Object Model"
  "docs/03_schemas/hash_canonicalization_examples.md|Hash Canonicalization Examples"
  "docs/04_refinery/ast_parsing_strategy.md|AST Parsing Strategy"
  "docs/04_refinery/re_refinement_protocol.md|Re-Refinement Protocol"
  "docs/04_refinery/qa_rubric.md|QA Rubric"
  "docs/05_retrieval_assembly/recipe_persistence_spec.md|Recipe Persistence Specification"
  "docs/06_interface_portal/consumer_interface_contract.md|Consumer Interface Contract"
  "docs/07_operations/change_management_test_matrix.md|Change Management Test Matrix"
  "docs/07_operations/incident_playbooks.md|Incident Playbooks"
  "docs/08_evaluation/cost_and_capacity_model.md|Cost and Capacity Model"
  "docs/08_evaluation/launch_readiness_scorecard.md|Launch Readiness Scorecard"
  "docs/11_implementation/repository_generator_design.md|Repository Generator Design"
  "docs/11_implementation/implementation_plan.md|Implementation Plan"
  "docs/11_implementation/milestone_roadmap.md|Milestone Roadmap"
  "docs/11_implementation/ci_cd_plan.md|CI/CD Plan"
  "docs/11_implementation/environment_bootstrap.md|Environment Bootstrap"
  "docs/12_seed_content/canonical_ontology_examples.md|Canonical Ontology Examples"
  "docs/12_seed_content/sample_textatom_corpus.md|Sample TextAtom Corpus"
  "docs/12_seed_content/sample_codeatom_corpus.md|Sample CodeAtom Corpus"
  "docs/12_seed_content/rule_to_code_bridge_examples.md|Rule-to-Code Bridge Examples"
  "docs/12_seed_content/initial_recipe_pack.md|Initial Recipe Pack"
)

for item in "${completed_docs[@]}"; do
  IFS='|' read -r path title <<< "$item"
  mkdir -p "$(dirname "$path")"
  create_doc "$path" "$title"
done

for item in "${remaining_docs[@]}"; do
  IFS='|' read -r path title <<< "$item"
  mkdir -p "$(dirname "$path")"
  create_doc "$path" "$title"
done

cat > manifests/repo_manifest.csv <<'EOF'
artifact_id,path,status
ART-0001,docs/02_architecture/uaks_v1_architecture_spec.md,drafted_in_chat
ART-0002,docs/02_architecture/uaks_v1_ontology_charter.md,drafted_in_chat
ART-0003,docs/03_schemas/uaks_v1_schema_pack.md,drafted_in_chat
ART-0004,docs/04_refinery/uaks_v1_text_refinery_spec.md,drafted_in_chat
ART-0005,docs/04_refinery/uaks_v1_code_refinery_spec.md,drafted_in_chat
ART-0006,docs/05_retrieval_assembly/uaks_v1_retrieval_scoring_spec.md,drafted_in_chat
ART-0007,docs/05_retrieval_assembly/uaks_v1_assembly_engine_spec.md,drafted_in_chat
ART-0008,docs/06_interface_portal/uaks_v1_resolver_contract_spec.md,drafted_in_chat
ART-0009,docs/07_operations/uaks_v1_change_management_sop.md,drafted_in_chat
ART-0010,docs/08_evaluation/uaks_v1_benchmark_corpus_definition.md,drafted_in_chat
ART-0011,docs/09_integrity/uaks_v1_hashing_standard.md,drafted_in_chat
ART-0012,docs/10_launch/uaks_v1_launch_pack.md,drafted_in_chat
EOF

cat > manifests/chat_pair_manifest.csv <<'EOF'
pair_id,user_title,assistant_title
CHATPAIR-001,Theoretical Specification Request,Atomic Knowledge Assembler Specification
CHATPAIR-002,Cost Benefit and Code-Lane Integration Request,Recommendation and Integration Strategy
CHATPAIR-003,Single v1 Architecture Spec Request,Unified v1 Architecture and Artifact Inventory
CHATPAIR-004,Proceed to Document-Grade Spec,Document-Grade Architecture Specification
CHATPAIR-005,When to Provide Addenda,Addenda Timing Guidance
CHATPAIR-006,Addendum Submission,Addendum Integration Review
CHATPAIR-007,Proceed with All Addendum Follow-Ons,Diagram Ontology GraphQL and Integration Spec
CHATPAIR-008,Proceed to Schema Pack,Schema Pack v1
CHATPAIR-009,Proceed All to Refinery and Operations Specs,Refinery Retrieval Assembly and Inventory Set
CHATPAIR-010,Proceed to Retrieval Spec,Retrieval Scoring and Control Specs
CHATPAIR-011,Proceed to Templates and Report Formats,Template Provenance Trace Impact Resolver Set
CHATPAIR-012,Proceed to Query and Workflow Specs,Query Access Portal Intake Review Set
CHATPAIR-013,Remaining Steps Until Phase Completion,Phase Completion Roadmap
CHATPAIR-014,Proceed to Operations Pack,Operations Pack v1
CHATPAIR-015,Proceed to Evaluation Pack A,Evaluation Pack A v1
CHATPAIR-016,Proceed and Ask Remaining Rounds,Evaluation Pack B and Round Count
CHATPAIR-017,Proceed to Truth Lifecycle Pack,Truth Lifecycle Pack v1
CHATPAIR-018,Proceed to Integrity Pack,Integrity Pack v1
CHATPAIR-019,Proceed to Launch Pack,Launch Pack v1 and Phase Completion
CHATPAIR-020,Generate Visual Architecture Diagram,Image Diagram Generation
CHATPAIR-021,Repository Generator and Final Artifact Request,Repository Generator Manifest Matrix and Handoff Prompts
EOF

cat > prompts/ai_handoff_full.md <<'EOF'
You are the implementation and repository-assembly engineer for the Unified Atomic Knowledge Substrate. Reconstruct the full repository from the conversation-derived artifact set without losing semantics, IDs, lineage, or scope boundaries. Create a local repository that preserves every drafted specification as a separate file, externalizes all manifests, creates placeholders for remaining undrafted artifacts, and adds implementation scaffolding for ingestion, refinery, graph, vector, CAS, retrieval, assembly, portal, operations, evaluation, integrity, and launch control. Preserve canonical document IDs, object families, relation vocabulary, trust states, and phase-completion logic. Do not collapse evidence, primary atoms, and analytical derivatives into one type. Use the repository manifest and chat-pair manifest as authoritative mapping tables. Output a complete directory tree, write every file, seed benchmark and gold data directories, create environment-based bootstrap scripts, and leave explicit TODO markers only where the conversation never supplied final content.
EOF

cat > prompts/ai_handoff_one_paragraph.md <<'EOF'
Rebuild the entire UAKS repository locally from the supplied conversation artifacts by externalizing every drafted specification into its own file, preserving all IDs, ontology boundaries, trust states, relation types, manifests, and lifecycle rules, creating placeholders for any still-undrafted documents, generating the full directory structure, bootstrap scripts, seed data folders, and implementation scaffolding, and ensuring nothing from the architecture, governance, refinery, retrieval, assembly, portal, operations, evaluation, integrity, or launch layers is lost, flattened, or silently altered.
EOF

cat > scripts/bootstrap_env.sh <<EOF
#!/usr/bin/env bash
export PROJECT_SLUG="${PROJECT_SLUG}"
export REPO_ROOT="${REPO_ROOT}"
export AUTHOR_NAME="${AUTHOR_NAME}"
export DATE_STAMP="${DATE_STAMP}"
export DEFAULT_BRANCH="${DEFAULT_BRANCH}"
export PYTHON_BIN="${PYTHON_BIN}"
EOF
chmod +x scripts/bootstrap_env.sh

cat > scripts/print_tree.py <<'EOF'
from pathlib import Path

def walk(path: Path, prefix: str = ""):
    entries = sorted([p for p in path.iterdir()], key=lambda p: (p.is_file(), p.name))
    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)
        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            walk(entry, prefix + extension)

root = Path(".")
print(root.resolve().name)
walk(root)
EOF

if [ ! -d .git ]; then
  git init -b "${DEFAULT_BRANCH}"
fi

echo "Repository scaffold created at: ${REPO_ROOT}"
echo "Next step: paste drafted document content into the generated markdown files."


Suggested usage


export PROJECT_SLUG="uaks"
export REPO_ROOT="$HOME/work/uaks"
export AUTHOR_NAME="AJP"
bash scripts/bootstrap_uaks_repo.sh



2. Complete List of Remaining Artifacts


There are really three categories of “remaining” artifacts.


A. Drafted in chat, but not yet externalized into files

Status ID
Artifact
EXT-001
All drafted markdown specs generated in this conversation
EXT-002
Image diagram file and companion explanatory markdown
EXT-003
Consolidated repository manifest
EXT-004
Consolidated phase-completion index

B. Not yet fully drafted as standalone final docs

Status ID
Artifact
REM-001
Vision and Thesis Document
REM-002
Scope and Exclusions Charter
REM-003
Naming Convention Standard
REM-004
Security and Rights Policy
REM-005
Logical Data Model
REM-006
Physical Storage Architecture
REM-007
Service Decomposition Specification
REM-008
Trust Boundary Map
REM-009
Failure Mode and Resilience Analysis
REM-010
Nonfunctional Requirements Specification
REM-011
CAS Object Model
REM-012
Recipe Persistence Specification
REM-013
Re-Refinement Protocol
REM-014
QA Rubric
REM-015
Consumer Interface Contract
REM-016
Change Management Test Matrix
REM-017
Incident Playbooks
REM-018
Cost and Capacity Model
REM-019
Canonical Ontology Examples
REM-020
Sample TextAtom Corpus
REM-021
Sample CodeAtom Corpus
REM-022
Rule-to-Code Bridge Examples
REM-023
Initial Recipe Pack
REM-024
Implementation Plan
REM-025
Milestone Roadmap
REM-026
CI/CD Plan
REM-027
Environment Bootstrap Guide

C. Implementation artifacts still required to make the repo operational

Status ID
Artifact
IMP-001
src/ codebase for source intake
IMP-002
src/ text refinery implementation
IMP-003
src/ code refinery implementation
IMP-004
graph storage integration
IMP-005
vector index integration
IMP-006
CAS storage layer
IMP-007
GraphQL service
IMP-008
projection service
IMP-009
evaluation harness code
IMP-010
benchmark dataset fixtures
IMP-011
gold atom fixtures
IMP-012
CI workflow files
IMP-013
environment bootstrap scripts
IMP-014
import pipeline for external analysis bundles
IMP-015
observability dashboards / metrics wiring
IMP-016
release automation and rollback scripts


3. Full Manifest of This Chat


Unique ID and title for each prompt/response pair

Pair ID
User Prompt Title
Assistant Response Title
CHATPAIR-001
Design Theoretical Specifications
Atomic Knowledge Assembler Theoretical Specification
CHATPAIR-002
Cost, Benefits, and Recommendation
Artifact Ranking and Code-Lane Integration Recommendation
CHATPAIR-003
Single v1 Architecture Spec Request
Unified v1 Architecture Spec and Foundational Artifact Inventory
CHATPAIR-004
Proceed to Document-Grade Architecture
Document-Grade UAKS Architecture Specification
CHATPAIR-005
Addendum Timing Question
Addendum Intake Timing Guidance
CHATPAIR-006
Addendum Submission
Addendum Integration Review and Domain Expansion
CHATPAIR-007
Proceed with All Addendum Follow-Ons
Diagram, Ontology Charter, GraphQL Draft, and Analysis Integration Spec
CHATPAIR-008
Proceed to Schema Pack
UAKS Schema Pack v1
CHATPAIR-009
Proceed All on Remaining Core Specs
Text Refinery, Code Refinery, Relation Catalog, Trust Policy, Assembly Spec
CHATPAIR-010
Proceed to Retrieval Layer
Retrieval Scoring, Deduplication, AST Strategy, Portal, Release, Readiness
CHATPAIR-011
Proceed to Template and Reporting Layer
Template Catalog, Provenance Rendering, Trace, Impact, Resolver Contract
CHATPAIR-012
Proceed to Query and Workflow Layer
Query Pattern Library, Access Model, Portal Data Model, Intake SOP, Review SOP
CHATPAIR-013
Remaining Steps Until Phase Completion
Phase Closure Roadmap and Pack Strategy
CHATPAIR-014
Proceed to Operations Pack
Operations Pack v1
CHATPAIR-015
Proceed to Evaluation Pack A
Benchmark Corpus, Gold Atom Set, Query Dataset, Trace Benchmark
CHATPAIR-016
Proceed and Ask Remaining Rounds
Evaluation Pack B and Remaining Round Count
CHATPAIR-017
Proceed to Truth Lifecycle Pack
Supersession, Contradiction, and Provenance Governance
CHATPAIR-018
Proceed to Integrity Pack
Hashing, Canonicalization, Atomicity, Deduplication, Integrity Verification
CHATPAIR-019
Proceed to Launch Pack
Capacity, Storage, Scaling, Readiness, Phase Completion
CHATPAIR-020
Generate Final Visual Diagram
UAKS Visual Architecture Diagram
CHATPAIR-021
Repository Generator and Final Preservation Request
Bootstrap Script, Remaining Artifacts, Manifest, Completion Matrix, Handoff Prompts


4. Completion Matrix Checklist


Everything needed to take this chat into a fully realized local directory

Matrix ID
Work Item
Current State
Required Next Action
Completion
CM-001
Extract drafted specs from chat
drafted in chat
paste into markdown files
☐
CM-002
Create canonical repo tree
not externalized
run bootstrap script
☐
CM-003
Save visual architecture diagram
image generated
place under docs/02_architecture/ or assets/
☐
CM-004
Build repository manifest
partial
expand manifest to all artifacts
☐
CM-005
Build chat pair manifest
done conceptually
save as CSV/MD
☐
CM-006
Externalize governance docs
partial
finalize missing standalone docs
☐
CM-007
Externalize architecture docs
mostly drafted
save and normalize IDs
☐
CM-008
Externalize schema docs
mostly drafted
convert to machine-readable JSON Schema/TS
☐
CM-009
Externalize refinery docs
drafted
create implementation tickets
☐
CM-010
Externalize retrieval/assembly docs
drafted
create config and test fixtures
☐
CM-011
Externalize portal/interface docs
drafted
define API file layout
☐
CM-012
Externalize operations docs
drafted
create executable SOP checklists
☐
CM-013
Externalize evaluation docs
drafted
create datasets and harness code
☐
CM-014
Externalize integrity docs
drafted
implement canonicalization and hashing code
☐
CM-015
Externalize launch docs
drafted
compute readiness thresholds in code
☐
CM-016
Create benchmark corpus files
not built
populate data/benchmark/
☐
CM-017
Create gold atom fixtures
not built
populate data/gold/
☐
CM-018
Create sample import bundles
not built
populate data/import_samples/
☐
CM-019
Implement source intake
not built
create src/intake/
☐
CM-020
Implement text refinery
not built
create src/refinery/text/
☐
CM-021
Implement code refinery
not built
create src/refinery/code/
☐
CM-022
Implement analysis normalization membrane
not built
create src/imports/analysis/
☐
CM-023
Implement graph layer
not built
create graph adapters and models
☐
CM-024
Implement vector layer
not built
create embedding/index adapters
☐
CM-025
Implement CAS layer
not built
create content store and hash verification
☐
CM-026
Implement GraphQL contract
not built
create schema and resolvers
☐
CM-027
Implement assembly engine
not built
create template-aware assembler
☐
CM-028
Implement projection layer
not built
create workspace/document/trace projections
☐
CM-029
Implement evaluation harnesses
not built
create test runners and reports
☐
CM-030
Implement observability
not built
connect metrics and dashboards
☐
CM-031
Implement release controls
not built
create release scripts and rollback path
☐
CM-032
Normalize document IDs and filenames
partial
enforce canonical naming
☐
CM-033
Preserve provenance from chat to files
partial
annotate each file with source lineage
☐
CM-034
Create AI handoff pack
partial
save prompts and manifests
☐
CM-035
Final repo QA pass
not done
verify tree, manifests, IDs, and missing docs
☐


5. AI Handoff Prompt


Full version


Use this when handing the job to an AI engineer or coding agent.


You are the repository-assembly and implementation engineer for the Unified Atomic Knowledge Substrate (UAKS). Your job is to reconstruct the entire local repository from the architecture conversation artifact set without losing semantics, document IDs, ontology boundaries, trust states, relation vocabulary, provenance rules, or lifecycle logic. Create the full repository tree, externalize every drafted specification into its own markdown file, preserve all canonical IDs and titles, create manifests for artifacts and chat-pair lineage, add placeholders only for content that was never fully drafted, and scaffold implementation directories for source intake, text refinery, code refinery, analysis normalization, graph storage, vector retrieval, content-addressable storage, GraphQL, assembly, portal projection, operations, evaluation, integrity verification, and launch control. Preserve the distinction between source evidence, primary atoms, and derivative analytical atoms. Preserve supersession, contradiction, provenance, and trust policies exactly. Generate bootstrap scripts, sample data directories, benchmark and gold fixture directories, and implementation TODO markers where code does not yet exist. Do not compress or merge distinct artifact families. Do not silently rename canonical documents. Produce a final repository tree, a completeness report, a list of unresolved placeholders, and a verification pass confirming that nothing from the conversation was dropped or flattened.



6. One-Paragraph Prompt


Minimal version for an AI engineer


Rebuild the full UAKS repository locally from the conversation-derived architecture set by externalizing every drafted spec into its own file, preserving all canonical IDs, ontology distinctions, trust states, provenance rules, relation types, supersession and contradiction logic, manifests, and workflow documents, creating placeholders only for still-undrafted artifacts, scaffolding the full implementation tree and bootstrap scripts, seeding benchmark and gold-data directories, and producing a final verification report that confirms nothing from the architecture, governance, refinery, retrieval, assembly, portal, operations, evaluation, integrity, or launch layers was lost, merged incorrectly, or silently altered.


7. Best next move


Run the bootstrap script first, then paste the drafted documents into the generated files in repository order: governance, architecture, schemas, refinery, retrieval/assembly, interface/portal, operations, evaluation, integrity, launch.