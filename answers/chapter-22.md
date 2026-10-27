# Chapter 22: Choose Service Boundaries — worked answers

Harbor and the bookstore example are fictional. Earlier R7 API/integration/governance/funding remain proposed; existing assistant has no independent send, learner-record write, eligibility or case authority. Receipt for review does not establish satisfaction.

## Conceptual teach-back

A module is a cohesive responsibility inside one deployable application; a microservice can be deployed and operated independently, normally with its own data and contract. Separate processes do not create business independence if every release and decision still moves in lockstep. Ask the student to distinguish who owns a copied receipt *view* from who owns the receipt fact and who owns Policy's satisfaction meaning. The kitchen analogy helps with specialization and coordination, but it hides network failure, data copies and irreversible external effects.

## Paper packet worked answer

Choose M, a modular shared deployment, as the provisional design. One team, monthly joint change, no distinct scaling/availability requirement and no second owner offer little evidence of useful independent deployment; the new service adds network/on-call/contract burden. Maintain explicit module interfaces, tests and access boundaries so M is not a ball of shared state. S can become preferable if there is measured release blocking, distinct load or availability, real owners with staffed operations, clear contracts, private data and a business outcome improved by independent change. An actual legal/data boundary could also reverse the choice.

On stale Approved Wording after Receipt View updates, compare the source event and Policy version at composition. Stop the misleading view/draft route if versions cannot be reconciled. Use approved static wording with a visible “current status unavailable” condition or an accepted manual route; do not infer satisfaction. Policy owns wording, Engineering owns binding/test, operations owns stop/recovery, Support owns only an accepted human route, release owns exposure. Reconcile affected view IDs and assess who saw wrong guidance. A code rollback cannot recall a message already read.

Accept S if a student supplies credible new facts that the packet lacks and prices/owns the extra operations. A bare “microservices scale better” is insufficient. A simple current path without a new R7 build can also be correct if the capability need has not been demonstrated.

## Synthetic cost arithmetic

Shared platform care: 6 invented hours/week. Separate: `3 × 5 + 7 = 22` invented hours/week. Difference: `22 − 6 = 16`. If a real independent-release benefit removed a **measured** 25-hour weekly bottleneck and owners could cover the 22 hours, S might deserve evaluation; 25 is merely an illustrative switching assumption, not a Harbor baseline or ROI. This arithmetic excludes incident severity and learner impact, so it cannot decide alone.

## Two common wrong answers and feedback

- “Each noun needs a service.” Feedback: name a cohesive domain responsibility, state owner and independent deployment benefit. A bounded context can be a module. More services can add synchronous dependencies and eventual-consistency work.
- “Rollback restores the business.” Feedback: distinguish code state from external state. A message or payment already delivered needs reconciliation and possibly a separate corrective action, which itself can fail.

For the payment-like thought experiment, a second request ID after timeout is a second intended operation to the receiver. Reuse the original identity and reconcile before any refund; a refund is not erasure of the original charge.

## Transfer rubric (12 points)

Award 0–2 each for: (1) business capability and actual independent-change reason; (2) module and service boundaries with cohesion/coupling; (3) authoritative data/effect owner and explicit forbidden inferences; (4) change/deploy/operational cost with team and on-call capacity; (5) partial success, timeout/retry identity, rollback-versus-external-state recovery; (6) justified recommendation, countercondition, bounded AI assistance and manual fallback. Full marks require an explicit condition that would reverse the recommendation and a per-learner access check where protected records are involved. No points depend on choosing microservices.
