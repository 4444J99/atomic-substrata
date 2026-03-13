---
title: "CAS Object Model"
artifact_id: uaks_v1_cas_object_model_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# CAS Object Model

Document ID: uaks_v1_cas_object_model_20260311

## 1. CAS Overview

The Canonical Atom Structure (CAS) defines the standard format for all atoms in UAKS, ensuring consistent representation across different content types.

## 2. Base Object Structure

### 2.1 JSON Schema

```json
{
  "$schema": "https://uaks.schema.org/v1/atom.json",
  "type": "object",
  "required": ["id", "type", "family", "canonical_form", "hash", "provenance"],
  "properties": {
    "id": { "$ref": "#/definitions/atom_id" },
    "type": { "$ref": "#/definitions/atom_type" },
    "family": { "$ref": "#/definitions/atom_family" },
    "canonical_form": { "$ref": "#/definitions/canonical_content" },
    "hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "provenance": { "$ref": "#/definitions/provenance_chain" },
    "metadata": { "$ref": "#/definitions/atom_metadata" }
  }
}
```

## 3. Type Definitions

### 3.1 Atom Types

| Type | Description | Required Fields |
|------|-------------|-----------------|
| TEXT | Textual content | normalized_text, language |
| CODE | Code content | language, parse_tree |
| RELATION | Graph relation | source, target, relation_type |
| METADATA | Metadata atom | key_value_pairs |

### 3.2 Atom Families

| Family | Description | Example |
|--------|-------------|---------|
| CONCEPT | Abstract idea | "democracy" |
| FACT | Verifiable statement | "water boils at 100C" |
| PROCEDURE | Step-by-step process | "how to compile" |
| REFERENCE | External reference | citation to paper |
| CITATION | Source attribution | "according to Smith 2024" |

## 4. Canonical Content

### 4.1 Text Canonical Form

```json
{
  "normalized_text": "string with whitespace normalized",
  "language": "en-US",
  "encoding": "UTF-8",
  "line_endings": "LF",
  "whitespace": "collapsed to single space"
}
```

### 4.2 Code Canonical Form

```json
{
  "code": "whitespace normalized",
  "language": "python",
  "version": "3.11",
  "ast_hash": "sha256 of AST representation",
  "imports": ["list of import paths"]
}
```

## 5. Serialization

### 5.1 Primary Format

- JSON for API responses and storage
- Binary CBOR for efficient transfer

### 5.2 Validation

- Schema validation on ingest
- Hash verification on storage
- Provenance required for all atoms

## 6. Source Lineage

Derived from the UAKS architecture conversation artifact set.
