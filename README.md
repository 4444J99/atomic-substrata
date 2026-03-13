# Unified Atomic Knowledge Substrate (UAKS)

> *"The atom is the smallest unit of meaning that retains integrity."*

A technical knowledge storage and retrieval system based on atomic knowledge principles. UAKS preserves source evidence, primary atoms, and derivative analytical atoms as distinct layers.

## Status

| Component | Status |
|-----------|--------|
| Repository Structure | ✅ Complete |
| Source Artifacts | ✅ Preserved |
| Pipeline Script | ✅ Operational |
| Academic API Suite | ✅ Built |
| Roadmap | ✅ Defined |

## Quick Start

```bash
# Show pipeline status
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

# Find academic papers
python scripts/pipeline.py find-paper "knowledge graph"

# List all atoms
python scripts/pipeline.py list-atoms
```

## Architecture

### Pipeline Stages

```
Source → Intake → Refinery → Deduplication → Storage → Assembly → Output
```

### Atom Types

- **TextAtom**: Smallest interpretable text unit
- **CodeAtom**: Smallest interpretable code unit

### Key Files

- `scripts/pipeline.py` - UAKS pipeline CLI
- `scripts/academic/` - Academic paper API clients
- `docs/` - 100+ artifacts across 13 categories
- `source_artifacts/` - Original transcript sources

## Repository Intent

This repository preserves:
1. **Source evidence** - Original transcripts and artifacts
2. **Primary atoms** - TextAtom and CodeAtom types
3. **Analytical atoms** - Derived insights and patterns
4. **Pipeline infrastructure** - Processing and assembly

## Roadmap

See [there-and-back-again.md](there-and-back-again.md) for the complete path to Omega.

## Metrics

- **Artifacts**: 100+
- **Categories**: 13
- **Placeholders Filled**: 32
- **Scripts**: 5+

---

*Generated: 2026-03-12*
*Source: Atomic Knowledge Assembler conversation*
