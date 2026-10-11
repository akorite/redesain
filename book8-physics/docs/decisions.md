# Decisions — user-approved, 2026-10-10 (binding)

Recorded verbatim from the coordinator's approval. Applies to all eight books; each book
also has its own `docs/outline.md`, `docs/notation.md` and (books 3/4/6) `docs/notation-shared.md`.

1. **Logarithms:** `log` = natural log in all 8 books. Write `ln` only when contrasting
   with another base. Other bases always explicit (`log_2`, `log_10`). In Book 1, complexity
   uses `log_2`, with one sentence that the base does not matter inside `O()`.
2. **Symbol collisions** (sigma, lambda, etc.) in Books 4/6: accepted. Each book's
   `notation.md` lists every collision and its local resolution. Never use a colliding
   symbol in two meanings within one chapter without redefining it at the point of use.
3. **Book 1:** DP optimisation and Sprague–Grundy are "routed, not taught": a short chapter
   section plus named problems and external references. Do not copy CP4 (Halim); cite it and
   paraphrase ideas only. Geometry and probability chapters stay in, marked `[optional]` and
   excluded from the core page budget.
4. **Book 2:** Chen/Zhao free handouts replace EGMO as the anchor; cite them, do not
   reproduce them. Merge ch15 and ch16 so the book lands at 240 pages or fewer. No SageMath;
   Python with SymPy. The capstone lives in `portfolio/` (a template plus 20 proof stubs the
   reader completes himself), and ch18 explains how to use it.
5. **Book 3:** determinants stay mid-book (Strang order), with a boxed note on the
   determinant-free (Axler) view. CS229 archived notes are allowed as a cited, read-only
   source. Reproduce nothing.
6. **Book 5:** Tang Nano 9K is the reference board; its price and Indonesian availability
   are marked `[unverified]` with an access date. Use the current stable KiCad at writing
   time and pin the version in `code/README.md` (verify, don't assume). Mains voltage is out
   of scope: one safety note telling the reader not to work on it without proper supervision.
   Custom 8-bit ISA for the book CPU, with a short chapter section mapping it to a RISC-V
   subset so it leads into Book 7. Op-amp and power chapters may merge if needed for the
   page budget.
7. **Book 5:** every chapter gets a "Common mistakes" section (floating inputs, missing
   pull-ups, inferred latches, clock-domain slips, missing testbench cases, etc.).
8. **Hosting:** NO GitHub, no remote of any kind. Local git repositories only
   (`git init`, commit per chapter, tag `v0.1` at release). Delivery = one zip per finished
   book (repo without build junk) plus `main.pdf`, plus a progress zip of `docs/` after each
   outline and each completed book. If files cannot be attached, say exactly how to retrieve.

## Process rules from the same approval

- Wave-2 outlines (books 4, 6, 7, 8) go through the same §3B research + approval gate;
  no Wave-2 chapters until approved. Book 4 ← shared notation, Book 6 ← shared notation,
  Book 7 ← Book 5 outline, Book 8 free.
- Chapter loop: one author agent + an independent reviewer per chapter, in chapter order;
  never more than 4 agents at once.
- §3A strictly: ≥4 figures and the required code listings per chapter with real outputs;
  a one-page summary table or diagram at the end of each chapter.
- Report only when: a Wave-2 outline is ready, a whole book is finished, or a user-owned
  decision blocks work. No per-chapter reports.
- Page-budget pressure → use the compression order named in the outline; never cut figures,
  code outputs, worked examples, or Common mistakes sections.
- Keep `docs/progress.md`, `docs/review-log.md`, `docs/sources.md`, `docs/unverified.md`
  current as we go.
