---
title: "Canonical Ontology Examples"
artifact_id: uaks_v1_canonical_ontology_examples_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Canonical Ontology Examples

Document ID: uaks_v1_canonical_ontology_examples_20260311

## 1. Concept Atoms

### 1.1 Basic Concepts

| Concept | Definition | Family |
|---------|------------|--------|
| knowledge | Information organized for use | CONCEPT |
| atom | Smallest irreducible unit of knowledge | CONCEPT |
| relation | Connection between atoms | CONCEPT |
| recipe | Documented transformation process | CONCEPT |

### 1.2 Domain Concepts

| Concept | Domain | Definition |
|---------|--------|------------|
| text_atom | extraction | Parsed textual knowledge unit |
| code_atom | extraction | Parsed code knowledge unit |
| provenance | integrity | Source lineage tracking |

## 2. Fact Atoms

### 2.1 System Facts

- "Atoms are identified by SHA-256 hash"
- "Relations connect exactly two atoms"
- "Recipes produce assemblies from atoms"

## 3. Relation Examples

| Source | Relation | Target |
|--------|----------|--------|
| atom:type:text | is_a | atom:type:knowledge |
| atom:hash:abc | derives_from | source:doc123 |
| recipe:query | uses | atom:concept:retrieval |

## 4. Ontology Validation

All seed ontology atoms must:
- Have valid hash identifiers
- Include complete provenance
- Follow naming conventions
- Connect to existing relations

## 5. Source Lineage

Derived from the UAKS architecture conversation artifact set.
