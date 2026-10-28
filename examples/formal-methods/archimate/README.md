# Small ArchiMate 4 teaching view

Original editable JSON graph and SVG, not the Open Group exchange format or a vendor-native project. No ArchiMate 3.2 tool is represented as a version 4 validator. Element/relationship scope is deliberately limited; rules are manually traced to the supplied ArchiMate 4 specification. The JSON and the supplied SVGs remain editable; this companion does not include an automatic graph renderer. The book authoring repository holds that renderer. A future tool import must verify its own supported version.

- `r7-explanation.json`: corrected proposed target, five elements and four relationships.
- `r7-explanation-broken.json`: serving direction is reversed relative to the stated service meaning, and a capability is mislabeled as an application. These are meaning errors, not necessarily forbidden type pairs.

Run `python3 scripts/check_archimate_teaching.py` in the companion or book root. It checks references, the selected relationship profile and the exercise's stated semantic expectations. Passing does not certify arbitrary ArchiMate models, actual implementation, authority or requirement satisfaction. Specification PDFs are not distributed.

Inspect the companion’s `examples/formal-methods/fig-ch04-03.svg` and the [deliberately broken view](r7-explanation-broken.svg), then compare each relationship with its sentence in the chapter.
