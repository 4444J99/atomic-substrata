---
title: "Recipe Persistence Specification"
artifact_id: uaks_v1_recipe_persistence_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Recipe Persistence Specification

Document ID: uaks_v1_recipe_persistence_20260311

## 1. Overview

Recipe Persistence defines how assembly recipes are stored, versioned, and retrieved throughout their lifecycle.

## 2. Storage Model

### 2.1 Repository Structure

```
/recipes/
├── {recipe_id}/
│   ├── v1/
│   │   ├── recipe.json
│   │   ├── input_schema.json
│   │   ├── output_schema.json
│   │   └── metadata.json
│   └── v2/
│       └── ...
├── index/
│   ├── by_intent.json
│   ├── by_creator.json
│   └── by_date.json
```

### 2.2 Database Schema

```sql
CREATE TABLE recipes (
  id UUID PRIMARY KEY,
  intent VARCHAR(500) NOT NULL,
  version INTEGER NOT NULL,
  creator_id UUID REFERENCES users(id),
  input_atoms JSONB NOT NULL,
  transformations JSONB NOT NULL,
  output_spec JSONB NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL,
  
  UNIQUE(intent, version)
);

CREATE INDEX idx_recipes_intent ON recipes(intent);
CREATE INDEX idx_recipes_creator ON recipes(creator_id);
```

## 3. Versioning

### 3.1 Version Strategy

- Semantic versioning: MAJOR.MINOR.PATCH
- MAJOR: Breaking changes to inputs/outputs
- MINOR: New capabilities, backward compatible
- PATCH: Bug fixes

### 3.2 Version Lookup

```
Latest:     GET /recipes/{id}/latest
Specific:   GET /recipes/{id}/v{major}.{minor}.{patch}
All:        GET /recipes/{id}/versions
```

## 4. Lifecycle States

| State | Description | Transitions |
|-------|-------------|-------------|
| draft | Under development | → active |
| active | Available for use | → deprecated, archived |
| deprecated | Use with caution | → archived |
| archived | Not available | none |

## 5. Persistence Operations

### 5.1 Create

1. Validate recipe structure
2. Assign version (or 1.0.0 for new)
3. Store to database
4. Update indices
5. Return recipe ID

### 5.2 Update

- Create new version
- Preserve old version
- Update latest pointer

### 5.3 Delete

- Soft delete (archive)
- Preserve history
- Remove from indices

## 6. Caching

| Cache | TTL | Invalidation |
|-------|-----|--------------|
| Recipe latest | 1 min | On update |
| Recipe specific | 1 hour | Never |
| Index listings | 5 min | On create/update |

## 7. Source Lineage

Derived from the UAKS architecture conversation artifact set.
