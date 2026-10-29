# Chapter 18: Set Architecture Direction — worked answers

Harbor and both ten-case worksheets are invented. This guide does not confer Harbor policy, architecture or release approval.

## Teach-back

Architecture direction is a small, reasoned set of outcome-linked constraints that makes local decisions compatible. A principle explains how to choose; a standard states a more specific constraint; a guardrail tests or blocks a forbidden path; an ADR preserves one significant proposed or accepted choice; governance assigns decision and exception authority. The distinction is practical: writing “use current R7” cannot stop an API from interpreting document receipt as requirement satisfaction. Source/version binding, separate statuses, negative tests, learner-object access and named human decisions are needed.

The Chapter 18 ADR is **proposed**. It recommends evaluating approved static wording first, with a human route, while a staff-reviewed AI path remains a separate conditional comparison. It does not authorize learner-facing exposure. The Chapter 15 $12,000/two-week request remains unapproved. Policy, Support, Security, operations and release owners have distinct decisions. The architecture facilitator coordinates tradeoffs and records rationale; they cannot accept another domain's obligation.

## Worked answer to the separate paper packet

A defensible direction is: “Improve truthful R7 receipt language on the existing approved path and retain an accessible human route for unresolved cases. Preserve current Policy meaning and learner-specific access across static or staff-reviewed variants. Evaluate any AI expansion only after source/version, expert correction burden, Support receiving capacity, Security access and release conditions are accepted and tested.” Choosing to wait/repair the existing path before any new learner-facing change is also defensible if even the static wording is not currently accepted.

Two principles could be (1) meaning has a versioned Policy source, so `documents_received_for_review` never becomes `requirement_satisfied` by inference; and (2) no read of a learner object without learner-specific authorization, even in a staff-reviewed AI path. Other acceptable principles include reviewable/stoppable AI suggestions and accepted human receiving duty, if their consequences and tests are concrete.

Engineering can decide locally how to implement the approved static text or represent distinct status states inside its owned module, subject to the accepted contract and normal technical review. It cannot locally change R7 policy meaning, grant broad data access, promise Support coverage or expose a new learner-facing path. Three conditions before any change might be Policy acceptance of wording/negative case, Support acceptance of route and funded capacity, and Security proof of per-learner access; release authority must then decide exposure with operations' stop/reduced-mode evidence. Full-credit responses need the release decision as well, even if they group conditions differently.

A revisit trigger is an observed pattern of legitimate exception cases that the static route cannot explain well, accompanied by a tested staff-reviewed alternative and accepted support/access controls; a new policy interpretation or wrong-guidance event is another. A correct one-sentence ADR status is: “R7-01 is proposed for evidence gathering only; no owner has approved learner-facing release.” The request to skip learner-object authorization is rejected because the experiment must not expose another learner's information; narrow the experiment to synthetic cases or fix authorization first. An exception cannot convert missing security authority into permission.

The static worksheet gives 8/10 correct explanations in its invented sample and two human referrals. The separate AI worksheet has 3/10 requiring correction and one wrong “satisfied” draft. These samples are neither paired nor representative and use different outcome definitions. We do not know whether the AI drafts were reviewed before exposure, how difficult the cases were, the review time, access behavior or the effect on learners. It is invalid to subtract the two percentages and call the difference an AI effect. A fair later comparison would use the same approved cases, source versions and outcome criteria, record reviewer time/corrections and include important exception/accessibility cases; even then, a small test would not alone prove population benefit.

## Transfer rubric (12 points)

Award one point each for:

1. Names an affected-person result and actual current work before choosing a platform.
2. Separates a durable principle, a specific standard and an enforcing guardrail.
3. States a bounded first slice, non-goals and a simpler/non-AI alternative.
4. Gives an explicit, versioned meaning/source contract and negative case where relevant.
5. Addresses access, data minimization and who can read or act on a specific object.
6. Connects the technical direction to receiving capacity, accessible route and recovery.
7. Records an ADR status, context, options, tradeoff, consequence, confidence and revisit trigger.
8. Delegates ordinary implementation decisions while routing policy/security/support/release decisions to the proper owners.
9. Gives an exception request a bounded scope, risk, owner, evidence, expiry and fail-closed state.
10. Walks one bottleneck, owner-without-authority or permanent-exception failure through detection, containment, correction and residual effect.
11. Bounds AI to authorized sources and a human-verified contribution with enforced access/approval limits and a non-AI fallback.
12. Names evidence that could falsify the direction and a decision process to revise it without rewriting history.

A learner may favor a staff-reviewed AI evaluation earlier than the worked answer if they keep it staff-only until source, authorization, expert review and receiving/stop conditions exist. They may also reject AI for this service. Score the reasoning and authority, not agreement with the instructor's option order.

## Common wrong answers and feedback

- **“The architecture board approved the diagram, so R7 is ready.”** Ask which Policy version, Support capacity, Security test and release decision the board actually had authority to accept.
- **“Every team must seek architecture sign-off for every change.”** Ask which shared contract a local change could violate. Delegate in-contract choices; reserve escalation for boundary changes and significant tradeoffs.
- **“Temporary means we can ignore source checks until automation arrives.”** Ask who verifies each manual source digest, where the run is bounded, when the permission expires, and what stops the path on mismatch. If those answers are absent, reject the rehearsal exception.
- **“The ten-case worksheets prove static is 80% and AI is 90% accurate.”** They measure different invented samples and outcomes. Require a comparable task, denominators, representative cases and expert correction cost before making a comparative claim.

The teach-back question is: “How can a principle increase team autonomy while protecting a learner?” A strong answer uses a concrete local decision that no longer needs a committee and a cross-boundary condition that still needs its actual owner.

## ADM target-repair paper packet — worked answer

Three defects: receipt is treated as satisfaction without Policy authority; all exceptions are assigned to Admissions beyond its accepted evidence-review scope/hours; replacement of help removes continuity without a demonstrated alternative. Neither an AI label nor a complete diagram repairs them.

A defensible revised target preserves receipt-only wording on an authorized path, keeps satisfaction with authorized evidence review, routes only the accepted evidence-review subset during staffed hours, and retains ownership of other unresolved work until an appropriate receiver accepts it. Keep existing help available; defer any exposure that lacks a usable permitted route. No autonomous AI mark, send, write or case creation follows from this packet.

Trace the semantic repair to Policy and a receipt-only negative test; the route repair to the sending/receiving owners and refusal/out-of-hours rehearsal; continuity to operations/release and a demonstrated stop/fallback path. Missing baseline facts include current help availability/accessibility, actual routing behavior, access enforcement and operating capacity. State these as unknowns rather than inventing a deployed architecture.

A broader target would require a legitimate need, approved meanings and action boundaries, accepted receiver capacity and permitted context, demonstrated access/continuity, comparative evidence and actual release authority. Merely obtaining an AI model with better test scores is insufficient. A learner can defend delaying the entire change if the current route cannot be established.

Score ten points: three for the distinct defects, three for owner-and-check repair links, two for honest baseline unknowns, one for keeping proposal/evaluation separate from release, and one for evidence that could change the recommendation. For transfer, require comparable concerns, a legitimate participant objection and a visible revision, rather than a particular diagram shape.
