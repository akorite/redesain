# Finish checklist — textbook-linalg-ml (§5 consistency pass, 2026-10-11)

Book status: **all 16 chapters written**, 191 pp, pdflatex clean —
0 overfull >3 pt, 0 undefined references, 0 errors, index built
(159 entries). Local git only; latest commit on `main`.

## 1. Notation audit — DONE

Checked every chapter against `docs/notation.md` +
`docs/notation-shared.md`.

- `\ln` → `\log` (binding decision: log = natural log): 11 sites in
  ch15 (Gibbs derivation, Gaussian-entropy formula, CE training note,
  tripwire, hint, summary table) + 2 sites in ch16 (GNB worked
  example). The surviving `\ln`-mention is prose *about* the
  convention, now written `\log`.
- Bare `\sum` → explicit bounds: ch05 (2, `_{i=1}^{k}`), ch07 (3,
  tr/det identities `_{i=1}^{n}`), ch08 (3, normal-equation matrix
  cells), ch13 (3, σ̂² + summary + NLL `_{i=1}^{n}`), ch15 (3,
  `_{x}` over the support). `\sum_{i<j}` relational forms pre-exist
  and are consistent.
- `\operatorname{softmax}` written out (was σ-named in ch11's
  derivative table) — σ reserved for sigmoid/singular values.
- Verified already-conformant: `\Pr[·]`, `\mathbb E[·]`,
  `\operatorname{Var}[·]` square brackets (zero round-bracket
  occurrences); design matrix one-row-per-sample (ch08, ch16);
  `\mathcal N` reserved for the Gaussian (no `\mathcal N(A)` kernel
  clash — `\ker` used); σ/λ/Σ collisions used only in their
  documented contexts; `\mathbb N` unused so the {1,2,…} convention
  is untested but unbroken.
- Open flag for the user (from notation-shared.md): books 3/4/6
  harmonized on `\log`; Book 2 still uses `\ln` — its harmonization
  is a coordinator/user decision, not book-local.

## 2. Cross-references — DONE

- `main.log`: zero undefined references/citations after the full
  pdflatex×2 + makeindex + pdflatex loop.
- ch16 capstone back-references verified semantically: OLS/normal
  equations → ch8 ✓, PCA → ch10 ✓, Bayes/MLE/GNB → ch13 ✓, GD →
  ch14 ✓, CE price of confident wrong answer → ch15 ✓, FD check →
  ch11/14 ✓. Chapters cross-reference in prose ("ch.8"), not by
  `\ref{ch:}` — consistent book-wide.

## 3. Contract sweep — DONE (flags in docs/progress.md)

Per-chapter counts measured, not fabricated: see the audit table in
`docs/progress.md`. ch14–16 fully meet the new contract. ch01–13
predate the 2026-10-11 directive: all pass the old floors; every
one lacks Further reading + Watch; WEs short of 5 in ch01/02/04/
05/06/09 (3) and ch03/10/11/12/13 (4); additional exercises short
of 15 in all of ch01–13 (10–14). Retrofit is deferred to the depth
pass per the directive ("don't retrofit now").

## 4. Bibliography / unverified / index — DONE

- All 18 `\bibitem` keys cited: `sannemo2025` was orphaned (0 cites)
  — now cited in ch01's notes where the CP-facing reference belongs.
- `docs/unverified.md`: was empty-header; now logs the two ch16
  StatQuest durations (oEmbed-verified identity, duration
  unconfirmable post-YouTube-lockdown) + a book5-awareness row.
- Index: 159 entries, alphabetical; one split entry unified
  (`bias--variance trade-off`/`tradeoff` → `tradeoff`).

## 5. Notes/chapternotes double heading — DONE

`\chapternotes` already emits `\section*{Notes}` (lifeos.sty:143).
The manual `\section*{Notes}` + `\addcontentsline` stacked on top of
it in ch05–ch15 (+ch10/11) is removed: single heading now. ch16
keeps its manual heading (it heads the numbered-citations enumerate)
and the `\chapternotes` token was dropped there instead. ch01–04
were already correct.

## Outstanding (not blockers)

- Depth retrofit for ch01–13 per the progress.md table (needs the
  coordinator's depth-pass go-ahead).
- Video durations are unverifiable platform-wide until a metadata
  source better than oEmbed exists (watch pages rate-limited;
  piped/invidious down). Handled honestly as "unconfirmed".
- `docs/watch.md` has rows for ch14/15/16 only — the retrofit adds
  rows for earlier chapters when their Watch sections land.
