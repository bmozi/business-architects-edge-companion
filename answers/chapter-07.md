# Chapter 7: Automate workflows responsibly — worked answers

Instructor material; separate from the reader manuscript. All Harbor facts, timing and rates are invented teaching assumptions. The candidate action workflow is a hypothetical later path; the first recommended increment remains a better form with optional staff-reviewed draft.

## Paper exercise: five transitions

| Event | Defensible decision | Reason and protected consequence |
|---|---|---|
| A: P51 reviewed, no submission approval | **Reject** the create attempt; keep or discard the draft | Review of wording is not approval of an external effect. Otherwise an AI or worker could turn an editable suggestion into a case without accountable staff consent. |
| B: approved unchanged O51 dispatched before expiry, reply lost | **Reconcile O51**; record `UNKNOWN`, preserve the approved payload and attempt, query receiver status | Timeout does not prove the create failed. A fresh O52 may create a duplicate and shift work or disclose the case twice. Do not discard the accepted operation because the approval clock later expires. |
| C: receiver lookup returns C51 for O51 and matching approved payload | **Record confirmed success** with the destination receipt | The destination, not a green local workflow state, provides evidence of the effect. Confirm payload/scope identity before marking the operation complete. |
| D: O51 never dispatched, first send would occur after expiry | **Cancel/reject that first dispatch** and seek new human approval if the task still matters | Local acceptance is not perpetual authorization. No remote effect occurred under these facts; current actor/state/stop checks still matter if new approval is sought. |
| E: manual case under H51 while automation paused | **Reconcile without a new operation**; link the manual receipt to H51 and inspect whether the candidate O51 was ever dispatched | “No dispatch receipt” alone does not prove absence of an effect. If trusted local/destination evidence establishes no dispatch and manual work completed the handoff, cancel the pending automated action. If dispatch may have occurred, resolve O51 against the receiver first. Resume must not duplicate staff work. |

Accept equivalent wording if the student clearly separates local workflow state from the external case effect and keeps the same intent/operation identity through uncertainty. For E, do not require a claimed receiver lookup result the question did not supply. A learner who says “cancel immediately because staff submitted manually” must explain how the prior dispatch uncertainty is resolved; otherwise the cancellation may hide a duplicate already created.

## Backlog arithmetic

During outage, unfinished work grows by **60 − 20 = 40 requests/day**. Over two days the backlog is **80**, assuming no starting backlog, constant arrivals/capacity and all completed manual requests are reconciled. On return, **75 total completions/day − 60 new/day = 15/day** is available to clear the old backlog. Five full days clear 75 of 80; five remain, so under the model the sixth day clears them. Equivalently, `ceil(80/15) = 6` whole days. This is not a service promise. Staffing absences, prioritization of urgent arrivals, wrong-answer correction, shared identity failure, variable arrival rate or reconciliation time could worsen it. Award credit for at least two justified limits.

## Teach-back

The engine can know the states and transitions it persisted under its own contract: approval accepted, dispatch attempted, task timed out, perhaps a returned receipt. It cannot infer from a lost response that the destination did nothing. The receiver's lookup/idempotency contract and receipt establish the remote effect as far as that system can report it. A policy/business owner judges whether the content and handoff served the learner correctly, whether reduced service is acceptable, and how to repair affected work. These are three different kinds of evidence and authority.

## Self-study paper rubric: 20

Five events with correct decision and business rationale, **10** (two each); outage backlog and daily recovery arithmetic, **4** (two each); six-day ceiling calculation and stated assumptions/limitations, **2**; three-layer teach-back explaining workflow state, receiver effect and business meaning, **4**. Total **20**. Do not award full credit for “retry every failure,” “a green workflow means the learner was helped,” or “manual fallback has unlimited capacity.”

## Transfer task: worked example and 12-point rubric

A sound fictional transfer might choose an internal facilities request. Outcome: route one broken-door report to a qualified human without granting an AI permission to unlock doors. Simpler alternative: a form with location, severity and photo preview. States: opened, draft ready, staff reviewed, accepted for one internal ticket, dispatched, unknown/confirmed/rejected. Authority: authenticated staff may approve an exact ticket and destination; the model may summarize only permitted reports. Effect: stable operation ID and destination status lookup; no second ticket because of timeout. Continuity: a staffed, accessible phone/form route with known daily capacity and independent access to the queue. A facilities lead decides which safety hazards need faster response and what delay is acceptable; staff periodically practice triage and ticket reconciliation so takeover remains a real skill. Evidence: compare completeness, correction effort, duplicates and time to qualified response; expand only if the simpler path fails a meaningful need.

Score two points each for: **outcome and simpler alternative**; **states and invariants**; **actor/data/approval boundaries**; **effect identity, retry and reconciliation**; **realistic human continuity with access, owner, capacity, priority and practiced takeover**; **evidence and a condition that changes the design**. Total **12**. A recommendation to keep the form can earn full credit if the argument is supported. Feedback should identify which missing field would make a real decision unsafe or unverifiable, rather than praising extra architecture.

## Common wrong answers and repair

- “The timer expired, so the case never happened.” A clock tells us when the local wait ended. Query or reconcile the destination using the same operation identity before another create.
- “The engine says complete, so the message was right.” A completed execution can faithfully deliver a false R7 interpretation. Compare meaning with the approved passage, review affected cases and give the policy/business owner the correction decision.
- “Use a second AI provider as the manual fallback.” That provider may share identity, data or workflow dependencies and may handle R7 differently. The fallback must have tested access, meaning, capacity and authority.
- “Compensate by deleting the case.” Deleting a record may destroy evidence and cannot make a message unread. Choose a domain-approved correction with an audit trail and affected-person response.

The instructor should invite a student to challenge the candidate action workflow if a better form or reviewed draft meets the outcome. That is a valid architectural decision, not avoidance of the topic.

## BPMN repair: notation and business evidence

The cross-pool solid sequence flow is invalid. Keep the staff and receiver sequence paths inside their own participants and connect the submission to the receiver through message flow. The same-pool dashed message flow is also invalid; remove it or model the intended internal ordering with sequence flow, after deciding what work it actually represents. Do not change a line style without checking the process it claims to express.

Rename the staff end to submitted, not learner problem resolved. Even a confirmed receiving disposition does not establish learner understanding or a successful start. Missing operating evidence includes accepted case types/context, permitted data, receiving hours/capacity, receipt and return handling, unresolved-work owner, accessible alternative and a test of the route with appropriate people. No such acceptance is supplied by this exercise. A recommendation to narrow or defer the route can be correct.

The corrected native model treats the two workflows as separate participants for this collaboration. A justified alternative can place internal teams in lanes of a single participant; then sequence flow may cross those lanes, and internal message flow is not the right substitute. Explain what boundary changed and what the model now hides. A department name alone cannot decide the notation.

Score: cross-pool repair with reason 2; same-pool repair with reason 2; truthful end label and distinction from learner outcome 2; two concrete missing operating commitments 2; defensible participant/lane explanation 2. Total 10. Existing workflow/state and arithmetic rubrics remain separate.

Transfer feedback: require a named decision, ordinary/adverse paths, precise end meanings, receiver objection and revision, permitted information and a current human owner. A diagram without a runtime is legitimate descriptive work; it is not an executed workflow. AI-generated labels do not establish authority or capacity.
