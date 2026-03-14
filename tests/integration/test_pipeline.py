#!/usr/bin/env python3
"""
Integration tests for UAKS pipeline.
Tests the complete flow from source intake to assembly.
"""

import json
import os
import sys
import tempfile
from pathlib import Path

import pytest

# Add src to path
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))
scripts_path = Path(__file__).parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_path))

from uaks.text_refinery import TextRefinery
from uaks.code_refinery import CodeRefinery
from uaks.source_intake import SourceIntake
from uaks.vector_retrieval import VectorRetrieval, Document
from assembly import AssemblyEngine
from graph_storage import GraphStorage, GraphNode


class TestPipelineIntegration:
    """Integration tests for the complete UAKS pipeline."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for tests."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    @pytest.fixture
    def sample_texts(self):
        """Sample texts for testing."""
        return [
            "The quick brown fox jumps over the lazy dog.",
            "Machine learning is a subset of artificial intelligence.",
            "Python is a high-level programming language.",
            "Knowledge graphs store entities and relationships.",
            "Natural language processing deals with text.",
        ]

    @pytest.fixture
    def sample_code(self):
        """Sample code for testing."""
        return '''
def hello(name):
    """Return a greeting."""
    return f"Hello, {name}!"

class Greeter:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return hello(self.name)
'''

    def test_full_text_pipeline(self, temp_dir, sample_texts):
        """Test complete text processing pipeline."""
        # Source Intake
        intake = SourceIntake()

        # Create test files
        test_files = []
        for i, text in enumerate(sample_texts):
            filepath = temp_dir / f"test_{i}.txt"
            filepath.write_text(text)
            test_files.append(str(filepath))

        # Ingest files
        sources = []
        for fp in test_files:
            source = intake.ingest_file(fp)
            sources.append(source)

        assert len(sources) == len(sample_texts)
        assert all(s.source_type == "file" for s in sources)

        # Refine texts
        refinery = TextRefinery()
        atoms = []
        for source in sources:
            atom = refinery.refine(source.content, source.path)
            atoms.append(atom)

        assert len(atoms) == len(sample_texts)
        assert all(atom.tokens for atom in atoms)

        # Build vector index
        retrieval = VectorRetrieval()
        for atom in atoms:
            doc = Document(atom.id, atom.content)
            retrieval.add_document(doc)

        retrieval.build_index()

        # Search
        results = retrieval.search("machine learning", top_k=3)

        assert len(results) <= 3
        assert all(r.score >= 0 for r in results)

    def test_full_code_pipeline(self, temp_dir, sample_code):
        """Test complete code processing pipeline."""
        # Write code to file
        code_file = temp_dir / "test_code.py"
        code_file.write_text(sample_code)

        # Source Intake
        intake = SourceIntake()
        source = intake.ingest_file(str(code_file))

        assert source.source_type == "file"

        # Code Refinery
        refinery = CodeRefinery()
        atom = refinery.refine(source.content, str(code_file), str(code_file))

        assert atom.language == "python"
        assert len(atom.functions) > 0
        assert len(atom.classes) > 0

    def test_assembly_with_refined_atoms(self, temp_dir, sample_texts):
        """Test assembly using refined atoms."""
        # Create pipeline state
        state_file = temp_dir / "pipeline_state.json"
        state = {
            "atoms": {
                "text": [
                    {
                        "id": f"atom_{i}",
                        "type": "text",
                        "content": text,
                        "hash": f"hash_{i}",
                        "source": f"source_{i}",
                        "size": len(text),
                        "status": "refined",
                    }
                    for i, text in enumerate(sample_texts)
                ],
                "code": [],
            }
        }

        with open(state_file, "w") as f:
            json.dump(state, f)

        # Test assembly
        original_cwd = os.getcwd()
        os.chdir(temp_dir)

        try:
            engine = AssemblyEngine(state_file)
            engine.load_atoms()
            engine.build_index()

            result = engine.assemble("programming language", top_k=3)

            assert result.query == "programming language"
            assert len(result.atoms) <= 3
            assert result.confidence >= 0
        finally:
            os.chdir(original_cwd)

    def test_graph_storage_integration(self, temp_dir, sample_texts):
        """Test graph storage with atoms."""
        graph_file = temp_dir / "graph.json"
        graph = GraphStorage(graph_file)

        # Add atoms as nodes
        for i, text in enumerate(sample_texts[:3]):
            node = GraphNode(
                id=f"node_{i}",
                type="text",
                hash=f"hash_{i}",
                content=text,
                source=f"source_{i}",
                created_at="2024-01-01",
            )
            graph.add_node(node)

        # Verify nodes
        assert len(graph.nodes) == 3

        # Add edges (references)
        for i in range(len(sample_texts[:3]) - 1):
            from graph_storage import GraphEdge

            edge = GraphEdge(
                id=f"edge_{i}",
                source_id=f"node_{i}",
                target_id=f"node_{i + 1}",
                relationship="references",
            )
            graph.add_edge(edge)

        assert len(graph.edges) == 2

        # Test traversal
        results = graph.traverse("node_0", max_depth=2)

        assert 0 in results
        assert 1 in results

    def test_mixed_atom_types(self, temp_dir, sample_texts, sample_code):
        """Test pipeline with mixed text and code atoms."""
        state_file = temp_dir / "pipeline_state.json"
        state = {
            "atoms": {
                "text": [
                    {
                        "id": "text_1",
                        "type": "text",
                        "content": sample_texts[0],
                        "hash": "hash1",
                        "source": "source1",
                        "size": len(sample_texts[0]),
                        "status": "refined",
                    }
                ],
                "code": [
                    {
                        "id": "code_1",
                        "type": "code",
                        "content": sample_code,
                        "hash": "hash2",
                        "source": "source2",
                        "size": len(sample_code),
                        "status": "refined",
                    }
                ],
            }
        }

        with open(state_file, "w") as f:
            json.dump(state, f)

        original_cwd = os.getcwd()
        os.chdir(temp_dir)

        try:
            engine = AssemblyEngine(state_file)
            engine.load_atoms()

            assert len(engine.atoms) == 2

            text_atoms = [a for a in engine.atoms if a.type == "text"]
            code_atoms = [a for a in engine.atoms if a.type == "code"]

            assert len(text_atoms) == 1
            assert len(code_atoms) == 1
        finally:
            os.chdir(original_cwd)

    def test_pipeline_error_handling(self, temp_dir):
        """Test pipeline error handling."""
        # Test with empty state
        state_file = temp_dir / "empty_state.json"
        state = {"atoms": {"text": [], "code": []}}

        with open(state_file, "w") as f:
            json.dump(state, f)

        original_cwd = os.getcwd()
        os.chdir(temp_dir)

        try:
            engine = AssemblyEngine(state_file)
            engine.load_atoms()
            engine.build_index()

            result = engine.assemble("test query")

            assert result.confidence == 0.0
            assert "No atoms found" in result.assembled_text
        finally:
            os.chdir(original_cwd)

    def test_deduplication_workflow(self, temp_dir):
        """Test deduplication in pipeline."""
        # Create state with duplicate content
        state_file = temp_dir / "pipeline_state.json"
        state = {
            "atoms": {
                "text": [
                    {
                        "id": "atom_1",
                        "type": "text",
                        "content": "Same content",
                        "hash": "same_hash",
                        "source": "source1",
                        "size": 12,
                        "status": "raw",
                    },
                    {
                        "id": "atom_2",
                        "type": "text",
                        "content": "Same content",
                        "hash": "same_hash",
                        "source": "source2",
                        "size": 12,
                        "status": "raw",
                    },
                    {
                        "id": "atom_3",
                        "type": "text",
                        "content": "Different content",
                        "hash": "different_hash",
                        "source": "source3",
                        "size": 16,
                        "status": "raw",
                    },
                ],
                "code": [],
            }
        }

        with open(state_file, "w") as f:
            json.dump(state, f)

        # Test in graph storage
        graph_file = temp_dir / "graph.json"
        graph = GraphStorage(graph_file)

        from graph_storage import GraphNode, GraphEdge

        for atom in state["atoms"]["text"]:
            node = GraphNode(
                id=atom["id"],
                type=atom["type"],
                hash=atom["hash"],
                content=atom["content"],
                source=atom["source"],
                created_at="2024-01-01",
            )
            graph.add_node(node)

        # Find duplicates by hash
        hash_groups = {}
        for node in graph.nodes.values():
            if node.hash not in hash_groups:
                hash_groups[node.hash] = []
            hash_groups[node.hash].append(node.id)

        # Should find same_hash group with 2 nodes
        assert "same_hash" in hash_groups
        assert len(hash_groups["same_hash"]) == 2
        assert "different_hash" in hash_groups
        assert len(hash_groups["different_hash"]) == 1


class TestEndToEnd:
    """End-to-end workflow tests."""

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for tests."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def test_complete_workflow(self, temp_dir):
        """Test complete UAKS workflow."""
        # Step 1: Create source files
        sources_dir = temp_dir / "sources"
        sources_dir.mkdir()

        (sources_dir / "doc1.txt").write_text("Python is a programming language.")
        (sources_dir / "doc2.txt").write_text("Machine learning uses algorithms.")
        (sources_dir / "code.py").write_text("def foo(): return 42")

        # Step 2: Intake
        intake = SourceIntake()
        results = intake.ingest_directory(str(sources_dir))

        assert len(results) == 3

        # Step 3: Refine
        refinery = TextRefinery()
        code_refinery = CodeRefinery()

        atoms = []
        for source in results:
            if source.source_type == "file" and source.path.endswith(".py"):
                atom = code_refinery.refine(source.content, source.path, source.path)
            else:
                atom = refinery.refine(source.content, source.path)
            atoms.append(atom)

        assert len(atoms) == 3

        # Step 4: Build retrieval index
        retrieval = VectorRetrieval()
        for atom in atoms:
            doc = Document(atom.id, atom.content)
            retrieval.add_document(doc)

        retrieval.build_index()

        # Step 5: Search
        results = retrieval.search("programming", top_k=2)

        assert len(results) <= 2

        # Step 6: Graph storage
        graph_file = temp_dir / "graph.json"
        graph = GraphStorage(graph_file)

        from graph_storage import GraphNode

        for atom in atoms:
            atom_type = (
                atom.type
                if hasattr(atom, "type")
                else (atom.language if hasattr(atom, "language") else "unknown")
            )
            atom_source = atom.source if hasattr(atom, "source") else "unknown"

            node = GraphNode(
                id=atom.id,
                type=atom_type,
                hash=atom.hash,
                content=atom.content[:100],
                source=atom_source,
                created_at="2024-01-01",
            )
            graph.add_node(node)

        assert len(graph.nodes) == 3

        stats = graph.get_stats()
        assert stats["total_nodes"] == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
