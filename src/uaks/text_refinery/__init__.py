#!/usr/bin/env python3
"""
Text Refinery
=============
Processes raw text into refined TextAtoms.

Features:
- Tokenization
- Sentence parsing
- Entity extraction
- Metadata generation
- Content hashing
"""

import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class TextAtom:
    """Represents a refined text atom."""

    id: str
    content: str
    hash: str
    tokens: list[str] = field(default_factory=list)
    sentences: list[str] = field(default_factory=list)
    entities: list[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    refined_at: str = field(default_factory=lambda: datetime.now().isoformat())


class TextRefinery:
    """Refines raw text into TextAtoms."""

    def __init__(self):
        self.tokenizer_pattern = re.compile(r"\b\w+\b")
        self.sentence_pattern = re.compile(r"[.!?]+")

    def refine(self, content: str, source: str = "") -> TextAtom:
        """
        Refine raw text into a TextAtom.

        Args:
            content: Raw text content
            source: Optional source identifier

        Returns:
            TextAtom with extracted features
        """
        # Compute hash
        atom_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        atom_id = f"text_{atom_hash}"

        # Tokenize
        tokens = self.tokenize(content)

        # Extract sentences
        sentences = self.extract_sentences(content)

        # Extract entities (simple pattern-based)
        entities = self.extract_entities(content)

        # Generate metadata
        metadata = {
            "source": source,
            "char_count": len(content),
            "token_count": len(tokens),
            "sentence_count": len(sentences),
            "entity_count": len(entities),
            "avg_word_length": sum(len(t) for t in tokens) / len(tokens)
            if tokens
            else 0,
        }

        return TextAtom(
            id=atom_id,
            content=content,
            hash=atom_hash,
            tokens=tokens,
            sentences=sentences,
            entities=entities,
            metadata=metadata,
        )

    def tokenize(self, text: str) -> list[str]:
        """Tokenize text into words."""
        text = text.lower()
        tokens = self.tokenizer_pattern.findall(text)
        return tokens

    def extract_sentences(self, text: str) -> list[str]:
        """Split text into sentences."""
        # Simple sentence splitting
        sentences = re.split(r"[.!?]+", text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences

    def extract_entities(self, text: str) -> list[dict]:
        """
        Extract entities from text.

        Currently implements simple pattern-based extraction.
        Can be extended with NLP models.
        """
        entities = []

        # Extract capitalized phrases (potential proper nouns)
        cap_pattern = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b")
        matches = cap_pattern.findall(text)

        seen = set()
        for match in matches:
            if match.lower() not in seen and len(match) > 1:
                entities.append(
                    {
                        "text": match,
                        "type": "PROPER_NOUN",
                        "start": text.find(match),
                    }
                )
                seen.add(match.lower())

        # Extract numbers
        num_pattern = re.compile(r"\b\d+(?:\.\d+)?\b")
        for match in num_pattern.findall(text):
            entities.append(
                {
                    "text": match,
                    "type": "NUMBER",
                    "start": text.find(match),
                }
            )

        return entities

    def batch_refine(self, texts: list[tuple[str, str]]) -> list[TextAtom]:
        """
        Refine multiple texts.

        Args:
            texts: List of (content, source) tuples

        Returns:
            List of TextAtoms
        """
        return [self.refine(content, source) for content, source in texts]


def main():
    """CLI for text refinery."""
    import sys

    refinery = TextRefinery()

    if len(sys.argv) < 2:
        print("Usage: text_refinery.py <text>")
        print("  or:  text_refinery.py --file <path>")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("Error: --file requires a path")
            sys.exit(1)

        path = Path(sys.argv[2])
        if not path.exists():
            print(f"Error: File not found: {path}")
            sys.exit(1)

        content = path.read_text()
        source = str(path)
    else:
        content = " ".join(sys.argv[1:])
        source = "cli"

    atom = refinery.refine(content, source)

    print(f"TextAtom: {atom.id}")
    print(f"Hash: {atom.hash}")
    print(f"Tokens: {len(atom.tokens)}")
    print(f"Sentences: {len(atom.sentences)}")
    print(f"Entities: {len(atom.entities)}")
    print(f"\nMetadata:")
    for key, value in atom.metadata.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
