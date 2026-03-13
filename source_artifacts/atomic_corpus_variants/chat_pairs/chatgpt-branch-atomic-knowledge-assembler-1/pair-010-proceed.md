---
source_export: "ChatGPT-Branch \u00b7 Atomic Knowledge Assembler (1).json"
pair_number: 10
prompt_title: "Proceed"
response_title: "Metadata and Identity Charter v1"
prompt_sha256: "f01847dfc94126426b4849004762a12557de2332ae0ca1b4602210b341f0281b"
response_sha256: "a6b4464f5880d1f799d78c910146d110825b3f76123596c8e4dfee11816e61f2"
---

# Pair 010

## Prompt

Proceed

## Response

Metadata and Identity Charter v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_metadata_identity_charter_20260311
Version: 1.0-draft
Status: Draft normative charter



0. Purpose


This charter defines the canonical metadata, identity, frontmatter, registry, and synchronization model for UAKS-v1.


Its purpose is to ensure that:


the human-facing repository remains legible,
the implementation codebase remains stable,
the knowledge substrate remains governable,
and all three stay synchronized without relying on brittle manual editing.


This document resolves the boundary between:


artifact-level metadata,
source-registry metadata,
and atom-level substrate metadata.



1. Governing Principle


The system MUST distinguish three metadata planes.

Plane
What it describes
Canonical storage location
Artifact plane
Human-authored documents and repository-visible artifacts
YAML frontmatter or equivalent envelope
Source plane
Registered ingested files and source objects
Source registry
Atomic plane
Refined atoms and substrate objects
Graph / metadata store / CAS-linked substrate

These planes MAY reference one another, but they MUST NOT be collapsed into one field set.



2. Core Rule


The canonical rule is:


Frontmatter describes artifacts.
The source registry describes ingested files.
The substrate schema describes atoms.


This means:


A markdown specification SHOULD have frontmatter.
A code file SHOULD be registered as a source object.
A CodeAtom SHOULD be created from parsing and provenance, not from hand-authored YAML at the top of the code file.



3. Identity Model


The system MUST use multiple identity namespaces. One identifier MUST NOT be overloaded to represent project, file, atom, and recipe simultaneously.


3.1 Canonical ID namespaces

ID Namespace
Purpose
Stability
project_id
Identifies a project or program boundary
Stable
repo_id
Identifies a repository
Stable
source_id
Identifies one ingested artifact/file/source object
Stable
document_id
Human-facing identifier for authored document artifacts
Stable
atom_id
Identifies one atomic substrate object
Stable
entity_id
Identifies a domain entity
Stable
recipe_id
Identifies an assembly recipe
Stable
analysis_run_id
Identifies one external analysis execution
Stable
import_job_id
Identifies one ingestion/normalization job
Event-scoped
relation_id
Identifies one graph edge when explicitly materialized
Stable
provenance_id
Identifies one provenance record
Stable
template_id
Identifies an assembly template
Stable

3.2 Identity requirements

Rule ID
Requirement
MID-01
Every major object family MUST have its own namespace.
MID-02
IDs MUST be globally unique within their namespace.
MID-03
IDs SHOULD remain stable even if file path, title, or display label changes.
MID-04
Human-readable identifiers MAY exist, but internal canonical IDs MUST remain machine-safe and collision-resistant.
MID-05
File path MUST NOT be treated as canonical identity.
MID-06
Content hash MUST NOT replace logical identity. Both are required.


4. Logical Identity vs Content Identity


The system MUST separate logical identity from exact content state.

Identity Type
Meaning
Example behavior
Logical identity
What object this is conceptually
Same document after title edit
Content identity
What exact payload state exists right now
New hash after one line changes

4.1 Required fields

Field
Meaning
*_id
Stable logical object identity
content_hash
Immutable fingerprint of exact content payload
schema_version
Version of metadata contract governing the object
supersedes
Prior logical object or prior state if governed that way

4.2 Normative rule


A content change MUST produce a new content_hash.


A governed logical update MAY preserve the same logical identity if the object model allows mutable metadata with immutable payload lineage, or MAY create a successor object linked through supersession if the object is treated as immutable-at-logical-layer.


For atoms, verified content MUST NOT be silently overwritten.



5. Frontmatter Policy


5.1 Where frontmatter belongs


Frontmatter is appropriate for human-authored, repository-visible knowledge artifacts.

Artifact Type
Frontmatter policy
Markdown specifications
Required
Memos
Required
Charters
Required
Research notes
Required
Governance documents
Required
Prompt manuals
Required
ADR-style records
Recommended
Plain source code files
Not required by default
Generated artifacts
Not recommended
Binary files
Not applicable

5.2 Why code files usually should not get YAML frontmatter


Most code files already have syntax, parser expectations, formatter rules, and language-specific conventions. Injecting YAML into all code files creates noise, parser risk, and maintenance friction.


For code, the system SHOULD prefer:


source registration,
VCS metadata,
AST parsing,
symbol extraction,
and sidecar metadata where needed.



6. Canonical Frontmatter Schema for Documents


This schema applies to human-authored document artifacts such as markdown specs, charters, memos, research writeups, and knowledge notes.


6.1 Minimum required fields

Field
Required
Meaning
document_id
Yes
Stable document identity
source_id
Yes
Canonical ingested source identity
title
Yes
Human-readable title
artifact_kind
Yes
specification, memo, charter, note, etc.
project_id
Yes
Owning project
status
Yes
draft, review, active, archived, etc.
schema_version
Yes
Metadata schema version
created_at
Yes
Original creation date/time
updated_at
Yes
Last metadata/content update date/time
tags
Yes
Human tags
supersedes
Yes
Prior document IDs if any, else empty array

6.2 Recommended fields

Field
Meaning
author
Human or system author
repo_id
Repository identity
canonical_path
Preferred repository path
related_sources
Linked source IDs
related_documents
Linked document IDs
related_entities
Linked entity IDs
validation_state
Draft/review/verified for document governance
rights_class
Access or sensitivity class
summary
Short description
template_id
If document follows a known template
assembly_recipe_id
If document was assembled from recipe

6.3 Canonical frontmatter example


---
document_id: doc_uaks_v1_architecture_spec_20260311_001
source_id: src_01HTY6D9K8C2M4P7QW3X9Z2R5N
title: Unified Atomic Knowledge Substrate v1
artifact_kind: specification
project_id: proj_uaks
repo_id: repo_uaks_core
status: draft
schema_version: 1.0
created_at: 2026-03-11T00:00:00Z
updated_at: 2026-03-11T00:00:00Z
author: system
tags:
  - architecture
  - ontology
  - atomic-knowledge
supersedes: []
related_sources: []
related_documents: []
related_entities: []
validation_state: REVIEWED
rights_class: internal
summary: >
  Foundational architecture specification for the unified atomic
  knowledge and code substrate.
---



7. Source Registry Charter


The source registry is the canonical bridge between repository-visible artifacts and the substrate.


Every ingested file or source artifact MUST be represented by a source_id.


7.1 What counts as a source object

Source Type
Example
Document source
Markdown spec, note, memo
Code source
.py, .ts, .rs, .sh, etc.
Config source
YAML, TOML, JSON, env template
Transcript source
Chat export, interview transcript
Archive source
PDF, DOCX, HTML snapshot
Analysis bundle source
External analysis export package

7.2 Minimum source registry fields

Field
Required
Meaning
source_id
Yes
Stable source identity
repo_id
No
Owning repository if applicable
repo_path
No
Current repository path
artifact_kind
Yes
doc, code, config, transcript, bundle, etc.
mime_type
Yes
Media type
language
No
Source language where applicable
content_hash
Yes
Exact file/object fingerprint
git_first_seen
No
First observed commit/ref
git_last_seen
No
Most recent observed commit/ref
parser_status
No
parseable, partial, failed, n/a
archive_ref
Yes
Raw archive location
ingested_at
Yes
Ingestion timestamp
schema_version
Yes
Registry schema version

7.3 Recommended source registry fields

Field
Meaning
canonical_uri
Stable URI or canonical locator
file_size_bytes
Size
checksum_algorithm
Hash algorithm
detected_encoding
Text encoding
line_count
Structural count for text/code
owner_ref
Owning person/team/system
rights_class
Access policy
supersedes_source_id
Prior source object if modeled
language_runtime
Runtime environment
module_namespace
Technical namespace if applicable

7.4 Canonical source registry example for a code file


source_id: src_01JCODEFILE9K8C2M4P7QW3X9Z2
repo_id: repo_uaks_core
repo_path: src/refinery/code/parser.ts
artifact_kind: code
mime_type: text/typescript
language: typescript
content_hash: sha256:8c7f5d7fa1f1d7b5e9f2b4b2d4c77d32aa4fd9d6db3c8e70bb0c6d4a3f123456
git_first_seen: 1a2b3c4d
git_last_seen: 5e6f7a8b
parser_status: parseable
archive_ref: archive://raw/repo_uaks_core/src/refinery/code/parser.ts@5e6f7a8b
ingested_at: 2026-03-11T00:00:00Z
schema_version: 1.0



8. Atom Metadata Boundary


Atoms MUST NOT rely on frontmatter for their identity or lifecycle.


Atom metadata belongs to the substrate.


8.1 Minimum atom metadata fields

Field
Meaning
atom_id
Stable atom identity
atom_type
Text, code, policy, analysis, etc.
atom_class
Functional role
content_hash
Exact atom payload fingerprint
source_id
Source object from which it derives
source_span
Precise origin location
provenance_id
Lineage object
validation_state
Trust/lifecycle state
supersedes
Prior atom if applicable
created_at
Creation time
updated_at
Metadata update time

8.2 Boundary rule


A document may carry document_id and source_id in frontmatter.


A refined atom created from that document MUST carry atom_id, source_id, and source_span in the substrate, not in the original markdown header.



9. Synchronization Model


The system MUST synchronize repository artifacts and substrate objects through registry and provenance, not through manual metadata editing alone.


9.1 Sync layers

Layer
Canonical anchor
Human document sync
document_id + source_id
Code artifact sync
source_id + repo_path + VCS lineage
Substrate sync
source_id + content_hash + provenance_id
Cross-version sync
supersession and lineage edges

9.2 Machine-synchronized fields


The following fields SHOULD be system-derived rather than manually edited where possible.

Field
Why
content_hash
Derived from actual content
updated_at
Derived from modification or ingestion
repo_path
Derived from repository state
git_first_seen
Derived from VCS
git_last_seen
Derived from VCS
parser_status
Derived from refinery
source_span
Derived from parsing/segmentation
provenance_id
Derived from ingestion/refinement events

9.3 Human-maintained fields


The following fields MAY be human-maintained.

Field
Why
title
Human semantic labeling
summary
Human framing
tags
Human classification
status
Governance intent
author
Ownership context
supersedes
Document-level governance when explicit


10. Path Changes, Renames, and Moves


A path change MUST NOT destroy identity continuity.


10.1 Canonical rule


If a file moves from one path to another but remains the same logical source object, the source_id MUST remain stable.


The registry MUST update the current repo_path.


10.2 Rename semantics

Event
Identity effect
File renamed only
Same source_id
File moved only
Same source_id
Content changed
New content_hash
Artifact split into multiple new documents
New source_ids for resulting canonical artifacts, linked by provenance
Multiple sources merged
New target source object plus provenance links to originals


11. Existing Codebase Integration Policy


The current codebase already exists and SHOULD be integrated through source registration before any invasive metadata rewrite.


11.1 Required policy

Rule ID
Requirement
ECI-01
Existing code files MUST first be treated as source objects.
ECI-02
The system MUST assign each code artifact a source_id.
ECI-03
The code refinery MUST derive CodeAtoms from parser output and provenance.
ECI-04
Inline YAML frontmatter MUST NOT be forced into existing code files by default.
ECI-05
Sidecar manifests MAY be used for exceptional code metadata needs.

11.2 Safe migration sequence

Phase
Action
A
Register all existing code files as sources
B
Bind repo path, hash, language, VCS metadata
C
Parse and emit CodeAtoms
D
Add sidecar metadata only where necessary
E
Link policy/doc/test atoms to code atoms


12. Sidecar Metadata Policy


Where code-adjacent metadata is needed but inline file modification is undesirable, the system MAY use sidecar metadata files or registry-managed manifests.


12.1 Appropriate sidecar cases

Case
Recommendation
Parser exceptions
Sidecar allowed
Manual semantic annotation of module intent
Sidecar allowed
Legacy files that cannot be modified
Sidecar preferred
Generated code
Sidecar preferred
External vendored code
Sidecar preferred

12.2 Sidecar identity rule


A sidecar object MUST reference the canonical source_id of the artifact it annotates.


It MUST NOT create a competing identity system.



13. YAML Frontmatter Synchronization Rules


13.1 Artifact-to-registry sync


When a document with frontmatter is ingested:

Rule ID
Requirement
YFS-01
document_id and source_id MUST be read from frontmatter if present.
YFS-02
If source_id is absent, the intake system MAY create one and optionally write it back under governance rules.
YFS-03
The source registry MUST remain the canonical machine record.
YFS-04
Frontmatter and registry conflicts MUST be resolved by explicit precedence rules.

13.2 Precedence rules


Recommended v1 precedence:

Field category
Preferred source
Identity fields
Registry unless frontmatter explicitly authorizes canonical document ID
Path and VCS fields
Registry
Hash fields
Registry
Human semantic fields
Frontmatter
Derived parse fields
Refinery/substrate


14. Canonical Hashing Rules


The system MUST standardize how content is hashed.


14.1 Hashing policy

Rule ID
Requirement
HASH-01
The system MUST use a declared canonical hash algorithm.
HASH-02
The algorithm MUST be recorded in metadata where necessary.
HASH-03
Equivalent canonicalized payloads MUST produce equivalent hashes.
HASH-04
Canonicalization rules MUST be versioned.

14.2 Recommended v1 approach

Element
Recommendation
Hash algorithm
SHA-256
Text canonicalization
Normalize line endings, encoding, and trailing newline policy
Structured payload canonicalization
Stable key ordering where applicable
Code hashing
Hash raw source bytes and, where useful, optionally also normalized AST signature as separate derived measure

14.3 Important distinction


The system MAY maintain more than one fingerprint:

Fingerprint
Use
Raw content hash
Exact file state identity
Canonical payload hash
Stable normalized content identity
Structural hash
Optional AST or semantic structural fingerprint

These MUST NOT be confused.



15. Schema Versioning Policy


Every metadata-bearing object SHOULD declare the schema version under which it is interpreted.


15.1 Required objects

Object
Schema version required
Frontmatter-bearing documents
Yes
Source registry records
Yes
Atom records
Yes
Provenance records
Yes
Analysis import envelopes
Yes

15.2 Compatibility rule


Changes to metadata fields SHOULD be additive where possible.


Breaking changes MUST increment schema version and trigger migration rules.



16. Metadata Consistency Checks


The implementation SHOULD provide consistency audits.


16.1 Required audits

Audit
Purpose
Frontmatter vs registry identity audit
Detect mismatched source_id / document_id
Registry vs repository path audit
Detect moved/missing files
Registry vs hash audit
Detect stale registry records
Source-to-atom provenance audit
Detect orphan atoms
Frontmatter schema audit
Detect malformed metadata
Duplicate identity audit
Detect ID collisions
Sidecar linkage audit
Detect unattached sidecars


17. Repository Governance Rules


The repository and the substrate MUST evolve together under explicit governance.


17.1 Governance rules

Rule ID
Requirement
RG-01
Human-facing artifacts SHOULD carry stable document metadata if they are part of the governed knowledge corpus.
RG-02
Code files SHOULD remain syntactically clean unless a language-specific metadata header is explicitly approved.
RG-03
The source registry MUST be authoritative for ingested source synchronization.
RG-04
The substrate MUST be authoritative for atom metadata and provenance.
RG-05
Changes in implementation code SHOULD trigger re-refinement only for affected source objects.


18. Minimal v1 Metadata Profiles


18.1 Minimal document profile


---
document_id: doc_example_001
source_id: src_example_001
title: Example Document
artifact_kind: specification
project_id: proj_example
status: draft
schema_version: 1.0
created_at: 2026-03-11T00:00:00Z
updated_at: 2026-03-11T00:00:00Z
tags: []
supersedes: []
---


18.2 Minimal registry profile


source_id: src_example_001
artifact_kind: doc
mime_type: text/markdown
content_hash: sha256:...
archive_ref: archive://...
ingested_at: 2026-03-11T00:00:00Z
schema_version: 1.0


18.3 Minimal code registry profile


source_id: src_code_example_001
repo_id: repo_example
repo_path: src/module/example.ts
artifact_kind: code
mime_type: text/typescript
language: typescript
content_hash: sha256:...
archive_ref: archive://...
ingested_at: 2026-03-11T00:00:00Z
schema_version: 1.0



19. Final Charter Decision


The metadata system for UAKS-v1 is now defined as:

Layer
Canonical mechanism
Human document metadata
YAML frontmatter
File/source identity and sync
Source registry
Atomic object metadata
Substrate schema
Exact state identity
Content hash
Continuity over time
Supersession + provenance

That means the existing codebase can be integrated safely without rewriting every file, while the non-atomic writing and document corpus can become human-legible, frontmatter-governed source artifacts.



20. Immediate Next Artifact


The highest-value next artifact is:


Schema Pack v1


That should formalize:


the frontmatter schema,
the source registry schema,
the atom base schema,
the TextAtom schema,
the CodeAtom schema,
and the provenance schema


in machine-readable form.


The cleanest continuation is to draft Schema Pack v1 next.