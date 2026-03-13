---
title: "Portal Projection Data Model v1"
artifact_id: uaks_v1_portal_projection_data_model_20260311
pair_id: CHATPAIR-012
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Portal Projection Data Model v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_portal_projection_data_model_20260311
Version: 1.0-draft
Status: Draft normative data model


1. Purpose


This data model defines the object structures used to create, store, inspect, and reconstruct workspace, document, trace, review, and historical projections over the substrate.


2. Projection thesis


A projection is a structured view, not a source of truth. The model therefore separates projection identity, projection state, projection nodes, and canonical substrate references.


3. Core projection objects

Object
Role
ProjectionDescriptor
root metadata for one projection
ProjectionNode
one visible node within a projection
ProjectionGroup
hierarchical grouping or container
ProjectionEdge
visible relation between projection nodes
ProjectionRecipeBinding
link between projection and recipe
ProjectionStateSnapshot
reconstructable state hash and object refs

4. ProjectionDescriptor

Field
Meaning
projectionId
unique projection identifier
projectionType
workspace, document, code, trace, review, historical
scopeDescriptor
scope constraints used to build it
rootRefs
seed object references
recipeRef
optional driving recipe
projectionStateHash
exact state identifier
createdAt
creation time
createdBy
actor or service
visibilityClass
access label
status
active, archived, superseded

5. ProjectionNode

Field
Meaning
projectionNodeId
unique node within projection
projectionId
parent projection
nodeType
folder, file, symbol, section, report_block, entity_ref
label
displayed name
canonicalRef
underlying atom/entity/CAS/source/recipe ref
parentGroupId
containing group if any
ordinal
ordering index
stateHash
rendered or projected state hash
renderMetadata
display metadata
accessFiltered
whether portions are hidden/redacted

6. ProjectionGroup

Field
Meaning
projectionGroupId
unique group identifier
projectionId
parent projection
groupType
workspace_folder, document_section, trace_segment, review_bucket
label
displayed grouping label
parentGroupId
nesting parent
ordinal
ordering index

7. ProjectionEdge

Field
Meaning
projectionEdgeId
unique projection edge
projectionId
parent projection
sourceNodeId
node origin
targetNodeId
node target
edgeType
visible relation or navigation link
canonicalRelationRef
optional backing relation edge
renderMetadata
display metadata

8. ProjectionRecipeBinding

Field
Meaning
bindingId
unique binding
projectionId
target projection
recipeRef
recipe used
templateRef
template used
resolutionLevel
projection depth
generatedAt
timestamp

9. ProjectionStateSnapshot

Field
Meaning
snapshotId
unique snapshot
projectionId
owning projection
projectionStateHash
exact projection state hash
includedRefs
canonical refs included
generatedAt
timestamp
historicalMode
whether snapshot reflects non-current state
notes
optional generation notes

10. Projection node types

Node type
Meaning
folder
grouping container in workspace view
file
document or code-like projection
symbol
code-level symbol representation
section
document section
report_block
report subsection
entity_ref
conceptual anchor
trace_node
node in a trace path
review_item
item under adjudication

11. Projection generation rules

Rule ID
Requirement
PDM-01
every projection node MUST retain a canonical reference or explicitly declare itself synthetic
PDM-02
synthetic connective nodes MUST be marked as synthetic
PDM-03
historical projections MUST declare historical mode
PDM-04
projection hashes SHOULD change when included refs or render-relevant ordering changes
PDM-05
redacted projections MUST mark filtered nodes or fields

12. Minimal example


{
  "projectionId": "proj_workspace_001",
  "projectionType": "workspace",
  "scopeDescriptor": {
    "projectIds": ["project_uaks"]
  },
  "rootRefs": ["entity_project_uaks"],
  "recipeRef": "recipe_workspace_default_v1",
  "projectionStateHash": "sha256:proj001",
  "createdAt": "2026-03-11T17:00:00Z",
  "createdBy": "svc_projection",
  "visibilityClass": "internal",
  "status": "active"
}


13. Final normative judgment


A valid portal projection model MUST preserve reconstructability, canonical references, access compatibility, and historical visibility, while remaining explicitly secondary to the underlying substrate.
