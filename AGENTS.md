# AGENTS.md - Agentic Coding Guidelines

This file provides guidance for AI coding agents operating in the atomic-substrata repository.

## Project Overview

**atomic-substrata** is the Unified Atomic Knowledge Substrate (UAKS) - a technical knowledge storage and retrieval system based on atomic knowledge principles. It preserves source evidence, primary atoms, and derivative analytical atoms as distinct layers.

## Build, Test, and Development Commands

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run unit tests only
python -m pytest tests/unit/ -v

# Run integration tests only
python -m pytest tests/integration/ -v

# Run a specific test file
python -m pytest tests/unit/test_uaks_modules.py -v

# Run a single test class
python -m pytest tests/unit/test_uaks_modules.py::TestTextRefinery -v

# Run a single test method
python -m pytest tests/unit/test_uaks_modules.py::TestTextRefinery::test_refine -v

# Run with coverage
python -m pytest tests/ -v --cov=src --cov-report=term-missing

# Run tests matching a pattern
python -m pytest -k "test_refine" -v
```

### Running the Pipeline

```bash
# Check pipeline status
python scripts/pipeline.py status

# Ingest a source file
python scripts/pipeline.py ingest path/to/file.txt

# Refine an atom
python scripts/pipeline.py refine atom_abc123

# Run deduplication
python scripts/pipeline.py deduplicate

# Verify integrity
python scripts/pipeline.py integrity

# Assemble atoms for a query
python scripts/pipeline.py assemble "your query here"

# Use assembly engine directly
python scripts/assembly.py "knowledge atoms"

# Graph storage operations
python scripts/graph_storage.py import
python scripts/graph_storage.py stats

# REST API (requires Flask)
python scripts/api_server.py
```

### Code Quality

```bash
# Install dependencies
pip install requests pytest pytest-cov

# Lint with ruff
ruff check src/
ruff format src/
```

## Code Style Guidelines

### Python Conventions

- **Indentation**: 4 spaces (no tabs)
- **Line Length**: Maximum 88 characters (ruff default)
- **Encoding**: UTF-8

### Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Modules/Packages | snake_case | `source_intake`, `text_refinery` |
| Classes | PascalCase | `SourceIntake`, `TextRefinery`, `Atom`, `GraphNode` |
| Functions/Methods | snake_case | `def ingest_content()`, `def refine()` |
| Variables | snake_case | `atom_id`, `content_hash` |
| Constants | UPPER_SNAKE_CASE | `MAX_LENGTH`, `DEFAULT_ENCODING` |

### Import Organization

```python
# Standard library
import hashlib
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

# Third-party packages
try:
    import nltk
    HAS_NLTK = True
except ImportError:
    HAS_NLTK = False

# Local imports
from .module import ClassName
from ..package import function
```

### Type Hints

Use type hints throughout. Avoid `Any` when possible.

```python
def process_atoms(atoms: list[dict]) -> list[str]:
    results: list[str] = []
    return results
```

### Error Handling

- Use specific exception types
- Never use bare `except:`
- Use context managers

```python
try:
    result = process_content(content)
except ValueError as e:
    logger.error(f"Invalid content: {e}")
    raise

with open(filepath, 'r') as f:
    content = f.read()
```

## Project Structure

```
atomic-substrata/
├── src/uaks/              # Core modules (16 modules)
│   ├── text_refinery/    # Text atom extraction
│   ├── code_refinery/    # Code atom extraction
│   ├── source_intake/    # Source ingestion
│   ├── vector_retrieval/ # Vector search
│   └── ...               # Other modules
├── scripts/               # CLI tools and utilities
│   ├── pipeline.py       # Main pipeline CLI
│   ├── assembly.py       # Vector similarity assembly
│   ├── graph_storage.py # Graph operations
│   ├── api_server.py    # REST API
│   └── academic/        # Academic paper APIs
├── tests/                # Test suite
│   ├── unit/            # Unit tests
│   └── integration/      # Integration tests
├── docs/                 # Documentation
├── data/                 # Runtime data (gitignored)
├── pyproject.toml        # Project config
└── README.md
```

## Testing Guidelines

### Test File Organization

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Name test classes `Test*` and test methods `test_*`

```python
class TestTextRefinery:
    """Tests for Text Refinery module."""

    def test_refine(self):
        """Test text refinement."""
        ...
```

### Assertions

Use descriptive assertions with clear error messages:

```python
assert result.id is not None, "Atom ID should be generated"
assert len(atoms) > 0, "Should extract at least one atom"
```

## Commit Conventions

Use Conventional Commits:

| Prefix | Use For |
|--------|---------|
| `feat:` | New features |
| `fix:` | Bug fixes |
| `docs:` | Documentation |
| `chore:` | Maintenance, refactoring |
| `ci:` | CI/CD changes |
| `test:` | Test changes |

```bash
git commit -m "feat: add content hashing to intake module"
git commit -m "fix: resolve regex parsing error"
git commit -m "docs: update README"
```

## Security Best Practices

- Never commit secrets, API keys, or credentials
- Use environment variables for sensitive config
- Add secrets to `.gitignore`

---

*Last updated: 2026-03-14*

<!-- ORGANVM:AUTO:START -->
## Agent Context (auto-generated — do not edit)

This repo participates in the **ORGAN-I (Theory)** swarm.

### Active Subscriptions
- *No active event subscriptions*

### Production Responsibilities
- *No production responsibilities*

### External Dependencies
- *No external dependencies*

### Governance Constraints
- Adhere to unidirectional flow: I→II→III
- Never commit secrets or credentials

*Last synced: 2026-05-23T00:26:31Z*
<!-- ORGANVM:AUTO:END -->
