#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path("/Users/4jp/Downloads/New Folder With Items/atomic-corpus")
DEST_ROOT = REPO_ROOT / "source_artifacts" / "atomic_corpus_variants"


@dataclass(slots=True)
class PairRecord:
    pair_number: int
    prompt: str
    response: str
    prompt_hash: str
    response_hash: str
    prompt_title: str
    response_title: str


def now_utc() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "artifact"


def first_meaningful_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.lower().startswith("thought for "):
            continue
        return stripped.rstrip(":")
    return "Untitled"


def render_front_matter(data: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {json.dumps(value)}")
    lines.append("---")
    return "\n".join(lines)


def load_json_pairs(path: Path) -> tuple[dict, list[PairRecord]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    messages = payload["messages"]
    pairs: list[PairRecord] = []
    for offset in range(0, len(messages), 2):
        prompt = messages[offset]["say"]
        response = messages[offset + 1]["say"]
        pairs.append(
            PairRecord(
                pair_number=offset // 2 + 1,
                prompt=prompt,
                response=response,
                prompt_hash=sha256_text(prompt),
                response_hash=sha256_text(response),
                prompt_title=first_meaningful_line(prompt),
                response_title=first_meaningful_line(response),
            )
        )
    return payload, pairs


def export_slug(filename: str) -> str:
    stem = Path(filename).stem
    return slugify(stem)


def copy_raw_exports() -> list[Path]:
    ensure_dir(DEST_ROOT / "raw")
    copied: list[Path] = []
    for source in sorted(SOURCE_ROOT.glob("*")):
        if source.is_file() and source.suffix in {".json", ".md"}:
            target = DEST_ROOT / "raw" / source.name
            shutil.copy2(source, target)
            copied.append(target)
    return copied


def write_pair_archives(json_path: Path, pairs: list[PairRecord]) -> None:
    variant_root = DEST_ROOT / "chat_pairs" / export_slug(json_path.name)
    ensure_dir(variant_root)
    for pair in pairs:
        pair_path = variant_root / f"pair-{pair.pair_number:03d}-{slugify(pair.prompt_title)[:80]}.md"
        front_matter = render_front_matter(
            {
                "source_export": json_path.name,
                "pair_number": pair.pair_number,
                "prompt_title": pair.prompt_title,
                "response_title": pair.response_title,
                "prompt_sha256": pair.prompt_hash,
                "response_sha256": pair.response_hash,
            }
        )
        body = "\n\n".join(
            [
                front_matter,
                f"# Pair {pair.pair_number:03d}",
                "## Prompt",
                pair.prompt,
                "## Response",
                pair.response,
            ]
        )
        write_text(pair_path, body)


def build_manifest() -> dict[str, object]:
    exports: list[dict[str, object]] = []
    exact_pair_index: dict[tuple[str, str], list[dict[str, object]]] = {}
    for json_path in sorted(SOURCE_ROOT.glob("*.json")):
        payload, pairs = load_json_pairs(json_path)
        write_pair_archives(json_path, pairs)
        for pair in pairs:
            key = (pair.prompt_hash, pair.response_hash)
            exact_pair_index.setdefault(key, []).append(
                {"file": json_path.name, "pair_number": pair.pair_number}
            )
        exports.append(
            {
                "file": json_path.name,
                "title": payload["metadata"]["title"],
                "message_count": len(payload["messages"]),
                "pair_count": len(pairs),
                "pair_records": [
                    {
                        "pair_number": pair.pair_number,
                        "prompt_title": pair.prompt_title,
                        "response_title": pair.response_title,
                        "prompt_sha256": pair.prompt_hash,
                        "response_sha256": pair.response_hash,
                    }
                    for pair in pairs
                ],
            }
        )

    for export in exports:
        unique_pairs = []
        for pair in export["pair_records"]:
            key = (pair["prompt_sha256"], pair["response_sha256"])
            if len(exact_pair_index[key]) == 1:
                unique_pairs.append(
                    {
                        "pair_number": pair["pair_number"],
                        "prompt_title": pair["prompt_title"],
                        "response_title": pair["response_title"],
                    }
                )
        export["unique_pairs"] = unique_pairs

    shared_exact_pairs = [
        {
            "occurrences": occurrences,
        }
        for occurrences in exact_pair_index.values()
        if len(occurrences) > 1
    ]

    return {
        "generated_at": now_utc(),
        "source_root": str(SOURCE_ROOT),
        "destination_root": str(DEST_ROOT),
        "exports": exports,
        "shared_exact_pairs": shared_exact_pairs,
    }


def write_summary(manifest: dict[str, object]) -> None:
    lines = [
        "# Atomic Corpus Variant Summary",
        "",
        f"- Generated: `{manifest['generated_at']}`",
        f"- Source root: `{manifest['source_root']}`",
        "",
        "## Exports",
        "",
    ]
    for export in manifest["exports"]:
        lines.append(
            f"- `{export['file']}`: `{export['pair_count']}` pairs, `{len(export['unique_pairs'])}` unique exact pairs."
        )
    lines.extend(
        [
            "",
            "## Shared Exact Pair Groups",
            "",
            f"- `{len(manifest['shared_exact_pairs'])}` pair groups appear in more than one export.",
            "",
        ]
    )
    write_text(DEST_ROOT / "normalized" / "variant_summary.md", "\n".join(lines) + "\n")


def main() -> int:
    ensure_dir(DEST_ROOT)
    copy_raw_exports()
    manifest = build_manifest()
    write_text(DEST_ROOT / "normalized" / "variant_manifest.json", json.dumps(manifest, indent=2))
    write_summary(manifest)
    print(
        json.dumps(
            {
                "status": "pass",
                "generated_at": manifest["generated_at"],
                "destination_root": str(DEST_ROOT),
                "export_count": len(manifest["exports"]),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
