# Chapter 9: Choose Azure architecture — worked answers

This key answers a synthetic Harbor paper exercise. It is not an Azure configuration, security assessment, measured workload or proposed institutional deployment.

## Teach-back

Staff Entra sign-in identifies a person and, with configured claims/roles, can permit entry to a route. A Function managed identity identifies the running workload to Azure services; its assigned Azure RBAC roles and scopes determine which Azure resource actions that workload may take. Harbor's staff-to-learner authorization is a separate business decision: may *this staff member* view *this learner* for *this purpose now*? It must be enforced before status is fetched or included in a model request. Neither the staff token nor the Function identity answers it alone.

## Worked paper packet

**Trust boundaries.** The staff UI crosses into the protected HTTP endpoint; token/route permission must be validated. The Function then crosses from user request to Harbor's authoritative learner-assignment/status systems; the missing object-level check is there, before an overbroad storage read. A further boundary is the Function's managed identity and Azure RBAC access to storage/model resources. The model processing boundary depends on selected deployment type and Harbor privacy policy. Staff review is the final decision boundary. No assistant permission to send, write or determine R7 satisfaction is inferred.

**Correct order.** Validate the caller and route role; bind that trusted identity to the requested learner and purpose; require a fresh positive assignment/tenant check; retrieve only permitted status fields; select the current approved R7 version; minimize the model context; verify permitted deployment location/quota and call the model if useful; present a draft and source/version to authorized staff; record minimal outcome/correction metadata. If an essential check fails, deny or use a verified human route without guessing status.

**Arithmetic.** Six hundred original calls × 1,800 input tokens = **1,080,000 input**. Six hundred × 250 output = **150,000 output**. Ten percent retried once adds 60 calls, 108,000 input and 15,000 output. Totals are **660 attempts, 1,188,000 input tokens and 165,000 output tokens** under constant-size assumptions. This is not an Azure invoice; actual model, deployment type, Region, token sizes, host/network/log charges and rate limits are unspecified.

**Choice.** Improve the existing staff form/wording and accepted human route first if it can supply current status, learner-level authorization, accessibility, evidence and continuity. There is no verified missing capability in the packet. A Function becomes plausible if a necessary boundary or integration cannot be met in the existing platform and a bounded request/runtime fits. Container Apps becomes plausible if sustained/custom container behavior is demonstrated and its additional operation is funded. A different first choice earns credit if the learner supplies a concrete verified unmet constraint, equivalent controls and a credible cost/recovery comparison.

**Global suggestion and fallback.** Do not switch to a Global model deployment simply because a geography-based deployment is busy; processing locations differ, and Harbor has not approved Global. Cap retries and make delay visible. The manual staff route works only if identity, trustworthy status, approved R7 guidance, accessibility and staff capacity remain available. A shared identity-provider or status-service outage could invalidate it. Staff cannot promote receipt to satisfaction to keep throughput high.

## Transfer rubric (12 points)

Award one point each for:

1. Names the staff/learner outcome and R7 receipt-versus-satisfaction rule.
2. Preserves human review and no autonomous send/write/eligibility decision.
3. Compares current platform, Function and Container Apps under the same requirement.
4. Names evidence that would justify or reject a new runtime.
5. Separates staff token/route authorization from learner-object authorization.
6. Separates runtime managed identity and scoped RBAC from deployment-pipeline identity.
7. Traces approved status and versioned R7 content, including owner/freshness.
8. Distinguishes inbound private access from outbound VNet connectivity.
9. States permitted model deployment type/processing boundary and exact quota check.
10. Uses explicit usage, peak and total-cost assumptions without claiming a bill.
11. Describes detection, containment, owners, recovery and residual harm for one failure.
12. Tests a realistic human fallback and names a condition that changes the recommendation.

## Wrong answers and repair

- “The `draft.read` role means S18 can see L42.” It means a configured route-level action. Ask for the authoritative current staff–learner relation and a denied-pair test.
- “Managed identity removes all secrets.” It removes the application's need to manage credentials for supported token-based service calls. Pipeline credentials, third-party connections and mis-scoped roles remain separate risks.
- “VNet integration makes the endpoint private.” Functions documentation separates outbound VNet integration from inbound private access. Draw both routes and their DNS/access controls.
- “Blob versioning guarantees current policy and recovery.” A version can consistently contain obsolete R6; the policy owner chooses current R7, and the team must test restore of the whole workflow.
- “The monthly average proves model capacity.” A short burst must be compared with token-per-minute quota, function concurrency, latency and staff review ability.
- “Service Bus prevents duplicate effects.” Peek-lock can redeliver; receiver idempotency and an accepted business operation remain required for any later authorized action branch.

The learner need not memorize Azure product names to earn a strong score. The defensible answer ties cloud behavior to a named person, current permission, approved meaning, sustained operation and evidence that can change the design.
