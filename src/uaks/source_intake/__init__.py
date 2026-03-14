#!/usr/bin/env python3
"""
Source Intake
=============
Handles ingestion of various source types into UAKS.

Features:
- File system sources
- URL sources
- Text input
- Batch processing
"""

import hashlib
import json
import re
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class IntakeSource:
    """Represents a source for ingestion."""

    id: str
    source_type: str  # file, url, text
    path: str
    content: str
    hash: str
    metadata: dict = field(default_factory=dict)
    ingested_at: str = field(default_factory=lambda: datetime.now().isoformat())


class SourceIntake:
    """Handles ingestion of various source types."""

    def __init__(self):
        self.supported_extensions = {
            ".txt",
            ".md",
            ".py",
            ".js",
            ".ts",
            ".jsx",
            ".tsx",
            ".go",
            ".rs",
            ".java",
            ".c",
            ".cpp",
            ".h",
            ".hpp",
            ".cs",
            ".rb",
            ".php",
            ".swift",
            ".kt",
            ".scala",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".xml",
            ".html",
            ".sql",
            ".sh",
            ".bash",
            ".zsh",
        }
        self.url_pattern = re.compile(r"^https?://")

    def ingest(self, source: str, source_type: str = "auto") -> IntakeSource:
        """
        Ingest a source.

        Args:
            source: Path, URL, or text content
            source_type: Type of source (file, url, text, auto)

        Returns:
            IntakeSource with content and metadata
        """
        if source_type == "auto":
            source_type = self.detect_source_type(source)

        if source_type == "file":
            return self.ingest_file(source)
        elif source_type == "url":
            return self.ingest_url(source)
        elif source_type == "text":
            return self.ingest_text(source)
        else:
            raise ValueError(f"Unknown source type: {source_type}")

    def detect_source_type(self, source: str) -> str:
        """Detect the type of source."""
        if self.url_pattern.match(source):
            return "url"

        path = Path(source)
        if path.exists() and path.is_file():
            return "file"

        return "text"

    def ingest_file(self, filepath: str) -> IntakeSource:
        """Ingest a file."""
        path = Path(filepath)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        if not path.is_file():
            raise ValueError(f"Not a file: {filepath}")

        content = path.read_text(encoding="utf-8")
        atom_hash = hashlib.sha256(content.encode()).hexdigest()[:16]

        source_id = f"file_{atom_hash}"

        metadata = {
            "filepath": str(path.absolute()),
            "filename": path.name,
            "extension": path.suffix,
            "size": path.stat().st_size,
            "modified": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
        }

        return IntakeSource(
            id=source_id,
            source_type="file",
            path=str(path),
            content=content,
            hash=atom_hash,
            metadata=metadata,
        )

    def ingest_url(self, url: str) -> IntakeSource:
        """Ingest content from a URL."""
        if not self.url_pattern.match(url):
            raise ValueError(f"Invalid URL: {url}")

        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                content = response.read().decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"Failed to fetch URL: {e}")

        atom_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        source_id = f"url_{atom_hash}"

        metadata = {
            "url": url,
            "content_type": response.headers.get("Content-Type", "unknown"),
        }

        return IntakeSource(
            id=source_id,
            source_type="url",
            path=url,
            content=content,
            hash=atom_hash,
            metadata=metadata,
        )

    def ingest_text(self, text: str, source_name: str = "cli") -> IntakeSource:
        """Ingest raw text."""
        atom_hash = hashlib.sha256(text.encode()).hexdigest()[:16]
        source_id = f"text_{atom_hash}"

        metadata = {
            "source_name": source_name,
            "char_count": len(text),
        }

        return IntakeSource(
            id=source_id,
            source_type="text",
            path=source_name,
            content=text,
            hash=atom_hash,
            metadata=metadata,
        )

    def batch_ingest(self, sources: list[tuple[str, str]]) -> list[IntakeSource]:
        """
        Ingest multiple sources.

        Args:
            sources: List of (source, source_type) tuples

        Returns:
            List of IntakeSources
        """
        results = []
        for source, source_type in sources:
            try:
                result = self.ingest(source, source_type)
                results.append(result)
            except Exception as e:
                print(f"Error ingesting {source}: {e}")
        return results

    def ingest_directory(
        self, dirpath: str, recursive: bool = True
    ) -> list[IntakeSource]:
        """
        Ingest all supported files in a directory.

        Args:
            dirpath: Path to directory
            recursive: Whether to recurse into subdirectories

        Returns:
            List of IntakeSources
        """
        path = Path(dirpath)

        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {dirpath}")

        if not path.is_dir():
            raise ValueError(f"Not a directory: {dirpath}")

        results = []

        if recursive:
            pattern = "**/*"
        else:
            pattern = "*"

        for filepath in path.glob(pattern):
            if filepath.is_file() and filepath.suffix in self.supported_extensions:
                try:
                    result = self.ingest_file(str(filepath))
                    results.append(result)
                except Exception as e:
                    print(f"Error ingesting {filepath}: {e}")

        return results


def main():
    """CLI for source intake."""
    import sys

    intake = SourceIntake()

    if len(sys.argv) < 2:
        print("Usage: source_intake.py <source>")
        print("  source: file path, URL, or text")
        print("")
        print("Examples:")
        print("  source_intake.py /path/to/file.txt")
        print("  source_intake.py https://example.com")
        print("  source_intake.py --dir /path/to/directory")
        sys.exit(1)

    if sys.argv[1] == "--dir":
        if len(sys.argv) < 3:
            print("Error: --dir requires a path")
            sys.exit(1)

        results = intake.ingest_directory(sys.argv[2])
        print(f"Ingested {len(results)} files:")
        for r in results:
            print(f"  - {r.id}: {r.metadata.get('filename', r.path)}")
    else:
        source = sys.argv[1]
        result = intake.ingest(source)

        print(f"Source: {result.id}")
        print(f"Type: {result.source_type}")
        print(f"Hash: {result.hash}")
        print(f"Content length: {len(result.content)}")
        print(f"\nMetadata:")
        for key, value in result.metadata.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
