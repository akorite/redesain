# Independent re-review — textbook-linalg-ml depth retrofit (ch01–13)
Reviewer: elec session devin-0006303d6e9349e78f9eb75df6ca0190 · 2026-10-11
Scope (as briefed): verify ONLY new depth content — FR URLs live (curl),
Watch videos verified (oembed + lengthSeconds/page checks), new exercises/WEs
mathematically sound, no invented refs. Base text NOT re-reviewed.
ch14–16 excluded per brief.

## Method
- Extracted every `\url{}` + watch-link from ch01–13 + docs/watch.md:
  63 unique URLs (35 HTTP links + 28 youtu.be video links).
- Curl sweep with two UAs (plain curl + full browser string) to kill
  bot-block false positives.
- Sampled the final [hard] exercise in all 13 chapters and verified the
  math by hand.
- Re-grepped contract counts: every ch01–13 has ≥5 WEs, ≥6 figures,
  ≥17 additional exercises, a Watch rulebox (2 items each, youtu.be
  links), and FR lists — all PASS.

## Link results
- 62/63 live on verification. All 28 youtu.be watch links return oembed
  200 (verified individually). All FR links live.
- **1 dead link:** `https://linear.ups.edu/` (Beezer, *A First Course in
  Linear Algebra*, ch03:434–437) — connection failure 000 on both UA
  attempts. The FR item is tagged "Verified 2026-10-11", which the dead
  host contradicts.
  - Evidence the resource itself is real: Wayback Machine
    `https://web.archive.org/web/2026/https://linear.ups.edu/` → 200.
  - `docs/unverified.md` has NO row for it; no alternative Beezer link
    is offered in-chapter.

## Findings

### REVISE — 1 item
**ch03 Further reading, Beezer item.** The URL is dead (000) while the
item claims "Verified 2026-10-11". Verbatim fix — replace lines 434–438:

```
\item A.~Beezer, \emph{A First Course in Linear Algebra}, sections
SS, B, D, RNM (free online) --- proof-heavy companion for anyone who
wants every claim justified. \newline
\url{https://web.archive.org/web/2026/https://linear.ups.edu/}
(original linear.ups.edu unreachable at check time).
Verified via archive 2026-10-11.
```

and add to `docs/unverified.md`:
`| linear.ups.edu (Beezer FCLA) | ch03 Further reading | connection failure 000 on 2026-10-11; Wayback mirror substituted |`

## Math spot-checks — all 13 PASS
| ch | checked | verdict |
|---|---|---|
| 01 | Ax=0 never inconsistent; smallest-integer convention | correct |
| 02 | (A²)_ii=deg(i), tr(A²)=2E; tr(A³) counts 6·triangles | correct |
| 03 | rank–nullity edge cases | sound |
| 04 | P²=P, P^T=P ⟺ orthogonal projection | correct |
| 05 | orthogonal nonzero ⟹ independent; converse fails | correct |
| 06 | det(A⁻¹)=1/det A, product + volume proofs | correct |
| 07 | λ=1 steady state; swap matrix periodic counterexample | correct |
| 08 | ŷ=projection, A^T r=0 (normal equations) | correct |
| 09 | Rayleigh max principle max x^TAx=λ₁ | correct |
| 10 | Eckart–Young rank-1 case | correct |
| 11 | ∇f ⊥ level sets (chain-rule argument) | correct |
| 12 | CLT continuity-correction estimate | sound |
| 13 | E[σ̂²]=(n−1)/n σ² Bessel bias | correct |

## review-log rows to append
| ch01 Systems and Gaussian elimination | book3/book1 | elec session | PASS 2026-10-11 — links live, math sampled clean | |
| ch02 Matrix algebra | book3/book1 | elec session | PASS 2026-10-11 — links live, (A²)ii/tr(A³) verified | |
| ch03 Vector spaces and rank–nullity | book3/book1 | elec session | REVISE 2026-10-11 — linear.ups.edu dead (000); Wayback fix verbatim in findings | |
| ch04 Projections and orthogonality | book3/book1 | elec session | PASS 2026-10-11 — links live, projection iff verified | |
| ch05 Orthogonalisation and inner products | book3/book1 | elec session | PASS 2026-10-11 — links live, Gram–Schmidt exercise verified | |
| ch06 Determinants | book3/book1 | elec session | PASS 2026-10-11 — links live, det(A⁻¹) verified | |
| ch07 Eigenvalues and eigenvectors | book3/book1 | elec session | PASS 2026-10-11 — links live, Markov-chain example verified | |
| ch08 Least squares and regression | book3/book1 | elec session | PASS 2026-10-11 — links live, normal-equations exercise verified | |
| ch09 Symmetric matrices and quadratic forms | book3/book1 | elec session | PASS 2026-10-11 — links live, Rayleigh principle verified | |
| ch10 The SVD | book3/book1 | elec session | PASS 2026-10-11 — links live, Eckart–Young rank-1 verified | |
| ch11 Gradients and optimisation | book3/book1 | elec session | PASS 2026-10-11 — links live, ∇⊥level-sets verified | |
| ch12 Probability for ML | book3/book1 | elec session | PASS 2026-10-11 — links live, CLT exercise sound | |
| ch13 Estimation and inference | book3/book1 | elec session | PASS 2026-10-11 — links live, Bessel bias verified | |

## Notes for the author (not REVISE)
- ch01–12 Watch items use youtu.be short links; all verified but format
  differs from other books' watch?v= — cosmetic.
- docs/watch.md ch16 rows carry "unconfirmed" length fields (oEmbed-
  verified) — ch14–16 out of scope here, flagged for whoever reviews them.
