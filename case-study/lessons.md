# Lessons — what the review loop actually catches

Growing file. Per-book retrospectives land as each book finishes.

## Book 2 (discrete) — what review caught

The independent-review gate caught **4 real math errors in 17 chapters** — roughly one blocker per 4 chapters:

1. **False incenter angle split (ch15 geometry).** The proof sketch claimed `∠IBM = ∠IBA + ∠ABM` — a split that doesn't exist; the correct decomposition is `∠IBC + ∠CBM` where `∠CBM = ∠CAM = A/2` (both subtend arc CM). Caught because the reviewer hand-re-derived every proof step, not because anything "looked off."
2. **Wrong Schur grouping identity (ch13 inequalities).** A "proof" expanded `(a−b)[b(b−c)−c(a−b)]` as if it were an identity — it isn't. Coordinator applied the reviewer's verbatim replacement.
3. **Broken induction-salvage claim (ch03 induction).** The classic "all horses one colour" autopsy claimed the broken link could still salvage a statement about adjacent pairs — it can't; only P(1) is ever established. Rewritten to prove-impossibility.
4. **Mislabelled AMC problem (ch01 logic).** "AMC 12B 2024 P5" was cited as a parity problem; the real problem is magnitude-bounding. Caught by a reviewer who actually opened the problem.

Plus a **silent-author-defect class**: chapters repeatedly shipped without `\input{chNN}` in main.tex — invisible to the author's own compile claim, caught at the coordinator's merge gate by page-count mismatch. And an off-by-one in cp-ch09's `closing_farm.cpp` (answer computed after re-inserting a vertex instead of before) — caught by the reviewer's 200-case forward-simulation harness.

## What review missed / process gaps so far

- **Tag-case drift (linalg, 4 chapters).** Exercise label casing drifted chapter to chapter; reviewers noted it as a nit each time but it kept shipping — fixed only when a batch nit-pass was run. Lesson: recurring nits need a fix-once rule, not per-chapter flags.
- **Review packets missing prior chapters.** Coordinator's hand-built tarballs included only the current + previous chapter; reviewers had to reconstruct earlier chapters to compile. Fixed: packets are now the full repo tarball.
- **Stale landing rows in review-log.** Verdicts were landing in the wrong table column; now normalized at each book close.
- **Caption overclaims.** Two instances of "verbatim"/"≈ exactly" wording on interpolated or float64-lost-precision rows — now a standard reviewer check.

## What works

- Byte-exact reruns are the cheapest high-yield check: every fabricated-or-stale output dies instantly.
- "Verify-before-resolve": coordinator greps every claimed fix in the landed file — authors have twice claimed fixes that weren't in the file.
- Verbatim-spec fixes for math errors beat round-trip re-reviews: reviewer writes the replacement text, coordinator applies + greps.
- A deferred-nit batch per book keeps per-chapter latency low without losing the fixes.

## cp ch16/17 review cycle (2026-10-11)
- **Caught:** dead cp-algorithms FR link (`nearest-points` → correct slug `nearest_points`) — found by the reviewer's live curl check (404 vs 200), not by reading. Confirms live-checking FR/Watch items catches what eyeballing misses.
- **Process gap:** book2's first cp-review pass worked on a STALE package (md5-identical re-verify) instead of the owed ch16/17 — cost a full cycle. Fix applied: dedicated minimal package containing ONLY the files under review (ch16/17 + their figures + context docs), which removed ambiguity about what "current" meant.
- **Label-only drift:** the reviewer noted earlier-vs-current diffs were label-only (USACO-B/CF abbreviations) and correctly accepted prior full test-runs instead of re-running — good reviewer judgement, keep this pattern.
