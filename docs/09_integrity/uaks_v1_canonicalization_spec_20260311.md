---
title: "2 Canonicalization Specification v1"
artifact_id: uaks_v1_canonicalization_spec_20260311
pair_id: CHATPAIR-018
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

2 Canonicalization Specification v1


Document ID: uaks_v1_canonicalization_spec_20260311


2.1 Purpose


Canonicalization ensures that semantically identical atoms produce identical hashes.


Without canonicalization the system would accumulate duplicates.



2.2 Canonicalization rules

Rule
Description
whitespace normalization
collapse extra spaces
punctuation normalization
consistent punctuation
case normalization
lowercase where appropriate
field ordering
deterministic field order
metadata normalization
stable schema order


2.3 Canonical payload format


Example canonical representation:


{
  "atomType": "PolicyAtom",
  "canonicalStatement": "analysis bundles must pass normalization before publication",
  "sourceObjectId": "src_doc_034",
  "sourceSpan": "p12"
}


Hash is computed over this structure.
