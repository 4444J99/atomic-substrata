---
title: "Sample CodeAtom Corpus"
artifact_id: uaks_v1_sample_codeatom_corpus_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Sample CodeAtom Corpus

Document ID: uaks_v1_sample_codeatom_corpus_20260311

## 1. Sample Code Atoms

### 1.1 Python Function

```json
{
  "id": "atom_py001_000001",
  "type": "CODE",
  "family": "PROCEDURE",
  "canonical_form": {
    "code": "def compute_hash(content: str) -> str:\n    import hashlib\n    return hashlib.sha256(content.encode()).hexdigest()",
    "language": "python",
    "version": "3.11"
  },
  "hash": "py001abc123def456789012345678901234567890123456789012345678901234",
  "provenance": {
    "source_type": "seed",
    "source_ref": "seed:code:v1",
    "confidence": 1.0
  }
}
```

### 1.2 JavaScript Function

```json
{
  "id": "atom_js001_000002",
  "type": "CODE",
  "family": "PROCEDURE",
  "canonical_form": {
    "code": "function computeHash(content) {\n  return crypto.createHash('sha256').update(content).digest('hex');\n}",
    "language": "javascript",
    "version": "ES2022"
  },
  "hash": "js001abc123def456789012345678901234567890123456789012345678901234",
  "provenance": {
    "source_type": "seed",
    "source_ref": "seed:code:v1",
    "confidence": 1.0
  }
}
```

## 2. Corpus Statistics

| Language | Count |
|----------|-------|
| Python | 20 |
| JavaScript | 15 |
| TypeScript | 10 |
| Go | 5 |

## 3. Source Lineage

Derived from the UAKS architecture conversation artifact set.
