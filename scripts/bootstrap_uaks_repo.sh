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
