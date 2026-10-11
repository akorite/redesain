# Study Textbooks — The Textbook Factory

## Goal
Produce eight university-style study textbooks in LaTeX, one per `bookN-*` directory, for a single reader: an 18-year-old Grade-12 student in Indonesia, strong at maths and programming, aiming at competitive programming, olympiad maths, ML, FPGA/CPU design, quantitative research and engineering physics. Every chapter ships with worked examples, figures, code listings with real captured output, graded exercises, common-mistakes pedagogy, a further-reading list and a verified watch list.

## Agent pipeline

| Role | Who | Duty |
|---|---|---|
| Coordinator | the root Devin session | Plans, splits work, runs the merge gate (clean build + real outputs + page count), applies reviewer-specified fixes, keeps docs current, talks to the reader. Never writes book content. |
| Author agents | one Devin session per book (max 4 active) | Write chapters to the approved outline: ≥5 worked examples, ≥6 figures in visual topics, ≥15 additional exercises, real code output, Further reading + Watch sections. |
| Reviewer agents | a *different* book session per chapter | Independent review: recompile, rerun every script, verify every claimed number against real output, check proofs. Verdicts PASS / REVISE(items) / BLOCKER(reason), logged in each book's `docs/review-log.md`. |

Hand-off: coordinator sends each author a chapter spec + a repo snapshot tarball + the style handoff; author returns changed files as attachments + structured output; coordinator lands, compiles, commits, then ships a full-repo packet to the reviewer session; verdicts route back through the coordinator.

Review pairs: book1↔book2, book3↔book5. Wave-2 books fill in as slots free.

## Repo architecture

- `bookN-*/` — one book each (LaTeX, `main.tex`, `chNN-*.tex`, `figures/`, `code/`, `docs/` including outline, notation, sources, progress, review-log, decisions, unverified, watch)
- `shared/` — `lifeos.sty` (frozen, never edited), `notation-shared.md`, `template/`
- `docs/` — `decisions.md` (all binding decisions), `status.md` (per-chapter state)
- `metrics.csv` — per-chapter metrics (see header)
- `case-study/` — `lessons.md` + per-book retrospectives
- `COMMUNICATION.md` — how issues/PRs/labels are used

## Risks and mitigations
- **Invented sources/URLs** — every source row is fetch-verified; videos must be actually opened; failures go to `docs/unverified.md`; link-rot re-check at release.
- **Real-output fraud** — reviewers rerun every listing byte-for-byte; "verbatim" claims get diffed against regenerated output.
- **Math errors** — reviewers hand-verify proofs; REVISE verdicts have caught real errors (see case-study/lessons.md).
- **Page creep** — floor 180, target 220–320, ceiling 350; substance only, cut repetition.
- **Missing `\input` in main.tex** — recurring author defect, caught at merge gate by page-count mismatch.
- **Attachment URLs expire** — coordinator re-uploads packages every dispatch.

## AI-use statement
All chapter text, figures, code and exercises are written by AI agents (Devin, swe-2-max) to a human-approved outline. Every chapter is independently reviewed by a second agent that recompiles the book and reruns every script byte-for-byte. All external sources were fetched and read; every video link was opened and confirmed. No content is copied verbatim from any source. The coordinator (also an agent) enforces the merge gate but does not write content. The human reader approved the outlines, the binding decisions in `docs/decisions.md`, and reviews finished books.
