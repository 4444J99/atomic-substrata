---
title: "Service Decomposition Specification"
artifact_id: uaks_v1_service_decomposition_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Service Decomposition Specification

Document ID: uaks_v1_service_decomposition_20260311

## 1. Service Architecture

### 1.1 Core Services

```
┌─────────────────────────────────────────────────────┐
│                  UAKS Platform                       │
├─────────────────────────────────────────────────────┤
│  Intake Service    │  Atomization Service            │
│  (Ingestion)       │  (Refinery Pipeline)            │
├────────────────────┼────────────────────────────────┤
│  Graph Service     │  Assembly Service               │
│  (Relations)       │  (Recipe Execution)            │
├────────────────────┼────────────────────────────────┤
│  Query Service     │  Portal Service                 │
│  (Retrieval)        │  (API Gateway)                 │
└─────────────────────────────────────────────────────┘
```

### 1.2 Supporting Services

| Service | Responsibility |
|---------|----------------|
| Integrity Service | Hash computation, verification |
| Provenance Service | Lineage tracking |
| Deduplication Service | Duplicate detection |
| Evaluation Service | Quality assessment |

## 2. Service Definitions

### 2.1 Intake Service

**Responsibilities:**
- Receive raw content from sources
- Validate input format and size
- Queue for processing
- Track ingestion status

**API:**
- `POST /intake/submit` - Submit content
- `GET /intake/status/{job_id}` - Check status

### 2.2 Atomization Service

**Responsibilities:**
- Text refinement (Text Refinery)
- Code parsing (Code Refinery)
- External analysis integration
- Atom canonicalization

**API:**
- `POST /atomize/text` - Process text
- `POST /atomize/code` - Process code

### 2.3 Graph Service

**Responsibilities:**
- Relation creation and management
- Graph queries
- Path finding
- Neighborhood queries

**API:**
- `POST /relations` - Create relation
- `GET /relations/{atom_id}` - Get atom relations

### 2.4 Assembly Service

**Responsibilities:**
- Recipe execution
- Atom retrieval
- Output rendering
- Recipe versioning

**API:**
- `POST /assemble` - Execute recipe
- `GET /recipes/{id}` - Get recipe

### 2.5 Query Service

**Responsibilities:**
- Search coordination
- Scoring computation
- Result ranking
- Cache management

**API:**
- `GET /query` - Execute query

## 3. Communication Patterns

### 3.1 Synchronous

- API Gateway → Core Services
- Query Service → Graph/Assembly

### 3.2 Asynchronous

- Intake → Atomization (message queue)
- Atomization → Graph (events)

## 4. Source Lineage

Derived from the UAKS architecture conversation artifact set.
