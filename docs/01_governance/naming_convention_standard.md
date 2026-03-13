---
title: "Naming Convention Standard"
artifact_id: uaks_v1_naming_convention_standard_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Naming Convention Standard

Document ID: uaks_v1_naming_convention_standard_20260311

## 1. Purpose

Standardized naming ensures consistent identification across the UAKS ecosystem, enabling reliable referencing, tooling support, and human readability.

## 2. Atom Naming

### 2.1 Atom ID Format

```
atom_{hash_prefix}_{sequence}
```

Where:
- `hash_prefix`: First 12 characters of SHA-256 hash
- `sequence`: Zero-padded 6-digit sequence number for collision resolution

Example: `atom_a1b2c3d4e5f6_000001`

### 2.2 Atom Type Prefixes

| Type | Prefix | Example |
|------|--------|---------|
| Text Atom | `txt` | `txt_` |
| Code Atom | `code` | `code_` |
| Relation Atom | `rel` | `rel_` |
| Metadata Atom | `meta` | `meta_` |

### 2.3 Atom Family Names

Families are lowercase, hyphen-separated:

- `concept`
- `fact`
- `procedure`
- `reference`
- `citation`

## 3. Relation Naming

### 3.1 Relation ID Format

```
rel_{source_type}-{relation_type}-{target_type}_{hash}
```

Example: `rel-concept-derives-from-fact_a1b2`

### 3.2 Relation Types

| Type | Description |
|------|-------------|
| `derives-from` | Semantic lineage |
| `supports` | Evidential relationship |
| `contradicts` | Opposition relationship |
| `refines` | Specificity relationship |
| `references` | Citation relationship |

## 4. Recipe Naming

### 4.1 Recipe ID Format

```
recipe_{intent}_{version}_{hash}
```

Example: `recipe_explain_quantum_physics_v1_a1b2`

## 5. File and Directory Conventions

### 5.1 Directory Structure

```
/atoms/{type}/{family}/{date}
/relations/{type}
/recipes/{intent}
/exports/{format}
```

### 5.2 File Naming

- All lowercase
- Hyphen-separated
- Date prefix for exports: `YYYY-MM-DD_{name}.{ext}`

## 6. Source Lineage

Derived from the UAKS architecture conversation artifact set.
