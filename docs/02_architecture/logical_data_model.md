---
title: "Logical Data Model"
artifact_id: uaks_v1_logical_data_model_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Logical Data Model

Document ID: uaks_v1_logical_data_model_20260311

## 1. Core Entities

### 1.1 Atom

The fundamental unit of knowledge.

```
Atom {
  id: AtomID (unique identifier)
  type: AtomType (TEXT | CODE | RELATION | METADATA)
  family: AtomFamily (CONCEPT | FACT | PROCEDURE | REFERENCE | CITATION)
  content: CanonicalContent
  hash: SHA256
  provenance: ProvenanceChain
  metadata: AtomMetadata
  created_at: Timestamp
  updated_at: Timestamp
}
```

### 1.2 Relation

Represents connections between atoms.

```
Relation {
  id: RelationID
  source_atom: AtomID
  target_atom: AtomID
  relation_type: RelationType
  confidence: Float (0.0-1.0)
  provenance: ProvenanceChain
  created_at: Timestamp
}
```

### 1.3 Recipe

Documents the assembly process.

```
Recipe {
  id: RecipeID
  intent: String
  version: Version
  input_atoms: [AtomID]
  transformations: [Transformation]
  output_assembly: Assembly
  creator: ActorID
  created_at: Timestamp
}
```

### 1.4 Assembly

The output of a recipe execution.

```
Assembly {
  id: AssemblyID
  recipe_id: RecipeID
  atoms: [AtomID]
  rendered_content: Content
  confidence_score: Float
}
```

## 2. Value Objects

### 2.1 AtomID

```
AtomID {
  prefix: String (12 chars)
  sequence: String (6 chars)
  full_hash: SHA256
}
```

### 2.2 ProvenanceChain

```
ProvenanceChain {
  source_type: SourceType
  source_ref: String
  extraction_method: String
  transforms: [TransformRecord]
  confidence: Float
}
```

### 2.3 CanonicalContent

```
CanonicalContent {
  normalized_text: String
  encoding: String (UTF-8)
  language: LanguageCode
  structural_hints: [String]
}
```

## 3. Relationships

| From | To | Type |
|------|-----|------|
| Atom | Atom | Relation |
| Recipe | Atom | uses (input) |
| Recipe | Atom | produces (output) |
| Assembly | Atom | contains |
| Assembly | Recipe | follows |

## 4. Constraints

- Every atom MUST have a valid SHA-256 hash
- Every relation MUST reference existing atoms
- Provenance chain MUST be non-empty for derived atoms
- Recipe transformations MUST be deterministic

## 5. Source Lineage

Derived from the UAKS architecture conversation artifact set.
