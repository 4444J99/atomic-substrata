---
title: "2. Gold-Standard Atom Set Specification v1"
artifact_id: uaks_v1_gold_atom_set_spec_20260311
pair_id: CHATPAIR-015
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

2. Gold-Standard Atom Set Specification v1


Document ID: uaks_v1_gold_atom_set_spec_20260311


2.1 Purpose


The gold-standard atom set defines the correct atomization output for benchmark sources.


It is used to evaluate:


refinery correctness

atomic boundary decisions

relation extraction

deduplication behavior



2.2 Gold atom design rules


Each gold atom MUST:


represent a single independent claim or function

include exact source span

include correct atom type

include expected relations



2.3 Gold atom schema

Field
Meaning
goldAtomId
canonical atom identifier
sourceRef
original source
atomType
TextAtom / PolicyAtom / CodeAtom / EvidenceAtom
canonicalStatement
distilled meaning
sourceSpan
exact location
expectedRelations
relation edges
validationState
expected trust level


2.4 Gold relation specification


Relations in the gold set define expected graph structure.

Relation
Example
SUPPORTED_BY
claim supported by evidence
IMPLEMENTS
code implements rule
AFFECTS
policy affects code
DERIVED_FROM
atom from source


2.5 Example gold atom


goldAtomId: gold_atom_014
sourceRef: src_policy_002
atomType: PolicyAtom
canonicalStatement: Imported analysis bundles must pass normalization before publication.
sourceSpan: lines 12–15
expectedRelations:
  - AFFECTS: atom_code_import_pipeline
validationState: VERIFIED
