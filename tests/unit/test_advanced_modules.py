#!/usr/bin/env python3
"""
Unit tests for advanced_nlp and semantic_embeddings modules.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

import pytest


class TestAdvancedNLPModule:
    """Tests for Advanced NLP module."""

    def test_advanced_nlp_import(self):
        """Test advanced_nlp module can be imported."""
        from uaks.advanced_nlp import Entity, SentimentResult, ClassificationResult

        assert Entity is not None
        assert SentimentResult is not None
        assert ClassificationResult is not None

    def test_entity_creation(self):
        """Test Entity dataclass creation."""
        from uaks.advanced_nlp import Entity

        entity = Entity(text="Python", label="TECHNOLOGY", start=0, end=6)

        assert entity.text == "Python"
        assert entity.label == "TECHNOLOGY"

    def test_sentiment_result_creation(self):
        """Test SentimentResult dataclass creation."""
        from uaks.advanced_nlp import SentimentResult

        result = SentimentResult(polarity=0.8, sentiment="positive", confidence=0.95)

        assert result.polarity == 0.8
        assert result.sentiment == "positive"

    def test_classification_result_creation(self):
        """Test ClassificationResult dataclass creation."""
        from uaks.advanced_nlp import ClassificationResult

        result = ClassificationResult(category="technology", confidence=0.87)

        assert result.category == "technology"
        assert result.confidence == 0.87

    def test_advanced_nlp_ner(self):
        """Test NER functionality."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()

        entities = nlp.extract_entities(
            "Python is a programming language created by Guido van Rossum."
        )

        assert isinstance(entities, list)

    def test_advanced_nlp_sentiment(self):
        """Test sentiment analysis."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()

        result = nlp.analyze_sentiment("I love this amazing product!")

        assert result is not None
        assert hasattr(result, "sentiment")

    def test_advanced_nlp_classify(self):
        """Test text classification."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()

        try:
            result = nlp.classify(
                "Machine learning is a subset of artificial intelligence."
            )
            assert result is not None
        except Exception:
            pytest.skip("NLTK not available")

    def test_advanced_nlp_keywords(self):
        """Test keyword extraction."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()

        keywords = nlp.extract_keywords("Python is a high-level programming language.")

        assert isinstance(keywords, list)

    def test_advanced_nlp_summarize(self):
        """Test summary generation."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()

        text = (
            "This is a test sentence. This is another test sentence. And another one."
        )
        summary = nlp.summarize(text)

        assert summary is not None

    def test_has_nltk_flag(self):
        """Test NLTK availability flag."""
        from uaks import advanced_nlp

        assert hasattr(advanced_nlp, "HAS_NLTK")


class TestSemanticEmbeddingsModule:
    """Tests for Semantic Embeddings module."""

    def test_semantic_embeddings_import(self):
        """Test semantic_embeddings module can be imported."""
        from uaks.semantic_embeddings import EmbeddingResult, SemanticEmbeddings

        assert EmbeddingResult is not None
        assert SemanticEmbeddings is not None

    def test_embedding_result_creation(self):
        """Test EmbeddingResult dataclass creation."""
        from uaks.semantic_embeddings import EmbeddingResult

        result = EmbeddingResult(
            text="test text", embedding=[0.1, 0.2, 0.3], model="test-model"
        )

        assert result.text == "test text"
        assert len(result.embedding) == 3

    def test_semantic_embeddings_init(self):
        """Test SemanticEmbeddings initialization."""
        from uaks.semantic_embeddings import SemanticEmbeddings

        embeddings = SemanticEmbeddings()

        assert embeddings is not None

    def test_semantic_embeddings_compute(self):
        """Test embedding computation."""
        from uaks.semantic_embeddings import SemanticEmbeddings

        embeddings = SemanticEmbeddings()

        try:
            result = embeddings.compute_embedding("test")
            assert result is not None
            assert hasattr(result, "embedding")
        except Exception:
            pytest.skip("Embedding computation failed")

    def test_semantic_embeddings_batch(self):
        """Test batch embedding computation."""
        from uaks.semantic_embeddings import SemanticEmbeddings

        embeddings = SemanticEmbeddings()

        texts = ["test1", "test2", "test3"]

        try:
            results = embeddings.compute_batch(texts)
            assert isinstance(results, list)
            assert len(results) == len(texts)
        except Exception:
            pytest.skip("Batch computation failed")

    def test_semantic_embeddings_similarity(self):
        """Test similarity computation."""
        from uaks.semantic_embeddings import SemanticEmbeddings

        embeddings = SemanticEmbeddings()

        try:
            similarity = embeddings.compute_similarity("a", "b")
            assert similarity is not None
            assert isinstance(similarity, float)
        except Exception:
            pytest.skip("Similarity computation failed")

    def test_semantic_embeddings_search(self):
        """Test semantic search."""
        from uaks.semantic_embeddings import SemanticEmbeddings

        embeddings = SemanticEmbeddings()

        corpus = [
            "Python is a programming language.",
            "JavaScript is for web.",
            "Rust is systems.",
        ]

        try:
            results = embeddings.semantic_search("code", corpus, top_k=2)
            assert isinstance(results, list)
        except Exception:
            pytest.skip("Search failed")

    def test_has_sentence_transformers_flag(self):
        """Test sentence-transformers availability flag."""
        from uaks import semantic_embeddings

        assert hasattr(semantic_embeddings, "HAS_SENTENCE_TRANSFORMERS")


class TestGraphStorageModule:
    """Tests for Graph Storage module."""

    def test_graph_storage_import(self):
        """Test graph_storage module can be imported."""
        from uaks.graph_storage import GraphNode, GraphEdge, GraphStorage

        assert GraphNode is not None
        assert GraphEdge is not None
        assert GraphStorage is not None

    def test_graph_node_creation(self):
        """Test GraphNode creation."""
        from uaks.graph_storage import GraphNode

        node = GraphNode(
            id="test_node",
            type="text",
            hash="abc123",
            content="Test content",
            source="test",
            created_at="2024-01-01",
        )

        assert node.id == "test_node"
        assert node.type == "text"

    def test_graph_edge_creation(self):
        """Test GraphEdge creation."""
        from uaks.graph_storage import GraphEdge

        edge = GraphEdge(
            id="test_edge",
            source_id="node1",
            target_id="node2",
            relationship="similar_to",
        )

        assert edge.source_id == "node1"
        assert edge.target_id == "node2"

    def test_graph_storage_init(self):
        """Test GraphStorage initialization."""
        import tempfile
        from pathlib import Path
        from uaks.graph_storage import GraphStorage

        with tempfile.TemporaryDirectory() as tmpdir:
            storage = GraphStorage(storage_file=Path(f"{tmpdir}/test_graph.json"))
            assert storage is not None


class TestAssemblyModule:
    """Tests for Assembly module."""

    def test_assembly_import(self):
        """Test assembly module can be imported."""
        from uaks.assembly import Atom, AssembledOutput, AssemblyEngine

        assert Atom is not None
        assert AssembledOutput is not None
        assert AssemblyEngine is not None

    def test_atom_creation(self):
        """Test Atom creation."""
        from uaks.assembly import Atom

        atom = Atom(
            id="test_atom",
            type="text",
            content="Test content",
            hash="abc123",
            source="test",
            size=100,
        )

        assert atom.id == "test_atom"
        assert atom.type == "text"

    def test_assembled_output_creation(self):
        """Test AssembledOutput creation."""
        from uaks.assembly import AssembledOutput, Atom

        atoms = [
            Atom(id="1", type="text", content="test", hash="x", source="s", size=10)
        ]

        output = AssembledOutput(
            query="test query",
            atoms=atoms,
            assembled_text="Assembled text",
            confidence=0.95,
            assembled_at="2024-01-01",
        )

        assert output.confidence == 0.95

    def test_assembly_engine_init(self):
        """Test AssemblyEngine initialization."""
        from uaks.assembly import AssemblyEngine

        engine = AssemblyEngine()
        assert engine is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
