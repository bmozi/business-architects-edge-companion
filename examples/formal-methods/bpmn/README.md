# R7 BPMN teaching models

The corrected model and intentionally broken exercise are original fictional, descriptive BPMN 2.0.2 collaborations. Neither is executable or an operating agreement. No new assistant action is authorized.

`r7-staff-handoff.bpmn` keeps sequence flows inside each participant and uses message flow for staff submission to the receiver. `r7-handoff-broken.bpmn` has a cross-participant sequence flow and same-participant message flow. Repair both; do not infer learner resolution from submission.

Run `python3 scripts/check_bpmn_teaching.py` from the repository root. This checks selected XML graph invariants and deliberately rejects the broken example; it is not complete XSD/conformance or engine validation. No dependencies, cloud account or credentials are needed for this check.

In the companion, open `examples/formal-methods/fig-ch24-03.svg` for visual inspection of the corrected view. Edit the `.bpmn` files in a viewer/editor that supports BPMN 2.0.2; importing a file is not proof that its business meaning is correct. The book authoring repository contains the pinned rendering build; installing that tooling is not required to use this companion exercise.
