#!/usr/bin/env python3
"""
Tests for UAKS scripts.
"""

import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Add scripts to path
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from assembly import AssemblyEngine, Atom, cosine_similarity, SimpleVectorizer
from graph_storage import GraphStorage, GraphNode, GraphEdge


class TestVectorizer:
    """Tests for SimpleVectorizer."""

    def test_tokenize(self):
        """Test tokenization."""
        vec = SimpleVectorizer()
        tokens = vec._tokenize("Hello World! Test 123.")
        assert "hello" in tokens
        assert "world" in tokens
        assert "test" in tokens

    def test_fit_transform(self):
        """Test fit_transform."""
        vec = SimpleVectorizer()
        texts = ["hello world", "world of code", "code hello"]
        vectors = vec.fit_transform(texts)

        assert len(vectors) == 3
        assert all(len(v) > 0 for v in vectors)

    def test_transform(self):
        """Test transform with fitted data."""
        vec = SimpleVectorizer()
        texts = ["hello world", "world of code"]
        vec.fit_transform(texts)

        new_texts = ["hello there"]
        vectors = vec.transform(new_texts)

        assert len(vectors) == 1
        assert len(vectors[0]) > 0


class TestCosineSimilarity:
    """Tests for cosine similarity."""

    def test_identical_vectors(self):
        """Test identical vectors return 1.0."""
        v = [1.0, 2.0, 3.0]
        assert cosine_similarity(v, v) == pytest.approx(1.0)

    def test_orthogonal_vectors(self):
        """Test orthogonal vectors return 0.0."""
        v1 = [1.0, 0.0]
        v2 = [0.0, 1.0]
        assert cosine_similarity(v1, v2) == pytest.approx(0.0)

    def test_opposite_vectors(self):
        """Test opposite vectors return -1.0."""
        v1 = [1.0, 2.0]
        v2 = [-1.0, -2.0]
        assert cosine_similarity(v1, v2) == pytest.approx(-1.0)


class TestAssemblyEngine:
    """Tests for AssemblyEngine."""

    @pytest.fixture
    def temp_state_file(self):
        """Create temporary state file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            state = {
                "atoms": {
                    "text": [
                        {
                            "id": "atom_001",
                            "type": "text",
                            "content": "This is about knowledge graphs",
                            "hash": "abc123",
                            "source": "test",
                            "size": 30,
                            "status": "raw",
                        },
                        {
                            "id": "atom_002",
                            "type": "text",
                            "content": "Code analysis is important",
                            "hash": "def456",
                            "source": "test",
                            "size": 30,
                            "status": "raw",
                        },
                    ],
                    "code": [],
                }
            }
            json.dump(state, f)
            temp_path = f.name

        yield Path(temp_path)

        # Cleanup
        os.unlink(temp_path)

    def test_load_atoms(self, temp_state_file):
        """Test loading atoms from state."""
        engine = AssemblyEngine(temp_state_file)
        engine.load_atoms()

        assert len(engine.atoms) == 2
        assert engine.atoms[0].id == "atom_001"

    def test_build_index(self, temp_state_file):
        """Test building search index."""
        engine = AssemblyEngine(temp_state_file)
        engine.load_atoms()
        engine.build_index()

        assert len(engine.vectors) == 2
        assert len(engine.vectors[0]) > 0

    def test_search(self, temp_state_file):
        """Test search functionality."""
        engine = AssemblyEngine(temp_state_file)
        engine.load_atoms()
        engine.build_index()

        results = engine.search("knowledge", top_k=2)

        assert len(results) <= 2
        assert all(isinstance(r[0], Atom) for r in results)
        assert all(isinstance(r[1], float) for r in results)

    def test_assemble(self, temp_state_file):
        """Test assemble functionality."""
        engine = AssemblyEngine(temp_state_file)

        result = engine.assemble("knowledge", top_k=2)

        assert result.query == "knowledge"
        assert result.confidence >= 0.0
        assert len(result.atoms) > 0


class TestGraphStorage:
    """Tests for GraphStorage."""

    @pytest.fixture
    def temp_graph_file(self):
        """Create temporary graph file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{}")
            temp_path = f.name

        yield Path(temp_path)

        # Cleanup
        if os.path.exists(temp_path):
            os.unlink(temp_path)

    def test_add_node(self, temp_graph_file):
        """Test adding a node."""
        graph = GraphStorage(temp_graph_file)

        node = GraphNode(
            id="node_001",
            type="text",
            hash="abc123",
            content="Test content",
            source="test",
            created_at="2024-01-01",
        )

        graph.add_node(node)

        assert "node_001" in graph.nodes

    def test_add_edge(self, temp_graph_file):
        """Test adding an edge."""
        graph = GraphStorage(temp_graph_file)

        # Add nodes first
        node1 = GraphNode("node_001", "text", "abc", "content1", "test", "2024-01-01")
        node2 = GraphNode("node_002", "text", "def", "content2", "test", "2024-01-01")
        graph.add_node(node1)
        graph.add_node(node2)

        # Add edge
        edge = GraphEdge(
            id="edge_001",
            source_id="node_001",
            target_id="node_002",
            relationship="references",
        )
        graph.add_edge(edge)

        assert "edge_001" in graph.edges

    def test_find_by_hash(self, temp_graph_file):
        """Test finding nodes by hash."""
        graph = GraphStorage(temp_graph_file)

        node = GraphNode(
            id="node_001",
            type="text",
            hash="abc123",
            content="Test",
            source="test",
            created_at="2024-01-01",
        )
        graph.add_node(node)

        results = graph.find_by_hash("abc123")
        assert len(results) == 1
        assert results[0].id == "node_001"

    def test_get_stats(self, temp_graph_file):
        """Test getting graph statistics."""
        graph = GraphStorage(temp_graph_file)

        node = GraphNode("node_001", "text", "abc", "content", "test", "2024-01-01")
        graph.add_node(node)

        stats = graph.get_stats()

        assert stats["total_nodes"] == 1
        assert stats["total_edges"] == 0
        assert stats["node_types"]["text"] == 1


class TestPipelineIntegration:
    """Integration tests for pipeline."""

    @pytest.fixture
    def repo_root(self):
        """Get repository root."""
        return Path(__file__).parent.parent.parent

    def test_state_file_exists(self, repo_root):
        """Test that pipeline state file exists."""
        state_file = repo_root / "data" / "pipeline_state.json"
        assert state_file.exists()

    def test_graph_storage_exists(self, repo_root):
        """Test that graph storage file exists."""
        graph_file = repo_root / "data" / "graph_storage.json"
        assert graph_file.exists()

    def test_pipeline_state_valid(self, repo_root):
        """Test that pipeline state is valid JSON."""
        state_file = repo_root / "data" / "pipeline_state.json"

        with open(state_file) as f:
            state = json.load(f)

        assert "atoms" in state
        assert "pipeline" in state
        assert "version" in state


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
