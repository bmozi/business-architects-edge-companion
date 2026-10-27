# Chapter 10: Deliver through CI/CD — worked answers

This guide works the fictional R7-C28 packet. It is not a GitHub configuration audit, a Harbor release record, a production metric or a claim that any learner saw the bad message.

## Teach-back

**Continuous integration** combines proposed code and runs repeatable checks so integration problems are found early. **Continuous delivery** keeps a built, checked change ready for an authorized release. **Continuous deployment** automatically promotes eligible changes to production under predefined policy. A team can practice CI and continuous delivery while retaining a human decision for this R7 release. Merge, deploy and release are distinct: the protected branch changes source, deployment places tested bytes, and release exposes behavior to people.

## Worked packet

The PR should **not merge or release**. It makes receipt imply satisfaction, directly contradicting R7. It deletes the negative assertion and changes a control file, while a job-level `if` condition skips the required `r7-contract` job for the mapping file. A workflow-level `paths` filter would instead leave its required check pending. GitHub may count a required skipped/neutral check as satisfied; a green merge box therefore supports only the narrow observation that configured status requirements were met as reported. It does not show that the R7 contract ran, that the canonical rule body was used, that the intent is right, or that the proposed database migration can be reversed safely.

**First stop and owner.** The engineer or reviewer stops the PR immediately on the semantic mismatch. The policy owner confirms R7 meaning. The CI/governance owner repairs the required job and its source of truth; the repository owner verifies branch protection, expected status source, control-file ownership and bypass roster. The agent gets no merge or rule-edit authority. If a bad version had escaped in a different scenario, operations would stop exposure and coordinate correction with learner-support and policy owners; do not claim a code rollback erases messages already shown.

**Repairing the gate.** Use the canonical rule body at an approved version/digest. Ensure a required job actually runs on every relevant PR and fails on missing inputs or an altered assertion. Verify its result at the PR SHA; do not conditionally skip the job for mapping changes. Do not use a workflow-level path filter that leaves required checks pending. Protect the workflow and CODEOWNERS files as well as the application code, with effective review rules and documented exceptions. An expected trusted check source helps prevent a different actor from simply reporting the same check name, but it does not guarantee the test logic is right. A local hook is useful feedback, not the authoritative gate.

**Prove both sides.** Dirty fixture: deliberately map `documents_received: true` to “requirement satisfied” while review remains pending; the exact required CI job must fail. Clean fixture: change to “received for staff review” with current R7 and unchanged no-write authority; local hooks on actual developer shells and CI must allow the change. Test an archived R6 passage, unknown status, denied learner, source timeout and accessible label. The reviewer records the exact fixture, runner, commit and result. If the clean path fails because of an obsolete shell built-in or an overly broad scanner pattern, repair the gate before mandating it.

**Schema later, if truly needed.** For a new `approved_policy_version` field, first add a compatible field while old readers still work. Then populate/backfill, update writers/readers behind a tested rollout, check coexistence and only later remove the old field after the rollback window. Separate schema, data and access-code changes. A backup or down migration may be needed for a destructive step; no blanket rollback guarantee follows from a deployment tool. The current wording correction requires no database migration unless evidence establishes one.

**Arithmetic and meaning.** The first synthetic month has `1 ÷ 20 = 0.05 = 5%` intervention releases. The second has `6 ÷ 30 = 0.20 = 20%`. Releases increased by 10; intervention releases by 5; the intervention proportion quadrupled. That does not show AI caused the change or that the same denominator definition was used in real life. The sponsor should also see change lead time, failed-deployment recovery time and deployment rework rate, plus R7 wrong-message reports, staff corrections, accessibility handoff completion and learner-facing impacts. Define each measure, time window and owner before comparing periods.

## Transfer rubric (12 points)

Award one point each for:

1. Names a human/business outcome and the invariant the change must preserve.
2. Separates CI, delivery, deployment, merge and release authority.
3. Uses a versioned intent/acceptance artifact and challenges whether the intent is right.
4. Bounds the AI agent's source, files, permissions and evidence report.
5. Provides a positive and a negative semantic contract case, including a clean-path check.
6. Protects actual canonical rule content rather than a familiar filename.
7. Makes the correct CI status required and tests skip/neutral and modified-workflow paths.
8. Assigns code/policy/workflow ownership, review and a narrow recorded exception path.
9. Separates untrusted PR validation from privileged build/deployment credentials.
10. Identifies and verifies the promoted artifact/digest, not only a green source SHA.
11. Plans compatible migration or justified no-migration, exposure stop and residual correction.
12. Pairs throughput with failure/recovery and user-facing outcome evidence; states unknowns.

## Common wrong answers and feedback

- **“Green means correct.”** Ask which exact fixture ran against which SHA, whether it could be skipped, and whether it represented approved R7. Green can reflect an incomplete or weakened specification.
- **“The agent promised not to change tests.”** A prompt is not a repository permission or branch rule. Remove its control-file authority and verify the independent gate/review configuration.
- **“CODEOWNERS makes it impossible to change the workflow.”** It supplies a review requirement only when configured with an effective protection rule, and authorized humans can still err or use a bypass.
- **“Roll back the app and everything is undone.”** An incompatible database migration, external communication, or already viewed wrong message may survive app rollback. Plan forward repair, compatible phases and human correction.
- **“More deployments prove success.”** A rising change-failure rate or unresolved learner confusion could erase the benefit. Compare denominators, definitions and the actual R7 outcome.

An answer may choose a content-only correction rather than a code PR if the governed content system can meet the same R7, accessibility, traceability and recovery requirements. The learner should defend that choice with evidence, not treat less automation as failure.
