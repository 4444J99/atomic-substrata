#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MAIN_MANIFEST_PATH = REPO_ROOT / "manifests" / "artifact_manifest.json"
BRANCH_MANIFEST_PATH = REPO_ROOT / "manifests" / "atomic_corpus_branch_artifact_manifest.json"

CANONICAL_DIR_PREFIXES = (
    "docs/02_architecture/",
    "docs/03_schemas/",
    "docs/04_refinery/",
    "docs/05_retrieval_assembly/",
    "docs/06_interface_portal/",
    "docs/07_operations/",
    "docs/08_evaluation/",
    "docs/09_integrity/",
    "docs/10_launch/",
)

NON_NORMATIVE_MAIN_PREFIXES = (
    "docs/00_meta/",
    "docs/11_implementation/",
)

SPECIAL_CONTEXT_PATHS = {
    "docs/02_architecture/uaks_v1_visual_architecture_image_generation_note.md": (
        "image generation note only; not a normative implementation spec"
    ),
}

BRANCH_SUPPLEMENTAL_ARTIFACTS = {
    "branch_addendum_memorandum_generation_2_migration": (
        "captures the Generation-1 to Generation-2 migration model"
    ),
    "branch_parallel_linguistic_analysis_integration_design": (
        "defines the external analytical lane and translation membrane"
    ),
    "uaks_v1_metadata_identity_charter_20260311": (
        "supplies the metadata, identity, and synchronization model absent from the mainline thread"
    ),
}


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_entry(item: dict[str, object], category: str, rationale: str) -> dict[str, object]:
    return {
        "artifact_id": item["artifact_id"],
        "title": item["title"],
        "path": item["path"],
        "category": category,
        "rationale": rationale,
    }


def build_manifest() -> dict[str, object]:
    main_items = load_json(MAIN_MANIFEST_PATH)
    branch_items = load_json(BRANCH_MANIFEST_PATH)["artifacts"]

    excluded_placeholders = [
        build_entry(item, "excluded_placeholder", "named in transcript but not fully drafted")
        for item in main_items
        if item["kind"] == "placeholder"
    ]
    excluded_placeholder_paths = {item["path"] for item in excluded_placeholders}

    canonical_mainline_specs: list[dict[str, object]] = []
    non_normative_context: list[dict[str, object]] = []

    for item in main_items:
        path = item["path"]
        if path in excluded_placeholder_paths:
            continue
        if path in SPECIAL_CONTEXT_PATHS:
            non_normative_context.append(
                build_entry(item, "non_normative_context", SPECIAL_CONTEXT_PATHS[path])
            )
            continue
        if path.startswith(NON_NORMATIVE_MAIN_PREFIXES):
            non_normative_context.append(
                build_entry(
                    item,
                    "non_normative_context",
                    "contextual or process guidance; useful for engineering orientation but not normative substrate law",
                )
            )
            continue
        if path.startswith(CANONICAL_DIR_PREFIXES):
            canonical_mainline_specs.append(
                build_entry(
                    item,
                    "canonical_mainline_spec",
                    "implementation-relevant mainline UAKS artifact from the authoritative 21-pair reconstruction",
                )
            )

    branch_supplemental_specs: list[dict[str, object]] = []
    for item in branch_items:
        artifact_id = item["artifact_id"]
        if artifact_id in BRANCH_SUPPLEMENTAL_ARTIFACTS:
            branch_supplemental_specs.append(
                build_entry(
                    item,
                    "branch_supplemental_spec",
                    BRANCH_SUPPLEMENTAL_ARTIFACTS[artifact_id],
                )
            )
        else:
            non_normative_context.append(
                build_entry(
                    item,
                    "non_normative_context",
                    "branch-only advisory or evaluative guidance retained for implementation context",
                )
            )

    canonical_mainline_specs.sort(key=lambda item: item["path"])
    branch_supplemental_specs.sort(key=lambda item: item["path"])
    non_normative_context.sort(key=lambda item: item["path"])
    excluded_placeholders.sort(key=lambda item: item["path"])

    all_included_paths = {
        item["path"] for item in canonical_mainline_specs + branch_supplemental_specs + non_normative_context
    }

    return {
        "generated_at": now_utc(),
        "objective": "Define the exact Markdown corpus to feed software distillation from the UAKS transcript reconstruction.",
        "counts": {
            "canonical_mainline_specs": len(canonical_mainline_specs),
            "branch_supplemental_specs": len(branch_supplemental_specs),
            "non_normative_context": len(non_normative_context),
            "excluded_placeholders": len(excluded_placeholders),
            "total_included_markdown": len(all_included_paths),
        },
        "canonical_mainline_specs": canonical_mainline_specs,
        "branch_supplemental_specs": branch_supplemental_specs,
        "non_normative_context": non_normative_context,
        "excluded_placeholders": excluded_placeholders,
        "ingestion_rule": {
            "include_categories": [
                "canonical_mainline_spec",
                "branch_supplemental_spec",
            ],
            "advisory_context_category": "non_normative_context",
            "exclude_category": "excluded_placeholder",
        },
    }


def write_markdown(manifest: dict[str, object]) -> None:
    lines = [
        "# Distillation Input Manifest",
        "",
        f"- Generated: `{manifest['generated_at']}`",
        f"- Objective: {manifest['objective']}",
        "",
        "## Counts",
        "",
    ]
    for key, value in manifest["counts"].items():
        lines.append(f"- `{key}`: `{value}`")

    sections = [
        ("canonical_mainline_specs", "Canonical Mainline Specs"),
        ("branch_supplemental_specs", "Branch Supplemental Specs"),
        ("non_normative_context", "Non-Normative Context"),
        ("excluded_placeholders", "Excluded Placeholders"),
    ]
    for key, heading in sections:
        lines.extend(["", f"## {heading}", ""])
        for item in manifest[key]:
            lines.append(f"- `{item['path']}` — {item['title']}")
            lines.append(f"  rationale: {item['rationale']}")

    lines.extend(
        [
            "",
            "## Distillation Rule",
            "",
            "- Distill directly from `canonical_mainline_specs` and `branch_supplemental_specs`.",
            "- Use `non_normative_context` only as engineering context, not as substrate law.",
            "- Do not ingest `excluded_placeholders` into implementation generation.",
            "",
        ]
    )
    write_text(REPO_ROOT / "manifests" / "distillation_input_manifest.md", "\n".join(lines))


def main() -> int:
    manifest = build_manifest()
    write_text(REPO_ROOT / "manifests" / "distillation_input_manifest.json", json.dumps(manifest, indent=2))
    write_markdown(manifest)
    print(
        json.dumps(
            {
                "status": "pass",
                "generated_at": manifest["generated_at"],
                "counts": manifest["counts"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
