---
title: "Initial Recipe Pack"
artifact_id: uaks_v1_initial_recipe_pack_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Initial Recipe Pack

Document ID: uaks_v1_initial_recipe_pack_20260311

## 1. Overview

The Initial Recipe Pack provides starter recipes for common UAKS operations.

## 2. Recipes

### R1: Text Atom Extraction

```json
{
  "id": "recipe_text_extract_v1",
  "intent": "Extract text atoms from document",
  "version": "1.0.0",
  "input_spec": {
    "document": "string"
  },
  "transformations": [
    {"type": "parse", "method": "text"},
    {"type": "normalize", "method": "whitespace"},
    {"type": "extract", "method": "sentences"}
  ],
  "output_spec": {
    "atoms": ["TEXT"]
  }
}
```

### R2: Code Atom Extraction

```json
{
  "id": "recipe_code_extract_v1",
  "intent": "Extract code atoms from source file",
  "version": "1.0.0",
  "input_spec": {
    "source_file": "string"
  },
  "transformations": [
    {"type": "parse", "method": "ast", "language": "auto"},
    {"type": "extract", "method": "functions"},
    {"type": "extract", "method": "classes"}
  ],
  "output_spec": {
    "atoms": ["CODE"]
  }
}
```

### R3: Basic Query

```json
{
  "id": "recipe_basic_query_v1",
  "intent": "Answer factual questions",
  "version": "1.0.0",
  "input_spec": {
    "query": "string"
  },
  "transformations": [
    {"type": "retrieve", "method": "semantic"},
    {"type": "rank", "method": "confidence"},
    {"type": "assemble", "method": "answer"}
  ],
  "output_spec": {
    "assembly": "FACT"
  }
}
```

### R4: Provenance Trace

```json
{
  "id": "recipe_provenance_trace_v1",
  "intent": "Generate provenance report",
  "version": "1.0.0",
  "input_spec": {
    "atom_id": "string"
  },
  "transformations": [
    {"type": "trace", "method": "lineage"},
    {"type": "format", "method": "report"}
  ],
  "output_spec": {
    "assembly": "REPORT"
  }
}
```

## 3. Source Lineage

Derived from the UAKS architecture conversation artifact set.
