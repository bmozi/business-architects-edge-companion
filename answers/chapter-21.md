# Chapter 21: Integrate the Enterprise — worked answers

Harbor and the vendor in this packet are fictional. The existing R7 assistant remains staff-draft-only. No API, message path, Policy determination, Support queue or release has been accepted. Receipt for review does not establish R7 satisfaction.

## Conceptual teach-back

A connection transports data; integration preserves the producer's meaning while enabling the consumer's permitted decision. A copy is not a new authority. An adapter can translate shape and protocol; an anti-corruption boundary protects the consumer model when the source uses different concepts. If two systems both say “complete,” a field-name match is evidence of almost nothing until owners define what was completed. The student should explain why the safest mapping sometimes says “do not map.”

## Paper packet worked answer

1. Rules: vendor `status=complete` maps only to `uploadTransferComplete=true` (if that field exists and the vendor manual/version is approved); it never maps to `requirementComplete=true`. Preserve stable source event ID and source meaning/version. On unknown version or absent learner mapping, hold for review and show neither an inferred `true` nor a fabricated authoritative `false`.
2. Prohibited mapping: `vendor.status=complete -> portal.requirementComplete=true`, because upload transfer and Policy satisfaction are different facts. If the portal has only the boolean, do not perform this integration until its model can express receipt-only/unknown or a separate Policy-owned determination exists.
3. Deduplication key: stable producer event ID within producer namespace (and consumer identity if multiple independent consumers share a ledger). Do not use delivery attempt, receive timestamp or shared correlation ID. Store processed ID and view update atomically, then acknowledge. A second delivery of the same ID is observed/skipped; it does not create a second receipt or any downstream action. If the atomic boundary is unavailable, state the gap and use an owned reconciliation process rather than claiming exactly once.
4. L2 report: source ID present but portal ID absent, with source snapshot time, schema/meaning version, last attempted delivery and age, accountable Engineering/operations owner, and a repair disposition. Recheck L2 authorization before displaying or replaying it. The source remains the receipt authority; the portal replica is incomplete.
5. Source outage: show the last view with an explicit observed/updated time only if that display is Policy/UX approved, say current status cannot be verified, and offer an accepted human path. If the last view could mislead, hide it and use the manual path. Do not display “R7 complete.”
6. Simpler option: corrected static wording plus existing staff-reviewed explanation and accessible human route, especially if no actual consumer or freshness requirement is evidenced.

Accept a synchronous read design instead of async if it addresses source outage/timeout, object-level authorization, rate budget and no invented satisfaction. Accept a batch design for a non-learner-facing low-urgency report if freshness is explicit. The choice must follow the business need, not a pattern preference.

## Reconciliation arithmetic

The chapter figure's 100 distinct source IDs divide into 96 identity-and-version matches, one present but version-mismatched ID, and three source IDs missing in the portal. `96 + 1 + 3 = 100`; portal presence `96 + 1 = 97`. One duplicate delivery is outside the distinct-ID denominator and does not raise it to 101. A report stating only “97 present” misses the version defect and three gaps.

## Two common wrong answers and feedback

- “Both systems call the field `complete`, so copy it.” Feedback: ask *what* completed and who may assert R7 satisfaction. Upload completion is a transport fact, not a Policy determination. Require a negative mapping rule and an unknown state.
- “The broker acknowledged it, so the portal is correct.” Feedback: separate accepted delivery, durable consumer application and learner-facing meaning. Acknowledgment can be lost after commit; source and replica can diverge. Reconcile stable IDs **and** meaning version, with an owner for gaps.

Also challenge any plan that stores a learner receipt in a shared view without per-learner read authorization; copying data never creates permission.

## Transfer rubric (12 points)

Award 0–2 each for: (1) producer/consumer definitions and one semantic mismatch; (2) authority map, prohibited translation and unknown handling; (3) minimal contract with stable identity/version and purpose-limited data; (4) justified sync/async/batch choice with outage and rate consequences; (5) duplicate/partial-failure recovery and source-to-consumer reconciliation; (6) access, receiving owner, vendor change and bounded AI/fallback. Full marks require a real counterexample that would change the choice. A simpler static/manual solution can earn full marks when it meets the need and names its human capacity.
