# Chapter 4: Ground and evaluate AI answers — worked answers

## Synthetic 100-question table

Coverage = 70/100 = 70%. Support among answers = 54/70 ≈ 77.14%. Supported-answer coverage = 54/100 = 54%. Unnecessary abstention among answerable questions = 20/80 = 25%. Unsupported answering among unanswerable questions = 10/20 = 50%.

The 16 unsupported answers include 6 answerable questions answered incorrectly/without support and 10 unanswerable questions answered anyway. Thirty abstentions include 20 unnecessary and 10 appropriate. Do not call all abstentions safe successes or all failures. These labels are synthetic under the defined reference evidence, not measured learner outcomes or a release standard. High apparent support can be traded against low coverage; inspect joint behavior and consequences.

## Retrieval

Precision = 9/15 = 60%. Recall = 9/12 = 75%. Three relevant passages missed; six retrieved passages irrelevant. Completeness of known relevance labels is explicitly assumed in this toy task. Neither score establishes permission, version eligibility, sufficiency, faithful answer use, useful action, or business outcome. Accept any two well-explained limits.

## Grader failure

The candidate includes both required strings, so a keyword check passes despite its unsupported approval. Correct reference behavior preserves staff review and does not establish permission. Use a rubric that checks the implication, validate status/action constraints where possible, and challenge with paraphrases, negations, contradictory clauses, and otherwise fluent violations. Pair with relevant domain review; also pass a correct, authorized R7 explanation through the revised grader to check that the guardrail does not reject ordinary good work. Do not claim a new keyword list proves semantic correctness. Preserve the failed evaluation record and explain changes.

Zero observed failures does not prove absence of future failures. Even an independent fixed-probability binomial example with n=100 has p_upper=1−0.05^(1/100)≈0.029513=2.95% for the one-sided 95% exact upper limit. For the chapter’s intuition check, `0.97^100 ≈ 0.04755`: a fixed 3% failure probability can still produce zero failures in about 4.76% of such independent 100-trial samples. Neither that illustration nor the upper bound defines an acceptable operational rate. This is not a Bayesian probability about a fixed parameter, an estimate of real model risk, or a license to use a 2.95% rate. Real cases may be selected/correlated/nonstationary, invalidating a naive application.

## Self-study paper rubric: 16 points

Five metrics with labeled denominators: 5. Retrieval calculations: 2. Two retrieval limits: 2. Grader diagnosis and correction/challenge: 4. Zero-failure reasoning and assumption limits: 3. Accept equivalent correct expressions and defensible test suggestions. Flag unsupported go-live conclusions or eligibility implications as substantive misunderstandings.

## Transfer worked Harbor answer

Decision: whether a narrowly scoped staff-reviewed explanation experiment merits continued testing, not direct autonomous approval. Cases: applicable R7 with receipt question; missing/conflicting source; a candidate that includes expected keywords but falsely authorizes a start. Expected behavior and prohibited actions follow the explanation-only boundary.

Checks: source version and prohibited tool invocation via code; implication and usefulness via explicit rubric/domain reviewers. Human disagreement triggers policy/rubric clarification; it is not resolved by asking a model to silently relabel references. Held-out cases separated from development variants and regression collection; record overlap/near-duplicates. Measures: support/coverage with denominators, source eligibility, consequential errors, review workload, latency/cost per acceptable task. Offline scores do not establish learner completion or staffing savings.

Recommendation may pause learner delivery, inspect causes, compare a reviewed template, and continue only within approved access and staff capacity. Policy owner validates meaning; technical owner enforces controls and maintains evaluation; Operations owns receiving support; business owner authorizes the progression. Fallback is maintained reviewed guidance/manual path. Monitor source/model/grader changes and operational outcomes under privacy limits. No universal score threshold or guarantee.

Proposed transfer rubric: decision/scope 2; cases/reference behavior 2; checks/reviewer responsibility 2; held-out/metrics/limits 2; fallback/ownership/change handling 2 = 10.

Common misconceptions: more citations means grounded; a model judge is objective because it returns a number; all abstentions are errors; a no-write tool makes misleading answers harmless; one repaired counterexample proves the grader is robust. Ask learners which assumption would need evidence before the conclusion follows.
