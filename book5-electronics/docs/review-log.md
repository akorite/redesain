# Review log
| Chapter | Author | Reviewer | Findings | Resolution |
|---|---|---|---|---|
| ch01 electricity | book5 session | book3 session (devin-33ac...) | PENDING — landed pre-review; 0 overfull>3pt/0 undef coordinator recheck 2026-10-10 | |
| ch02 Ohm/simulator | book5 session | book3 session | RESOLVED — Exercise 2.5 flipped inequality (R≥V²/P not ≤); stale test-file re-flag; dup-qty + .dat nits fixed by coordinator — 0 overfull>3pt/0 undef 2026-10-10 | |
| ch03 KCL/KVL/Thévenin | book5 session | book3 session | RESOLVED 2026-10-10 — mesh hint now 8.34/5.61V (ngspice-verified by book3 + coord), load-line labelled "every 4th row of 21"| |
| ch04 RC/RL transients | book5 session | book3 session | RESOLVED 2026-10-10 — lst:rcdata now prints actual .dat rows (0.999ms→3.158V, 1.099ms→3.334V) w/ adaptive-steps caption; grep-verified| |
| ch05 diodes | book5 session | book3 session | ACCEPTED 2026-10-10 (book3) — all sim numbers byte-exact or recompute-verified vs ngspice-47, verbatim discipline held| |
| ch06 transistors | book5 session | ACCEPTED 2026-10-10 — PASS (all 4 dats byte-identical; NM margins recomputed; nits: ch:transients resolves at assembly, decks accumulate in code/)| PENDING — 0 overfull>3pt/0 undef, 75pp 2026-10-10 | |
| ch07 op-amps + power | book5 session | book3 session | ACCEPTED 2026-10-10 — PASS (all 3 decks byte-identical ngspice-47; every claim recomputes; tanh macro sound) | |
| ch08 numbers/bits/Boolean | book5 session | book3 session | ACCEPTED 2026-10-10 — PASS (signed-byte WE 3 ways; alarm K-map EQUIVALENT; iverilog verbatim; read-only contract honored) | |
| ch09 combinational | book5 session | book3 session | PENDING — 0/0, 105pp 2026-10-10 | |
