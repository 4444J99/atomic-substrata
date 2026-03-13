#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VARIANT_ROOT = REPO_ROOT / "source_artifacts" / "atomic_corpus_variants" / "raw"

BRANCH_DOCS = [
    {
        "artifact_id": "branch_assessment_existing_generation_1_repository",
        "source_export": "ChatGPT-Branch · Atomic Knowledge Assembler.json",
        "pair_number": 3,
        "path": "docs/13_branch_excavations/assessment_of_existing_generation_1_repository.md",
        "title": "Assessment of Existing Generation-1 Repository",
        "source_title_exact": "Assessment",
        "kind": "branch_non_id_document",
    },
    {
        "artifact_id": "branch_addendum_memorandum_generation_2_migration",
        "source_export": "ChatGPT-Branch · Atomic Knowledge Assembler.json",
        "pair_number": 4,
        "path": "docs/13_branch_excavations/addendum_memorandum_generation_2_migration.md",
        "title": "Addendum Memorandum",
        "source_title_exact": "Addendum Memorandum",
        "kind": "branch_non_id_document",
    },
    {
        "artifact_id": "branch_parallel_linguistic_analysis_integration_design",
        "source_export": "ChatGPT-Branch · Atomic Knowledge Assembler.json",
        "pair_number": 5,
        "path": "docs/13_branch_excavations/parallel_linguistic_analysis_integration_design.md",
        "title": "Parallel Linguistic Analysis Integration Design",
        "source_title_exact": "Yes — design for it now",
        "kind": "branch_non_id_document",
    },
    {
        "artifact_id": "branch_feature_lock_and_evolution_guidance",
        "source_export": "ChatGPT-Branch · Atomic Knowledge Assembler (1).json",
        "pair_number": 8,
        "path": "docs/13_branch_excavations/feature_lock_and_evolution_guidance.md",
        "title": "Feature Lock and Evolution Guidance",
        "source_title_exact": "Short answer: features are not locked. In a system like the one you are building, evolution is not just allowed—it is an explicit design property of the architecture.",
        "kind": "branch_non_id_document",
    },
    {
        "artifact_id": "branch_frontmatter_and_codebase_sync_guidance",
        "source_export": "ChatGPT-Branch · Atomic Knowledge Assembler (1).json",
        "pair_number": 9,
        "path": "docs/13_branch_excavations/frontmatter_and_codebase_sync_guidance.md",
        "title": "Frontmatter and Codebase Sync Guidance",
        "source_title_exact": "Not fully.",
        "kind": "branch_non_id_document",
    },
    {
        "artifact_id": "uaks_v1_metadata_identity_charter_20260311",
        "source_export": "ChatGPT-Branch · Atomic Knowledge Assembler (1).json",
        "pair_number": 10,
        "path": "docs/13_branch_excavations/uaks_v1_metadata_identity_charter_20260311.md",
        "title": "Metadata and Identity Charter v1",
        "source_title_exact": "Metadata and Identity Charter v1",
        "kind": "branch_drafted_document",
    },
]


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")


def render_front_matter(data: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {json.dumps(value)}")
    lines.append("---")
    return "\n".join(lines)


def load_response(source_export: str, pair_number: int) -> tuple[str, str]:
    payload = json.loads((VARIANT_ROOT / source_export).read_text(encoding="utf-8"))
    prompt_index = (pair_number - 1) * 2
    prompt = payload["messages"][prompt_index]["say"]
    response = payload["messages"][prompt_index + 1]["say"]
    return prompt, response


def write_docs() -> list[dict[str, object]]:
    generated_at = now_utc()
    manifest: list[dict[str, object]] = []
    for item in BRANCH_DOCS:
        prompt, response = load_response(item["source_export"], item["pair_number"])
        output_path = REPO_ROOT / item["path"]
        front_matter = render_front_matter(
            {
                "title": item["title"],
                "artifact_id": item["artifact_id"],
                "kind": item["kind"],
                "source_export": item["source_export"],
                "source_pair_number": item["pair_number"],
                "source_title_exact": item["source_title_exact"],
                "generated_at": generated_at,
                "branch_only": True,
            }
        )
        write_text(output_path, front_matter + "\n\n" + response.strip() + "\n")
        manifest.append(
            {
                "artifact_id": item["artifact_id"],
                "title": item["title"],
                "source_title_exact": item["source_title_exact"],
                "path": item["path"],
                "source_export": item["source_export"],
                "source_pair_number": item["pair_number"],
                "kind": item["kind"],
                "prompt_preview": " ".join(prompt.split())[:120],
            }
        )
    return manifest


def write_manifest(manifest: list[dict[str, object]]) -> None:
    generated_at = now_utc()
    write_text(
        REPO_ROOT / "manifests/atomic_corpus_branch_artifact_manifest.json",
        json.dumps({"generated_at": generated_at, "artifacts": manifest}, indent=2),
    )
    lines = [
        "# Atomic Corpus Branch Artifact Manifest",
        "",
        f"- Generated: `{generated_at}`",
        f"- Artifact count: `{len(manifest)}`",
        "",
    ]
    for item in manifest:
        lines.append(
            f"- `{item['artifact_id']}` -> `{item['path']}` from `{item['source_export']}` pair `{item['source_pair_number']}`"
        )
    write_text(REPO_ROOT / "manifests/atomic_corpus_branch_artifact_manifest.md", "\n".join(lines) + "\n")


def main() -> int:
    manifest = write_docs()
    write_manifest(manifest)
    print(
        json.dumps(
            {
                "status": "pass",
                "artifact_count": len(manifest),
                "manifest_path": str(REPO_ROOT / "manifests/atomic_corpus_branch_artifact_manifest.json"),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
