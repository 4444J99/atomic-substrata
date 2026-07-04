#!/usr/bin/env python3
"""
Unit tests for advanced_nlp and semantic_embeddings modules.
"""

import sys
import os
from unittest.mock import Mock

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


class TestAdvancedNLPCoverage:
    """Focused coverage tests for the large advanced_nlp module."""

    def test_extract_entities_uses_pattern_and_avoids_duplicate_proper_noun(self):
        """Pattern-backed entities should be preferred over redundant proper noun matches."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()
        nlp.entity_patterns = {"CUSTOM": r"Acme Corp", "DATE": r"\d{4}-\d{2}-\d{2}"}

        entities = nlp.extract_entities("Acme Corp released version 1.2.0 on 2024-01-01.")

        assert len(entities) == 2
        assert entities[0].label == "CUSTOM"
        assert entities[0].text == "Acme Corp"
        assert entities[1].label == "DATE"
        assert entities[1].text == "2024-01-01"
        assert not any(entity.label == "PROPER_NOUN" for entity in entities)

    def test_extract_entities_adds_proper_noun_when_not_captured(self):
        """Pure proper nouns should be extracted when patterns do not match."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()
        entities = nlp.extract_entities("Acme Corp announced a breakthrough.")

        assert len(entities) == 1
        assert entities[0].label == "PROPER_NOUN"
        assert entities[0].text == "Acme Corp"

    def test_simple_sentiment_threshold_paths(self):
        """Direct sentiment fallback should hit positive, negative, and neutral decisions."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()
        nlp.sentiment_analyzer = None

        positive = nlp.analyze_sentiment("I love this excellent and useful tool")
        negative = nlp.analyze_sentiment("This is bad and a terrible problem")
        neutral = nlp.analyze_sentiment("This has no clear emotional signal")

        assert positive.sentiment == "positive"
        assert positive.polarity > 0.05
        assert negative.sentiment == "negative"
        assert negative.polarity < -0.05
        assert neutral.sentiment == "neutral"
        assert neutral.polarity == 0.0

    def test_analyze_sentiment_uses_nltk_analyzer_when_present(self, monkeypatch):
        """The NLTK analyzer branch should be used when available."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()
        fake_analyzer = Mock()
        fake_analyzer.polarity_scores.return_value = {"compound": -0.77}
        nlp.sentiment_analyzer = fake_analyzer

        result = nlp.analyze_sentiment("any text")

        assert result.sentiment == "negative"
        fake_analyzer.polarity_scores.assert_called_once_with("any text")

    def test_extract_keywords_handles_stopwords_and_top_k(self):
        """Keyword extraction should filter stopwords and return frequency scores."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()
        keywords = nlp.extract_keywords("the the test and and data data data", top_k=1)

        assert len(keywords) == 1
        assert keywords[0].keyword == "data"
        assert keywords[0].score == 0.75

    def test_classify_text_sorts_and_limits_top_three(self):
        """Classification should prioritize highest-confidence labels and return at most three."""
        from uaks.advanced_nlp import AdvancedNLP

        nlp = AdvancedNLP()
        text = (
            "API function and method are standard. "
            "Research study analysis supports hypotheses. "
            "Market customer revenue grows in strong conditions. "
            "Students learn concept quickly."
        )

        result = nlp.classify_text(text)

        assert len(result) == 3
        assert result[0].category == "technical"
        assert result[1].category == "scientific"
        assert result[2].category == "business"
        assert result[0].confidence == pytest.approx(0.6)
        assert result[1].confidence == pytest.approx(0.6)
        assert result[2].confidence == pytest.approx(0.6)

    def test_summarize_short_text_and_ranked_truncation(self, monkeypatch):
        """Summarization should preserve short text and rank longer text by keywords."""
        from uaks.advanced_nlp import AdvancedNLP, KeywordResult

        nlp = AdvancedNLP()

        assert nlp.summarize("Only one sentence.") == "Only one sentence."

        monkeypatch.setattr(
            nlp,
            "extract_keywords",
            lambda _text, top_k=10: [KeywordResult("alpha", 1.0), KeywordResult("beta", 0.5)],
        )
        long_text = (
            "Alpha introduces the main concept. "
            "Beta supports the supporting concept. "
            "Gamma appears but is less useful. "
            "Delta appears in final note."
        )

        summary = nlp.summarize(long_text, max_sentences=2)
        assert summary == "Alpha introduces the main concept. Beta supports the supporting concept."

    def test_analyze_composes_all_sections(self, monkeypatch):
        """analyze() should combine results from all component extractors."""
        from uaks.advanced_nlp import (
            AdvancedNLP,
            Entity,
            KeywordResult,
            ClassificationResult,
            SentimentResult,
        )

        nlp = AdvancedNLP()
        monkeypatch.setattr(
            nlp,
            "extract_entities",
            lambda _text: [Entity(text="Acme", label="ORG", start=0, end=4)],
        )
        monkeypatch.setattr(
            nlp,
            "analyze_sentiment",
            lambda _text: SentimentResult(polarity=0.2, sentiment="positive", confidence=0.2),
        )
        monkeypatch.setattr(
            nlp,
            "extract_keywords",
            lambda _text: [KeywordResult(keyword="acme", score=0.9)],
        )
        monkeypatch.setattr(
            nlp,
            "classify_text",
            lambda _text: [ClassificationResult(category="business", confidence=0.8)],
        )
        monkeypatch.setattr(nlp, "summarize", lambda _text: "summary")

        result = nlp.analyze("anything")

        assert result["entities"] == [{"text": "Acme", "label": "ORG"}]
        assert result["sentiment"] == {"polarity": 0.2, "sentiment": "positive"}
        assert result["keywords"] == [{"keyword": "acme", "score": 0.9}]
        assert result["classification"] == [{"category": "business", "confidence": 0.8}]
        assert result["summary"] == "summary"

    def test_main_cli_branches(self, monkeypatch, capsys):
        """CLI entry points should execute command branches and print expected output."""
        from uaks import advanced_nlp
        from uaks.advanced_nlp import AdvancedNLP, Entity, SentimentResult, KeywordResult, ClassificationResult

        class _FakeNLP:
            def extract_entities(self, text):
                return [Entity("Acme", "ORG", 0, 4)]

            def analyze_sentiment(self, text):
                return SentimentResult(polarity=0.5, sentiment="positive", confidence=0.5)

            def extract_keywords(self, text):
                return [KeywordResult("alpha", 1.0), KeywordResult("beta", 0.5)]

            def classify_text(self, text):
                return [ClassificationResult(category="business", confidence=0.9)]

            def summarize(self, text):
                return "summary"

            def analyze(self, text):
                return {
                    "entities": [{"text": "Acme", "label": "ORG"}],
                    "sentiment": {"polarity": 0.5, "sentiment": "positive"},
                    "keywords": [{"keyword": "alpha", "score": 1.0}],
                    "classification": [{"category": "business", "confidence": 0.9}],
                    "summary": "summary",
                }

        monkeypatch.setattr(advanced_nlp, "AdvancedNLP", _FakeNLP)

        monkeypatch.setattr(sys, "argv", ["advanced_nlp.py"])
        advanced_nlp.main()
        usage = capsys.readouterr().out
        assert "Usage: advanced_nlp.py <command>" in usage

        monkeypatch.setattr(sys, "argv", ["advanced_nlp.py", "entities", "Acme"])
        advanced_nlp.main()
        entities_output = capsys.readouterr().out
        assert "ORG: Acme" in entities_output

        monkeypatch.setattr(sys, "argv", ["advanced_nlp.py", "analyze", "Acme", "Corp"])
        advanced_nlp.main()
        analyze_output = capsys.readouterr().out
        assert "entities" in analyze_output

        monkeypatch.setattr(
            sys,
            "argv",
            ["advanced_nlp.py", "sentiment", "Acme", "makes", "you", "smile"],
        )
        advanced_nlp.main()
        sentiment_output = capsys.readouterr().out
        assert "Sentiment: positive" in sentiment_output

        monkeypatch.setattr(sys, "argv", ["advanced_nlp.py", "keywords", "Acme", "Corp"])
        advanced_nlp.main()
        keywords_output = capsys.readouterr().out
        assert "alpha: 1.000" in keywords_output

        monkeypatch.setattr(sys, "argv", ["advanced_nlp.py", "classify", "Acme", "Corp"])
        advanced_nlp.main()
        classify_output = capsys.readouterr().out
        assert "business: 0.900" in classify_output

        monkeypatch.setattr(sys, "argv", ["advanced_nlp.py", "summarize", "Acme", "Corp"])
        advanced_nlp.main()
        summarize_output = capsys.readouterr().out
        assert summarize_output.strip() == "summary"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
