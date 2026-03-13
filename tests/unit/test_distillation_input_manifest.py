from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def load_manifest() -> dict:
    return json.loads((REPO_ROOT / "manifests/distillation_input_manifest.json").read_text(encoding="utf-8"))


def test_distillation_manifest_has_expected_sections() -> None:
    manifest = load_manifest()
    assert manifest["counts"]["canonical_mainline_specs"] > 0
    assert manifest["counts"]["branch_supplemental_specs"] == 3
    assert manifest["counts"]["non_normative_context"] > 0
    assert manifest["counts"]["excluded_placeholders"] == 32


def test_distillation_manifest_includes_required_specs() -> None:
    manifest = load_manifest()
    canonical_paths = {item["path"] for item in manifest["canonical_mainline_specs"]}
    branch_paths = {item["path"] for item in manifest["branch_supplemental_specs"]}

    assert "docs/02_architecture/uaks_v1_architecture_spec_20260311.md" in canonical_paths
    assert "docs/03_schemas/uaks_v1_graphql_schema_draft.md" in canonical_paths
    assert "docs/09_integrity/uaks_v1_integrity_pack_20260311.md" in canonical_paths

    assert "docs/13_branch_excavations/uaks_v1_metadata_identity_charter_20260311.md" in branch_paths
    assert "docs/13_branch_excavations/addendum_memorandum_generation_2_migration.md" in branch_paths
    assert "docs/13_branch_excavations/parallel_linguistic_analysis_integration_design.md" in branch_paths


def test_distillation_manifest_excludes_placeholders_from_included_sets() -> None:
    manifest = load_manifest()
    included_paths = {
        item["path"]
        for section in ("canonical_mainline_specs", "branch_supplemental_specs", "non_normative_context")
        for item in manifest[section]
    }
    placeholder_paths = {item["path"] for item in manifest["excluded_placeholders"]}

    assert included_paths.isdisjoint(placeholder_paths)
    assert "docs/02_architecture/logical_data_model.md" in placeholder_paths
    assert "docs/01_governance/vision_and_thesis.md" in placeholder_paths


def test_distillation_manifest_marks_branch_advisory_docs_as_context() -> None:
    manifest = load_manifest()
    context_paths = {item["path"] for item in manifest["non_normative_context"]}
    assert "docs/13_branch_excavations/assessment_of_existing_generation_1_repository.md" in context_paths
    assert "docs/13_branch_excavations/feature_lock_and_evolution_guidance.md" in context_paths
    assert "docs/13_branch_excavations/frontmatter_and_codebase_sync_guidance.md" in context_paths
