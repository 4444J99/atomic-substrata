---
title: "1 Capacity Model v1"
artifact_id: uaks_v1_capacity_model_20260311
pair_id: CHATPAIR-019
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

1 Capacity Model v1


Document ID: uaks_v1_capacity_model_20260311


1.1 Purpose


Estimates the scale characteristics of the atomic substrate.


The model predicts behavior for:


ingestion

atom growth

graph expansion

retrieval load

storage requirements



1.2 Atomic expansion model


Atomic systems expand at predictable ratios.


Typical ranges observed in knowledge systems:

Source Type
Atoms Produced
conversation transcript
5–20 atoms per paragraph
documentation
3–10 atoms per paragraph
policy document
2–6 atoms per paragraph
code file
10–40 code atoms
analysis bundle
5–30 analysis atoms


1.3 Example corpus projection


Example pilot corpus:

Source Type
Count
documents
1,000
conversations
500
code files
5,000
analysis bundles
200

Projected atoms:

Atom Type
Estimated Count
TextAtoms
80,000
PolicyAtoms
10,000
CodeAtoms
120,000
EvidenceAtoms
30,000
AnalysisAtoms
15,000

Total projected atoms:


~255,000 atoms



1.4 Graph expansion


Each atom produces relations.


Typical relation density:

Relation
Frequency
provenance
1 per atom
semantic relation
1–3 per atom
dependency relation
0–2 per atom
analysis relation
0–2 per atom

Projected edges:


~400,000–700,000 graph edges
