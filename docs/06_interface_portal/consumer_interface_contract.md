---
title: "Consumer Interface Contract"
artifact_id: uaks_v1_consumer_interface_contract_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Consumer Interface Contract

Document ID: uaks_v1_consumer_interface_contract_20260311

## 1. Overview

The Consumer Interface Contract defines the API contract that UAKS exposes to external consumers, including request/response formats, authentication, and error handling.

## 2. API Endpoints

### 2.1 Query Endpoint

```
POST /api/v1/query
```

**Request:**
```json
{
  "query": "What is the capital of France?",
  "options": {
    "max_results": 5,
    "include_provenance": true,
    "confidence_threshold": 0.7
  }
}
```

**Response:**
```json
{
  "results": [
    {
      "assembly": { ... },
      "confidence": 0.95,
      "provenance": [...]
    }
  ],
  "metadata": {
    "query_time_ms": 150,
    "atoms_searched": 10000
  }
}
```

### 2.2 Atom Retrieval

```
GET /api/v1/atoms/{atom_id}
```

**Response:**
```json
{
  "id": "atom_a1b2c3_000001",
  "type": "TEXT",
  "family": "FACT",
  "content": "Paris is the capital of France.",
  "hash": "...",
  "provenance": { ... }
}
```

### 2.3 Recipe Execution

```
POST /api/v1/recipes/{recipe_id}/execute
```

## 3. Authentication

### 3.1 API Key

```
Authorization: ApiKey {api_key}
```

### 3.2 JWT Token

```
Authorization: Bearer {jwt_token}
```

### 3.3 Rate Limits

| Tier | Requests/minute |
|------|-----------------|
| Free | 10 |
| Standard | 100 |
| Premium | 1000 |

## 4. Error Handling

### 4.1 Error Response Format

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Query cannot be empty",
    "details": { ... }
  }
}
```

### 4.2 Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| INVALID_REQUEST | 400 | Malformed request |
| UNAUTHORIZED | 401 | Invalid credentials |
| FORBIDDEN | 403 | Insufficient permissions |
| NOT_FOUND | 404 | Resource not found |
| RATE_LIMITED | 429 | Too many requests |
| INTERNAL_ERROR | 500 | Server error |

## 5. Versioning

### 5.1 API Versioning

- Version in URL: `/api/v1/`
- Deprecation policy: 12 months notice
- Migration guide provided

## 6. Source Lineage

Derived from the UAKS architecture conversation artifact set.
