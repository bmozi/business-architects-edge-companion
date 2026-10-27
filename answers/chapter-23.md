# Chapter 23: Reason About Distributed Failure — worked answers

Harbor and the bookstore are fictional. The draft-write operation is a hypothetical, unapproved teaching API; it is not a permission for the current staff-draft-only assistant. R7 receipt does not establish satisfaction. The point is to keep unknown outcomes honest and assigned.

## Conceptual teach-back

A timeout tells the caller that its waiting period ended. It does not tell us whether the receiver committed. The caller should retain one intended operation identity, enter UNKNOWN and use the receiver's actual replay/lookup guarantee or hold for human reconciliation. A local transaction can make one store atomic, but not another store, a lost response or a message already read. Compensation is a new domain action with its own failure modes. Ask the learner why an empty immediate lookup after timeout might still be inconclusive: the original request can still be in flight or finish later unless the receiver supplies a final cancellation/fence guarantee.

## Paper packet worked answer

`O7/K7` enters UNKNOWN after timeout, even though the unseen receiver truth is draft `D7`. If the receiver has a documented, tested scoped idempotency window and atomic result ledger, replay the identical `O7/K7` request; otherwise use an authorized lookup by `O7`. If that contract is absent, hold and assign a staff/operations owner. Do not generate `K8` for a new logical POST. On confirmed `D7`, show exactly one draft for authorized staff review; it has no learner-facing effect.

For source `R8` versus portal `R7`, report source identity/version and observation time, consumer last identity/version/time, gap age, owner and disposition. Verify the source event, replay/update only the authorized receipt view, and compare again. The learner should see approved receipt-only wording with an explicit current-status-unavailable or stale indicator and an accepted human route; never “R7 complete.” Document source owns receipt fact, portal Engineering/operations owns view and repair, Policy owns wording, Support owns only an accepted receiving route, and release owns exposure. Residual: a learner may have seen stale or misleading status and need correction after scope review.

Two layers × three **total attempts** each yield `3 × 3 = 9` deepest calls under the packet's assumption that every attempt reaches the receiver. Nine is not nine drafts: receiver-side idempotency can absorb repeated requests with one operation identity, and some attempts may fail before the write. Without verified idempotency, repeated effects are possible but still not proven by the attempt count.

## Three failures and feedback

- “Timeout means the write failed.” Feedback: classify the observation as UNKNOWN; seek receiver fact. Distinguish a client's wait deadline from a receiver commit.
- “Use a new key to make sure it goes through.” Feedback: a new key can mean a new intended operation. Reuse original identity under contract or reconcile, then stop if outcome remains uncertain.
- “Rollback fixes everything.” Feedback: code can revert, but a learner may have read wrong guidance or a payment may have settled. Corrective action is separate, authorized and auditable.

Accept an answer that eliminates the draft-write feature and uses an existing human process, if it explains how the original business need is met and who receives the work. Do not reward an invented `NOT_APPLIED` result based only on a momentarily empty status query.

## Transfer rubric (12 points)

Award 0–2 each for: (1) explicit PREPARED/IN_FLIGHT/UNKNOWN/CONFIRMED/HELD states and evidence; (2) stable operation identity versus tracing correlation; (3) receiver-side atomic effect/replay scope and expiry/reconciliation; (4) bounded retries with timeout budget, backoff/jitter and no multi-layer amplification; (5) partial-success, compensation/irreversible-effect limits and owner/stop; (6) truthful user status, per-object access, bounded AI role and practiced manual fallback. Full marks require a condition under which a retry is **not** safe. A read-only/manual alternative can earn full marks if it avoids an unneeded effect and handles stale data honestly.
