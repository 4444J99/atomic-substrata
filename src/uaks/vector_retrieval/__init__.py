#!/usr/bin/env python3
"""
Vector Retrieval
==============
Similarity search for atoms using vector embeddings.

Features:
- TF-IDF vectorization
- Cosine similarity search
- BM25 retrieval
- Hybrid search
"""

import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Document:
    """Represents a document for retrieval."""

    id: str
    content: str
    metadata: dict = field(default_factory=dict)


@dataclass
class RetrievalResult:
    """Represents a retrieval result."""

    doc_id: str
    score: float
    document: Optional[Document] = None


class VectorRetrieval:
    """Vector-based retrieval system."""

    def __init__(self):
        self.documents: dict[str, Document] = {}
        self.vocabulary: dict[str, int] = {}
        self.idf: dict[str, float] = {}
        self.doc_vectors: dict[str, dict[str, float]] = {}

    def add_document(self, doc: Document):
        """Add a document to the index."""
        self.documents[doc.id] = doc
        self._update_index(doc)

    def _update_index(self, doc: Document):
        """Update the inverted index for a document."""
        tokens = self._tokenize(doc.content)

        # Build term frequency
        tf = Counter(tokens)

        # Update vocabulary
        for token in tokens:
            if token not in self.vocabulary:
                self.vocabulary[token] = len(self.vocabulary)

        # Compute TF-IDF vector
        vector = {}
        for term, freq in tf.items():
            tf_value = 1 + math.log(freq)
            idf_value = self.idf.get(term, 0)
            vector[term] = tf_value * idf_value

        self.doc_vectors[doc.id] = vector

    def _tokenize(self, text: str) -> list[str]:
        """Tokenize text."""
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        tokens = text.split()
        return [t for t in tokens if len(t) > 1]

    def build_index(self):
        """Build the complete index."""
        # Compute IDF for all terms
        doc_count = len(self.documents)

        if doc_count == 0:
            return

        # Count document frequency
        df = defaultdict(int)
        for doc in self.documents.values():
            tokens = set(self._tokenize(doc.content))
            for token in tokens:
                df[token] += 1

        # Compute IDF
        for term, freq in df.items():
            self.idf[term] = math.log(doc_count / freq)

        # Rebuild vectors with IDF
        self.doc_vectors = {}
        for doc in self.documents.values():
            self._update_index(doc)

    def search(self, query: str, top_k: int = 10) -> list[RetrievalResult]:
        """
        Search for documents matching query.

        Args:
            query: Search query
            top_k: Number of results to return

        Returns:
            List of retrieval results
        """
        if not self.documents:
            return []

        # Ensure index is built
        if not self.idf:
            self.build_index()

        # Compute query vector
        query_tokens = self._tokenize(query)
        query_tf = Counter(query_tokens)

        query_vector = {}
        for term, freq in query_tf.items():
            tf_value = 1 + math.log(freq)
            idf_value = self.idf.get(term, math.log(len(self.documents)))
            query_vector[term] = tf_value * idf_value

        # Compute similarities
        results = []
        for doc_id, doc_vector in self.doc_vectors.items():
            similarity = self._cosine_similarity(query_vector, doc_vector)
            results.append(
                RetrievalResult(
                    doc_id=doc_id,
                    score=similarity,
                    document=self.documents.get(doc_id),
                )
            )

        # Sort by score
        results.sort(key=lambda r: r.score, reverse=True)

        return results[:top_k]

    def _cosine_similarity(
        self, vec1: dict[str, float], vec2: dict[str, float]
    ) -> float:
        """Compute cosine similarity between two vectors."""
        # Compute dot product
        dot_product = 0
        for term in vec1:
            if term in vec2:
                dot_product += vec1[term] * vec2[term]

        # Compute magnitudes
        mag1 = math.sqrt(sum(v * v for v in vec1.values()))
        mag2 = math.sqrt(sum(v * v for v in vec2.values()))

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot_product / (mag1 * mag2)

    def get_stats(self) -> dict:
        """Get retrieval statistics."""
        return {
            "document_count": len(self.documents),
            "vocabulary_size": len(self.vocabulary),
            "indexed_terms": len(self.idf),
        }


class BM25Retrieval:
    """BM25 retrieval system."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.documents: dict[str, Document] = {}
        self.doc_lengths: dict[str, int] = {}
        self.avg_doc_length: float = 0
        self.doc_freq: dict[str, int] = {}
        self.term_doc_freq: dict[str, dict[str, int]] = {}

    def add_document(self, doc: Document):
        """Add a document to the index."""
        self.documents[doc.id] = doc
        tokens = self._tokenize(doc.content)
        self.doc_lengths[doc.id] = len(tokens)

        # Update term document frequency
        for token in set(tokens):
            if token not in self.term_doc_freq:
                self.term_doc_freq[token] = {}
            self.term_doc_freq[token][doc.id] = tokens.count(token)

    def _tokenize(self, text: str) -> list[str]:
        """Tokenize text."""
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        return [t for t in text.split() if len(t) > 1]

    def build_index(self):
        """Build the BM25 index."""
        doc_count = len(self.documents)

        if doc_count == 0:
            return

        self.avg_doc_length = sum(self.doc_lengths.values()) / doc_count

        # Compute document frequency
        for term in self.term_doc_freq:
            self.doc_freq[term] = len(self.term_doc_freq[term])

    def search(self, query: str, top_k: int = 10) -> list[RetrievalResult]:
        """
        Search using BM25.

        Args:
            query: Search query
            top_k: Number of results

        Returns:
            List of retrieval results
        """
        if not self.documents:
            return []

        if not self.doc_freq:
            self.build_index()

        query_tokens = self._tokenize(query)
        doc_count = len(self.documents)

        results = []

        for doc_id, doc in self.documents.items():
            score = 0.0
            doc_length = self.doc_lengths.get(doc_id, 0)

            for term in query_tokens:
                if term in self.term_doc_freq:
                    tf = self.term_doc_freq[term].get(doc_id, 0)
                    df = self.doc_freq.get(term, 0)

                    # BM25 scoring
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (
                        1 - self.b + self.b * doc_length / self.avg_doc_length
                    )

                    idf = math.log((doc_count - df + 0.5) / (df + 0.5) + 1)

                    score += idf * numerator / denominator

            results.append(
                RetrievalResult(
                    doc_id=doc_id,
                    score=score,
                    document=doc,
                )
            )

        results.sort(key=lambda r: r.score, reverse=True)
        return results[:top_k]


def main():
    """CLI for vector retrieval."""
    import sys

    retrieval = VectorRetrieval()

    # Add some sample documents
    docs = [
        Document("1", "The quick brown fox jumps over the lazy dog"),
        Document("2", "A fast fox and a lazy dog in the forest"),
        Document("3", "Machine learning is a subset of artificial intelligence"),
        Document("4", "Deep learning uses neural networks with many layers"),
        Document("5", "Natural language processing deals with text data"),
    ]

    for doc in docs:
        retrieval.add_document(doc)

    retrieval.build_index()

    if len(sys.argv) < 2:
        print("Usage: vector_retrieval.py <query>")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    results = retrieval.search(query)

    print(f"Query: {query}")
    print(f"\nResults:")
    for r in results:
        print(f"  {r.doc_id}: {r.score:.4f} - {r.document.content[:50]}...")


if __name__ == "__main__":
    main()
