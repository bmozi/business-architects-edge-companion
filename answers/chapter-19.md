# Chapter 19: Govern Decisions and Exceptions — worked answers

Harbor is fictional. The decision route, board capacity, E07 exception and paper packet are teaching proposals; no WGU or Harbor approval or policy waiver is represented.

## Teach-back

Governance lets a team act promptly *inside* an accepted boundary and ensures a real owner accepts a choice that changes policy meaning, data access, receiving work or learner exposure. The change author, peer reviewer, Policy, Security, Support, operating owner and release owner have different jobs. A proposed ADR does not approve the design; an exception request does not change permission; an expiry date without a fail-closed check does not stop a workflow. Humans decide meaning/risk; configured tests, runtime authorization and stop controls enforce what machines can enforce. An architect facilitates coherence and escalation rather than signing for absent owners.

## Worked chapter queue and E07

The invented six-change/week queue with all six sent to a board that completes two/week grows `6 − 2 = 4` per week and `4 × 3 = 12` after three fixed-rate weeks from zero. If four are genuinely within an *already accepted* contract and handled by staffed peer review, the board receives two/week and can keep its queue at zero at capacity two/week. The work moves, not vanishes. No Harbor demand or quality effect has been measured; misclassification can create worse R7 harm. The sensible governance design makes the standard, negative tests and routing owner inspectable and watches both delay and escaped boundary defects.

E07 is **requested, not active**. The Chapter 18 example's 14-day clock has not started. A hypothetical future acceptance would need Policy, Security and rehearsal/operating owners to agree to synthetic-only manual source-digest matching, a named operator/backup, independent stop, start/expiry time, protected evidence and a fail-closed action check. No such acceptance grants learner exposure, access to real learner records or autonomous send/write/eligibility/case action. On mismatch, expiry or a latched stop request, new runs stop while the history remains. An available stop button alone does not prove that an activated stop prevents the next run; unknown stop state denies permission. A repeated renewal should cause a design decision, not an invisible permanent waiver.

## Separate paper packet answer

Three of nine weekly requests are cross-domain; reviewers finish two. Their queue grows `3 − 2 = 1` per week, reaching `1 × 4 = 4` after four fixed-rate weeks from zero. The six local requests still require independent peer capacity and relevant controls; their classification is an assumption, not a measured fact.

Two defensible responses are to fund or schedule enough qualified cross-domain capacity for three/week, and to narrow/simplify the work or sequence one boundary request later while providing a clear escalation route. It may also be possible to revise a standard after actual owner acceptance so some future *genuinely* in-contract work becomes local; do not simply rename a current policy/access change “routine.” If a regulation or real policy requires a formal body, preserve it and plan its capacity.

The fourth authorization-bypass request is outside the nine-request arithmetic. It goes to Security for an access decision, with Policy, privacy/release and architecture/engineering input as affected. Its present state is **requested or denied**, never active: no Security acceptance, no alternative control and live learner data in scope. A seven-day date limits duration only if a legitimate, enforceable exception exists; it cannot authorize an unauthorized cross-learner read. A safe alternative is synthetic data in a staff-only rehearsal or implement per-object authorization first. Architecture cannot waive Security's boundary.

A formatter edit that preserves approved R7 meaning may proceed through Engineering's independent peer review and required negative/source tests. A semantic R7 change needs the current Policy owner to interpret and version the rule before Engineering implements it. A new Support queue requires Support's receiving context, staffed capacity, backup and escalation acceptance; sponsor resources and Security/privacy review may also be needed. A learner-facing release needs its own release decision after all relevant gates.

One technical control: a required negative test tied to the protected CI job plus runtime learner-object authorization, depending on which defect is targeted. One human decision: Policy accepts the meaning or Security accepts the access condition; neither is an architect's signature. One operating signal: wrong R7 guidance, failed source-version match, cross-learner denial, growing unresolved queue or an expired exception attempt. The answer must connect a signal to a stop/correction owner rather than treating a dashboard as self-correcting.

## Transfer rubric (12 points)

Award one point each for:

1. Begins with an affected-person outcome and actual current decision path.
2. Separates in-contract local changes from semantic/access/receiving/release boundary changes.
3. Names preparer, independent reviewer, accepting authority, stop owner and backup for consequential choices.
4. Gives peer-review/test evidence for delegated changes without equating green CI with business approval.
5. Provides cross-domain review capacity, response path and escalation without making a central board the default for all work.
6. Records an ADR with proposed/accepted status, alternatives, tradeoff and a revisit trigger.
7. Creates an exception request with exact standard, scope, data, rationale, alternatives, residual risk and owner.
8. Requires acceptance evidence before activation, checks scope/source/expiry at action time and fails closed.
9. Separates historical exception record from current permission and defines closure/correction.
10. Walks misclassification, review queue or expired exception through detection, containment, owner, recovery and residual harm.
11. Bounds AI preparation to authorized sources, human verification and enforced tool/data authority, with a non-AI path.
12. Names observed measures that could change the governance design, including delay *and* escaped harm or burden.

## Common wrong answers and feedback

- **“A board should approve everything for safety.”** Ask how many changes the board can actually inspect, and whether peers plus enforced checks can handle true in-contract work while domain owners handle boundary changes. No fixed board size is endorsed.
- **“The rule is written in the prompt, so it is enforced.”** Ask what denies a forbidden learner-object read or assistant send at runtime, and which required check covers the negative R7 case.
- **“E07 has an expiry, so we may use it.”** Ask who accepted it, when its clock started, what data it covers and where expiry is checked. E07 remains requested.
- **“The review queue shrank, so the governance change worked.”** Ask whether escaped wrong guidance, access attempts, Support load and learner understanding improved or worsened.

Accept a stricter formal approval path where an actual institution requires it, provided the learner explains its authority, cost, capacity and evidence. Accept a simpler static service in place of AI when it meets the learner need more reliably.
