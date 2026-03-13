---
title: "Physical Storage Architecture"
artifact_id: uaks_v1_physical_storage_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Physical Storage Architecture

Document ID: uaks_v1_physical_storage_20260311

## 1. Storage Strategy

### 1.1 Multi-Layer Storage

UAKS uses a tiered storage approach:

| Tier | Technology | Use Case |
|------|------------|----------|
| Hot | In-memory / Redis | Active atoms, recent queries |
| Warm | SSD-backed database | Frequent access atoms |
| Cold | Object storage (S3) | Archive, historical atoms |

### 1.2 Data Distribution

```
/uaks-storage/
├── atoms/
│   ├── text/
│   │   ├── {hash_prefix}/
│   │   │   └── {atom_id}.atom.json
│   ├── code/
│   │   └── ...
│   └── relation/
│       └── ...
├── relations/
│   ├── graph/
│   │   └── ...
│   └── indices/
├── recipes/
│   └── ...
├── recipes/
│   └── ...
└── metadata/
    └── ...
```

## 2. Database Technology

### 2.1 Primary Store: PostgreSQL

- **Atoms**: Structured atom storage with full-text search
- **Relations**: Graph extensions for relation queries
- **Recipes**: Recipe versioning and history

### 2.2 Vector Store: pgvector

- Semantic similarity search
- Embedding-based retrieval

### 2.3 Cache Layer: Redis

- Session management
- Hot atom cache
- Rate limiting

### 2.4 Object Storage: S3/MinIO

- Large content blobs
- Archive storage
- Backup retention

## 3. Data Partitioning

### 3.1 Atom Sharding

Atoms sharded by hash prefix for even distribution:

- 00-FF hex prefixes
- 256 shards at base level
- Cross-shard relations supported

### 3.2 Time-Based Partitioning

Recipes and assemblies use date-based partitioning:

```
/recipes/2026/03/{recipe_id}.json
/assemblies/2026/03/{assembly_id}.json
```

## 4. Replication & Durability

### 4.1 Replication Factor

| Environment | Replicas |
|-------------|----------|
| Production | 3 |
| Staging | 2 |
| Development | 1 |

### 4.2 Backup Strategy

- Continuous replication to warm storage
- Daily snapshots to cold storage
- 30-day retention on warm
- 1-year retention on cold

## 5. Source Lineage

Derived from the UAKS architecture conversation artifact set.
