---
title: "Provenance Rendering Rules v1"
artifact_id: uaks_v1_provenance_rendering_rules_20260311
pair_id: CHATPAIR-011
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Provenance Rendering Rules v1


Unified Atomic Knowledge Substrate


Document ID: uaks_v1_provenance_rendering_rules_20260311
Version: 1.0-draft
Status: Draft normative rules


1. Purpose


These rules define how provenance is surfaced in rendered outputs, trace reports, review packets, portal projections, and inspection interfaces.


2. Provenance rendering thesis


Provenance must remain available without overwhelming every output. The system therefore supports graded provenance visibility based on output mode, template class, and trust context.


3. Provenance modes

Mode
Behavior
Hidden
provenance stored but not shown
Summary
high-level source summary shown
Inline
provenance attached near statements
Appendix
detailed lineage attached after main content
Forensic
full lineage, spans, operations, and states shown

4. Output-mode defaults

Output mode
Default provenance mode
Standard operational
Summary
Research
Inline or Appendix
Exploratory
Appendix
High-trust / compliance
Inline and Appendix
Review / adjudication
Forensic

5. Minimum provenance disclosure rules

Rule ID
Requirement
PRR-01
every rendered output SHOULD be able to resolve back to atom IDs used
PRR-02
high-trust outputs MUST expose source and validation lineage
PRR-03
analytical findings MUST be distinguishable from source-grounded claims
PRR-04
superseded or disputed objects MUST be visibly marked when shown
PRR-05
provenance summaries MUST not imply stronger certainty than underlying states justify

6. Statement-level rendering rules

Case
Rendering requirement
source-grounded primary claim
show source summary or inline reference when needed
accepted analysis finding
mark as analytical/derived
reviewed interpretation
mark inferential status where relevant
disputed object
visibly flag dispute
historical object
visibly flag non-current status

7. Provenance packet structure


A provenance packet SHOULD include:

Field
Meaning
atomId
governing atom reference
validationState
trust state
sourceRefs
raw source anchors
sourceSpans
exact locations where available
provenanceRefs
transformation lineage
supersessionStatus
current/historical
analysisRunRef
if analytical derivative
warnings
ambiguity, stale state, low trust

8. Rendering examples


8.1 Summary mode


Main statement followed by concise source note.


8.2 Inline mode


Main statement followed by compact provenance markers or structured parenthetical metadata.


8.3 Appendix mode


Main body remains readable; detailed atom and source table appears after body.


8.4 Forensic mode


Each claim is paired with atom identity, source span, transformation history, and trust state.


9. Final normative judgment


A valid provenance rendering implementation MUST preserve the distinction between source evidence and derivative analysis, MUST support stronger disclosure in higher-trust contexts, and SHOULD avoid clutter in low-friction summaries.
