#!/usr/bin/env python3
"""
UAKS Assembly Engine
====================
On-demand knowledge assembly from atoms with vector similarity.

Features:
- Vector-based similarity search
- Context window assembly
- Relevance ranking
- Caching for repeated queries
"""

import hashlib
import json
import os
import re
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import numpy as np

    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


@dataclass
class Atom:
    """Represents an atom in the UAKS."""

    id: str
    type: str
    content: str
    hash: str
    source: str
    size: int
    status: str = "raw"
    embedding: Optional[list[float]] = None
    metadata: dict = field(default_factory=dict)


@dataclass
class AssembledOutput:
    """Result of assembling atoms for a query."""

    query: str
    atoms: list[Atom]
    assembled_text: str
    confidence: float
    assembled_at: str


class SimpleVectorizer:
    """Simple TF-IDF-like vectorizer when numpy is not available."""

    def __init__(self):
        self.vocabulary = {}
        self.idf = {}

    def fit_transform(self, texts: list[str]) -> list[list[float]]:
        """Convert texts to vectors using simple bag-of-words."""
        vectors = []

        # Build vocabulary
        for text in texts:
            words = self._tokenize(text)
            for word in words:
                if word not in self.vocabulary:
                    self.vocabulary[word] = len(self.vocabulary)

        # Calculate IDF
        doc_count = len(texts)
        doc_freq = defaultdict(int)
        for text in texts:
            words = set(self._tokenize(text))
            for word in words:
                doc_freq[word] += 1

        for word, freq in doc_freq.items():
            self.idf[word] = doc_count / freq

        # Create vectors
        for text in texts:
            words = self._tokenize(text)
            vector = [0.0] * len(self.vocabulary)

            word_count = defaultdict(int)
            for word in words:
                word_count[word] += 1

            for word, count in word_count.items():
                if word in self.vocabulary:
                    tf = count / len(words) if words else 0
                    idf = self.idf.get(word, 1.0)
                    vector[self.vocabulary[word]] = tf * idf

            vectors.append(vector)

        return vectors

    def transform(self, texts: list[str]) -> list[list[float]]:
        """Transform texts using fitted vocabulary."""
        vectors = []

        for text in texts:
            words = self._tokenize(text)
            vector = [0.0] * len(self.vocabulary)

            word_count = defaultdict(int)
            for word in words:
                word_count[word] += 1

            for word, count in word_count.items():
                if word in self.vocabulary:
                    tf = count / len(words) if words else 0
                    idf = self.idf.get(word, 1.0)
                    vector[self.vocabulary[word]] = tf * idf

            vectors.append(vector)

        return vectors

    def _tokenize(self, text: str) -> list[str]:
        """Simple tokenization."""
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        return text.split()


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not HAS_NUMPY:
        # Simple implementation
        dot_product = sum(x * y for x, y in zip(a, b))
        magnitude_a = sum(x * x for x in a) ** 0.5
        magnitude_b = sum(x * x for x in b) ** 0.5

        if magnitude_a == 0 or magnitude_b == 0:
            return 0.0

        return dot_product / (magnitude_a * magnitude_b)
    else:
        a = np.array(a)
        b = np.array(b)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


class AssemblyEngine:
    """Main assembly engine for UAKS."""

    def __init__(self, state_file: Optional[Path] = None):
        self.state_file = state_file or Path("data/pipeline_state.json")
        self.cache = {}
        self.vectorizer = SimpleVectorizer()
        self.atoms: list[Atom] = []
        self.vectors: list[list[float]] = []

    def load_atoms(self):
        """Load atoms from state file."""
        if not self.state_file.exists():
            return

        with open(self.state_file, "r") as f:
            state = json.load(f)

        self.atoms = []

        for atom_data in state.get("atoms", {}).get("text", []):
            self.atoms.append(
                Atom(
                    id=atom_data.get("id", ""),
                    type="text",
                    content=atom_data.get("content", ""),
                    hash=atom_data.get("hash", ""),
                    source=atom_data.get("source", ""),
                    size=atom_data.get("size", 0),
                    status=atom_data.get("status", "raw"),
                )
            )

        for atom_data in state.get("atoms", {}).get("code", []):
            self.atoms.append(
                Atom(
                    id=atom_data.get("id", ""),
                    type="code",
                    content=atom_data.get("content", ""),
                    hash=atom_data.get("hash", ""),
                    source=atom_data.get("source", ""),
                    size=atom_data.get("size", 0),
                    status=atom_data.get("status", "raw"),
                )
            )

    def build_index(self):
        """Build search index from loaded atoms."""
        if not self.atoms:
            return

        contents = [atom.content for atom in self.atoms]
        self.vectors = self.vectorizer.fit_transform(contents)

    def search(self, query: str, top_k: int = 5) -> list[tuple[Atom, float]]:
        """
        Search for atoms relevant to query.

        Returns list of (atom, similarity_score) tuples.
        """
        if not self.atoms or not self.vectors:
            self.load_atoms()
            self.build_index()

        # Transform query
        query_vectors = self.vectorizer.transform([query])
        query_vector = query_vectors[0]

        # Calculate similarities
        similarities = []
        for i, atom in enumerate(self.atoms):
            if i < len(self.vectors):
                sim = cosine_similarity(query_vector, self.vectors[i])
                similarities.append((atom, sim))

        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:top_k]

    def assemble(
        self, query: str, top_k: int = 5, context_window: int = 200
    ) -> AssembledOutput:
        """
        Assemble atoms into coherent output for a query.

        Args:
            query: Search query
            top_k: Number of atoms to retrieve
            context_window: Characters to include per atom

        Returns:
            AssembledOutput with results
        """
        # Check cache
        cache_key = hashlib.md5(query.encode()).hexdigest()
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Search for relevant atoms
        results = self.search(query, top_k)

        if not results:
            return AssembledOutput(
                query=query,
                atoms=[],
                assembled_text="No atoms found for query.",
                confidence=0.0,
                assembled_at=datetime.now().isoformat(),
            )

        # Assemble text
        assembled_parts = [f"Query: {query}\n"]
        assembled_parts.append("=" * 40 + "\n\n")

        total_similarity = 0.0
        for atom, sim in results:
            total_similarity += sim

            # Get relevant snippet
            content = atom.content
            if len(content) > context_window:
                # Find best snippet (simple: first N chars)
                content = content[:context_window] + "..."

            assembled_parts.append(
                f"## {atom.id} ({atom.type}, similarity: {sim:.3f})\n"
            )
            assembled_parts.append(f"Source: {atom.source}\n")
            assembled_parts.append(f"Content:\n{content}\n\n")

        assembled_text = "".join(assembled_parts)

        confidence = total_similarity / len(results) if results else 0.0

        output = AssembledOutput(
            query=query,
            atoms=[a for a, _ in results],
            assembled_text=assembled_text,
            confidence=confidence,
            assembled_at=datetime.now().isoformat(),
        )

        # Cache result
        self.cache[cache_key] = output

        return output

    def clear_cache(self):
        """Clear the query cache."""
        self.cache = {}


def main():
    """CLI for assembly engine."""
    import sys

    engine = AssemblyEngine()
    engine.load_atoms()
    engine.build_index()

    if len(sys.argv) < 2:
        print("Usage: assembly.py <query>")
        print("  or:  assembly.py --search <query>")
        print("  or:  assembly.py --list")
        sys.exit(1)

    if sys.argv[1] == "--list":
        print(f"Loaded {len(engine.atoms)} atoms")
        for atom in engine.atoms[:10]:
            print(f"  - {atom.id}: {atom.content[:50]}...")
        return

    if sys.argv[1] == "--search":
        query = " ".join(sys.argv[2:])
    else:
        query = " ".join(sys.argv[1:])

    result = engine.assemble(query)

    print(f"\nQuery: {result.query}")
    print(f"Confidence: {result.confidence:.3f}")
    print(f"Atoms retrieved: {len(result.atoms)}")
    print("\n" + result.assembled_text)


if __name__ == "__main__":
    main()
