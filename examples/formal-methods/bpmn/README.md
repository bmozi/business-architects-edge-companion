# R7 BPMN teaching models

The corrected model and intentionally broken exercise are original fictional, descriptive BPMN 2.0.2 collaborations. Neither is executable or an operating agreement. No new assistant action is authorized.

`r7-staff-handoff.bpmn` keeps sequence flows inside each participant and uses message flow for staff submission to the receiver. `r7-handoff-broken.bpmn` has a cross-participant sequence flow and same-participant message flow. Repair both; do not infer learner resolution from submission.

Run `python scripts/check_bpmn_teaching.py` from the repository root. This checks selected XML graph invariants and deliberately rejects the broken example; it is not complete XSD/conformance or engine validation. Install the pinned rendering tool with `npm ci --prefix tools/formal-models --ignore-scripts`, then run `node scripts/render_bpmn_model.js` and `node scripts/render_figures.js`. Native import/export succeeded without warnings; human review of semantics is still necessary. Source: OMG BPMN 2.0.2 §§7.3, 7.6, 9.3–9.4, 10.3.3–10.3.4, 10.6.2. Full print/device proof pending integration completion.
