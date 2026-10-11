# study-textbooks

Eight university-style study textbooks in LaTeX, written and reviewed by coordinated AI agents, for a Grade-12 reader aiming at competitive programming, olympiad maths, ML, FPGA/CPU design, quant research and engineering physics.

| Book | Dir | Topic |
|---|---|---|
| 1 | `book1-cp/` | Competitive programming (C++) |
| 2 | `book2-discrete/` | Discrete mathematics & olympiad proof |
| 3 | `book3-linalg-ml/` | Linear algebra for machine learning |
| 4 | `book4-ml/` | Machine learning fundamentals |
| 5 | `book5-electronics/` | Electronics & digital design → FPGA |
| 6 | `book6-quant/` | Quantitative research & markets |
| 7 | `book7-systems/` | Computer systems & CPU design |
| 8 | `book8-physics/` | Physics for engineers |

Build any book: `cd bookN-* && make` (TinyTeX; `make test` runs the code harnesses). Shared style: `shared/lifeos.sty` (frozen). How this was built: `PROJECT.md`. Chapter metrics: `metrics.csv`. What the review loop caught: `case-study/lessons.md`.
