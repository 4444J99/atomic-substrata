---
title: "Trust Boundary Map"
artifact_id: uaks_v1_trust_boundary_map_20260311
status: drafted_from_context
generated_at: 2026-03-12T19:28:12Z
source_lineage: "Derived from the UAKS architecture conversation artifact set."
---

# Trust Boundary Map

Document ID: uaks_v1_trust_boundary_map_20260311

## 1. Trust Zones

### 1.1 Zone Definitions

```
┌─────────────────────────────────────────────────────────────┐
│                     UNTRUSTED ZONE                          │
│  External Sources, Unknown Clients, Public Internet          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    DMZ (Screened Subnet)                     │
│  API Gateway, Rate Limiter, TLS Termination                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   TRUSTED ZONE (Internal)                   │
│  Core Services, Database, Cache                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   HIGHLY TRUSTED ZONE                        │
│  Integrity Service, Key Management, Audit Logs              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Zone Descriptions

| Zone | Components | Trust Level |
|------|------------|-------------|
| Untrusted | External sources, public clients | None |
| DMZ | API Gateway, Auth proxy | Minimal |
| Trusted | Core services, DB | High |
| Highly Trusted | KMS, Integrity | Maximum |

## 2. Boundary Controls

### 2.1 Ingress Controls

- API Gateway enforces authentication
- Rate limiting at boundary
- Input validation and sanitization
- DDoS protection

### 2.2 Egress Controls

- Output validation
- Logging of all responses
- No direct database access from DMZ

### 2.3 Internal Controls

- Service-to-service mTLS
- Role-based access within trusted zone
- Audit logging

## 3. Data Flow Across Boundaries

### 3.1 Ingestion Flow

```
External Source → DMZ (validate) → Trusted (process) → Store
```

### 3.2 Retrieval Flow

```
Client → DMZ (auth) → Trusted (query) → Assemble → DMZ → Client
```

## 4. Trust Decisions

| Decision Point | Criteria | Action |
|----------------|----------|--------|
| Source intake | Format validation | Accept/Reject |
| Authentication | Token validity | Allow/Deny |
| Authorization | Role check | Permit/Deny |
| Atom creation | Hash verification | Store/Flag |
| Recipe execution | Input validation | Execute/Reject |

## 5. Source Lineage

Derived from the UAKS architecture conversation artifact set.
