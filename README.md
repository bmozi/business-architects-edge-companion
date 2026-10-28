# The Business Architect’s Edge — companion resources

Companion worksheets and worked technical fixtures for John Briggs's *The Business Architect’s Edge: Connecting AI, Engineering, and Business Outcomes*.

Harbor Learning and all records, people, costs, metrics, and systems in these files are fictional teaching examples. These files are not production configurations or evidence of results at any real institution.

## Worked answers and decision templates

The [chapter answer guide](answers/README.md) covers all 32 reader chapters. Attempt the paper exercise before opening its answer. The [decision templates](templates/README.md) provide eleven reusable worksheets with fictional filled examples for your decision dossier, from the first outcome charter through a capstone recommendation and career evidence.

## A practical route for a new business architect

1. Read Chapter 1 and start the [outcome charter](templates/outcome-charter/README.md) with one safely discussable problem.
2. Work through Chapters 26–29 and the four practice kits below. Add the [information map](templates/information-map/README.md) and [organization map](templates/organization-map/README.md) to explain meanings, contributions and actual commitments.
3. Use Chapters 18–19 to compare current and target architecture, identify gaps, plan usable transitions and route decisions. Inspect the [architecture decision worksheet](templates/architecture-decision/README.md) and [worked answers](answers/README.md).
4. Use the [BPMN handoff](examples/formal-methods/bpmn/README.md) and [ArchiMate 4 view](examples/formal-methods/archimate/README.md) when a workflow or supporting relationship needs more precision.
5. Attempt the Chapter 31 capstone before reading its [answer](answers/chapter-31.md). Produce a recommendation with viable alternatives, evidence, owner gates and a condition that would change your mind.

Keep the objection and revision with each artifact. A useful dossier shows how the reasoning changed, not just a completed worksheet. These exercises support practice; use your organization’s actual policies and experienced feedback when applying them at work.

## Resources by reader chapter

Use the printed chapter numbers below. Filenames such as `ch09` preserve authoring IDs; they are not the book's chapter numbers. The book can be read without running code. Solve each paper exercise before reading its worked answer.

| Book chapter | Resource | Use |
|---|---|---|
| 26 — Business capabilities | [Capability kit](business-practice/capabilities/README.md) | Blank gap worksheet, paper packet, worked answer and rubric |
| 27 — Strategy to execution | [Strategy kit](business-practice/strategy/README.md) | Trace, measure definitions, ownership and evidence gate |
| 28 — Investment | [Investment kit](business-practice/investment/README.md) | Fit-first options worksheet, synthetic cost model and checked sensitivities |
| 29 — Dependencies | [Dependency kit](business-practice/dependencies/README.md) | Supplier/receiver register, acceptance conditions, fallback and worked answer |
| 20 — API design | [OpenAPI example](examples/ch09-r7-api.yaml) | Proposed contract, authority limits, errors and idempotency |
| 21 — Enterprise integration | [Mapping worksheet](examples/ch10-r7-mapping.csv), [synthetic data](data/fig-ch10-data.json) | Source/view meaning and the 96 + 1 + 3 comparison |
| 22 — Microservices | [Boundary worksheet](examples/ch11-boundary-decision.csv) | Ownership of facts and effects |
| 23 — Distributed failure | [Recovery card](examples/ch12-recovery-card.csv) | Ambiguous dispatch and replay |
| 24 — Events | [Event fixture](examples/ch13-r7-events.json), [consumer decisions](examples/ch13-consumer-decisions.csv) | Order, duplicates, unknown versions and business meaning |
| 25 — Recovery | [Recovery ledger](examples/ch14-recovery-ledger.csv) | View repair without learner-facing effects |

Run the optional offline checks with Python 3: `python3 scripts/check_resources.py`. No dependencies, account, cloud service or credentials are required. This checks supplied fixtures and arithmetic, not your decision quality or a live integration.

The book gives the context, questions, and limits for each exercise. Work from the chapter before copying a fixture.

Copyright © 2026 John Briggs. All rights reserved. Permission is granted to download and use these files for personal study alongside the book. Redistribution, resale, and production use require the author's written permission.

## Optional model checks

The [formal-methods examples](examples/formal-methods/README.md) include corrected and deliberately broken models, editable SVGs and source-rule notes. Run these from the repository root with Python 3:

```sh
python3 scripts/check_bpmn_teaching.py
python3 scripts/check_archimate_teaching.py
```

Both use only Python’s standard library. The checks cover selected model rules and exercise expectations; they do not grade your judgment or certify general standards conformance. No model-rendering build tools are included in this companion.
