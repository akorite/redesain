# Retrospective — book2-discrete v0.1 (first finished book)

## Numbers (from metrics.csv)
- 17 chapters + back matter, 151 pp (pre-depth-pass; v0.2 target ~220)
- Review rounds: 17/17 chapters independently reviewed (book1 agent); verdicts: 13 ACCEPTED, 4 REVISE
- Defects caught pre-merge: 4 math/content errors (all fixed + verified), ~9 style/format nits (deferred batch, landed clean)
- Code: 1 listing/chapter (verify_*.py + test_*.sh), all run real — 0 code defects at review
- Sources: ~30 verified, ~8 failed-fetch honestly logged
- Time: ~5.5h wall clock first-draft→v0.1 across the 4-agent pipeline

## What review caught (full detail in case-study/lessons.md)
1. False inexcenter angle split (ch15 geometry) — real math error, fixed.
2. Wrong Schur grouping identity (ch09) — real math error, fixed.
3. Broken induction "salvage" claim (ch03 horses) — the strongest catch: author claimed a classic broken proof could be repaired; reviewer proved it couldn't; section rewritten as a taught failure-mode.
4. Mislabelled AMC problem (ch08) — citation error, re-sourced.

## What review missed / process gaps
- Recurring `\input{chNN}` missing from main.tex on 4 chapters — caught only by page-count mismatch at merge gate, not by reviewers. Fix: gate now greps main.tex first.
- Review packets built by hand missed earlier chapters (book5 nit). Fix: packets are now the full repo tarball.
- Tag-case drift on review-log verdicts (ACCEPTED vs Accepted) — cosmetic, normalized line-by-line.
- Several captions overclaimed figure content vs what the .tex actually drew — reviewers now asked to open figures, not trust captions.

## What worked
- Verbatim-fix convention (reviewer specifies exact replacement text, coordinator grep-verifies) resolved REVISEs without a full re-review round-trip.
- Deferred-nit batch: all 9 nits landed in one pass without re-review.
- Reviewer judging depth vs the *outline's* plan (not raw pages) kept chapters honest when pages dipped.

## Changes for v0.2 (depth pass, in flight)
- New contract applied retroactively: ≥5 WEs, ≥6 figures, ≥15 exercises, Further reading (verified links), Watch rulebox (verified videos), docs/watch.md, link-rot pass at release.
- Every changed chapter re-reviewed independently before the v0.2 tag.
