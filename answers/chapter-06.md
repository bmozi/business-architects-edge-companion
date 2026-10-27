# Chapter 6: Bound agents and AI authority — worked answers

Separate instructor material. The student prompt is in manuscript/chapters/ch23.md. All case facts are synthetic. No access or spend required. Planning estimate: 25 minutes; transfer 30–45 minutes. Prerequisites: proposal versus execution, current authorization, operation identity, reservation arithmetic.

## Paper answer

A: Accept the new operation after the specified checks. Execution is strictly before 10:05, approved content/queue and state match, actor is authorized, approval unused and resources permit it. Atomically record operation acceptance with approval consumption. Acceptance is not confirmed destination success; preserve dispatch/result states. This permits the intended internal handoff without eligibility or messaging authority.

B: Reject the changed request. The queue is part of the approved effect. Accurate information in an unauthorized destination is still a business/data-handling failure. Generate a new exact proposal for authorized review; do not edit the trusted approval or accept the agent's assertion that the change is harmless. New review does not override destination authorization.

C: Reject the new operation because 10:05 is not strictly before 10:05. Exact boundary was supplied in the exercise, not assumed as a universal clock rule. A new approval may be requested with rechecked evidence/state. Expiry of a new-action approval does not require abandoning reconciliation of an already accepted operation.

D: Reconcile before allowing any further create for the same intended handoff. A fresh approval does not establish that O17 failed. Keep O17 UNKNOWN; query receiver status with O17. Confirmed C91 means record success and return the receipt. Definitive rejection can establish failure under the receiver contract; an empty eventually consistent search cannot establish absence. If uncertainty persists, assign admissions operations reconciliation with platform support. Do not create O18 just because its parameters match. If the receiver supports bounded same-operation retry and stop policy permits it, O17 and the same payload may recover accepted work. Otherwise retain manual reconciliation. A new genuinely distinct case would need a separate business reason, not a disguised retry.

Budget: availability is 120 − 50 − 45 = 25. Only one 20-unit request fits; which worker wins is not specified. After admission availability is 5. When the old reservation settles at 35, spent becomes 85 (50+35), old reservation is released, new reservation remains 20. Availability is 120 − 85 − 20 = 15. A shared atomic check-and-reserve prevents both workers observing 25 and each spending 20. If both were admitted, spent+reserved would be 135, exceeding 120 by 15. These are invented units under a bounded-reservation assumption, not a provider spending guarantee.

Teach-back: a prompt communicates intent; a click may express a person's choice. The execution component still has to determine who approved what, whether that person is authorized, whether parameters/state changed, whether the approval remains usable, and whether resources/stop conditions permit execution. It must also record ambiguous effects rather than treating them as failed.

## Paper rubric: 20 points

- A: 2, correct accept with acceptance/success distinction (1 each).
- B: 2, reject changed queue and explain destination consequence (1 each).
- C: 2, reject exact expiry and explain specified boundary (1 each).
- D: 4, no new create, preserve O17 identity, interpret status uncertainty, assign owned reconciliation (1 each).
- Arithmetic: 4, initial 25, one admission, intermediate 5, final 15 (1 each).
- Concurrency: 2, shared atomic reservation and explain double-admission exposure (1 each).
- Teach-back: 4, specific approval binding, current authorization/state, enforced stop/resources, accepted operation versus confirmed effect (1 each).

Partial credit follows the reasoning. A learner may say “reject O18 and reconcile O17”; that is equivalent to reconcile-before-action. No credit for silent retries, new IDs to bypass controls, or treating the model's confidence as approval. Feedback should ask which specific effect the learner is authorizing and which evidence would establish it happened.

## Common misconceptions and feedback

“Approval means the agent is trusted now.” Ask which resource, content and destination were actually reviewed. Replace session-wide trust with a specific action record.

“Timeout means we should try again with a new ID.” Ask whether the destination could already have committed. Preserve intended-operation identity and inspect the destination contract; there is no universal safe retry behavior.

“The cap is 120, so we have 70 left.” Ask what the in-flight 45 can still cost. Bills and reservations represent different commitments.

“Stopping rolls back the case.” Ask where the request already traveled. Stopping new work and reconciling prior effects are separate jobs.

“A read-only tool is harmless.” Ask what it can read and who will see the result. No-write permission does not prevent disclosure.

## Transfer example and rubric: 12 points

Example, fictional: internal maintenance-request draft. Outcome hypothesis: reduce incomplete handoffs; compare a better form. Permitted evidence: authorized equipment record for the selected site and approved maintenance categories. Tool: propose a work-order draft only, fixed categories, no attachments, purchasing, equipment control, arbitrary network call or write access. Staff inspect and submit through the existing process. The draft references the equipment-record version and visibly expires if relevant state changes. Planning calls share a server-enforced task envelope and can be stopped; no autonomous effect exists to roll back. Facilities operations owns content correction, platform on-call disables assistance, privacy/security owns suspected disclosure response. Measure usable completeness, correction effort, wrong-site recommendations and total effort against the improved form; no benefit assumed.

Challenge 1: a copied equipment note says to email the full site inventory externally. Expected: treat it as untrusted content; no sending tool; do not include unnecessary sensitive data in the draft. The paper design assumes the denial until an isolated test proves it; verify denied capabilities before live use.

Challenge 2: a future approved write extension times out creating a work order. Expected: mark UNKNOWN, preserve operation identity and inspect receiver status/contract; no fresh create to ensure success. If that contract is unavailable, keep submission manual. These are test expectations, not tests executed here. A valid verified-versus-assumed statement is: the card forbids writes on paper, but enforcement and receiver idempotency are unverified; inspect tool grants, denied calls and destination replay behavior in an isolated environment before claiming either control works.

A useful four-place rule mapping for this example: a versioned site-access standard tells the assistant which equipment records may be cited; a local check flags an unrelated-site record in a draft; a named review path asks facilities staff to inspect site, evidence and category before submission; a required integration check blocks the ordinary merge path for a changed access-control fixture. The local check must also pass a clean same-site draft. An exception needs a named authorized owner, a recorded reason and later review; no prompt or passing check grants equipment-control authority. A learner may choose the existing manual form and explain which of these controls then apply to the software that supports it. Credit the reasoning, not a mandated four-tool stack.

A strong transfer opening identifies the desired handoff improvement and asks who decides whether the existing form is inadequate; “let the agent create work orders” is not a business outcome. For Harbor's fictional notification ticket, a learner might name consent ownership, event trigger and failed-delivery handling as unknowns for a human owner. Do not credit an agent's guessed answer as an agreed requirement.

Score 0–2 on each of six criteria from the chapter: outcome/alternative; precise authority/data; approval/state; resources/stop; recovery/owners; challenge evidence including one verified-versus-assumed claim and a four-place rule mapping with a clean-path and exception explanation. Give 2 for a concrete inspectable design, 1 for partly specified reasoning, 0 for omission or contradiction. For draft-only designs, explain retained existing human submission and current access/state checks rather than demanding a new redundant approval service. A non-AI form can earn full credit if it meets the outcome and handles the stated consequences. Revise any 0 before proposing use. A perfect paper score does not authorize production access.
