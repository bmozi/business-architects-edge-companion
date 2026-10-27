# Chapter 24: Design Event-Driven Flows — worked answers

Harbor and the events are fictional. The current assistant remains staff-draft-only and cannot send/write/decide eligibility/create a case. R7 receipt for review does not imply requirement satisfaction. The event flow is conditional and unapproved.

## Conceptual teach-back

An event records an occurrence in past tense; a command asks a particular receiver to act. A published `DocumentReceived` fact does not prove that every consumer heard it, applied it or sent any message. CloudEvents provides common envelope fields. Its released 1.0.2 spec still uses `specversion: 1.0` on wire; it does not prescribe R7 meaning, delivery guarantee, order, privacy authorization or business effect. For a source event, `(source,id)` is a deduplication identity, not the same as learner sequence or a correlation ID.

## Paper packet worked answer

Start at applied sequence 6. Under the deliberately **gap-holding** consumer contract in the chapter/data file:

1. `E8(seq 8, rev_109)` arrives while 7 is missing. Validate schema/identity, hold E8, report missing 7, and reconcile with source; keep projected seq 6 and show a truthful stale/unknown state. If a different agreed contract allows jumping to latest absolute state, applying E8 can be defensible, but it must still report the gap and prove no required intermediate effect was skipped.
2. `E7(seq 7, rev_108)` is a **distinct** event, not a duplicate of E8. Apply 7 and then held 8 in source order under the local atomic view/processed-ID rule; latest safe projected receipt is `rev_109`, seq 8. Never map either to R7 satisfaction.
3. Second `E8` has the same `(source,id)` as first E8. Acknowledge as a duplicate after verifying the stored result; no new view update, message or case. Projected receipt remains `rev_109`, seq 8.
4. `E10(seq 10, rev_110)` arrives with 9 missing. Hold 10, report gap, query authoritative source or repair the missing fact, and keep seq 8 view explicitly stale/unknown until the contract's recovery condition is met. Do not use arrival time as sequence authority.

The full document body is unnecessary for this receipt-view consumer. It broadens access/retention across subscribers, logs, failed-message stores and backups. Use a minimized protected payload or a pointer followed by authorized fetch, approved retention and a deletion/correction procedure. Replay should rebuild the read view with stable original identities and **send effects disabled**. The current assistant lacks independent send authority regardless of replay. Any later notice action needs separate permission and idempotent effect ledger.

A no-event alternative is corrected static wording with the current staff/human path, or a bounded authorized synchronous read if a real portal consumer needs current receipt state. The decision depends on consumer need, freshness, source availability and operating owners.

## Two common wrong answers and feedback

- “The event says received, so send a completion notice.” Feedback: receipt is not satisfaction, and event delivery is not an action command or approval. Name the owner of the proposed notice and its separate permission/result.
- “The queue says exactly once, so replay cannot duplicate a message.” Feedback: broker deduplication has a documented scope; a consumer database update and an external notification are separate effects. Preserve original event/effect IDs and disable send in view replay.

A third error is treating E7 as an E8 duplicate because both concern the same learner; dedup by `(source,id)`, then use learner sequence for current-view order.

## Transfer rubric (12 points)

Award 0–2 each for: (1) exact event fact versus command and business outcome; (2) versioned envelope/payload with source/id, sequence scope and minimized authorized data; (3) producer state+publication and schema evolution contract; (4) consumer duplicate, order/gap, atomic application and reconciliation; (5) poison/replay/retention/privacy and receiving owner; (6) justified event-versus-sync/batch/manual choice, bounded AI and fallback. Full marks require one countercondition that would make the event flow unnecessary or unsafe. No broker purchase, cloud spend or employer data is needed.
