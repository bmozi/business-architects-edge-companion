# Chapter 11: Modernize Developer Experience — worked answers

This guide works a fictional Harbor packet. It is not an actual institutional study, actual developer interview, observed CI pipeline or demonstration that a platform purchase pays for itself.

## Teach-back

Developer experience is the lived ease or difficulty of completing software work with correct feedback, manageable mental effort and enough focus. A business capability is a repeatable organizational ability, here changing learner-facing R7 explanations accurately and safely. A portal, template or agent subscription is an asset that may support that ability. A paved road is a supported common route with known tests, owners, release path and exceptions. The paved road succeeds only when a clean change can pass, a dangerous change fails, and teams can understand and support the route.

## Worked paper packet

Draw: request → policy meaning/version → bounded draft → contract/accessibility test → independent review → release → observed learner/staff effect. The packet says three of six changes had a rule-version wait, two confusing CI failures and one an environment wait; those categories may overlap. No duration, severity or post-release effect is supplied. Interview and inspect a representative accepted task before claiming that rule version dominates total delay. Ask how long the waits lasted, what the CI failure said, whether an accessible support route is staffed, whether a platform already distributes approved rules, and which team owns the canonical version.

A defensible first increment is **B**, conditional on the policy owner confirming current R7 and a receiving owner for the accessible fallback. Publish an approved version/digest and five-sentence intent example; expose it through the current governed path; add a positive fixture for `documents_received=true, review=pending → “received for review”`; add a negative fixture proving that same input must **not** yield “requirement satisfied.” Include unknown/source-timeout and accessibility label in the real acceptance set. Make CI name the R7 case and source when it fails. Give the platform/CI owner the check and the policy owner the meaning. A clean wording fix must pass the exact required job; a deliberately wrong receipt→approved mapping must fail it. Verify the job ran on the relevant commit rather than returning skipped. The product and support owners accept the handoff and recovery route.

Option **C** may become first if timed journey evidence shows environment setup is the dominant delay and policy/version clarity is already controlled. An isolated, safe self-service environment then has a direct task-flow hypothesis. Option **A** may become attractive after specifications, source, tests and boundaries are dependable and a bounded agent trial shows whole accepted-task improvement without quality or skill erosion. A smaller no-platform content-system correction is also valid if it meets the same policy, accessibility, review and recovery requirements. None of the options earns approval from the counts alone.

Balanced measures: elapsed accepted-task time with wait and correction components; rate and severity of wrong R7 messages and check false positives; developer ability to find the approved rule and understand CI feedback; support handoff completion and learner confusion; and maintenance/on-call effort. Define windows, denominators, task mix and source before comparison. Generated PRs are an activity count and can rise while the real task slows or quality falls.

The only numerical statement supported by the packet is **3/6 = 50% of these six changes had a reported rule-version wait**. It is neither 50% of elapsed time nor a representative organization-wide rate. Two of six had confusing CI failures and one of six an environment wait, but overlap prevents adding the counts into disjoint proportions. Without durations, overlap, prices and benefit evidence, savings and ROI cannot be calculated.

Stop or pivot if the canonical source cannot be verified, the accessible handoff is unstaffed, the negative fixture passes, the clean fixture fails due to false positives, or the pilot shifts correction/on-call work elsewhere while accepted-task or learner effect deteriorates. A policy-critical first failure is a stop; an arbitrary “two failures allowed” rule would be inappropriate.

## Chapter's separate illustrative arithmetic

The chapter's invented before/pilot illustration uses eight changes in each period. `160/8 = 20` and `136/8 = 17` elapsed hours per accepted change. Policy-clarification components are `48/8 = 6` and `20/8 = 2.5` hours per change. Correction components are `24/8 = 3` and `18/8 = 2.25` hours per change. The difference of 3 hours per change in elapsed averages is **not** attributed to the roadmap. Sample size, task mix, staff availability and definition shifts remain plausible explanations; no actual Harbor baseline was measured.

The five-sentence same-task experiment is learning practice. Keep tool/repository/review criteria fixed and record all preparation and correction. The second trial benefits from exposure to the same task, so a result is not clean causal evidence. A later pilot can counterbalance order over comparable tasks and assess accepted behavior, reviewer burden and skill retention.

## Transfer rubric (12 points)

Award one point each for:

1. Names a human/business outcome beyond platform adoption.
2. Defines the organizational capability separately from a tool or project.
3. Maps request-to-release journey with people and system handoffs.
4. Distinguishes observed friction from a hypothesis and asks who is affected.
5. Compares a simpler existing-process repair with platform and AI options.
6. Provides a first reversible increment and condition for a later investment.
7. Names policy, platform, product, security, support and release authorities as relevant.
8. Specifies technical state/source/version and positive/negative acceptance cases.
9. Tests both a deliberately wrong change and an ordinary clean change through the effective gate.
10. Sets a bounded AI role, allowed material, denied authority, review and outage fallback.
11. Uses balanced task-flow, quality, developer and learner/staff measures including costs and denominators.
12. Names a credible falsifier, stop/pivot gate and residual uncertainty.

## Common wrong answers and feedback

- **“Buy the agent because three changes waited.”** The packet says the wait was for policy version; generation speed may be unrelated. Gather durations, owner and source evidence first.
- **“Every cross-team approval is friction.”** The policy owner must still authorize R7 meaning. Remove ambiguity and unnecessary handoffs, not accountability.
- **“A portal is the capability.”** A portal can distribute stale content and shift toil. Test whether the organization can repeatedly deliver an accurate accepted change.
- **“Same task twice proves the spec helped.”** Repeat exposure and order can explain part of the difference. Record total effort and use counterbalanced comparable tasks for a stronger pilot.
- **“Green means safe.”** Verify the exact required job ran the negative semantic case at the intended commit and did not self-skip. Check the specification itself.

Accept a different first option when the learner states what new observation changes the decision, preserves R7 authority, and proposes evidence and a stop condition. Scoring is for reasoning, not allegiance to option B.
