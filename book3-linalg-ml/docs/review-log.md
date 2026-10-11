# Review log
| Chapter | Author | Reviewer | Findings | Resolution |
|---|---|---|---|---|
| ch01 | book3 session | book5 session (devin-360c...) | REVISE — 1 blocker: Example 1.1 reuses Strang's signature 3x3 verbatim; re-roll + regen outputs. Nits: dead best_of() vs min(); ~11pp vs 14; [hard] hint convention | RESOLVED 2026-10-10: new system (x+2y+z=7, 3x+8y+z=17, 2y+3z=11 → (2,1,3)), outputs regenerated, recompiled clean |
| ch02 matrices | book3 session | book5 session (devin-360c...) | ACCEPTED 2026-10-10 — PASS 0 blockers (delivered 18:00); ex2.1 clause clarified; timings nit noted (machine-specific by design) | |
| ch03 vector spaces/4 subspaces | book3 session | book5 session | PENDING — 0 overfull>3pt/0 undef 2026-10-10 | |
| ch04 linear maps/change of basis | book3 session | book5 session | ACCEPTED 2026-10-10 — 0 blockers; B^-1AB direction verified; ex:changebasis stumble already signalled in text | |
| ch05 orthogonality/projections/QR | book3 session | book5 session | PENDING — 0 overfull>3pt/0 undef 2026-10-10 | |
| ch05 orthogonality/QR | book3 session | book5 session | PENDING — 0 overfull>3pt/0 undef, 63pp 2026-10-10 | |
| ch06 determinants | book3 session | book5 session | PENDING — 0 overfull>3pt/0 undef, 72pp 2026-10-10 | |
| ch07 eigenvalues | book3 session | book5 session | PENDING — 0 overfull>3pt/0 undef, 85pp 2026-10-10 | |
| ch08 least squares | book3 session | book5 session | RESOLVED 2026-10-10 — cond² caption fixed: 3.267e15 is float64-computed, 14% off exact 2.86e15, caption now says so honestly (was "exactly")| |
| ch09 spectral theorem | book3 session | ACCEPTED 2026-10-10 — PASS (all 3 scripts byte-exact; both proofs sound; nit: tag-case drift noted)| PENDING — 0 overfull>3pt/0 undef, 109pp 2026-10-10 | |
| ch10 SVD + PCA (capstone 2) | book3 session | ACCEPTED 2026-10-10 — PASS (4 scripts byte-exact; SVD hand-verified)| PENDING — 0 overfull>3pt/0 undef, 120pp 2026-10-10 | |
| ch11 gradients/Jacobians/Hessians | book3 session | ACCEPTED 2026-10-10 — PASS (FD U-shape byte-exact; proofs sound)| PENDING — 0 overfull>3pt/0 undef, 131pp 2026-10-10 | |
| ch12 probability/RVs | book3 session | ACCEPTED 2026-10-10 — PASS (all 4 scripts byte-exact; tag-case drift fixed)| PENDING — 0/0, 142pp 2026-10-10 | |
| ch13 statistics/Bayes | book3 session | book5 session | ACCEPTED 2026-10-10 — PASS (all 4 .py byte-exact; Beta post-mean 0.500→0.646 verified) | |
