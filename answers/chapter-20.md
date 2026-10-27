# Chapter 20: Design APIs as Promises — worked answers

The chapter's Harbor API and learner IDs are fictional. The draft-write route is hypothetical and unapproved; the existing assistant remains staff-draft-only without send, learner write, eligibility or case authority. A complete answer must preserve R7 receipt ≠ satisfaction.

## Conceptual teach-back

An API is a promise to another program about permitted requests, response meaning, errors and effects. `200 OK` can mean the receipt view was returned; it does not mean Policy determined R7 satisfied. `201 Created` can mean a review draft was stored; it does not mean staff accepted it or a learner received it. A timeout is an unknown write outcome. Authentication identifies the caller; object-level authorization decides whether this caller can see this learner's record. If a learner says “it's like a menu,” ask what the menu analogy misses: per-person privacy, retries after lost responses, semantic versions and operational ownership.

## Paper packet worked answer

1. Screen: “We received your R7 document for review. Receipt does not mean the requirement is complete. Check your current status or contact an authorized advisor for questions.” The actual approved wording and route would require Policy/Support acceptance; this is illustrative.
2. After timeout, the client retains `K1` and `O1`, then retries the *same request* with `K1` within the defined retention window or uses an authorized lookup/reconciliation by `O1` when the window/status is uncertain. It must not invent `K2` and assume the first draft failed. The server must store key/fingerprint/result atomically to make replay meaningful. Replay/lookup must recheck current learner-specific access; revocation denies disclosure without deleting deduplication history. Missing expired history is not proof of no earlier write. If this control is not built, pause the write path and reconcile manually; do not claim exactly-once.
3. For learner B's URL, a valid token for A is insufficient. The server checks B-specific authorization and denies without B's receipt data. A consistent `404` can conceal existence; a `403` may be appropriate under a different documented disclosure policy. The object check must be server-side and tested with two different learner identities.
4. Support must accept the new review queue and its capacity/handoff. Policy accepts wording/meaning; Security access; Engineering implementation; operations recovery; release exposure. The architect cannot accept for them.
5. `200` only proves the HTTP read succeeded; `201` if received only proves a draft was stored; timeout proves neither success nor failure. None is a Policy satisfaction determination. A non-API alternative is corrected static wording on the existing path plus staff-reviewed explanation/human route, tested for understanding and handoff.

Accept a narrower answer that omits the draft POST entirely and uses current staff work, if it explains why the new API has no demonstrated consumer or accepting owner. Reject an answer that turns receipt into completion or treats a timeout as proof of no effect.

## Two common wrong answers and feedback

- “We received `200`, so show `R7 complete`.” Feedback: name the resource and field. The returned `receiptStatus` is `RECEIVED_FOR_REVIEW`; HTTP status describes delivery of the representation, not Policy's determination.
- “After a timeout, simply POST again with a new key.” Feedback: the first write may have committed. Preserve original operation identity, replay under its scoped key where valid, then reconcile; otherwise two drafts or later messages can result.

A third frequent error is relying on a valid login for every learner path. Ask for the negative test using learner A's token on B's object.

## Transfer rubric (12 points)

Award 0–2 each for: (1) business meaning and excluded effects, with no wire/business conflation; (2) read and potential write resources/methods with a justified simpler alternative; (3) authentication plus per-object authorization and purpose-limited fields; (4) timeout, original operation identity, replay/conflict and post-expiry reconciliation; (5) stable error shape and semantic compatibility migration across real consumers; (6) named Policy/Security/Engineering/operations/receiving/release owners, failure correction and bounded AI role. Full marks require a credible negative case and explain who can stop the service. If there is no defensible write need, omitting the write and explaining the avoided risk can earn full marks for criterion 2/4 with a hypothetical retry analysis. Score the reasoning, not tool use or jargon.

Instructor check: ask whether the student's contract would still be safe if the network drops the response *after* commit, an old consumer sees a new enum, and a legitimate user guesses a neighboring ID. Those three changes expose superficial contracts.
