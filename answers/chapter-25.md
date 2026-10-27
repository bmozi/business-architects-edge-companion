# Chapter 25: Operate Events and Recover State — worked answers

Harbor, E9 and all counts are fictional; no event flow is deployed or approved. R7 receipt for review never establishes satisfaction. The existing assistant remains staff-draft-only, with no independent send, learner-record write, eligibility or case action.

## Conceptual teach-back

A published event is not yet an applied view; an applied view is not necessarily a current or correct business answer. Queue count/age describe transport under product-specific rules, not source-to-view equality or learner understanding. A failure hold needs an owner and controlled return. Redrive re-enters processing; it is not automatically safe. A broker-assigned message ID may change on redrive, whereas the event producer's `(source,id)` should remain the same logical event identity under this proposed contract.

## Paper packet worked answer

Five defensible actions, in order, with stop gates:

1. **Contain:** Keep portal wording at approved receipt-only or truthful stale/unknown state and accepted human route. Do not display “R7 complete” or send notices. Operations and release/Policy own the stop/wording decision.
2. **Diagnose source:** Source owner proves whether E9 committed, what schema/version/meaning it carries, and whether outbox publication is pending. If E9 is only a reserved number, do not invent it; obtain an authoritative skip disposition under the source contract.
3. **Inspect failure hold:** Engineering with Policy/Security compares the unknown schema field with approved source meaning and data classification. Ignore-only parsing is unsafe until meaning and compatibility are established. Restrict access to any sensitive payload.
4. **Repair and replay:** Fix the handler or relay only after decision; redrive original E9 identity through a view-only path at a bounded rate, with processed-ID/inbox and sequence checks. No notice send or case effect. Apply E9 then held E10 only under the approved per-learner ordering rule, and acknowledge after durable view commit.
5. **Verify and return:** Reconcile latest source ID, per-learner sequence, schema/Policy meaning version and protected portal view; test duplicate/out-of-order negative cases and accessible stale fallback. Policy, Security, Support/receiving and release owners decide their conditions. Monitor after return; keep manual route if any condition is absent.

From the separate 100-source-ID worksheet, `1 + 3 = 4` IDs are **not fully reconciled**; 96 have both identity and version agreement. Zero visible queue messages does not reduce four to zero. One ignored duplicate delivery is outside the 100 distinct-ID denominator. This says nothing about actual Harbor quality or learner outcomes.

Accept a simpler answer that does not redrive because the event projection is unnecessary and current static/manual path can meet the need, provided it names who checks the source and how learners get an accurate answer.

## Two common wrong answers and feedback

- “The queue is empty, so the incident is over.” Feedback: compare authoritative source identities and versions with consumer view; inspect hold/DLQ and learner-facing meaning. Transport and business state are different.
- “Redrive everything after adding an ignore-unknown-fields parser.” Feedback: the new field may change meaning or contain protected data; a broad redrive can duplicate external effects and overload a receiver. Verify schema/meaning, restrict scope/rate, replay view-only and reconcile.

A third error is deduplicating by the broker's new message ID after redrive; use the stable producer `(source,id)` under the event contract.

## Transfer rubric (12 points)

Award 0–2 each for: (1) source/consumer/display facts separated; (2) detection using outbox, queue/DLQ, gap, schema and source-to-view reconciliation rather than one green metric; (3) access/minimization/retention of held payload; (4) scoped replay with stable identity, order, idempotent view and external side effects disabled; (5) named owner, stop/manual route, correction and return evidence; (6) justified event versus simpler alternative, bounded AI contribution and resilience when AI is down. Full marks require one failure that a queue metric misses and a condition that blocks redrive.
