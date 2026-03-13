---
title: "AST Parsing Strategy"
artifact_id: uaks_v1_ast_parsing_strategy_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# AST Parsing Strategy

Document ID: uaks_v1_ast_parsing_strategy_20260311

## 1. Overview

The AST (Abstract Syntax Tree) Parsing Strategy defines how code atoms are extracted, normalized, and represented in UAKS for accurate deduplication and relation mapping.

## 2. Supported Languages

### 2.1 Tier 1 (Full AST Support)

| Language | Parser | Version |
|----------|--------|---------|
| Python | ast module | 3.11+ |
| JavaScript | Acorn/Babel | ES2024 |
| TypeScript | TypeScript AST | 5.0+ |
| Java | JavaParser | 4.0+ |
| Go | go/ast | 1.21+ |

### 2.2 Tier 2 (Basic Structure)

| Language | Parser | Coverage |
|----------|--------|----------|
| Rust | syn | Functions, types |
| C/C++ | Tree-sitter | Declarations |
| Ruby | Parser | Methods, classes |
| PHP | PHP-Parser | Functions |

## 3. Parsing Pipeline

### 3.1 Extraction Stages

```
Source Code → Lexer → Parser → AST → Normalizer → Code Atom
```

### 3.2 Stage Details

1. **Lexical Analysis**
   - Tokenization
   - Comment removal
   - Whitespace normalization

2. **Syntax Analysis**
   - Build AST
   - Validate syntax
   - Extract structure

3. **Semantic Analysis**
   - Resolve imports
   - Build symbol table
   - Extract dependencies

4. **Normalization**
   - Canonicalize whitespace
   - Sort imports
   - Standardize naming

## 4. AST Representation

### 4.1 Node Types

```json
{
  "node_type": "FunctionDef",
  "name": "hello",
  "args": [],
  "body": [...],
  "decorators": []
}
```

### 4.2 Key Extractions

| Code Element | Extraction | Purpose |
|--------------|------------|---------|
| Functions | name, params, body | Knowledge atoms |
| Classes | name, methods, inheritance | Structure mapping |
| Imports | path, alias | Dependency relations |
| Types | name, definition | Concept atoms |
| Comments | content, location | Context atoms |

## 5. Deduplication Strategy

### 5.1 Semantic Hash

Code atoms use AST-derived hashes:

```
code_hash = SHA256(
  normalized_ast_json +
  language_version +
  import_hash
)
```

### 5.2 Difference Detection

Structural comparison detects:
- Renamed variables
- Reformatted code
- Refactored functions

## 6. Error Handling

### 6.1 Parse Failures

| Scenario | Handling |
|----------|----------|
| Syntax error | Reject, return error |
| Partial parse | Extract valid nodes |
| Unknown syntax | Log, continue |

## 7. Source Lineage

Derived from the UAKS architecture conversation artifact set.
