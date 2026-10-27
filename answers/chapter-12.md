# Chapter 12: Operate and Modernize Platforms — worked answers

This guide works the fictional Harbor R7-D29 case and its separate paper exercise. It is not a production runbook, WGU operational record, provider deployment or human sign-off.

## Teach-back

Service availability asks whether the system responds; task correctness asks whether the answer fits the authorized policy and learner context; resilience asks whether people can detect both visible and quiet failure, stop propagation, provide reduced service, correct effects and return. A fast HTTP response or model evaluation score does not establish R7 meaning. An operating contract specifies purpose, boundary, source/version, owners, signals, stop, fallback, effect record, recovery, cost and retirement. A prompt instruction is not an enforcement control.

## Worked paper packet

During the separate fictional outage, arrivals exceed manual completions by `40 − 15 = 25` requests per day. Two days yield `25 × 2 = 50` unfinished requests, assuming steady arrivals, all 15 manual completions are accepted, no starting backlog, no duplicates and complete access to policy/identity/context. After restoration, 50 total accepted completions against 40 new arrivals drain `50 − 40 = 10` old requests per day; `50 ÷ 10 = 5` full days. This is capacity arithmetic, not an SLA or fair priority plan. A business owner must still decide which requests are urgent, acceptable delay, communication, accessible route and how additional capacity is supplied. Before trusting the numbers, verify the manual guide and identity/context work during the same failure and that qualified staff really can accept 15/day; also verify post-restore 50/day is total, not 50 backlog completions plus new arrivals. If a shared identity outage prevents manual work, the calculation is invalid and backlog would rise faster.

For the fluent wrong R7 answer, stop new AI draft exposure via a control reachable independently of the model; preserve the approved manual/staff route. Inspect source/policy digest, retrieval index, prompt, model/application versions, exact output, staff acceptance and any learner-facing communications. Policy owner confirms R7 semantics; platform/on-call isolates the source/index or release; security/privacy assess unauthorized access or disclosure; support/product and the authorized communication owner identify affected learners and decide correction. An effect ledger and protected metadata support that work. Correcting the index or rolling back prevents future copies but does not erase a message already read. Unknown effect history remains recorded as uncertainty.

A second model is **not** validated fallback from the packet. The dependency map is unknown and may share identity, retrieval, provider or network; its R7 and authorization behavior has not been evaluated; cost and data terms are unknown. A different model may be tested against the same task and independently reachable control, but a human-led reduced route can be safer first. An answer may choose full pause when policy/context cannot be reached and explain how affected people are notified.

Possible measures: technical health = percentage of requests completed within an owned latency/error window, with denominator and time window; policy quality = count of sampled/confirmed receipt→satisfied violations plus exact negative-canary results and source freshness; affected-person = wrong-message reports, corrected learner communications or accepted accessible handoffs with owner and lag. A low wrong-report count is not proof of no wrong answers; review coverage and reporting accessibility matter.

## Chapter's separate illustrative numbers

The chapter's other invented Harbor continuity scenario reuses earlier ch24 values: `60 − 20 = 40` backlog/day; `40 × 2 = 80` after two days; restored total capacity 75 with 60 new arrivals gives `75 − 60 = 15` net backlog completions/day; `ceil(80/15) = 6` days, conditional on all capacity and routing assumptions. It does not mix with the exercise's 40/15/50 packet. The separate latency illustration is `980/1000 = 98%` under the proposed three-second target; it says nothing about semantic correctness. One wrong answer in 20 conveniently selected reviews is `1/20 = 5%` of that sample, not a valid population error estimate.

## Transfer rubric (12 points)

Award one point each for:

1. Names the human/business purpose and authorized R7-style task boundary.
2. Distinguishes technical availability, answer quality, downstream effect and resilience.
3. Records policy, prompt, retrieval, model and application versions and their owners.
4. Enforces caller and object authorization, data minimization and denied actions outside prompt prose.
5. Specifies health, quality and affected-person signals with denominators/coverage/lag.
6. Identifies independently reachable stop and a named incident/release decision owner.
7. Describes a reduced service with actual skill, access, capacity, priority and acceptable delay.
8. Maps shared vendor/identity/data dependencies and tests the fallback.
9. Records submitted, manually completed, draft accepted and communicated effects without conflating them.
10. Walks quiet wrong-output correction, communication and residual consequences as well as outage recovery.
11. Tests model/vendor migration against the same requirements with cost, privacy and exit obligations.
12. Names a retirement trigger or a condition for narrowing/avoiding AI and a safe drill.

## Common wrong answers and feedback

- **“The model is up, so learners are safe.”** Ask which R7 semantic test and human feedback would catch a plausible wrong answer.
- **“Switch to another model.”** Show its shared dependencies and prove the same policy, access, data, cost and quality boundaries first.
- **“Manual fallback covers everything.”** Capacity, accessible route, policy access and staff skill may fall short. Prioritize and communicate delay honestly.
- **“Rollback closes the incident.”** Identify accepted drafts, human communications and downstream decisions; some effects require correction rather than reversal.
- **“Log every prompt for safety.”** Full content may include sensitive learner data. Choose minimal protected metadata, approved sampling, access and retention; verify provider endpoint coverage.

A strong answer may retire AI for the task, use a simpler governed form, or delay migration if it can show that the required capability and people are better served. The rubric scores the operating reasoning, not preference for a provider.
