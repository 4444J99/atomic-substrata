from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_branch_artifact_manifest_exists_and_counts() -> None:
    manifest = json.loads(
        (REPO_ROOT / "manifests/atomic_corpus_branch_artifact_manifest.json").read_text(encoding="utf-8")
    )
    artifacts = manifest["artifacts"]
    assert len(artifacts) == 6
    artifact_ids = {item["artifact_id"] for item in artifacts}
    assert "uaks_v1_metadata_identity_charter_20260311" in artifact_ids
    assert "branch_parallel_linguistic_analysis_integration_design" in artifact_ids


def test_branch_excavation_docs_exist() -> None:
    docs = [
        "docs/13_branch_excavations/assessment_of_existing_generation_1_repository.md",
        "docs/13_branch_excavations/addendum_memorandum_generation_2_migration.md",
        "docs/13_branch_excavations/parallel_linguistic_analysis_integration_design.md",
        "docs/13_branch_excavations/feature_lock_and_evolution_guidance.md",
        "docs/13_branch_excavations/frontmatter_and_codebase_sync_guidance.md",
        "docs/13_branch_excavations/uaks_v1_metadata_identity_charter_20260311.md",
    ]
    for relative in docs:
        assert (REPO_ROOT / relative).exists()


def test_metadata_identity_charter_preserves_canonical_title() -> None:
    charter = (REPO_ROOT / "docs/13_branch_excavations/uaks_v1_metadata_identity_charter_20260311.md").read_text(
        encoding="utf-8"
    )
    assert 'title: "Metadata and Identity Charter v1"' in charter
    assert "Document ID: uaks_v1_metadata_identity_charter_20260311" in charter
