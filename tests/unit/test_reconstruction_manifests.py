from __future__ import annotations

import importlib.util
import json
import sys
from functools import lru_cache
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


@lru_cache(maxsize=1)
def load_reconstruction_module():
    script_path = REPO_ROOT / "scripts/reconstruct_uaks_repo.py"
    spec = importlib.util.spec_from_file_location("reconstruct_uaks_repo", script_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_verification_report_passes() -> None:
    report = json.loads(
        (REPO_ROOT / "manifests/verification_report.json").read_text(encoding="utf-8")
    )
    assert report["status"] == "pass"
    assert report["pair_count"] == 6
    assert report["missing_document_ids"] == []
    assert report["title_integrity_issues"] == []
    assert report["content_boundary_issues"] == []


def test_chat_pair_manifest_count() -> None:
    manifest = json.loads(
        (REPO_ROOT / "manifests/chat_pair_manifest.json").read_text(encoding="utf-8")
    )
    assert len(manifest) == 6


def test_problematic_artifact_titles_are_preserved() -> None:
    manifest = {
        item["artifact_id"]: item
        for item in json.loads(
            (REPO_ROOT / "manifests/artifact_manifest.json").read_text(encoding="utf-8")
        )
    }
    expected_titles = {
        "uaks_v1_ast_parsing_strategy_20260311": "AST Parsing Strategy v1",
        "uaks_v1_release_checklist_20260311": "Release Checklist v1",
        "uaks_v1_launch_readiness_scorecard_20260311": "Launch Readiness Scorecard v1",
        "uaks_v1_runbook_set_20260311": "3. Runbook Set v1",
        "uaks_v1_observability_dashboard_spec_20260311": "4. Observability Dashboard Spec v1",
        "uaks_v1_query_eval_dataset_20260311": "3. Evaluation Query Dataset v1",
        "uaks_v1_assembly_eval_harness_spec_20260311": "2 Assembly Evaluation Harness Specification",
    }
    for artifact_id, expected_title in expected_titles.items():
        assert manifest[artifact_id]["title"] == expected_title


def test_extract_doc_blocks_skips_adjacent_table_fragments() -> None:
    module = load_reconstruction_module()
    payload = module.load_export()
    expectations = {
        10: {
            "uaks_v1_ast_parsing_strategy_20260311": "AST Parsing Strategy v1",
            "uaks_v1_release_checklist_20260311": "Release Checklist v1",
            "uaks_v1_launch_readiness_scorecard_20260311": "Launch Readiness Scorecard v1",
        },
        14: {
            "uaks_v1_runbook_set_20260311": "3. Runbook Set v1",
            "uaks_v1_observability_dashboard_spec_20260311": "4. Observability Dashboard Spec v1",
        },
        15: {
            "uaks_v1_query_eval_dataset_20260311": "3. Evaluation Query Dataset v1",
        },
        16: {
            "uaks_v1_assembly_eval_harness_spec_20260311": "2 Assembly Evaluation Harness Specification",
        },
    }
    for pair_number, expected_titles in expectations.items():
        response_text = payload["messages"][(pair_number - 1) * 2 + 1]["say"]
        blocks = {
            block["document_id"]: block
            for block in module.extract_doc_blocks(response_text)
        }
        for artifact_id, expected_title in expected_titles.items():
            assert blocks[artifact_id]["title"] == expected_title
            assert (
                module.first_non_empty_line(blocks[artifact_id]["content"])
                == expected_title
            )
