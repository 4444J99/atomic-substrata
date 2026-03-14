#!/usr/bin/env python3
"""
Semantic Embeddings Module
=========================
Provides semantic embeddings for atoms using sentence transformers.

Features:
- Sentence transformer embeddings
- Fallback to TF-IDF
- Semantic similarity search
- Batch processing
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    from sentence_transformers import SentenceTransformer

    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False

from vector_retrieval import VectorRetrieval, Document


@dataclass
class EmbeddingResult:
    """Result of embedding computation."""

    text: str
    embedding: list[float]
    model: str


class SemanticEmbeddings:
    """
    Semantic embeddings using sentence transformers.

    Falls back to TF-IDF if sentence-transformers is not available.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = None
        self.embeddings_cache = {}

        if HAS_SENTENCE_TRANSFORMERS:
            try:
                self.model = SentenceTransformer(model_name)
                self.use_transformers = True
            except Exception as e:
                print(f"Warning: Could not load model '{model_name}': {e}")
                self.use_transformers = False
        else:
            self.use_transformers = False

    def embed_text(self, text: str) -> EmbeddingResult:
        """
        Compute embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            EmbeddingResult with embedding vector
        """
        if self.use_transformers and self.model:
            embedding = self.model.encode(text).tolist()
            return EmbeddingResult(
                text=text, embedding=embedding, model=self.model_name
            )
        else:
            # Fallback to simple hash-based embedding
            return EmbeddingResult(
                text=text, embedding=self._simple_embedding(text), model="simple_hash"
            )

    def embed_batch(self, texts: list[str]) -> list[EmbeddingResult]:
        """
        Compute embeddings for multiple texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of EmbeddingResults
        """
        if self.use_transformers and self.model:
            embeddings = self.model.encode(texts).tolist()
            return [
                EmbeddingResult(text=t, embedding=e, model=self.model_name)
                for t, e in zip(texts, embeddings)
            ]
        else:
            return [self.embed_text(t) for t in texts]

    def _simple_embedding(self, text: str, dim: int = 384) -> list[float]:
        """
        Simple fallback embedding using character frequencies.

        Args:
            text: Text to embed
            dim: Embedding dimension

        Returns:
            Embedding vector
        """
        import math

        # Initialize vector
        embedding = [0.0] * dim

        # Use character frequencies for simple embedding
        for i, char in enumerate(text):
            idx = (ord(char) * (i + 1)) % dim
            embedding[idx] += 1

        # Normalize
        magnitude = math.sqrt(sum(x * x for x in embedding))
        if magnitude > 0:
            embedding = [x / magnitude for x in embedding]

        return embedding

    def cosine_similarity(self, emb1: list[float], emb2: list[float]) -> float:
        """Compute cosine similarity between embeddings."""
        dot_product = sum(a * b for a, b in zip(emb1, emb2))
        mag1 = sum(a * a for a in emb1) ** 0.5
        mag2 = sum(b * b for b in emb2) ** 0.5

        if mag1 == 0 or mag2 == 0:
            return 0.0

        return dot_product / (mag1 * mag2)

    def semantic_search(
        self, corpus: list[str], query: str, top_k: int = 5
    ) -> list[tuple[int, float]]:
        """
        Perform semantic search.

        Args:
            corpus: List of texts to search
            query: Query text
            top_k: Number of results

        Returns:
            List of (index, similarity) tuples
        """
        # Compute query embedding
        query_result = self.embed_text(query)

        # Compute corpus embeddings
        corpus_results = self.embed_batch(corpus)

        # Compute similarities
        similarities = []
        for i, corpus_result in enumerate(corpus_results):
            sim = self.cosine_similarity(
                query_result.embedding, corpus_result.embedding
            )
            similarities.append((i, sim))

        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:top_k]


class HybridRetrieval:
    """
    Combines semantic embeddings with keyword search.

    Provides better results by combining both approaches.
    """

    def __init__(self, semantic_weight: float = 0.7):
        self.embeddings = SemanticEmbeddings()
        self.vector_retrieval = VectorRetrieval()
        self.semantic_weight = semantic_weight
        self.keyword_weight = 1.0 - semantic_weight

        self.corpus_embeddings: list[list[float]] = []
        self.corpus_texts: list[str] = []

    def index_corpus(self, documents: list[Document]):
        """Index documents for hybrid search."""
        # Store texts
        self.corpus_texts = [doc.content for doc in documents]

        # Compute semantic embeddings
        self.corpus_embeddings = []
        for doc in documents:
            result = self.embeddings.embed_text(doc.content)
            self.corpus_embeddings.append(result.embedding)

        # Also index in vector retrieval for keyword search
        for doc in documents:
            self.vector_retrieval.add_document(doc)

        self.vector_retrieval.build_index()

    def search(self, query: str, top_k: int = 5) -> list[tuple[int, float, str]]:
        """
        Hybrid search combining semantic and keyword matching.

        Args:
            query: Search query
            top_k: Number of results

        Returns:
            List of (index, score, method) tuples
        """
        # Semantic search
        semantic_results = self.embeddings.semantic_search(
            self.corpus_texts,
            query,
            top_k * 2,  # Get more for blending
        )

        # Keyword search
        keyword_results = self.vector_retrieval.search(query, top_k * 2)

        # Build index maps
        semantic_scores = {idx: score for idx, score in semantic_results}
        keyword_scores = {}
        for kr in keyword_results:
            # Find index by doc_id
            for i, doc in enumerate(self.corpus_texts):
                if f"doc_{i}" in str(kr.document.id) if kr.document else False:
                    keyword_scores[i] = kr.score
                    break

        # Combine scores
        combined = {}
        all_indices = set(semantic_scores.keys()) | set(keyword_scores.keys())

        for idx in all_indices:
            sem_score = semantic_scores.get(idx, 0.0)
            key_score = keyword_scores.get(idx, 0.0)

            combined[idx] = (
                self.semantic_weight * sem_score + self.keyword_weight * key_score
            )

        # Sort by combined score
        results = sorted(combined.items(), key=lambda x: x[1], reverse=True)

        return [(idx, score, "hybrid") for idx, score in results[:top_k]]


def main():
    """CLI for semantic embeddings."""
    import sys

    embeddings = SemanticEmbeddings()

    if len(sys.argv) < 2:
        print("Usage: embeddings.py <text>")
        print(
            f"Model: {embeddings.model_name if embeddings.use_transformers else 'simple (fallback)'}"
        )
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    result = embeddings.embed_text(text)

    print(f"Text: {text[:50]}...")
    print(f"Model: {result.model}")
    print(f"Embedding dimension: {len(result.embedding)}")
    print(f"First 5 values: {result.embedding[:5]}")


if __name__ == "__main__":
    main()
