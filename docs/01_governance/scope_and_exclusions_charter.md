---
title: "Scope and Exclusions Charter"
artifact_id: uaks_v1_scope_and_exclusions_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Scope and Exclusions Charter

Document ID: uaks_v1_scope_and_exclusions_20260311

## 1. In-Scope

### 1.1 Core Capabilities

UAKS explicitly covers:

- **Atomic knowledge extraction** from text and code sources
- **Canonical representation** of atoms with cryptographic identifiers
- **Graph-based relation mapping** between atoms
- **Retrieval assembly** with documented recipes
- **Integrity verification** through SHA-256 hashing
- **Deduplication** at the atom level

### 1.2 Target Users

- Knowledge engineers building verified knowledge bases
- Research teams requiring provenance-aware retrieval
- Systems requiring audit trails for assembled outputs
- Organizations needing deduplicated knowledge stores

### 1.3 Deployment Contexts

- Single-tenant pilot deployments
- Multi-tenant knowledge consortiums
- Embedded knowledge services

## 2. Out-of-Scope

### 2.1 Explicit Exclusions

UAKS does not cover:

- **Real-time data ingestion** from live APIs (use separate ingestion layer)
- **Natural language generation** beyond recipe assembly
- **User authentication** beyond basic access control
- **Billing/metering** for multi-tenant usage
- **Content moderation** (external policy layer)
- **Legal compliance** (jurisdiction-specific, external)

### 2.2 Not Yet Supported

These features are planned but not in v1:

- Cross-substrate federation
- Distributed consensus for atom canonicalization
- Automated conflict resolution
- Real-time collaborative editing

## 3. Boundary Conditions

### 3.1 Integration Boundaries

| Boundary | Responsibility |
|----------|----------------|
| Source → Intake | External systems provide raw content |
| UAKS → Consumer | UAKS provides assembled atoms/recipes |
| UAKS → External Analysis | UAKS invokes, does not host analysis |

### 3.2 Data Ownership

- Source content remains owned by source providers
- Derived atoms are owned by the organization operating UAKS
- Assembly recipes are owned by the assembly creator

## 4. Source Lineage

Derived from the UAKS architecture conversation artifact set.
