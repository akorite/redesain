# Independent re-review — depth-passed content, textbook-cp ch01–13
Reviewer: ml session (devin-f668200453f145a4ab3116a5536cf4ec), 2026-10-11.
Scope: NEW content only (Further reading, Watch rulebox, added WEs/exercises). Base text not re-reviewed.

## Verified clean (all chapters)
- **FR URLs:** 65/65 distinct non-video URLs live-checked with curl → all HTTP 200 (usaco.guide modules, cp-algorithms pages, cses.fi tasks+book, cppreference, wikipedia, research.google blog).
- **Watch videos:** 26/26 verified via YouTube oEmbed (title + channel match claimed) and watch-page `approxDurationMs` — every claimed duration within ~0.6 min of actual (all claims are honest roundings). Content-match annotations plausible; no invented videos.
- **Cited refs:** every `\cite{}` key resolves to a real `\bibitem`; all bib URLs live (incl. usaco.guide/PAPS1.pdf, cses.fi/problemset/list, icpc.global/worldfinals/rules, cpbook.net). `laaksonen2024` chapter-number citations checked against the actual CPH PDF table of contents (see below — 3 items wrong/half-wrong, rest correct: ch01 ch.1–2 ✓, ch02 ch.5 ✓, ch03 ch.6 ✓, ch06 ch.8 ✓, ch09 ch.15 ✓).
- **Exercise soundness:** all named problems are real CSES/USACO problems correctly mapped to each chapter's technique (spot-verified task titles on cses.fi: 1644 Maximum Subarray Sum II, 1193 Labyrinth, 1688 Company Queries II, 2220 Counting Numbers, 1647 Static Range Minimum, 1673 High Score, 1660 Subarray Sums I — all exact). No invented problem names.
- **Code claims:** all 13 test suites re-run under bash → ALL PASS (stress counts reproduced: 200–400 rounds per chapter).

## REVISE items (verbatim fixes)

### REVISE-1 — ch04 Further reading: wrong CPH chapter
`ch04-cp.tex` ≈ line 385–386, item reads:

> `\item Laaksonen, \emph{Competitive Programmer's Handbook}, ch.~4 ``Binary search'' (beginner).`

CPH ch.4 is "Data structures". Binary search lives in **§3.3 of ch.~3 "Sorting"** (verified against cses.fi/book/book.pdf TOC). Fix verbatim:

> `\item Laaksonen, \emph{Competitive Programmer's Handbook}, ch.~3 ``Binary search'' (beginner).`

### REVISE-2 — ch07 Further reading: wrong CPH chapter
`ch07-cp.tex` ≈ line 289–290, item reads:

> `\item Laaksonen, \emph{Competitive Programmer's Handbook}, ch.~7 ``Graph algorithms'' (beginner).`

CPH ch.7 is "Dynamic programming"; no chapter is titled "Graph algorithms". The traversal material is ch.~11 "Basics of graphs" and ch.~12 "Graph traversal". Fix verbatim:

> `\item Laaksonen, \emph{Competitive Programmer's Handbook}, ch.~11--12 ``Basics of graphs''/``Graph traversal'' (beginner).`

### REVISE-3 — ch05 Further reading: half-wrong CPH chapter
`ch05-cp.tex` ≈ line 364–366, item reads:

> `\item Laaksonen, \emph{Competitive Programmer's Handbook}, ch.~8 (beginner). ... --- prefix sums and the sliding-window minimum-sum problems in one short read.`

Ch.~8 "Amortized analysis" does contain §8.1 two pointers and §8.3 sliding-window minimum, but prefix sums are formally ch.~9 "Range queries" (§9.1). The cited span should include both. Fix verbatim:

> `ch.~8` → `ch.~8--9`  (keep the annotation; it then covers two pointers, sliding-window minima AND prefix sums)

## Nits / observations (not blocking)

- **Systemic, not chapter-specific:** `Makefile` line ~15 runs `sh "$$f"` over `code/test_*.sh`, but test_ch02–ch17 use bash syntax. `make test` fails: ch03/ch04 die with `syntax error near unexpected token '('`, and ch02 reports "SOME CHECKS FAILED" under `sh` despite passing all checks under `bash`. Fix verbatim: `sh "$$f"` → `bash "$$f"` (or downgrade scripts to POSIX sh). Under bash all 13 suites pass.
- **Exercise counts (if ≥15-total floor applies to depth pass):** ch04 = 14 total (12 additional), ch06 = 14 total (11 additional; already a logged nit from the earlier review). ch01 = 17, ch02/09 = 15, all others ≥16.
- **WE/figure floors (observation only — depends on contract scope):** `example` environments count 4 in ch01/ch02/ch04/ch06/ch09 (<5 elsewhere ≥5); `figure` floats: ch02/ch04 = 4, ch07/ch12 = 6, all others = 5. If the ≥5-WE / ≥6-figure floor applies to depth-passed chapters, ch01/02/04/06/09 need +1 WE and most chapters need +1–2 figures; if the pass was content-additions-only, these are inherited gaps worth noting for a future pass.
