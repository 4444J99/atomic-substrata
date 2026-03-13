---
title: "Addendum Memorandum"
artifact_id: "branch_addendum_memorandum_generation_2_migration"
kind: "branch_non_id_document"
source_export: "ChatGPT-Branch \u00b7 Atomic Knowledge Assembler.json"
source_pair_number: 4
source_title_exact: "Addendum Memorandum"
generated_at: "2026-03-12T20:19:51Z"
branch_only: true
---

Addendum Memorandum


Subject: Architectural Evolution Plan for the Atomic Knowledge Assembler System
Relation to Existing Repository: Conceptual Mapping and Expansion
Status: Draft
Purpose: Establish a forward architectural path that builds upon the existing system while avoiding duplication of implementation artifacts.



1. Context


The current repository represents a functioning knowledge ingestion, indexing, and retrieval environment capable of extracting value from conversations, documents, and external sources.


Its capabilities include:


FTS-based search
vector similarity retrieval
LLM-assisted extraction
multi-source ingestion
relationship inference
web and CLI interfaces


These elements already provide a practical knowledge extraction system.


However, the architectural ambition has evolved toward something structurally stronger:


an Atomic Knowledge Assembler, where knowledge exists as governed semantic primitives that can be recomposed into arbitrary outputs.


The current repository should therefore be interpreted as Generation-1 infrastructure.


This memorandum describes how to evolve it into Generation-2 architecture without discarding the functioning foundation.



2. Architectural Shift


The most important conceptual shift is:


documents are no longer primary storage objects


Instead:


Atomic units become the persistent substrate.
Documents become assembled projections.


Generation-1 organizes knowledge around sources.


Generation-2 organizes knowledge around semantic primitives.


The goal is to transform the system from:


Source → Index → Retrieve


into:


Source → Refinery → Atomic Graph → Assembly Engine



3. Generation-1 Capabilities (Retained)


The following subsystems from the current repository remain valid and should be retained.


Ingestion Layer


Existing multi-source ingestion is valuable and should remain.


These include:


conversation exports
local files
notes
documents
browser captures
API-accessible content


In Generation-2 this becomes the Source Intake Layer.


The existing adapters can remain largely intact.



Hybrid Retrieval Stack


The combination of lexical search and vector similarity is appropriate.


Hybrid retrieval provides:


precision via lexical matching
semantic recall via embeddings


This capability remains necessary in the future system.


However, retrieval should operate on atoms, not on source fragments.



CLI and Web Interface


The interface layers are also valuable.


They provide:


interactive exploration
manual review capability
debugging surfaces


In Generation-2 these interfaces become assembly portals rather than simple search dashboards.



4. Components Requiring Refactoring


Several components must be structurally redesigned.



4.1 Atom Definition


The current atomic unit concept is primarily a searchable snippet.


Generation-2 requires a stronger definition.


An atom must be:


self-contained
contextually typed
provenance-linked
machine-addressable


Atoms therefore become first-class semantic objects.


Required Atom Classes


The architecture should support multiple atom types.


Examples include:


TextAtom
CodeAtom
EvidenceAtom
RelationAtom
PolicyAtom
RecipeAtom


Each atom type represents a distinct functional role in reasoning.



4.2 Immutable Identity


Atoms require stable identifiers.


Each atom must have:


a permanent identifier
a content fingerprint
a provenance reference


Content fingerprints allow the system to detect mutation and supersession.


This introduces state mutation rather than version numbering.



4.3 Provenance Precision


Generation-1 provenance references sources at coarse levels.


Generation-2 requires precise lineage.


Each atom must track:


origin artifact
exact location within artifact
transformation operations applied


This enables auditing, verification, and error correction.



4.4 Supersession


Atomic systems require explicit change handling.


Instead of overwriting existing data:


old_atom → superseded_by → new_atom


This allows the system to track knowledge evolution.



4.5 Assembly Recipes


Outputs must not be stored as static text artifacts.


Instead the system stores assembly recipes.


A recipe contains:


ordered atom identifiers
template instructions
resolution level


This enables outputs to regenerate automatically when atoms change.



5. Refinery Pipeline


Generation-2 introduces a formal knowledge refinery.


The refinery converts raw sources into governed atoms.


The pipeline consists of:


source segmentation
entity extraction
proposition decomposition
atomic distillation
metadata crystallization
deduplication
validation


The result is a set of semantic primitives suitable for recomposition.



6. Code Corpus Integration


The most significant expansion concerns code handling.


The Generation-1 system treats code primarily as text fragments.


Generation-2 must treat code as executable primitives.



6.1 Code Atoms


Code atoms represent functional units.


Typical examples include:


functions
methods
classes
modules
configuration blocks
test cases


Each code atom carries structured metadata such as:


runtime language
dependency references
input/output signatures
side-effect classification
complexity indicators



6.2 AST-Driven Refinement


Code must be parsed structurally.


Instead of regex extraction, the system should analyze:


syntax trees
symbol graphs
dependency relationships


This enables the system to understand intent rather than raw text.



6.3 Dependency Graph


Code atoms form dependency structures.


These structures are represented as directed graphs.


Dependency awareness enables:


impact analysis
automatic propagation of fixes
cross-project bug awareness



6.4 Cross-Domain Linking


A key feature is text-to-code bridging.


Examples include:


policy atoms referencing enforcement logic
documentation atoms referencing implementation atoms
test atoms verifying code atoms


This creates a unified knowledge-logic graph.



7. Storage Architecture Evolution


The storage model should expand into a hybrid system.


The Generation-2 architecture contains four layers.


Graph Substrate


Stores relationships and dependency structures.


Vector Substrate


Stores embeddings for semantic retrieval.


Source Archive


Stores immutable raw artifacts.


Content-Addressable Store


Stores immutable atom payloads referenced by hash.


This layered approach balances:


semantic search
logical reasoning
historical traceability



8. Assembly Layer


The assembly engine converts atoms into outputs.


This process includes:


scope determination
atom selection
structural arrangement
connective synthesis


The assembly layer allows the same knowledge to appear as:


summaries
technical documentation
analysis reports
decision memos



9. Governance Layer


Atomic knowledge systems require governance.


Important governance functions include:


validation states
contradiction handling
trust weighting
policy enforcement


Without governance the atomic pool becomes noisy.



10. Migration Strategy


The existing repository should evolve gradually.


A recommended approach is parallel schema introduction.


Generation-2 atoms can coexist with existing units.


Migration steps include:


introducing new atom schema
adding a refinery pipeline
gradually shifting retrieval to new atoms
maintaining compatibility during transition


This approach preserves operational functionality while evolving the system.



11. Conceptual Model


The final architecture may be summarized as:


Sources
   ↓
Refinery
   ↓
Atomic Graph
   ↓
Assembly Engine
   ↓
Rendered Knowledge



12. Strategic Outcome


When complete, the system functions as a knowledge operating system.


Knowledge becomes:


composable
traceable
update-propagating
cross-domain


Documents, summaries, and analyses become temporary renderings of atomic truth.



13. Next Recommended Step


The next document should define the Generation-2 atom schema and identity model.


This schema will determine:


data structure
refinery behavior
storage design
assembly semantics


Because once atom identity is defined, the remainder of the system follows logically.



If useful, the next step could also include a visual architecture diagram showing the full refinery → atom pool → assembly pipeline, because that will make the system dramatically easier to reason about during development.
