# Chapter 8: Choose AWS architecture — worked answers

This key supports the fictional Harbor R7 exercise. It is a worked decision, not a deployed configuration, an institutional baseline, or a claim that an AWS service is necessary.

## Paper exercise: protect one learner before scaling

**1. Locate the authority gap.** The gateway checks the staff token and route scope. The proposed service must still verify that this staff member may inspect this *particular* learner for this purpose, using an authoritative current assignment/tenant relationship. Make that check before retrieving status, consulting the model, or returning a draft. A test matrix should include allowed and denied staff–learner pairs, cross-tenant IDs, changed assignments, expired tokens, and missing source data. A guessed learner ID is never authority.

**2. Separate the controls.** A JWT authorizer authenticates a token and may enforce a route scope. IAM limits AWS actions of the workload role. Encryption protects data in transit or at rest against some exposures. None of those automatically performs Harbor's object-level staff-to-learner authorization. A successful token check followed by an overbroad backend read is still a disclosure.

**3. Compute the synthetic workload.** At 1,000 proposed calls × 2,000 input tokens = **2,000,000 input tokens**. At 1,000 × 300 output = **300,000 output tokens**. If 10% are retried once at the same sizes, 100 extra calls produce **1,100 attempted calls**, **2,200,000 input tokens** and **330,000 output tokens**. These are workload assumptions, not Bedrock charges or measured Harbor use. A retry may generate different output length in reality. Price requires a dated model, Region, invocation mode, rates and other service charges.

**4. Choose provisionally.** Keep the existing approved staff platform and improve the form, wording and human handoff first if it can enforce learner-level access, current policy version, review, observability and a tested fallback. If a verified requirement cannot be met there, a narrow API Gateway + synchronous Lambda draft path may be the next candidate for bounded traffic. ECS/Fargate needs a demonstrated sustained/custom runtime or network reason, plus operating capacity. The choice changes if evidence shows a necessary isolation, latency or operational requirement the existing platform cannot satisfy. This is a conditional recommendation, not “AWS always loses.”

**5. Test the fallback.** The manual path is credible only if staff can still authenticate, access current approved R7 wording and trustworthy learner status, have permission to use the path, and have enough capacity to absorb the workload within the outcome owner's acceptable delay. If the identity provider or status source is common to both paths and down, “use the manual form” is not a recovery plan. Staff should not infer approval from receipt or use stale guidance simply to keep throughput high.

## Transfer task: defend a cloud choice from the person outward

A strong response identifies the affected person and the outcome before drawing compute boxes. It states R7's receipt-versus-review distinction and the no-autonomous-send/write boundary. It names three viable options and the specific requirement that would disqualify each. It traces authentication, object-level authorization, source/version, minimal model context, staff review and evidence. It checks account, role, network/egress, logging, Region/data rules, costs/limits and end-to-end recovery. It proposes a small test, measurements, a stop rule and the decision owner. It admits that the Harbor facts are synthetic and identifies what evidence would change the recommendation.

Suggested **12-point rubric**, one point each:

1. States the learner/staff outcome and consequence of wrong R7 meaning.
2. Preserves receipt ≠ satisfaction and human final decision.
3. Compares existing-platform, Lambda and Fargate options on the same requirement.
4. States a falsifiable trigger for introducing a new AWS workload.
5. Separates gateway/token checks from learner-resource authorization.
6. Specifies least-privilege workload role and data minimization.
7. Identifies current policy/status sources and version promotion owner.
8. Traces actual network paths and external dependencies.
9. Bounds model/Region/logging choices against privacy and policy.
10. Uses a dated, assumption-aware cost/usage model rather than a price claim.
11. Tests shared dependencies and staff capacity in degraded service.
12. Names evidence, owner and stop/correction route.

## Common misconceptions to repair

- “API Gateway authorized the route, so the learner is authorized.” Ask which source proves this staff member may read this learner **now**.
- “Private subnet means the model is private and reachable.” Ask for the route, endpoint, DNS, security and data-location design; a subnet label is not a complete boundary.
- “Bedrock logging gives accountability.” Ask what content is captured, who can read it, how long it is kept, and how a source/version and staff decision are recorded.
- “Versioned S3 guidance is current policy.” Ask who approved the version and how effective/retired status is selected.
- “Multi-Region model access is recovery.” Remove the identity or status service and see whether the entire staff workflow still works.
- “Serverless has no operating cost.” Name API, function, model, networking, log, security, support and correction costs, including retries.

An answer may reasonably choose a different option if it supplies a different verified constraint and retains every authority, policy, human-review and recovery boundary. Reward reasoning from evidence, not service-name memorization.
