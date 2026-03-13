---
title: "2 Storage Model v1"
artifact_id: uaks_v1_storage_model_20260311
pair_id: CHATPAIR-019
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

2 Storage Model v1


Document ID: uaks_v1_storage_model_20260311


2.1 Storage layers


The system stores data across four substrates.

Layer
Purpose
CAS store
immutable atom payloads
graph database
relationships
vector index
semantic retrieval
source archive
raw artifacts


2.2 Storage estimate


Pilot system:

Layer
Size
CAS atoms
5–15 GB
graph database
2–5 GB
vector index
2–4 GB
source archive
10–30 GB

Total estimated footprint:


20–50 GB
