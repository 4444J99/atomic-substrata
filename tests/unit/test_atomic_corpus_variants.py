from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]


def test_atomic_corpus_variant_manifest_counts() -> None:
    manifest = json.loads(
        (REPO_ROOT / "source_artifacts/atomic_corpus_variants/normalized/variant_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    exports = {item["file"]: item for item in manifest["exports"]}
    assert len(exports) == 3
    assert exports["ChatGPT-Atomic Knowledge Assembler.json"]["pair_count"] == 21
    assert exports["ChatGPT-Branch · Atomic Knowledge Assembler (1).json"]["pair_count"] == 10
    assert exports["ChatGPT-Branch · Atomic Knowledge Assembler.json"]["pair_count"] == 5


def test_atomic_corpus_variant_raw_copy_count() -> None:
    raw_root = REPO_ROOT / "source_artifacts/atomic_corpus_variants/raw"
    raw_files = sorted(path.name for path in raw_root.iterdir() if path.is_file())
    assert len(raw_files) == 6
    assert "ChatGPT-Atomic Knowledge Assembler.json" in raw_files
    assert "ChatGPT-Branch · Atomic Knowledge Assembler (1).json" in raw_files
    assert "ChatGPT-Branch · Atomic Knowledge Assembler.json" in raw_files


def test_atomic_corpus_variant_pair_archive_counts() -> None:
    root = REPO_ROOT / "source_artifacts/atomic_corpus_variants/chat_pairs"
    expected = {
        "chatgpt-atomic-knowledge-assembler": 21,
        "chatgpt-branch-atomic-knowledge-assembler-1": 10,
        "chatgpt-branch-atomic-knowledge-assembler": 5,
    }
    for slug, count in expected.items():
        pair_files = sorted((root / slug).glob("pair-*.md"))
        assert len(pair_files) == count
