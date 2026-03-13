---
title: "Addenda Timing Guidance"
artifact_id: docs::00_meta::addenda_timing_guidance.md
pair_id: CHATPAIR-005
status: drafted_in_chat
generated_at: 2026-03-12T19:28:12Z
---

Now.


The best point to introduce external addenda is before the ontology charter and schema pack are drafted, because those two artifacts will lock vocabulary, object boundaries, and relation semantics. If the addenda materially affect atom classes, provenance rules, CAS assumptions, graph relations, code granularity, or interface design, bringing them in later creates avoidable churn.


Operationally, the best sequence is:

Timing
Value
Before Ontology Charter v1
Highest value; changes can still shape the conceptual model
Before Schema Pack v1
Very high value; prevents schema rework
Before refinery specs
High value if the addenda affect atomization logic
After GraphQL contract
Much lower value; likely causes cascading revisions

So the correct answer is: provide them in the next message.


If they are long, paste both in full and label them ADDENDUM_A and ADDENDUM_B. If they conflict with the current v1 spec, I will normalize them into one of three buckets:

Bucket
Meaning
Accept
Should be integrated directly into v1
Defer
Good idea, but better for v1.1+
Reject / isolate
Conflicts with core architecture or introduces instability

Then I will revise the architecture baseline accordingly before moving to the ontology charter.
