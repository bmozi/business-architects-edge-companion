# Chapter 29: Expose cross-functional dependencies — worked answers

The reader's paper packet, Harbor register and API are fictional. No team, vendor or learner has actually agreed to, tested or used the proposed route. The aim is to make an exchange decision-ready and to preserve the difference between a named, agreed and working dependency.

## Teaching purpose and pacing

The learner should identify the supplier and **receiving** function, authority over meaning, acceptance evidence, capacity, sequence and fallback. A strong answer changes a launch plan when the receiver cannot accept the work; it does not turn honest refusal into a villain. Suggested use: 30 minutes individual work, 15 minutes paired supplier/receiver challenge, 15 minutes for a revised register. In self-study, solve before reading this key.

## Paper exercise: worked register

The packet permits several valid three-row priorities. One defensible set is:

| Priority and contribution | Supplier → receiver; authorized owner | Evidence and sequence | If absent; escalation and fallback |
|---|---|---|---|
| **1. Correct status meaning** | Policy owner approves R7; status-service owner supplies actual field contract → content/technical channel receives and policy owner validates the mapping | Test received-but-unreviewed, pending and reviewed cases against approved R7 wording before any status claim goes live. Version and permitted fields recorded. | `documents_received: true` must not become “approved.” Hold or correct the message through authorized owners. Use accurate “received, review pending” wording where supported; unresolved questions go to verified human support. |
| **2. Usable learner route** | Support/channel owner supplies contact path → affected learners test access and support/admissions receive the question | Appropriate people can reach and use the offered channel; a verified alternative exists before advertising the route. Do not infer accessibility from a successful link test. | Do not advertise the untested route. Use existing verified contact methods, ask the service/outcome owner to resolve scope and access, and record remaining barriers. |
| **3. Actionable acceptance and capacity** | Admissions operations defines eligible case types, required context and staffing → support/technology send only within that agreement | Admissions owner inspects sample cases with requirement ID, status, rule version, permitted return path and confirms what a reviewer can accept, return or reject; capacity/coverage agreed before new volume. | Keep current human handoff, narrow case types or delay volume. Sponsor/outcome owner decides resources and timing; admissions is not recorded as committed by meeting attendance. Returned cases retain a sending owner. |

An alternative three-row answer may put **status data contract** and **correction/fallback** ahead of the learner route, provided it still explains how affected learners get help and why new volume cannot be sent without a receiver. A team could also merge policy meaning with status semantics in one row if it keeps distinct approvers and tests. Do not require the exact IDs D1–D4; reward the logic and the acceptance evidence.

`documents_received: true` says the service reports receipt under whatever contract has been agreed. It does **not** establish satisfaction, authorized review, permission to start, or that the data are current or correctly associated with the learner. HTTP **202 Accepted** means an HTTP request was accepted for processing; under RFC 9110, the processing has **not** been completed and may not ultimately be acted upon. The packet's endpoint has no defined business acceptance, reviewer assignment, resolution or learner notification contract. It therefore cannot prove an admissions reviewer accepted the case, that the question was answered, that a requirement was satisfied, or that a learner was told the result. The learner may mention that a receiver-specific status/reconciliation path must be agreed; do not let a 202 response stand in for one.

A defensible immediate decision: correct misleading wording through the policy-approved existing channel if active wording is confirmed wrong; do **not** advertise the proposed new route or send extra case volume until access and admissions acceptance/capacity are agreed and tested. The sponsor can choose narrower scope, real capacity, a verified current route or a delayed promise. One strong question is, “Which case types can admissions accept with what fields, coverage and return state, and who has authority to make that commitment?” Another is, “Which people cannot use the proposed help channel and what route will serve them while we fix it?”

## Challenge and feedback

Ask, “Who would say the case is usable?” The receiver, with actual authority and capacity, not the sending team's test suite alone. Ask, “What happens when a case has insufficient context?” A strong answer keeps it owned and returned with a reason or routed through a defined correction path; it does not let it vanish. Ask, “What can the sponsor decide today?” Scope, resources, sequencing and a verified fallback, but not R7 meaning by fiat. Ask, “How would we know six months later that the route still works?” Evidence of accepted cases, backlog/returns, version drift, learner access, steward and review trigger.

Common wrong answer 1: “The endpoint returned 202, so admissions accepted the learner's issue.” Feedback: the protocol says accepted for processing, not completed; the receiver-specific business state is undefined. Ask for a status inquiry and a human acceptance rule.

Common wrong answer 2: “Admissions was in the planning meeting, so the dependency is green.” Feedback: a named/attended dependency is not an agreement. Ask the actual admissions owner what case types, fields, capacity, timing and return path it accepts. Record a disagreement rather than inventing consent.

Common wrong answer 3: “We can use AI to assign an owner to every exception.” Feedback: a model can suggest missing owners from approved notes, but only authorized people can commit a team or change policy. It cannot make capacity appear. Keep the accessible human fallback.

Common wrong answer 4: “We must delay the wording fix until the entire case API is built.” Feedback: the known misleading meaning can often be corrected or contained through existing approved channels. Separate that near-term obligation from the unready new route.

## Transfer-task rubric (12 points)

Score each dimension 0, 1 or 2. Give 2 for concrete, internally consistent and challengeable work; 1 for a partial or vague entry; 0 for missing or contradictory work. Do not convert the sum into a claim about job readiness or real operational performance.

| Dimension | What earns 2 points |
|---|---|
| Outcome and scope | Names the affected stakeholder outcome and a bounded exchange, with a useful simpler path or explicitly justified automation. |
| Meaning and authority | Separates semantic/policy approval, operating commitments and technical implementation, including who can decide each. |
| Supplier–receiver acceptance | Names both sides, actual or labeled fictional acceptance evidence, rejected/returned work and ongoing steward. |
| Timing and capacity | Shows which condition blocks a promise, needed-by/sequence, receiving coverage and what can proceed in parallel. |
| Failure and fallback | Traces a wrong/late/unknown contribution through detection, containment, reconciliation or rollback, residual effect and manual/accessible route. |
| Adaptive influence and AI limits | Records a legitimate objection that changes scope or sequence; bounds AI to approved inputs, traceable proposals and human validation/commitment. |

Feedback should begin with the first missing receiver or unsupported “ready” claim. Invite revision from the receiving function's point of view. A sanitized or fictional work example earns full credit when reasoning is sound; privileged employer details are not required. APQC, UK readiness guidance and RFC 9110 support distinctions and protocol meaning, not a claim that the invented Harbor handoff has been accepted or tested.

## Organization-map repair: worked answer

The register overstates Admissions acceptance. Narrow the proposed route to review questions carrying the accepted requirement identifier and permitted review context; even this does not create extra staffing or a response-time promise. Keep policy-meaning and upload-mechanism questions outside that acceptance until Policy/Support and the appropriate technical owner agree their respective routes. Sending staff retain unresolved/returned work under an explicit arrangement; do not abandon it between boxes.

The map's contribution link means Admissions participates in the capability, not that it receives every case. An organization chart or responsibility matrix cannot replace the receiver's agreement. Unknowns include coverage/capacity, volume, accessible alternatives, required context for other case types, return handling, current protected-use conditions and which authority can commit each change. The sponsor can decide resources or scope, not assign review authority by implication.

Score 2 each: distinguish contribution from acceptance; narrow case types correctly; route other decisions to appropriate roles without invented commitments; preserve sending/return responsibility; identify two concrete unknowns including time/capacity. Total 10. Transfer feedback checks unit/role/capability separation, information cross-map, a receiver's legitimate objection and a consequential revision.

## Maintained-definition exercise: worked answer

The memo's permission to approve after upload contradicts R7 regardless of CAP-02's name or revision. Explanation communicates permitted facts; an authorized review decision is a different ability. Revision 2 is a proposal and cannot authorize approval, model sending or a receiving commitment. Do not relabel this as a newly discovered real Harbor deployment.

Inspect at least two connected artifacts, such as the value-stage cross-map and information concept mapping, or the G1 decision and D1/D4 receiving agreements. A corresponding message/test/initiative may also need inspection. Policy decides rule meaning; Admissions decides authorized review; the sending and receiving owners settle scope and accepted capacity; Support's proposed steward maintains the record. Engineering implements the approved semantic boundary and negative tests, not a new eligibility rule.

Retain the old memo/revision as history, mark the invalid assumption and reopen its funding/release decision with the actual authorities. If the memo never led to exposure, do not invent recipients to correct. If real exposure were discovered, authorized operations would investigate and manage its consequences. No acceptance date is supplied; leave it unknown.

Score 2 each for identifying invalid permission; distinguishing revision from acceptance; two consequential impact links; rightful owners and retained history; a useful transfer objection or justified refusal to merge. Total 10. Feedback on “merge both status capabilities”: ask which produces the decision and which explains it. Similar labels do not erase distinct authority. Feedback on “buy a repository”: ask whether a controlled file and clear maintainer could support this bounded decision.
