---
title: "1 Supersession Policy v1"
artifact_id: uaks_v1_supersession_policy_20260311
pair_id: CHATPAIR-017
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

1 Supersession Policy v1


Document ID: uaks_v1_supersession_policy_20260311


1.1 Purpose


Supersession defines how atoms are replaced when knowledge evolves.


Atoms are never overwritten. Instead a new atom replaces the old one via a relation.


old_atom  →  IS_SUPERSEDED_BY  →  new_atom


This preserves the complete knowledge history.



1.2 Supersession triggers


Supersession occurs when:

Trigger
Example
policy revision
rule updated
factual correction
incorrect statement corrected
analysis refinement
improved analytical interpretation
code revision
function implementation changed
ontology revision
classification corrected


1.3 Supersession requirements


A valid supersession requires:

Requirement
Meaning
new atom created
old atom preserved
relation recorded
explicit supersession edge
provenance recorded
reason for replacement
timestamp
time of change
reviewer validation
if high-impact


1.4 Supersession chain


Supersession chains form temporal lineage.


Atom A (2024)
   ↓ superseded_by
Atom B (2025)
   ↓ superseded_by
Atom C (2026)


Assemblies default to latest accepted atom.


Historical views may access older atoms.



1.5 Supersession safety rules


Assemblies MUST NOT:


mix superseded atoms with current atoms

hide supersession chains

discard historical atoms
