---
title: "Auth and Access Model v1"
artifact_id: uaks_v1_auth_access_model_20260311
pair_id: CHATPAIR-012
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Auth and Access Model v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_auth_access_model_20260311
Version: 1.0-draft
Status: Draft normative model


1. Purpose


This model defines authentication assumptions, authorization layers, access scopes, and result-filtering behavior for UAKS-v1. It governs who may view, query, assemble, mutate, review, or import across the substrate.


2. Access thesis


Authorization in UAKS-v1 MUST apply at more than one layer. It is not sufficient to secure only the API. Access decisions MUST be compatible with source sensitivity, atom trust state, projection context, and mutation risk.


3. Access layers

Layer
Function
Identity layer
authenticate actor
Role layer
assign functional role
Scope layer
restrict project/repository/domain reach
Object layer
restrict source/atom/entity visibility
Action layer
restrict operations such as import, review, relation creation
Output layer
restrict what may appear in assemblies or projections

4. Actor classes

Actor class
Meaning
Reader
may inspect allowed objects
Researcher
may access broader read-only analytical contexts
Reviewer
may adjudicate trust states and review packets
Editor
may submit structured changes and new relations
Importer
may submit external analysis bundles
Operator
may manage pipelines and release operations
Administrator
may manage policy and access controls
ServiceAccount
non-human system actor with constrained privileges

5. Core permissions

Permission
Meaning
read_object
inspect object by ID
query_collection
run filtered retrieval
assemble_output
generate rendered outputs
view_provenance
inspect lineage details
view_forensic
inspect full forensic provenance
create_relation
create governed relations
import_analysis
submit external analysis envelope
change_validation_state
promote or dispute objects
manage_projection
create and persist projections
manage_policy
update governance rules
operate_pipeline
run refinery or import jobs

6. Scope descriptors for access


Authorization SHOULD operate with scopes such as:

Scope type
Example
project scope
project_alpha
repository scope
repo_refinery
source scope
specific source IDs
domain scope
policy, code, research, operations
sensitivity scope
public, internal, restricted, privileged
environment scope
development, staging, production

7. Object sensitivity classes


Every stored object SHOULD carry a sensitivity class.

Sensitivity class
Meaning
Public
broadly viewable
Internal
authenticated internal readers
Restricted
limited by role and scope
Privileged
limited to reviewers/operators/admins
Sealed
accessible only via special policy or emergency route

8. Access decision model


An access decision SHOULD be computed as:

Factor
Question
authenticated
who is the actor
role fit
does the role allow the requested action
scope fit
does the actor have required project/domain scope
sensitivity fit
is the object too sensitive for this actor
trust fit
may the actor see low-trust or disputed objects
mode fit
is the output mode allowed for this actor

9. Read rules


9.1 Direct object read


A direct object read MAY succeed even for superseded or disputed objects if the actor has inspection rights. Read access and normal assembly eligibility are distinct concepts.


9.2 Collection query read


Collection queries MUST filter inaccessible objects before ranking and return stable semantics for filtered results.


9.3 Provenance read


Forensic provenance SHOULD be more restricted than summary provenance.

Provenance level
Minimum role suggestion
summary
Reader
inline
Reader / Researcher
appendix
Researcher / Reviewer
forensic
Reviewer / Operator / Administrator

10. Mutation rules

Mutation
Minimum role
create relation
Editor or above
import analysis
Importer or above
promote validation state
Reviewer or above
dispute object
Reviewer or above
change governance policy
Administrator
rerun or operate pipeline
Operator or Administrator

11. Analytical lane access


Because the analytical lane is derivative and may contain unstable interpretations, its visibility SHOULD be role- and mode-aware.

Analysis state
Typical visibility
IMPORTED
Importer, Reviewer, Operator
MACHINE_DERIVED
Researcher, Reviewer, Operator
REVIEWED
Researcher, Reviewer, Operator
ACCEPTED
same as primary substrate visibility unless sensitivity says otherwise
EXPERIMENTAL
Researcher, Reviewer, Operator
DISPUTED
Reviewer, Operator, Administrator by default

12. Projection access


A projection MUST NOT reveal objects the actor could not independently access. Projection convenience does not override object-level authorization.


13. Error semantics

Access error
Meaning
unauthorized
not authenticated or invalid identity
forbidden
authenticated but lacks permission
filtered
object exists but removed by policy from this result
redacted
object partially accessible but sensitive fields hidden

14. Final normative judgment


A valid UAKS-v1 access implementation MUST enforce authorization across query, assembly, provenance, mutation, and projection layers, MUST not let projections bypass object restrictions, and SHOULD distinguish clearly between visibility and assembly eligibility.
