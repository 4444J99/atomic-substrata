---
source_export: "ChatGPT-Branch \u00b7 Atomic Knowledge Assembler (1).json"
pair_number: 9
prompt_title: "Have we designed the metadata and YML frontmatter unique ID info? And if so, how do we ensure that it is in sync with what the codebase will be that it is getting implemented into? Right, we're gonna process non-atomic writing and documents as the knowledge, but then there's a codebase that already kind of exists."
response_title: "Not fully."
prompt_sha256: "2251b8cfdf6b685b07b1d82c13fce6220c2ad5ce8a9372d3383e1de43103592b"
response_sha256: "672d11d47a81dd5b746dbcdcea84835b68ec868dd273a1a3ace4e07a132b9d74"
---

# Pair 009

## Prompt

Have we designed the metadata and YML frontmatter unique ID info? And if so, how do we ensure that it is in sync with what the codebase will be that it is getting implemented into? Right, we're gonna process non-atomic writing and documents as the knowledge, but then there's a codebase that already kind of exists.

## Response

Not fully.


We have designed the identity model, the object families, the provenance model, and the core schema fields, but we have not yet finalized a canonical human-facing metadata / YAML frontmatter standard for files, notes, specs, or code-adjacent artifacts.


So the answer is:


The substrate-level metadata model exists.
The file-level frontmatter convention does not yet exist as a locked artifact.


That is the next thing to formalize if you want the repository layer and the atomic layer to stay coherent.


1. What already exists


What is already designed at the architecture level is this:

Designed already
Status
Stable logical identity for atoms
Yes
Content hash / immutable state identity
Yes
Provenance references
Yes
Validation states
Yes
Supersession model
Yes
Source object registration
Yes
Recipe identity
Yes
Analysis run identity
Yes

So the database / graph / CAS layer already has an identity model.


What is still missing is the artifact-envelope model for human-authored files.


That means things like:

Not yet fully formalized
Status
YAML frontmatter schema for documents
Not finalized
File-level unique ID convention
Not finalized
Mapping between file IDs and atom IDs
Not finalized
Mapping between repo paths and canonical source objects
Not finalized
Rules for code-file metadata headers
Not finalized
Sync protocol between frontmatter and graph metadata
Not finalized

2. The important distinction


You now have two metadata planes that must be kept separate but linked.


A. Artifact-level metadata


This is the metadata attached to a source file, note, markdown document, spec, transcript, or code file.


Examples:


document_id
source_id
project_id
title
created_at
updated_at
author
tags
status
schema_version


This is what YAML frontmatter is good for.


B. Atom-level metadata


This is the metadata attached to refined atomic objects after ingestion.


Examples:


atomId
contentHash
atomType
provenanceRef
validationState
supersedes
embeddingRef


This is not something you want manually maintained in frontmatter for every atom.


So the rule should be:


Frontmatter describes artifacts.
The substrate schema describes atoms.


That separation is critical.


3. What should get a frontmatter envelope


Not everything in the codebase needs YAML.


The clean design is:

Object
Frontmatter?
Reason
Markdown design docs
Yes
Human-authored knowledge artifact
Specs / memos / charters
Yes
Strong document identity needed
Research notes
Yes
Good source registration and traceability
Prompt manuals / protocol docs
Yes
Stable governance objects
Plain code files
Usually no
Native language syntax should remain clean
Config files
Case-by-case
Depends on format
Generated artifacts
No
Metadata should live in manifest, not hand-edited header

So for the existing codebase, I would not force YAML frontmatter into every source file unless the language or repo conventions make that clean and safe.


For code, metadata should usually come from:


repo path
git history
parser output
module declarations
manifest files
sidecar metadata


rather than inline YAML at the top of every file.


4. The correct sync model


You asked the core question: how do we ensure this stays in sync with the codebase that already exists?


The answer is: do not make manual frontmatter the source of truth for code synchronization.


That will drift.


Instead, use a three-layer sync model.


Layer 1 — Canonical source registration


Every file or artifact entering the system gets a source_id.


That source_id is the stable bridge between the repository object and the substrate object.


For example:

Field
Meaning
source_id
Canonical internal identity for the artifact
repo_uri
Repository identity
repo_path
Current logical file path
git_commit_first_seen
First observed commit
git_commit_last_seen
Most recent observed commit
content_hash
Exact file content fingerprint
artifact_kind
doc, code, config, note, transcript

That is the real sync anchor.


Layer 2 — Artifact envelope


For human-facing docs, add frontmatter with a stable source_id or document_id.


Example:


---
document_id: doc_uaks_architecture_20260311_001
source_id: src_01HTY6D9K8C2M4P7QW3X9Z2R5N
title: Unified Atomic Knowledge Substrate v1
artifact_kind: specification
project_id: proj_uaks
status: draft
schema_version: 1.0
created_at: 2026-03-11
updated_at: 2026-03-11
tags:
  - architecture
  - ontology
  - atomic-knowledge
supersedes: []
---


This is good for docs because the author can see and maintain it.


Layer 3 — Refinery-derived atomic layer


Once ingested, the refinery creates atoms and binds them back to the source via:


source_id
source_span
content_hash
provenance_ref


That means sync is computed, not hand-maintained.


5. The rule for the existing codebase


For the codebase that already exists, do not start by editing all files to add frontmatter.


That would be disruptive and brittle.


Instead:


Phase A


Treat the current codebase as registered source artifacts.


Each file gets:


source_id
repo_path
repo_commit_context
file_hash
language
parser_status


from the intake layer.


Phase B


The code refinery parses those files and emits CodeAtoms.


Each emitted CodeAtom carries:


source_id
ast_span
symbol_name
content_hash
module_path


Phase C


Only after that, decide whether selected code-adjacent files need sidecar metadata or inline headers.


That is the safe migration path.


6. How frontmatter and codebase remain in sync


The practical answer is:


Frontmatter should never be the only sync mechanism.


You keep sync by reconciling four things:

Sync axis
Mechanism
File identity
stable source_id
File state
content_hash
Repo location
repo_path + git metadata
Atomic derivation
provenance links from source to atoms

So if a file moves, the system still knows it is the same logical artifact because of source_id and lineage.


If a file changes, the content_hash changes.


If atoms need regeneration, provenance shows which source and which spans must be re-refined.


That is far more reliable than trusting hand-edited YAML alone.


7. Recommended ID architecture


You should define different IDs for different ontological levels.


Do not overload one ID for everything.


Recommended model:

ID Type
Example role
project_id
identifies the broader system/project
source_id
identifies an ingested artifact or file
document_id
human-facing identifier for authored document
atom_id
identifies an atomic object
recipe_id
identifies an assembly plan
analysis_run_id
identifies one external analysis execution
entity_id
identifies a domain object

That separation prevents chaos later.


8. Best metadata strategy for docs vs code


For non-atomic writing and documents


Use YAML frontmatter.


That is appropriate and useful.


Recommended minimum fields:


---
document_id:
source_id:
title:
artifact_kind:
project_id:
status:
schema_version:
created_at:
updated_at:
author:
tags: []
supersedes: []
related_sources: []
---


For codebase artifacts


Prefer registry + parser + sidecar manifest.


Recommended minimum source registry fields:


source_id:
repo_id:
repo_path:
artifact_kind:
language:
content_hash:
git_first_seen:
git_last_seen:
parser_status:
schema_version:


This can live in the system registry, not necessarily inside the file.


9. What has to be synchronized automatically


The following should be machine-synchronized, not hand-maintained:

Field
Why
content_hash
derived from actual file contents
updated_at
derived from ingestion or git state
repo_path
derived from current repository
git commit refs
derived from VCS
parser_status
derived from code refinery
atom provenance links
derived during refinement

The following can be human-maintained:

Field
Why
title
semantic label
tags
human categorization
status
draft/review intent
author
ownership/context
supersedes
document-level governance

10. What we should draft next


So the truthful answer is:


No, the YAML/frontmatter spec is not yet fully designed.
Yes, the underlying identity model is already designed.
The correct way to sync it with the existing codebase is through a source registry and provenance bridge, not by trusting inline metadata alone.


The next concrete artifact should be:


Metadata and Identity Charter v1


It should define:

Section
Content
ID namespaces
project_id, source_id, document_id, atom_id, etc.
Frontmatter schema
for markdown/spec/research artifacts
Source registry schema
for code and all ingested files
Sync rules
how file changes propagate into substrate changes
Canonical hashing rules
how content state is fingerprinted
Sidecar policy
when metadata lives beside code instead of inside it
Migration policy
how the existing codebase is registered without disruption

11. My recommendation for your current situation


Because you already have a codebase and you also have non-atomic documents, the best architecture is:


documents get frontmatter
code gets source registration
atoms get substrate metadata
sync is enforced through provenance and hashing


That is the cleanest way to avoid drift between the repository as humans see it and the knowledge substrate as the assembler sees it.


The correct next move is to draft the Metadata and Identity Charter v1 before implementation begins.