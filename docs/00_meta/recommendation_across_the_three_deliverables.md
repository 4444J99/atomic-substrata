---
title: "Recommendation across the three deliverables"
artifact_id: docs::00_meta::recommendation_across_the_three_deliverables.md
pair_id: CHATPAIR-002
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Thought for 20s


Recommendation across the three deliverables


You asked for the cost and benefit profile of the three suggested next artifacts, and whether the code-centric atomic layer should be built together with the text-centric system or separately.


My recommendation is this:


Build the formal system architecture specification first, model the code corpus in the same conceptual program, and postpone the full pilot playbook until after the architecture and economics are stable. The code layer should be designed in unison at the schema and identity level, but implemented as a separate refinery and storage pipeline. The reason is structural: text atoms and code atoms can share IDs, provenance, graph relations, recipes, and assembly logic, but code requires AST-aware parsing, dependency analysis, runtime metadata, and stronger determinism than prose. Tree-sitter exists specifically to incrementally parse source into syntax trees, while content-addressable systems such as LLVM CAS and IPFS-style Merkle DAGs assume immutable objects identified by content hashes. GraphQL is suitable as the API contract because it is storage-agnostic and schema-driven rather than tied to one backend. GraphQL+6Tree-sitter+6LLVM+6


1. Formal system architecture specification


This artifact has the highest leverage and the lowest strategic regret. Its main benefit is that it forces you to settle the ontology, atom classes, identity model, provenance rules, supersession logic, retrieval contract, recipe persistence, and the boundary between graph, vector, raw-source, and CAS layers before you spend serious engineering time. Since graph databases are optimized for nodes, relationships, and traversals, and vector databases are optimized for similarity search on embeddings, the architecture spec is where you decide what each layer is allowed to do and what it is not allowed to do. Milvus+3Graph Database & Analytics+3Graph Database & Analytics+3


Its cost is mostly design labor and delay of visible demos. You will spend time resolving naming, schema boundaries, mutation policy, contradiction handling, and API semantics before you can point at a flashy prototype. The failure mode is over-abstracting and writing a grand theory that is too detached from the first working refinery. But among the three options, this is still the cheapest place to discover bad assumptions. The architecture artifact is also where you can decide whether the “Portal” idea is merely a virtual projection layer or a strict content-addressed workspace backed by Merkle-linked objects and immutable snapshots. IPFS documentation makes clear that content addressing and Merkle DAGs are excellent for immutable, verifiable objects, but that does not automatically mean you should adopt distributed IPFS networking for the first internal version. IPFS Docs+4IPFS Docs+4IPFS Docs+4


Net judgment: highest benefit, moderate cost, first thing to do.


2. Unit-economics / complexity simulation model


This artifact has the highest planning value for feasibility, especially if you are serious about scale. The benefit is that it converts an attractive conceptual system into resource terms: ingestion cost per source type, atomization yield, deduplication rate, embedding storage growth, graph edge growth, AST parse cost, retrieval latency, cache hit rate, recipe reuse rate, and human-review burden. It gives you a way to estimate whether this becomes a lightweight personal knowledge OS, a research platform, or an expensive infrastructure sink. Because Milvus is designed for scalable vector retrieval and Neo4j explicitly separates graph storage from graph analytics, a realistic economics model has to assume you are paying for multiple substrate types, not “one database.” Graph Database & Analytics+3Milvus+3Milvus+3


Its cost is that the model can become speculative if done too early. Without one or two real corpora, your assumptions about atom density, merge rates, dependency fan-out, and AST extraction success will be weak. This is especially true for the code layer, where function-level atomization may work very differently across Python, JavaScript, Rust, shell, notebooks, and generated code. Still, even a rough simulation is useful because it surfaces where costs are nonlinear. CAS systems deduplicate immutable identical objects by content; that is a strong benefit, but it also means a large number of small objects, many hashes, indexing overhead, and recipe bookkeeping. LLVM’s CAS model explicitly treats objects as immutable value objects addressed by strong hashes, which is powerful but operationally more complex than plain file storage. IPFS Docs+3LLVM+3LLVM+3


Net judgment: second thing to do, after the architecture is stable enough to simulate against.


3. Pilot-scale operational playbook


This artifact has the highest execution value once the architecture is clear. Its benefit is practical: it translates theory into intake SOPs, validation workflows, error handling, review states, merge policy, rollback, re-indexing, supersession, and operator responsibilities. This is where you define how a real corpus enters the refinery, how disputed atoms are handled, how code-policy links are verified, how recipes are approved, and what counts as production-ready. It is the document that turns the architecture from a theory into an operational system. IPLD+3GraphQL+3GraphQL+3


Its cost is that it is premature if done before the other two. A playbook written too early becomes theater. You end up documenting procedures for components whose schema, scoring rules, and storage choices are still moving. In other words, this artifact becomes expensive when the underlying system is unstable, because every architecture change forces SOP rewrites. It has high value later, but it is not the correct first move unless you are forced to run a pilot immediately.


Net judgment: third thing to do, after architecture and a first-pass economics model.


Comparative view

Artifact
Primary benefit
Primary cost
Best timing
My rank
Formal system architecture specification
Settles ontology, boundaries, contracts, mutation rules, and backend roles
Up-front abstraction work, slower visible prototype
Immediately
1
Unit-economics / complexity model
Exposes scaling cost, review burden, storage growth, and latency risk
Depends on assumptions if done too early
Right after architecture v1
2
Pilot-scale operational playbook
Makes the system executable by humans and teams
Becomes stale fast if architecture is unsettled
After v1 architecture and model
3

Should the code-centric atomic feature be built in unison or separately?


The correct answer is both, but at different layers.


It should be built in unison conceptually and separately operationally.


The shared layer should include the identity model, provenance model, graph relation model, supersession rules, retrieval API, recipe format, temporal weighting, contradiction handling, and assembly semantics. This allows a business-rule text atom to point to the code atom that implements it, and lets a policy change trigger impact analysis across code and documentation. This is precisely where graph relations are strong: representing entities, relationships, and dependencies explicitly. Graph Database & Analytics+2Graph Database & Analytics+2


The separate layer should include the refinery and persistence behavior for code. Code is not just another prose source. It needs AST-aware parsing, dependency extraction, symbol resolution, runtime metadata, complexity metrics, and more rigid validation. Tree-sitter is built for concrete syntax trees and efficient incremental updates, which makes it a sensible parser layer for a code refinery. For storage, content-addressed immutability is a good fit for code atoms and build artifacts, as shown by LLVM CAS and by IPFS/IPLD’s use of CIDs and Merkle DAGs for immutable linked objects. IPFS Docs+5Tree-sitter+5LLVM+5


So the design rule is:


One ontology, two refineries.
One graph of truth, separate atomizers.
One retrieval contract, distinct storage optimizations.


What I recommend specifically


I recommend a phased hybrid architecture.


Phase 1 should define a unified atom schema that covers both prose atoms and code atoms, but with subtype-specific fields. For example, code atoms would add AST node type, signature, imports, runtime, dependency edges, side-effect profile, test coverage pointer, and content hash. Text atoms would retain source span, semantic type, evidentiary role, and temporal scope. Both would share IDs, provenance, graph edges, supersession, validation state, and recipe participation.


Phase 2 should implement text/document atoms first and code atoms second, but the schema must be designed for both from day one. This avoids the common mistake where the prose system becomes impossible to extend into executable logic later.


Phase 3 should use local or internal content-addressable storage, not full IPFS as a first deployment. IPFS and IPLD are valuable conceptual references for CIDs, Merkle DAGs, and linkable immutable objects, but for an internal system the distributed network layer is usually unnecessary overhead at the start. A Git-like or LLVM-CAS-like internal CAS is more appropriate initially; GraphQL can sit above it as a typed retrieval and assembly contract. GraphQL+6IPFS Docs+6IPFS Docs+6


Phase 4 should add cross-domain bridges: policy atom → requirement atom → test atom → function atom → build artifact atom → deployment state atom.


Where I would be cautious


I would not start with a fully versionless ideology in the literal sense. Content-addressable systems are immutable and excellent for exact states, but humans still need understandable revision semantics. IPNS exists precisely because immutable CIDs need a mutable naming layer above them. In practice, your system will want both immutable objects and stable human-facing names or portals. IPFS Docs+1


I would also not start with “pure function atomization” as the only code model. It works for many functions, but real code contains stateful procedures, I/O boundaries, configuration surfaces, class methods, declarative infrastructure, tests, migrations, UI components, and glue code that are not clean pure functions. AST-based extraction should therefore identify several code atom types, not just one.


I would also avoid assuming that vector retrieval alone can recover code intent. For code, symbol graphs, call graphs, import graphs, AST features, and test relations often matter more than raw embedding proximity. That is another reason the code layer should be a specialized subsystem, not merely “text atomization plus embeddings.”


Final recommendation


My ranked recommendation is:


First: formal system architecture specification.
Second: unit-economics / complexity simulation model.
Third: pilot-scale operational playbook.


For the added feature, I recommend:


Design it now in the same architecture. Implement it as a separate refinery and storage path.


That gives you a unified knowledge OS rather than two incompatible systems, while still respecting the fact that code is structurally different from prose.


The next best move is to draft a single v1 architecture spec that includes both TextAtom and CodeAtom as first-class types, plus a decision matrix for Graph + Vector + CAS + Raw Source Archive + GraphQL API.
