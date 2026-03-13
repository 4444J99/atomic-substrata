---
title: "Portal Projection Specification v1"
artifact_id: uaks_v1_portal_projection_spec_20260311
pair_id: CHATPAIR-010
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Portal Projection Specification v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_portal_projection_spec_20260311
Version: 1.0-draft
Status: Draft normative specification


1. Purpose


The portal projection layer provides human-usable and tool-usable views over the atomic substrate without treating those views as primary storage truth. It materializes stable, intelligible workspace views from content-addressed objects, graph relations, and recipes.


2. Projection thesis


The substrate stores atoms and immutable content objects. Users and tools often need familiar workspace projections: project trees, file-like structures, documentation bundles, trace reports, code views, and assembled artifacts.


The portal projection layer therefore MUST provide ergonomic structure while preserving the deeper truth that these are projected states, not primary containers.


3. Projection objects

Projection type
Purpose
workspace projection
project/repository-shaped view
document projection
rendered text or spec
code projection
file/module/function-oriented view
trace projection
lineage and relation inspection
review projection
validation and dispute workflow view
historical projection
time-sliced state view

4. Core projection inputs

Input
Role
CAS objects
exact payload states
atoms
semantic and technical units
entities
conceptual anchors
relations
structural map
recipes
reusable assembly/projection patterns
scope descriptor
project/time/user constraints

5. Projection rules


5.1 Identity rule


Projected paths, names, and folders MAY be stable human-facing aliases, but MUST NOT replace content identity or logical atom identity.


5.2 Reproducibility rule


A projection SHOULD be reconstructable from its recipe, object references, and scope context.


5.3 Non-destructive rule


Edits in a projection layer MUST be mediated back into refinery/governance flows rather than silently mutating canonical substrate truth.


6. Projection schema


6.1 ProjectionDescriptor

Field
Meaning
projectionId
unique projection object
projectionType
workspace, document, code, trace, review, historical
scopeDescriptor
project/repository/time constraints
rootRefs
seed atom/entity/CAS refs
recipeRef
generation recipe if any
createdAt
creation time
projectionStateHash
exact projected state identifier

7. Workspace projection behavior


A workspace projection SHOULD provide a familiar hierarchy built from substrate objects.


Possible mapping:

Projected path concept
Backing substrate
folder
entity cluster, repo, module, or recipe grouping
file
assembled document or code CAS object
symbol view
code atom
spec section
ordered atom sequence
trace panel
graph traversal

8. Historical projection behavior


Historical projections MUST support viewing prior superseded states, prior recipes, and prior code payloads without collapsing them into the current state.


9. Final normative judgment


A valid UAKS-v1 projection layer MUST:

Requirement
Status
separate projection identity from canonical identity
mandatory
support reproducible projections
mandatory
preserve historical state views
mandatory
avoid silent truth mutation through projection edits
mandatory
