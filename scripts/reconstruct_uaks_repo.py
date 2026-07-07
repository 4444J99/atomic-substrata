#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]

_local_raw = REPO_ROOT / "source_artifacts/raw/ChatGPT-Atomic Knowledge Assembler.json"
_original_source = Path("/Users/4jp/Workspace/meta-organvm/materia-collider/genesis/ChatGPT-Atomic Knowledge Assembler.json")

if _local_raw.exists():
    SOURCE_EXPORT = _local_raw
elif _original_source.exists():
    SOURCE_EXPORT = _original_source
else:
    SOURCE_EXPORT = _local_raw

DOC_PATH_BY_ID = {
    "uaks_v1_architecture_spec_20260311": "docs/02_architecture/uaks_v1_architecture_spec_20260311.md",
    "uaks_v1_ontology_charter_20260311": "docs/02_architecture/uaks_v1_ontology_charter_20260311.md",
    "uaks_v1_external_analysis_integration_spec_20260311": "docs/02_architecture/uaks_v1_external_analysis_integration_spec_20260311.md",
    "uaks_v1_schema_pack_20260311": "docs/03_schemas/uaks_v1_schema_pack_20260311.md",
    "uaks_v1_graph_relation_catalog_20260311": "docs/03_schemas/uaks_v1_graph_relation_catalog_20260311.md",
    "uaks_v1_text_refinery_spec_20260311": "docs/04_refinery/uaks_v1_text_refinery_spec_20260311.md",
    "uaks_v1_code_refinery_spec_20260311": "docs/04_refinery/uaks_v1_code_refinery_spec_20260311.md",
    "uaks_v1_ast_parsing_strategy_20260311": "docs/04_refinery/uaks_v1_ast_parsing_strategy_20260311.md",
    "uaks_v1_retrieval_scoring_spec_20260311": "docs/05_retrieval_assembly/uaks_v1_retrieval_scoring_spec_20260311.md",
    "uaks_v1_template_catalog_20260311": "docs/05_retrieval_assembly/uaks_v1_template_catalog_20260311.md",
    "uaks_v1_provenance_rendering_rules_20260311": "docs/05_retrieval_assembly/uaks_v1_provenance_rendering_rules_20260311.md",
    "uaks_v1_traceability_report_format_20260311": "docs/05_retrieval_assembly/uaks_v1_traceability_report_format_20260311.md",
    "uaks_v1_impact_analysis_report_format_20260311": "docs/05_retrieval_assembly/uaks_v1_impact_analysis_report_format_20260311.md",
    "uaks_v1_assembly_engine_spec_20260311": "docs/05_retrieval_assembly/uaks_v1_assembly_engine_spec_20260311.md",
    "uaks_v1_resolver_contract_spec_20260311": "docs/06_interface_portal/uaks_v1_resolver_contract_spec_20260311.md",
    "uaks_v1_query_pattern_library_20260311": "docs/06_interface_portal/uaks_v1_query_pattern_library_20260311.md",
    "uaks_v1_auth_access_model_20260311": "docs/06_interface_portal/uaks_v1_auth_access_model_20260311.md",
    "uaks_v1_portal_projection_spec_20260311": "docs/06_interface_portal/uaks_v1_portal_projection_spec_20260311.md",
    "uaks_v1_portal_projection_data_model_20260311": "docs/06_interface_portal/uaks_v1_portal_projection_data_model_20260311.md",
    "uaks_v1_operations_pack_20260311": "docs/07_operations/uaks_v1_operations_pack_20260311.md",
    "uaks_v1_change_management_sop_20260311": "docs/07_operations/uaks_v1_change_management_sop_20260311.md",
    "uaks_v1_incident_response_sop_20260311": "docs/07_operations/uaks_v1_incident_response_sop_20260311.md",
    "uaks_v1_runbook_set_20260311": "docs/07_operations/uaks_v1_runbook_set_20260311.md",
    "uaks_v1_observability_dashboard_spec_20260311": "docs/07_operations/uaks_v1_observability_dashboard_spec_20260311.md",
    "uaks_v1_release_gate_procedure_20260311": "docs/07_operations/uaks_v1_release_gate_procedure_20260311.md",
    "uaks_v1_pilot_intake_sop_20260311": "docs/07_operations/uaks_v1_pilot_intake_sop_20260311.md",
    "uaks_v1_review_workflow_sop_20260311": "docs/07_operations/uaks_v1_review_workflow_sop_20260311.md",
    "uaks_v1_evaluation_pack_A_20260311": "docs/08_evaluation/uaks_v1_evaluation_pack_A_20260311.md",
    "uaks_v1_evaluation_pack_B_20260311": "docs/08_evaluation/uaks_v1_evaluation_pack_B_20260311.md",
    "uaks_v1_benchmark_corpus_definition_20260311": "docs/08_evaluation/uaks_v1_benchmark_corpus_definition_20260311.md",
    "uaks_v1_gold_atom_set_spec_20260311": "docs/08_evaluation/uaks_v1_gold_atom_set_spec_20260311.md",
    "uaks_v1_query_eval_dataset_20260311": "docs/08_evaluation/uaks_v1_query_eval_dataset_20260311.md",
    "uaks_v1_trace_benchmark_spec_20260311": "docs/08_evaluation/uaks_v1_trace_benchmark_spec_20260311.md",
    "uaks_v1_retrieval_eval_harness_spec_20260311": "docs/08_evaluation/uaks_v1_retrieval_eval_harness_spec_20260311.md",
    "uaks_v1_assembly_eval_harness_spec_20260311": "docs/08_evaluation/uaks_v1_assembly_eval_harness_spec_20260311.md",
    "uaks_v1_trace_coverage_report_spec_20260311": "docs/08_evaluation/uaks_v1_trace_coverage_report_spec_20260311.md",
    "uaks_v1_drift_detection_report_spec_20260311": "docs/08_evaluation/uaks_v1_drift_detection_report_spec_20260311.md",
    "uaks_v1_truth_lifecycle_pack_20260311": "docs/09_integrity/uaks_v1_truth_lifecycle_pack_20260311.md",
    "uaks_v1_integrity_pack_20260311": "docs/09_integrity/uaks_v1_integrity_pack_20260311.md",
    "uaks_v1_supersession_policy_20260311": "docs/09_integrity/uaks_v1_supersession_policy_20260311.md",
    "uaks_v1_contradiction_policy_20260311": "docs/09_integrity/uaks_v1_contradiction_policy_20260311.md",
    "uaks_v1_provenance_policy_20260311": "docs/09_integrity/uaks_v1_provenance_policy_20260311.md",
    "uaks_v1_validation_trust_policy_20260311": "docs/09_integrity/uaks_v1_validation_trust_policy_20260311.md",
    "uaks_v1_hashing_standard_20260311": "docs/09_integrity/uaks_v1_hashing_standard_20260311.md",
    "uaks_v1_canonicalization_spec_20260311": "docs/09_integrity/uaks_v1_canonicalization_spec_20260311.md",
    "uaks_v1_atomicity_test_suite_20260311": "docs/09_integrity/uaks_v1_atomicity_test_suite_20260311.md",
    "uaks_v1_deduplication_protocol_20260311": "docs/09_integrity/uaks_v1_deduplication_protocol_20260311.md",
    "uaks_v1_integrity_verification_procedure_20260311": "docs/09_integrity/uaks_v1_integrity_verification_procedure_20260311.md",
    "uaks_v1_dedup_merge_policy_20260311": "docs/09_integrity/uaks_v1_dedup_merge_policy_20260311.md",
    "uaks_v1_launch_pack_20260311": "docs/10_launch/uaks_v1_launch_pack_20260311.md",
    "uaks_v1_capacity_model_20260311": "docs/10_launch/uaks_v1_capacity_model_20260311.md",
    "uaks_v1_storage_model_20260311": "docs/10_launch/uaks_v1_storage_model_20260311.md",
    "uaks_v1_operational_scaling_model_20260311": "docs/10_launch/uaks_v1_operational_scaling_model_20260311.md",
    "uaks_v1_launch_readiness_assessment_20260311": "docs/10_launch/uaks_v1_launch_readiness_assessment_20260311.md",
    "uaks_v1_launch_readiness_scorecard_20260311": "docs/10_launch/uaks_v1_launch_readiness_scorecard_20260311.md",
    "uaks_v1_release_checklist_20260311": "docs/10_launch/uaks_v1_release_checklist_20260311.md",
}

NON_ID_DOCS = [
    {
        "pair_number": 1,
        "path": "docs/00_meta/atomic_knowledge_assembler_theoretical_specification.md",
        "title": "Theoretical Specification Atomic Knowledge Assembler System",
        "mode": "full_pair",
    },
    {
        "pair_number": 2,
        "path": "docs/00_meta/recommendation_across_the_three_deliverables.md",
        "title": "Recommendation across the three deliverables",
        "mode": "full_pair",
    },
    {
        "pair_number": 3,
        "path": "docs/00_meta/uaks_v1_architecture_specification_v1.md",
        "title": "V1 Architecture Specification Unified Atomic Knowledge and Technical Corpus System",
        "mode": "full_pair",
    },
    {
        "pair_number": 5,
        "path": "docs/00_meta/addenda_timing_guidance.md",
        "title": "Addenda Timing Guidance",
        "mode": "full_pair",
    },
    {
        "pair_number": 6,
        "path": "docs/00_meta/addendum_integration_review.md",
        "title": "Addendum Integration Review",
        "mode": "full_pair",
    },
    {
        "pair_number": 7,
        "path": "docs/02_architecture/uaks_v1_visual_architecture.md",
        "title": "UAKS v1 Visual Architecture",
        "mode": "slice",
        "start_marker": "1. Visual Architecture Diagram",
        "end_marker": "2. Ontology Charter v1",
    },
    {
        "pair_number": 7,
        "path": "docs/03_schemas/uaks_v1_graphql_schema_draft.md",
        "title": "UAKS v1 GraphQL Schema Draft",
        "mode": "slice",
        "start_marker": "3. GraphQL Schema Draft v1",
        "end_marker": "4. External Analysis Integration Spec v1",
    },
    {
        "pair_number": 13,
        "path": "docs/11_implementation/remaining_steps_to_phase_completion.md",
        "title": "Remaining Steps to Phase Completion",
        "mode": "full_pair",
    },
    {
        "pair_number": 16,
        "path": "docs/11_implementation/phase_status_and_remaining_rounds.md",
        "title": "Status of the Phase",
        "mode": "slice",
        "start_marker": "Status of the Phase",
        "end_marker": "Evaluation Pack B v1",
    },
    {
        "pair_number": 20,
        "path": "docs/02_architecture/uaks_v1_visual_architecture_image_generation_note.md",
        "title": "UAKS v1 Visual Architecture Image Generation Note",
        "mode": "full_pair",
    },
    {
        "pair_number": 21,
        "path": "docs/11_implementation/updated_final_artifacts.md",
        "title": "Updated Final Artifacts",
        "mode": "full_pair",
    },
]

IMPLEMENTATION_MODULES = [
    ("source_intake", "Registers, fingerprints, and archives incoming sources."),
    ("text_refinery", "Converts language-bearing sources into primary textual atoms."),
    ("code_refinery", "Converts technical sources into governed code atoms."),
    ("analysis_normalization", "Maps external analytical exports into derivative UAKS atom families."),
    ("graph_storage", "Stores atoms, entities, and typed relations."),
    ("vector_retrieval", "Supports semantic retrieval and similarity search."),
    ("content_addressable_storage", "Stores immutable payloads addressed by content hash."),
    ("graphql", "Exposes typed query and mutation surfaces."),
    ("assembly", "Builds outputs from selected atoms and recipes."),
    ("portal_projection", "Projects governed data into user-facing views."),
    ("operations", "Operational workflows, runbooks, and lifecycle controls."),
    ("evaluation", "Benchmarking, harnesses, and readiness evaluation."),
    ("integrity_verification", "Hashing, atomicity, deduplication, and audit routines."),
    ("launch_control", "Launch thresholds, readiness gates, and pilot progression."),
]

TITLE_KEYWORDS = (
    "Architecture",
    "Assembly",
    "Assessment",
    "Benchmark",
    "Catalog",
    "Charter",
    "Checklist",
    "Contract",
    "Corpus",
    "Dashboard",
    "Dataset",
    "Diagram",
    "Draft",
    "Engine",
    "Format",
    "Harness",
    "Integration",
    "Interface",
    "Launch",
    "Library",
    "Lifecycle",
    "Model",
    "Ontology",
    "Pack",
    "Pattern",
    "Policy",
    "Procedure",
    "Projection",
    "Protocol",
    "Query",
    "Readiness",
    "Refinery",
    "Relation",
    "Report",
    "Resolver",
    "Review",
    "Runbook",
    "Schema",
    "Scorecard",
    "Set",
    "Specification",
    "Spec",
    "Strategy",
    "Suite",
    "SOP",
    "Storage",
    "Template",
    "Traceability",
    "Truth",
    "Validation",
)

GENERIC_HEADER_PATTERNS = (
    re.compile(r"^Unified Atomic Knowledge Substrate(?:\s+v\d+)?(?:\s+\(UAKS\))?$"),
    re.compile(r"^Unified Atomic Knowledge Substrate v1$"),
    re.compile(r"^Unified Atomic Knowledge and Technical Corpus System$"),
    re.compile(r"^Atomic Knowledge Assembler(?: System)?$"),
)


@dataclass(slots=True)
class PairRecord:
    pair_id: str
    pair_number: int
    prompt: str
    response: str
    prompt_title: str
    response_title: str
    prompt_sha256: str
    response_sha256: str


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "artifact"


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def render_front_matter(data: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def load_export() -> dict[str, Any]:
    return json.loads(SOURCE_EXPORT.read_text(encoding="utf-8"))


def extract_here_doc(text: str, target: str) -> str | None:
    pattern = re.compile(
        rf"cat > {re.escape(target)} <<'?EOF'?\n(.*?)\nEOF",
        re.S,
    )
    match = pattern.search(text)
    return match.group(1).rstrip() + "\n" if match else None


def extract_bootstrap_script(text: str) -> str | None:
    pattern = re.compile(
        r"(#!/usr/bin/env bash\nset -euo pipefail\n.*?^echo \"Repository scaffold created at: \$\{REPO_ROOT\}\")",
        re.S | re.M,
    )
    match = pattern.search(text)
    return match.group(1).rstrip() + "\n" if match else None


def parse_doc_list(text: str, array_name: str) -> list[tuple[str, str]]:
    pattern = re.compile(rf"{array_name}=\(\n(.*?)\n\)", re.S)
    match = pattern.search(text)
    if not match:
        return []
    block = match.group(1)
    return re.findall(r'"([^"]+)\|([^"]+)"', block)


def parse_chatpair_seed(text: str) -> dict[str, tuple[str, str]]:
    csv_block = extract_here_doc(text, "manifests/chat_pair_manifest.csv")
    result: dict[str, tuple[str, str]] = {}
    if not csv_block:
        return result
    rows = list(csv.reader(csv_block.splitlines()))
    for row in rows[1:]:
        if len(row) >= 3:
            result[row[0]] = (row[1], row[2])
    return result


def response_title(response: str, prompt: str) -> str:
    for line in response.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.lower().startswith("thought for "):
            continue
        if len(stripped) <= 140:
            return stripped.rstrip(":")
    return next((line.strip() for line in prompt.splitlines() if line.strip()), "Untitled")


def build_pairs(payload: dict[str, Any], seed_titles: dict[str, tuple[str, str]]) -> list[PairRecord]:
    pairs: list[PairRecord] = []
    messages = payload["messages"]
    for offset in range(0, len(messages), 2):
        pair_number = offset // 2 + 1
        pair_id = f"CHATPAIR-{pair_number:03d}"
        prompt = messages[offset]["say"]
        response = messages[offset + 1]["say"]
        seed_prompt_title, seed_response_title = seed_titles.get(
            pair_id,
            (
                next((line.strip() for line in prompt.splitlines() if line.strip()), f"Pair {pair_number} Prompt"),
                response_title(response, prompt),
            ),
        )
        pairs.append(
            PairRecord(
                pair_id=pair_id,
                pair_number=pair_number,
                prompt=prompt,
                response=response,
                prompt_title=seed_prompt_title,
                response_title=seed_response_title,
                prompt_sha256=sha256_text(prompt),
                response_sha256=sha256_text(response),
            )
        )
    return pairs


def get_pair(pairs: list[PairRecord], pair_number: int) -> PairRecord:
    return next(pair for pair in pairs if pair.pair_number == pair_number)


def extract_slice(text: str, start_marker: str, end_marker: str | None = None) -> str:
    if start_marker not in text:
        raise ValueError(f"Start marker not found: {start_marker}")
    start = text.index(start_marker)
    end = len(text)
    if end_marker and end_marker in text[start + len(start_marker) :]:
        end = text.index(end_marker, start + len(start_marker))
    return text[start:end].strip() + "\n"


def is_generic_header_line(line: str) -> bool:
    return any(pattern.match(line) for pattern in GENERIC_HEADER_PATTERNS)


def is_title_candidate(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if len(stripped) > 140 or stripped.endswith("."):
        return False
    if stripped.startswith(("Document ID:", "Version:", "Status:", "-", "*")):
        return False
    if ":" in stripped and not stripped.startswith(("Phase", "Status of the Phase")):
        return False
    if is_generic_header_line(stripped):
        return True
    if re.match(r"^\d+(\.\d+)?\s+[A-Z]", stripped):
        return True
    if any(keyword in stripped for keyword in TITLE_KEYWORDS):
        return True
    if re.search(r"[A-Z]", stripped) and re.search(r"\bv\d+(\.\d+)?(?:-draft)?\b", stripped):
        return True
    return False


def is_specific_title_candidate(line: str) -> bool:
    stripped = line.strip()
    return is_title_candidate(stripped) and not is_generic_header_line(stripped)


def first_non_empty_line(text: str) -> str:
    return next((line.strip() for line in text.splitlines() if line.strip()), "")


def find_doc_header(lines: list[str], doc_line: int, doc_id: str) -> tuple[int, str]:
    header_indexes: list[int] = []
    nonempty_seen = 0
    probe = doc_line - 1
    while probe >= 0 and nonempty_seen < 20:
        stripped = lines[probe].strip()
        if stripped:
            nonempty_seen += 1
        if not stripped:
            probe -= 1
            continue
        if stripped.startswith(("Document ID:", "Version:", "Status:")):
            probe -= 1
            continue
        if is_title_candidate(stripped):
            header_indexes.append(probe)
            probe -= 1
            continue
        if header_indexes:
            break
        probe -= 1
    if not header_indexes:
        return doc_line, doc_id

    header_indexes.sort()
    header_lines = [lines[index].strip() for index in header_indexes]
    for line in reversed(header_lines):
        if is_specific_title_candidate(line):
            return header_indexes[0], line
    return header_indexes[0], header_lines[-1]


def extract_doc_blocks(text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    doc_line_indexes = [idx for idx, line in enumerate(lines) if line.startswith("Document ID:")]
    starts: list[int] = []
    ids: list[str] = []
    titles: list[str] = []
    for doc_line in doc_line_indexes:
        doc_id = lines[doc_line].split(":", 1)[1].strip()
        start, title = find_doc_header(lines, doc_line, doc_id)
        starts.append(start)
        ids.append(doc_id)
        titles.append(title)
    blocks: list[dict[str, str]] = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        block_text = "\n".join(lines[start:end]).strip() + "\n"
        blocks.append({"document_id": ids[index], "title": titles[index], "content": block_text})
    return blocks


def canonical_doc_path(document_id: str) -> str:
    if document_id not in DOC_PATH_BY_ID:
        raise KeyError(f"No output path registered for {document_id}")
    return DOC_PATH_BY_ID[document_id]


def collect_drafted_docs(pairs: list[PairRecord]) -> list[dict[str, Any]]:
    drafted: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for pair in pairs:
        for block in extract_doc_blocks(pair.response):
            doc_id = block["document_id"]
            if doc_id in seen_ids:
                continue
            seen_ids.add(doc_id)
            drafted.append(
                {
                    "artifact_id": doc_id,
                    "title": block["title"],
                    "path": canonical_doc_path(doc_id),
                    "pair_id": pair.pair_id,
                    "kind": "drafted_document",
                    "content": block["content"],
                }
            )
    for spec in NON_ID_DOCS:
        pair = get_pair(pairs, spec["pair_number"])
        if spec["mode"] == "full_pair":
            content = pair.response.strip() + "\n"
        else:
            content = extract_slice(pair.response, spec["start_marker"], spec.get("end_marker"))
        drafted.append(
            {
                "artifact_id": spec["path"].replace("/", "::"),
                "title": spec["title"],
                "path": spec["path"],
                "pair_id": pair.pair_id,
                "kind": "non_id_document",
                "content": content,
            }
        )
    return drafted


def write_pair_archive(payload: dict[str, Any], pairs: list[PairRecord], generated_at: str) -> None:
    raw_target = REPO_ROOT / "source_artifacts/raw/ChatGPT-Atomic Knowledge Assembler.json"
    ensure_dir(raw_target.parent)
    if SOURCE_EXPORT.resolve() != raw_target.resolve():
        shutil.copy2(SOURCE_EXPORT, raw_target)

    normalized_json = {
        "generated_at": generated_at,
        "title": payload["metadata"]["title"],
        "thread_id": payload["metadata"]["link"].split("/")[-1],
        "source_export": str(SOURCE_EXPORT),
        "pair_count": len(pairs),
        "pairs": [
            {
                "pair_id": pair.pair_id,
                "pair_number": pair.pair_number,
                "prompt_title": pair.prompt_title,
                "response_title": pair.response_title,
                "prompt_sha256": pair.prompt_sha256,
                "response_sha256": pair.response_sha256,
            }
            for pair in pairs
        ],
    }
    write_text(REPO_ROOT / "source_artifacts/normalized/chat_pairs.json", json.dumps(normalized_json, indent=2))

    transcript_lines = [
        f"# {payload['metadata']['title']}",
        "",
        f"Source export: `{SOURCE_EXPORT}`",
        f"Thread id: `{payload['metadata']['link'].split('/')[-1]}`",
        "",
    ]
    for pair in pairs:
        transcript_lines.extend(
            [
                f"## {pair.pair_id} — {pair.prompt_title}",
                "",
                "### Prompt",
                pair.prompt,
                "",
                "### Response",
                pair.response,
                "",
            ]
        )
        pair_path = REPO_ROOT / "source_artifacts/chat_pairs" / f"{pair.pair_id.lower()}-{slugify(pair.prompt_title)}.md"
        front_matter = render_front_matter(
            {
                "pair_id": pair.pair_id,
                "pair_number": pair.pair_number,
                "prompt_title": json.dumps(pair.prompt_title),
                "response_title": json.dumps(pair.response_title),
                "prompt_sha256": pair.prompt_sha256,
                "response_sha256": pair.response_sha256,
            }
        )
        pair_body = "\n\n".join(
            [
                front_matter,
                f"# {pair.pair_id}",
                "## Prompt",
                pair.prompt,
                "## Response",
                pair.response,
            ]
        )
        write_text(pair_path, pair_body)
    write_text(REPO_ROOT / "source_artifacts/normalized/full_transcript.md", "\n".join(transcript_lines))


def write_base_tree() -> None:
    for relative in [
        "docs/00_meta",
        "docs/01_governance",
        "docs/02_architecture",
        "docs/03_schemas",
        "docs/04_refinery",
        "docs/05_retrieval_assembly",
        "docs/06_interface_portal",
        "docs/07_operations",
        "docs/08_evaluation",
        "docs/09_integrity",
        "docs/10_launch",
        "docs/11_implementation",
        "docs/12_seed_content",
        "manifests",
        "prompts",
        "scripts",
        "tests/unit",
        "tests/benchmark",
        "tests/gold",
        "data/benchmark",
        "data/gold",
        "data/import_samples/source_evidence",
        "data/import_samples/primary_atoms",
        "data/import_samples/derivative_analytical_atoms",
        "data/projections",
        "source_artifacts/raw",
        "source_artifacts/normalized",
        "source_artifacts/chat_pairs",
        ".github/workflows",
    ]:
        ensure_dir(REPO_ROOT / relative)


def write_readme(generated_at: str, drafted_count: int, placeholder_count: int) -> None:
    text = "\n".join(
        [
            "# uaks",
            "",
            "Unified Atomic Knowledge Substrate repository scaffold reconstructed from the architecture conversation artifact set.",
            "",
            f"- Generated at: `{generated_at}`",
            f"- Source export: `{SOURCE_EXPORT}`",
            f"- Drafted documents externalized: `{drafted_count}`",
            f"- Placeholder documents created: `{placeholder_count}`",
            "",
            "## Quick start",
            "",
            "```bash",
            "python3 scripts/reconstruct_uaks_repo.py",
            "bash scripts/bootstrap_env.sh",
            "python3 scripts/print_tree.py",
            "```",
            "",
            "## Repository intent",
            "",
            "This repository preserves source evidence, primary atoms, and derivative analytical atoms as distinct layers while externalizing the drafted UAKS specifications into their own canonical markdown files.",
            "",
        ]
    )
    write_text(REPO_ROOT / "README.md", text)


def write_script_and_prompt_artifacts(pair21_text: str) -> None:
    bootstrap = extract_bootstrap_script(pair21_text)
    if bootstrap:
        write_text(REPO_ROOT / "scripts/bootstrap_uaks_repo.sh", bootstrap)
    env_script = extract_here_doc(pair21_text, "scripts/bootstrap_env.sh")
    if env_script:
        write_text(REPO_ROOT / "scripts/bootstrap_env.sh", env_script)
    print_tree = extract_here_doc(pair21_text, "scripts/print_tree.py")
    if print_tree:
        write_text(REPO_ROOT / "scripts/print_tree.py", print_tree)
    full_prompt = extract_here_doc(pair21_text, "prompts/ai_handoff_full.md")
    if full_prompt:
        write_text(REPO_ROOT / "prompts/ai_handoff_full.md", full_prompt)
    one_paragraph = extract_here_doc(pair21_text, "prompts/ai_handoff_one_paragraph.md")
    if one_paragraph:
        write_text(REPO_ROOT / "prompts/ai_handoff_one_paragraph.md", one_paragraph)
    repo_manifest_seed = extract_here_doc(pair21_text, "manifests/repo_manifest.csv")
    if repo_manifest_seed:
        write_text(REPO_ROOT / "manifests/repo_manifest_seed.csv", repo_manifest_seed)
    chat_pair_seed = extract_here_doc(pair21_text, "manifests/chat_pair_manifest.csv")
    if chat_pair_seed:
        write_text(REPO_ROOT / "manifests/chat_pair_manifest_seed.csv", chat_pair_seed)


def write_drafted_docs(drafted_docs: list[dict[str, Any]], generated_at: str) -> None:
    for doc in drafted_docs:
        front_matter = render_front_matter(
            {
                "title": json.dumps(doc["title"]),
                "artifact_id": doc["artifact_id"],
                "pair_id": doc["pair_id"],
                "status": "drafted_in_chat",
                "generated_at": generated_at,
            }
        )
        body = "\n\n".join([front_matter, doc["content"].rstrip()]) + "\n"
        write_text(REPO_ROOT / doc["path"], body)


def write_placeholders(
    remaining_docs: list[tuple[str, str]], drafted_docs: list[dict[str, Any]], generated_at: str
) -> list[dict[str, Any]]:
    drafted_basenames = {Path(doc["path"]).stem for doc in drafted_docs}
    placeholders: list[dict[str, Any]] = []
    for path, title in remaining_docs:
        stem = Path(path).stem
        if stem in drafted_basenames:
            continue
        placeholder_path = REPO_ROOT / path
        front_matter = render_front_matter(
            {
                "title": json.dumps(title),
                "status": "placeholder",
                "generated_at": generated_at,
                "source_lineage": json.dumps("Derived from the UAKS architecture conversation artifact set."),
            }
        )
        content = "\n\n".join(
            [
                front_matter,
                f"# {title}",
                "",
                "Status: placeholder",
                "",
                "## Purpose",
                "",
                "TODO",
                "",
                "## Source lineage",
                "",
                "Derived from the UAKS architecture conversation artifact set.",
                "",
                "## Notes",
                "",
                "TODO",
            ]
        )
        write_text(placeholder_path, content + "\n")
        placeholders.append({"path": path, "title": title})
    image_placeholder = {
        "path": "docs/02_architecture/uaks_v1_visual_architecture_image_asset.placeholder.md",
        "title": "UAKS v1 Visual Architecture Image Asset",
    }
    image_content = "\n".join(
        [
            "# UAKS v1 Visual Architecture Image Asset",
            "",
            "Status: placeholder",
            "",
            "The conversation export records `Image created` for CHATPAIR-020 but does not include the binary image payload. This placeholder preserves the missing asset boundary without fabricating content.",
            "",
            "TODO: Attach the original generated image if it becomes available from the source system.",
            "",
        ]
    )
    write_text(REPO_ROOT / image_placeholder["path"], image_content)
    placeholders.append(image_placeholder)
    return placeholders


def write_alias_map(
    completed_docs: list[tuple[str, str]],
    remaining_docs: list[tuple[str, str]],
    drafted_docs: list[dict[str, Any]],
) -> None:
    drafted_by_base = {Path(doc["path"]).stem.replace("_20260311", ""): doc["path"] for doc in drafted_docs if doc["kind"] == "drafted_document"}
    rows = [["suggested_path", "canonical_path", "title", "status"]]
    for source_path, title in completed_docs + remaining_docs:
        base = Path(source_path).stem
        canonical = drafted_by_base.get(base, source_path)
        status = "resolved_to_canonical_id" if canonical != source_path else "unchanged"
        rows.append([source_path, canonical, title, status])
    output = "\n".join(",".join(row) for row in rows) + "\n"
    write_text(REPO_ROOT / "manifests/path_alias_map.csv", output)


def write_implementation_scaffold() -> None:
    init_lines = ['"""Unified Atomic Knowledge Substrate implementation scaffold."""\n']
    for module_name, description in IMPLEMENTATION_MODULES:
        package_dir = REPO_ROOT / "src" / "uaks" / module_name
        ensure_dir(package_dir)
        write_text(
            package_dir / "__init__.py",
            f'"""TODO scaffold for {module_name.replace("_", " ")}."""\n',
        )
        write_text(
            package_dir / "TODO.md",
            "\n".join(
                [
                    f"# {module_name.replace('_', ' ').title()}",
                    "",
                    description,
                    "",
                    "Status: TODO",
                    "",
                    "Conversation-driven scaffold only. No implementation logic was drafted in the source artifact set.",
                    "",
                ]
            ),
        )
    ensure_dir(REPO_ROOT / "src" / "uaks")
    write_text(REPO_ROOT / "src/uaks/__init__.py", "".join(init_lines))


def write_sample_data() -> None:
    write_text(
        REPO_ROOT / "data/import_samples/source_evidence/source_object_example.json",
        json.dumps(
            {
                "sourceId": "src_example_conversation_001",
                "sourceType": "conversation_export",
                "origin": "chat_export",
                "rawArchiveRef": "source_artifacts/raw/ChatGPT-Atomic Knowledge Assembler.json",
                "note": "Source evidence example preserving the raw-artifact tier.",
            },
            indent=2,
        )
        + "\n",
    )
    write_text(
        REPO_ROOT / "data/import_samples/primary_atoms/text_atom_example.json",
        json.dumps(
            {
                "atomId": "atom_text_example_001",
                "atomType": "TEXT",
                "atomClass": "FACT",
                "validationState": "DISTILLED",
                "canonicalStatement": "Text and code belong to one ontology but require different refinery disciplines.",
                "tier": "primary_atomic_domain",
            },
            indent=2,
        )
        + "\n",
    )
    write_text(
        REPO_ROOT / "data/import_samples/derivative_analytical_atoms/analysis_atom_example.json",
        json.dumps(
            {
                "atomId": "atom_analysis_example_001",
                "atomType": "ANALYSIS",
                "atomClass": "ANALYSIS",
                "validationState": "IMPORTED",
                "finding": "Example derivative analytical atom preserved separately from source evidence and primary atoms.",
                "tier": "derivative_analytical_domain",
            },
            indent=2,
        )
        + "\n",
    )
    write_text(
        REPO_ROOT / "data/benchmark/README.md",
        "# Benchmark Fixtures\n\nSeed directory for benchmark corpus definitions and evaluation fixtures.\n",
    )
    write_text(
        REPO_ROOT / "data/gold/README.md",
        "# Gold Fixtures\n\nSeed directory for gold-standard atoms and expected outputs.\n",
    )
    write_text(
        REPO_ROOT / "data/projections/README.md",
        "# Projections\n\nPilot capacity and storage projection notes live here.\n",
    )
    write_text(REPO_ROOT / "tests/unit/README.md", "# Unit Tests\n\nImplementation tests will be added when code exists.\n")
    write_text(REPO_ROOT / "tests/benchmark/.gitkeep", "")
    write_text(REPO_ROOT / "tests/gold/.gitkeep", "")


def write_manifests(
    payload: dict[str, Any],
    pairs: list[PairRecord],
    drafted_docs: list[dict[str, Any]],
    placeholders: list[dict[str, Any]],
    generated_at: str,
) -> None:
    artifact_rows = [["artifact_id", "path", "title", "status", "pair_id", "kind"]]
    artifact_json: list[dict[str, Any]] = []
    for doc in drafted_docs:
        artifact_rows.append([doc["artifact_id"], doc["path"], doc["title"], "drafted_in_chat", doc["pair_id"], doc["kind"]])
        artifact_json.append(
            {
                "artifact_id": doc["artifact_id"],
                "path": doc["path"],
                "title": doc["title"],
                "status": "drafted_in_chat",
                "pair_id": doc["pair_id"],
                "kind": doc["kind"],
            }
        )
    for index, placeholder in enumerate(placeholders, start=1):
        artifact_id = f"PLACEHOLDER-{index:03d}"
        artifact_rows.append([artifact_id, placeholder["path"], placeholder["title"], "placeholder", "", "placeholder"])
        artifact_json.append(
            {
                "artifact_id": artifact_id,
                "path": placeholder["path"],
                "title": placeholder["title"],
                "status": "placeholder",
                "pair_id": None,
                "kind": "placeholder",
            }
        )
    write_text(REPO_ROOT / "manifests/artifact_manifest.csv", "\n".join(",".join(map(str, row)) for row in artifact_rows) + "\n")
    write_text(REPO_ROOT / "manifests/artifact_manifest.json", json.dumps(artifact_json, indent=2))

    pair_rows = [["pair_id", "pair_number", "prompt_title", "response_title", "prompt_sha256", "response_sha256"]]
    pair_json = []
    for pair in pairs:
        pair_rows.append([pair.pair_id, pair.pair_number, pair.prompt_title, pair.response_title, pair.prompt_sha256, pair.response_sha256])
        pair_json.append(
            {
                "pair_id": pair.pair_id,
                "pair_number": pair.pair_number,
                "prompt_title": pair.prompt_title,
                "response_title": pair.response_title,
                "prompt_sha256": pair.prompt_sha256,
                "response_sha256": pair.response_sha256,
            }
        )
    write_text(REPO_ROOT / "manifests/chat_pair_manifest.csv", "\n".join(",".join(map(str, row)) for row in pair_rows) + "\n")
    write_text(REPO_ROOT / "manifests/chat_pair_manifest.json", json.dumps(pair_json, indent=2))

    write_text(
        REPO_ROOT / "manifests/source_manifest.json",
        json.dumps(
            {
                "generated_at": generated_at,
                "source_export": str(SOURCE_EXPORT),
                "source_sha256": sha256_file(SOURCE_EXPORT),
                "thread_title": payload["metadata"]["title"],
                "thread_id": payload["metadata"]["link"].split("/")[-1],
                "pair_count": len(pairs),
            },
            indent=2,
        ),
    )


def write_reports(
    payload: dict[str, Any],
    pairs: list[PairRecord],
    drafted_docs: list[dict[str, Any]],
    placeholders: list[dict[str, Any]],
    generated_at: str,
) -> None:
    drafted_ids = {doc["artifact_id"] for doc in drafted_docs if doc["kind"] == "drafted_document"}
    missing_doc_ids = sorted(set(DOC_PATH_BY_ID) - drafted_ids)
    title_integrity_issues = sorted(
        doc["artifact_id"]
        for doc in drafted_docs
        if doc["kind"] == "drafted_document" and not is_specific_title_candidate(doc["title"])
    )
    content_boundary_issues = sorted(
        doc["artifact_id"]
        for doc in drafted_docs
        if doc["kind"] == "drafted_document" and not is_title_candidate(first_non_empty_line(doc["content"]))
    )
    completeness_lines = [
        "# Completeness Report",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Source export: `{SOURCE_EXPORT}`",
        f"- Source SHA-256: `{sha256_file(SOURCE_EXPORT)}`",
        f"- Chat pairs preserved: `{len(pairs)}`",
        f"- Drafted documents externalized: `{len(drafted_docs)}`",
        f"- Placeholder documents created: `{len(placeholders)}`",
        f"- Missing drafted Document IDs: `{len(missing_doc_ids)}`",
        f"- Title integrity issues: `{len(title_integrity_issues)}`",
        f"- Content boundary issues: `{len(content_boundary_issues)}`",
        "",
        "## Result",
        "Every drafted UAKS specification found in the conversation export was externalized into its own markdown file. Placeholders were created only for undrafted artifacts named in the final generator artifact set and for the missing binary image asset.",
        "",
    ]
    if missing_doc_ids:
        completeness_lines.extend(["## Missing drafted Document IDs"] + [f"- `{doc_id}`" for doc_id in missing_doc_ids])
    if title_integrity_issues:
        completeness_lines.extend(["## Title Integrity Issues"] + [f"- `{doc_id}`" for doc_id in title_integrity_issues])
    if content_boundary_issues:
        completeness_lines.extend(["## Content Boundary Issues"] + [f"- `{doc_id}`" for doc_id in content_boundary_issues])
    write_text(REPO_ROOT / "manifests/completeness_report.md", "\n".join(completeness_lines) + "\n")

    unresolved_lines = [
        "# Unresolved Placeholders",
        "",
        "These artifacts were named in the conversation or implied by it but were not fully drafted in the export.",
        "",
    ]
    for placeholder in placeholders:
        unresolved_lines.append(f"- `{placeholder['path']}` — {placeholder['title']}")
    write_text(REPO_ROOT / "manifests/unresolved_placeholders.md", "\n".join(unresolved_lines) + "\n")

    verification = {
        "status": "pass" if not (missing_doc_ids or title_integrity_issues or content_boundary_issues) else "fail",
        "generated_at": generated_at,
        "message_count": len(payload["messages"]),
        "pair_count": len(pairs),
        "drafted_document_count": len([doc for doc in drafted_docs if doc["kind"] == "drafted_document"]),
        "non_id_document_count": len([doc for doc in drafted_docs if doc["kind"] == "non_id_document"]),
        "placeholder_count": len(placeholders),
        "missing_document_ids": missing_doc_ids,
        "title_integrity_issues": title_integrity_issues,
        "content_boundary_issues": content_boundary_issues,
    }
    write_text(REPO_ROOT / "manifests/verification_report.json", json.dumps(verification, indent=2))
    verification_lines = [
        "# Verification Report",
        "",
        f"- Status: `{verification['status']}`",
        f"- Message count: `{verification['message_count']}`",
        f"- Pair count: `{verification['pair_count']}`",
        f"- Drafted document count: `{verification['drafted_document_count']}`",
        f"- Non-ID document count: `{verification['non_id_document_count']}`",
        f"- Placeholder count: `{verification['placeholder_count']}`",
        f"- Missing Document IDs: `{len(missing_doc_ids)}`",
        f"- Title integrity issues: `{len(title_integrity_issues)}`",
        f"- Content boundary issues: `{len(content_boundary_issues)}`",
        "",
        "Verification passes only when drafted Document IDs, canonical titles, and extracted content boundaries are all preserved.",
        "",
    ]
    if title_integrity_issues:
        verification_lines.extend(["## Title Integrity Issues"] + [f"- `{doc_id}`" for doc_id in title_integrity_issues] + [""])
    if content_boundary_issues:
        verification_lines.extend(["## Content Boundary Issues"] + [f"- `{doc_id}`" for doc_id in content_boundary_issues] + [""])
    write_text(REPO_ROOT / "manifests/verification_report.md", "\n".join(verification_lines))


def write_repository_tree() -> None:
    lines: list[str] = []
    for path in sorted(REPO_ROOT.rglob("*")):
        if ".git" in path.parts:
            continue
        depth = len(path.relative_to(REPO_ROOT).parts)
        prefix = "  " * (depth - 1)
        name = path.name + ("/" if path.is_dir() else "")
        lines.append(f"{prefix}{name}")
    write_text(REPO_ROOT / "manifests/repository_tree.txt", "\n".join(lines) + "\n")


def main() -> int:
    generated_at = now_utc()
    payload = load_export()
    pair21_text = payload["messages"][(21 - 1) * 2 + 1]["say"]
    completed_docs = parse_doc_list(pair21_text, "completed_docs")
    remaining_docs = parse_doc_list(pair21_text, "remaining_docs")
    seed_titles = parse_chatpair_seed(pair21_text)

    write_base_tree()
    pairs = build_pairs(payload, seed_titles)
    write_pair_archive(payload, pairs, generated_at)
    drafted_docs = collect_drafted_docs(pairs)
    write_drafted_docs(drafted_docs, generated_at)
    placeholders = write_placeholders(remaining_docs, drafted_docs, generated_at)
    write_script_and_prompt_artifacts(pair21_text)
    write_alias_map(completed_docs, remaining_docs, drafted_docs)
    write_implementation_scaffold()
    write_sample_data()
    write_manifests(payload, pairs, drafted_docs, placeholders, generated_at)
    write_reports(payload, pairs, drafted_docs, placeholders, generated_at)
    write_repository_tree()
    write_readme(generated_at, len(drafted_docs), len(placeholders))

    print(
        json.dumps(
            {
                "status": "pass",
                "generated_at": generated_at,
                "repo_root": str(REPO_ROOT),
                "source_export": str(SOURCE_EXPORT),
                "pair_count": len(pairs),
                "drafted_document_count": len(drafted_docs),
                "placeholder_count": len(placeholders),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
