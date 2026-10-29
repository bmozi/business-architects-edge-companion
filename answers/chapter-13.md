# Chapter 13: Lead Engineering Organizations — worked answers

This guide works fictional Harbor planning packets. It is not an employment, compensation, hiring, performance or on-call policy for any real employer.

## Teach-back

Capacity is accepted work a team can safely finish after existing commitments. Nominal payroll hours are only an upper envelope. Delegation is a decision space with information, authority, limits, review, escalation and backup—not simply naming someone responsible. Mentoring, policy clarification, verification, support and incident response make a service dependable and therefore belong in the plan. Team measures should help leaders improve the system; PR counts cannot represent individual or business value. A human reviewer needs knowledge, evidence, time and authority.

## Worked Harbor chapter example

The chapter's illustrative team has `4 × 40 = 160` nominal hours. Mutually exclusive buckets total `24 + 28 + 24 + 16 + 12 = 104`. New-change allowance is `160 − 104 = 56` hours. An 80-hour request creates `80 − 56 = 24` hours of unmet demand. The proposed 48 implementation hours for the R7 wording/accessible-handoff increment fit the invented new-change allowance, provided its coordination, verification and mentoring also fit their separately reserved buckets, leaving `56 − 48 = 8` hours of illustrated contingency. This is not a real forecast or a reason to consume the buffer automatically. A policy answer, support acceptance, effective R7 gate or unplanned incident may change the commitment. Do not close the gap by deleting negative tests, training or on-call recovery.

## Worked separate paper packet

Three engineers each have 40 nominal hours: `3 × 40 = 120`. Existing nonoverlapping commitments total `18 + 27 + 18 + 12 + 6 = 81`. Potential new-change capacity is `120 − 81 = 39`. The requested 50 hours exceed it by `50 − 39 = 11`. No real deadline or organizational authority is supplied, so the manager should offer options rather than promise fifty hours. One acceptable first option is a <=39-hour scope limited to correcting the R7 receipt wording and a staffed accessible route once policy and support owners accept them; keep verification and fallback. Another is to move the date or seek real, authorized help with onboarding and ownership cost included. A learner may defer a numeric commitment until the policy decision and actual team load are known. Hiring is a longer-term response to a persistent capability gap, not capacity this week.

Three-row decision card: (1) technical lead chooses implementation and tests within approved R7 and may stop on a bad source; peer review is required; (2) policy owner alone confirms whether receipt and approval wording is correct, with a named response/escalation point; (3) release authority approves learner exposure after support accepts the accessible route and the exact clean/dirty CI cases pass. Manager owns scope/capacity negotiation. Security/privacy own per-learner access, and support owns receiving capacity. These responsibilities may be combined in a small organization only if the people actually have the necessary authority and the review independence needed for the risk.

Skill rehearsal: the new engineer explains receipt≠satisfaction, locates the current policy digest, reviews one correct and one plausible wrong synthetic draft, runs a negative R7 test and tells a backup who can stop exposure. The backup repeats the task or shadows it in a safe drill. A completed course or named backup is weaker evidence than observed execution. Protect mentoring time.

AI may draft code/tests and compare permitted capacity scenarios from approved non-sensitive information. It cannot approve policy, access private personnel feedback for ranking, weaken its own required gate, merge or release. The technical lead verifies provenance, arithmetic, unusual affected-person concerns and the diff; credentials and repository controls enforce limits.

A “PRs per engineer” target may discourage defect reporting and reward unreviewed output. Better signals include accepted changes preserving R7, wrong-message reports with reporting coverage, clean/dirty gate behavior, support handoff completion, correction/on-call load, review time, backup rehearsal and team feedback on whether early concerns were heard and resolved. A higher defect report count might reflect better detection, so investigate rather than punish.

## Transfer rubric (12 points)

Award one point each for:

1. Names the learner/customer result and service promise, not only a delivery count.
2. Separates nominal hours, existing work, new change capacity and uncertainty.
3. Counts on-call/support, evaluation, coordination, learning and absence without double counting.
4. Shows the demand-capacity gap and offers an honest scope/date/resource tradeoff.
5. Keeps policy, security, accessible handoff and release authority with actual owners.
6. Gives a technical lead bounded decisions, information, stop/escalation and backup.
7. Specifies permitted AI contribution and enforced denial of policy/personnel/release authority.
8. Provides a concrete skill demonstration and coverage path, not just a training promise.
9. Inspects on-call quantity and quality and names a sustainable coverage question.
10. Shows how dissent or early defects change a decision without losing accountability.
11. Uses balanced team and affected-person signals, not individual PR/line quotas.
12. States a condition for changing scope, hiring, process or service hours and the evidence required.

## Common wrong answers and feedback

- **“160 hours means four engineers can do eighty hours of new work.”** Existing work consumes time. Show the buckets and ask which commitment an added request would displace.
- **“The agent removes review.”** R7 meaning, learner authorization and accessible handoff still need evidence and responsible humans. A fast draft can increase correction work.
- **“Give the lead accountability and they will find a way.”** Ask whether the lead can access current policy, stop release, get a policy decision and secure support acceptance.
- **“Defect reports are poor performance.”** They may reveal a control that is working. Investigate severity, reporting access and whether the warning changed the plan.
- **“Hire now to solve Friday.”** A role decision requires persistent demand, funding, skill scope and onboarding; it does not generate immediate experienced capacity.

Accept a different bounded option when the learner preserves the necessary controls, identifies the deciding owner and makes the tradeoff visible. The guide scores leadership judgment, not one fixed staffing model.
