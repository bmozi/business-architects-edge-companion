# The Business Architect’s Edge — companion resources

Companion worksheets and worked technical fixtures for John Briggs's *The Business Architect’s Edge: Connecting AI, Engineering, and Business Outcomes*.

Harbor Learning and all records, people, costs, metrics, and systems in these files are fictional teaching examples. These files are not production configurations or evidence of results at any real institution.

## Start here

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
| 23 — Orchestration | [Recovery card](examples/ch12-recovery-card.csv) | Ambiguous dispatch and replay |
| 24 — Events | [Event fixture](examples/ch13-r7-events.json), [consumer decisions](examples/ch13-consumer-decisions.csv) | Order, duplicates, unknown versions and business meaning |
| 25 — Recovery | [Recovery ledger](examples/ch14-recovery-ledger.csv) | View repair without learner-facing effects |

Run the optional offline checks with Python 3: `python3 scripts/check_resources.py`. No dependencies, account, cloud service or credentials are required. This checks supplied fixtures and arithmetic, not your decision quality or a live integration.

The book gives the context, questions, and limits for each exercise. Work from the chapter before copying a fixture.

Copyright © 2026 John Briggs. All rights reserved. Permission is granted to download and use these files for personal study alongside the book. Redistribution, resale, and production use require the author's written permission.
