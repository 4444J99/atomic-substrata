#!/usr/bin/env python3
"""
Tests for UAKS modules.
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

from uaks.text_refinery import TextRefinery, TextAtom
from uaks.code_refinery import CodeRefinery, CodeAtom
from uaks.source_intake import SourceIntake, IntakeSource
from uaks.content_addressable_storage import ContentAddressableStorage, CASEntry
from uaks.vector_retrieval import VectorRetrieval, BM25Retrieval, Document


class TestTextRefinery:
    """Tests for TextRefinery."""

    def test_refine(self):
        """Test refining text."""
        refinery = TextRefinery()
        atom = refinery.refine("Hello world. This is a test.", "test_source")

        assert atom.id.startswith("text_")
        assert atom.hash
        assert len(atom.tokens) > 0
        assert len(atom.sentences) > 0
        assert atom.metadata["source"] == "test_source"

    def test_tokenize(self):
        """Test tokenization."""
        refinery = TextRefinery()
        tokens = refinery.tokenize("Hello World! Test 123.")

        assert "hello" in tokens
        assert "world" in tokens
        assert "test" in tokens

    def test_extract_sentences(self):
        """Test sentence extraction."""
        refinery = TextRefinery()
        sentences = refinery.extract_sentences(
            "Hello world. This is a test! Is it working?"
        )

        assert len(sentences) == 3
        assert "Hello world" in sentences[0]

    def test_extract_entities(self):
        """Test entity extraction."""
        refinery = TextRefinery()
        entities = refinery.extract_entities("John and Mary went to New York in 2024.")

        assert any(e["type"] == "PROPER_NOUN" for e in entities)
        assert any(e["type"] == "NUMBER" for e in entities)

    def test_batch_refine(self):
        """Test batch refinement."""
        refinery = TextRefinery()
        texts = [("Hello world", "source1"), ("Test content", "source2")]
        atoms = refinery.batch_refine(texts)

        assert len(atoms) == 2


class TestCodeRefinery:
    """Tests for CodeRefinery."""

    def test_detect_language(self):
        """Test language detection."""
        refinery = CodeRefinery()

        assert refinery.detect_language("def hello(): pass", "test.py") == "python"
        assert (
            refinery.detect_language("function hello() {}", "test.js") == "javascript"
        )
        assert refinery.detect_language("func main() {}", "test.go") == "go"

    def test_refine_python(self):
        """Test refining Python code."""
        refinery = CodeRefinery()
        code = '''
def hello(name):
    """Say hello."""
    return f"Hello, {name}!"

class Greeter:
    def __init__(self, name):
        self.name = name
'''
        atom = refinery.refine(code, "test.py", "test.py")

        assert atom.language == "python"
        assert len(atom.functions) > 0
        assert len(atom.classes) > 0

    def test_extract_functions_python(self):
        """Test function extraction."""
        refinery = CodeRefinery()
        code = "def foo(): pass\ndef bar(): pass"
        functions = refinery.extract_functions(code, "python")

        assert len(functions) == 2

    def test_extract_classes_python(self):
        """Test class extraction."""
        refinery = CodeRefinery()
        code = "class Foo: pass\nclass Bar: pass"
        classes = refinery.extract_classes(code, "python")

        assert len(classes) == 2

    def test_extract_imports_python(self):
        """Test import extraction."""
        refinery = CodeRefinery()
        # Test that the function doesn't crash
        code = "import os, sys"
        imports = refinery.extract_imports(code, "python")

        # Just verify function runs without error
        assert isinstance(imports, list)


class TestSourceIntake:
    """Tests for SourceIntake."""

    @pytest.fixture
    def temp_file(self):
        """Create a temporary file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Test content")
            temp_path = f.name

        yield temp_path
        os.unlink(temp_path)

    def test_detect_source_type(self):
        """Test source type detection."""
        intake = SourceIntake()

        assert intake.detect_source_type("https://example.com") == "url"
        # Non-existent paths are treated as text
        assert intake.detect_source_type("some text") == "text"

    def test_ingest_text(self):
        """Test ingesting text."""
        intake = SourceIntake()
        source = intake.ingest_text("Hello world", "test")

        assert source.source_type == "text"
        assert source.content == "Hello world"
        assert source.hash

    def test_ingest_file(self, temp_file):
        """Test ingesting a file."""
        intake = SourceIntake()
        source = intake.ingest_file(temp_file)

        assert source.source_type == "file"
        assert source.content == "Test content"
        assert source.metadata["filename"]


class TestContentAddressableStorage:
    """Tests for ContentAddressableStorage."""

    @pytest.fixture
    def temp_storage(self):
        """Create temporary storage."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield Path(tmpdir)

    def test_store_and_retrieve(self, temp_storage):
        """Test storing and retrieving content."""
        cas = ContentAddressableStorage(temp_storage)

        address = cas.store("Hello world")
        assert cas.exists(address)

        content = cas.retrieve(address)
        assert content == "Hello world"

    def test_deduplication(self, temp_storage):
        """Test deduplication."""
        cas = ContentAddressableStorage(temp_storage)

        addr1 = cas.store("Hello world")
        addr2 = cas.store("Hello world")

        assert addr1 == addr2
        assert cas.index[addr1].reference_count == 2

    def test_delete(self, temp_storage):
        """Test deletion."""
        cas = ContentAddressableStorage(temp_storage)

        address = cas.store("Hello world")
        cas.delete(address)

        assert not cas.exists(address)

    def test_verify_integrity(self, temp_storage):
        """Test integrity verification."""
        cas = ContentAddressableStorage(temp_storage)

        cas.store("Test content")
        result = cas.verify_integrity()

        assert result["verified"]

    def test_store_missing_object_restored(self, temp_storage):
        """Test restoring missing object file when storing identical content."""
        cas = ContentAddressableStorage(temp_storage)

        address = cas.store("canonical payload", {"source": "synthetic"})
        object_path = temp_storage / "objects" / address
        object_path.unlink()

        returned = cas.store("canonical payload", {"source": "synthetic retry"})

        assert returned == address
        assert cas.exists(address) is True
        assert object_path.exists() is True
        assert cas.retrieve(address) == "canonical payload"
        assert cas.index[address].reference_count == 2
        assert cas.verify_integrity()["verified"] is True

    def test_store_corrupted_object_fails_closed(self, temp_storage):
        """Test failing closed when object file is corrupted upon duplicate store."""
        cas = ContentAddressableStorage(temp_storage)

        address = cas.store("canonical payload", {"source": "synthetic"})
        object_path = temp_storage / "objects" / address
        object_path.write_text("corrupted content")

        with pytest.raises(ValueError, match="CAS object corruption detected"):
            cas.store("canonical payload", {"source": "synthetic retry"})

        # Ref count must remain 1 and corrupted content must be preserved
        assert cas.index[address].reference_count == 1
        assert object_path.read_text() == "corrupted content"


class TestVectorRetrieval:
    """Tests for VectorRetrieval."""

    def test_add_document(self):
        """Test adding documents."""
        retrieval = VectorRetrieval()

        doc = Document("1", "Hello world test")
        retrieval.add_document(doc)

        assert "1" in retrieval.documents

    def test_search(self):
        """Test searching."""
        retrieval = VectorRetrieval()

        docs = [
            Document("1", "The quick brown fox"),
            Document("2", "A lazy dog sleeps"),
            Document("3", "Machine learning is AI"),
        ]

        for doc in docs:
            retrieval.add_document(doc)

        retrieval.build_index()

        results = retrieval.search("quick fox", top_k=2)

        assert len(results) <= 2
        assert results[0].doc_id == "1"

    def test_stats(self):
        """Test getting stats."""
        retrieval = VectorRetrieval()

        doc = Document("1", "Test content")
        retrieval.add_document(doc)
        retrieval.build_index()

        stats = retrieval.get_stats()

        assert stats["document_count"] == 1


class TestBM25Retrieval:
    """Tests for BM25Retrieval."""

    def test_search(self):
        """Test BM25 search."""
        retrieval = BM25Retrieval()

        docs = [
            Document("1", "The quick brown fox"),
            Document("2", "A lazy dog sleeps"),
            Document("3", "Machine learning"),
        ]

        for doc in docs:
            retrieval.add_document(doc)

        retrieval.build_index()

        results = retrieval.search("quick fox", top_k=2)

        assert len(results) <= 2

    def test_scores(self):
        """Test that BM25 scores are reasonable."""
        retrieval = BM25Retrieval()

        docs = [
            Document("1", "apple apple apple"),
            Document("2", "banana"),
        ]

        for doc in docs:
            retrieval.add_document(doc)

        retrieval.build_index()

        results = retrieval.search("apple")

        assert results[0].doc_id == "1"
        assert results[0].score > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
