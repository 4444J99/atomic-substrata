---
title: "Graph Relation Catalog v1"
artifact_id: uaks_v1_graph_relation_catalog_20260311
pair_id: CHATPAIR-009
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Graph Relation Catalog v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_graph_relation_catalog_20260311
Version: 1.0-draft
Status: Draft normative catalog


1. Purpose


This catalog defines the canonical edge vocabulary for the graph substrate. Relations represent typed, directional semantics between atoms, entities, sources, and recipes.


2. General rules

Rule ID
Requirement
GRC-01
every edge MUST have a source and target
GRC-02
every edge MUST have a declared relation type
GRC-03
every verified edge SHOULD have provenance
GRC-04
edge semantics MUST remain directional unless explicitly symmetric
GRC-05
contradictory edges MAY coexist if scope or provenance differs

3. Canonical relation catalog

Relation
Source
Target
Directional
Meaning
DERIVED_FROM
Atom
SourceObject or Atom
Yes
output derives from prior object
SUPPORTED_BY
Atom
EvidenceAtom or Atom
Yes
claim is backed by support
CONTRADICTS
Atom
Atom
Usually symmetric
scoped conflict
SUPERSEDES
Atom
Atom
Yes
later state replaces earlier
USES_ENTITY
Atom
Entity
Yes
references or invokes entity
ASSEMBLED_IN
Atom
RecipeAtom
Yes
recipe membership
REFINES
Atom
Atom
Yes
more specific or more resolved form
IMPLEMENTS
CodeAtom
TextAtom or PolicyAtom
Yes
code realizes rule/statement
DOCUMENTS
TextAtom
CodeAtom
Yes
text describes code
TESTS
CodeAtom
CodeAtom
Yes
test validates target
AFFECTS
PolicyAtom or TextAtom
CodeAtom
Yes
change in rule impacts code
EXPOSES_INTERFACE
CodeAtom
Entity
Yes
code exposes contract/interface
ANALYZES
Analysis family
SourceObject or Atom
Yes
analysis studies target
MAPS_TO
Analysis family
Entity or Atom
Yes
external label aligned to local concept
CHARACTERIZES
Analysis family
Entity or corpus target
Yes
structural description
DETECTS_DRIFT_IN
DriftAtom
Entity or Atom
Yes
temporal change detected
PROPOSES_TAXONOMY_FOR
TaxonomyProposalAtom
corpus/entity/concept set
Yes
taxonomy suggestion
REQUIRES_REVIEW_OF
Analysis family
Atom
Yes
flags re-evaluation
IS_SUPERSEDED_BY
Analysis family
Analysis family
Yes
analytical successor
DEPENDS_ON
CodeAtom
CodeAtom or Entity
Yes
operational dependency

4. Edge qualifiers


An edge MAY carry qualifiers.

Qualifier
Meaning
confidence
strength or trust score
scope
project/time/jurisdiction scope
provenanceRef
lineage record
effectiveFrom / effectiveTo
validity window
rationale
explanatory note

5. Recommended inverses


Some inverses MAY be materialized for convenience.

Primary edge
Optional inverse
SUPERSEDES
IS_SUPERSEDED_BY
DEPENDS_ON
DEPENDENT_OF as derived view only
IMPLEMENTS
IMPLEMENTED_BY as derived view only
TESTS
TESTED_BY as derived view only

The canonical stored edge SHOULD remain the primary direction unless operational needs justify both.


6. High-value relation patterns


6.1 Rule to code trace


PolicyAtom → AFFECTS → CodeAtom
CodeAtom → IMPLEMENTS → PolicyAtom


6.2 Claim support chain


TextAtom → SUPPORTED_BY → EvidenceAtom


6.3 Analysis-triggered maintenance


DriftAtom → REQUIRES_REVIEW_OF → TextAtom
TextAtom → AFFECTS → CodeAtom


6.4 Assembly trace


Atom → ASSEMBLED_IN → RecipeAtom
