---
title: "Sample TextAtom Corpus"
artifact_id: uaks_v1_sample_textatom_corpus_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Sample TextAtom Corpus

Document ID: uaks_v1_sample_textatom_corpus_20260311

## 1. Sample Atoms

### 1.1 Concept Atoms

```json
{
  "id": "atom_3a4b5c_000001",
  "type": "TEXT",
  "family": "CONCEPT",
  "canonical_form": {
    "normalized_text": "knowledge: organized information usable for decision-making",
    "language": "en"
  },
  "hash": "3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4",
  "provenance": {
    "source_type": "seed",
    "source_ref": "seed:ontology:v1",
    "confidence": 1.0
  }
}
```

### 1.2 Fact Atoms

```json
{
  "id": "atom_1a2b3c_000002",
  "type": "TEXT",
  "family": "FACT",
  "canonical_form": {
    "normalized_text": "SHA-256 produces a 64-character hexadecimal hash",
    "language": "en"
  },
  "hash": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2",
  "provenance": {
    "source_type": "seed",
    "source_ref": "seed:specs:v1",
    "confidence": 1.0
  }
}
```

### 1.3 Procedure Atoms

```json
{
  "id": "atom_2b3c4d_000003",
  "type": "TEXT",
  "family": "PROCEDURE",
  "canonical_form": {
    "normalized_text": "To verify atom integrity: compute SHA-256 of canonical form, compare to stored hash",
    "language": "en"
  },
  "hash": "2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3",
  "provenance": {
    "source_type": "seed",
    "source_ref": "seed:docs:v1",
    "confidence": 1.0
  }
}
```

## 2. Corpus Statistics

| Family | Count |
|--------|-------|
| CONCEPT | 50 |
| FACT | 100 |
| PROCEDURE | 25 |
| REFERENCE | 25 |

## 3. Source Lineage

Derived from the UAKS architecture conversation artifact set.
