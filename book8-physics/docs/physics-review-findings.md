# textbook-physics ch01-19 — independent review findings (2026-10-11)
Reviewer: book2/book6 session. Package: textbook-physics-pkg.tar.gz (shipped 157pp; fresh rebuild 149pp — delivered-state drift, see nits).

## Verified live
- ALL 19 code scripts ran clean (exit 0) on the review box; every output is real and physically correct. Spot-checks: projectile 40.816m (v0=20,45deg) + drag 25.86m; vt=51.12m/s; elastic equal-mass velocity swap + inelastic K-loss (1-e^2)/2=37.5%; symplectic bounded vs Euler x223084 blowup; I_rect=0.8333=exact; rolling race beta order (point>sphere>disk>hoop); resonance peak sqrt(w0^2-g^2/2) exact; orbit Verlet E/L drift 0.000% + Kepler III const 4pi^2=39.4784; dipole far-field 2p/r^3 axis, p/r^3 equator; Gauss flux 12.5664->4pi; -dV/dx=Ex match; RC 63.2%@tau + 50/50 energy split; Boris |v|=1.0000 vs Euler 19.8x drift; RLC wd 446.8 theory=measured; EM pulse v=1.0000 cells/s at CFL 0.70; standing-wave node/antinode + beat period 0.25=1/|f1-f2|; 2D MB mean 0.8876 vs theory 0.8862; motor w_ss=578.3 analytic=numeric, stall V/R=8.00A; workshop: meter-stick T=1.526s, Hohmann dv=1432m/s, Earth tunnel 5066s=84.4min, charge recoil 3.00m/s each — all recomputed correct.
- Links: 13/13 site URLs 200; 38/38 YouTube oembed resolve; durations verified EXACT to the second on sample (49:15=2955s, 10:25=625s, 9:03=543s, 37:36=2256s).
- Fresh compile: 0 `^!` errors, 0 undefined refs, 0 overfull >3pt.
- Notation: physics uses no \mathbb{E} or \Pr — zero collisions with notation-shared.
- Physics text spot-checks: Atwood a=2.45m/s^2; banked+friction sqrt(rg(sin+mu*cos)/(cos-mu*sin)); (3/2)kBT; constants correct.

## Verdicts (contract: >=5 WE, >=6 figs [visual], >=15 ex, CM, FR 5-10, Watch 1-3 verified)
| ch | verdict | reason |
|---|---|---|
| 01-05 | PASS | 5-6 WE, 6 figs, 16-18 ex, FR 6-7, Watch 2 |
| 06 | REVISE | 5 figs < 6 |
| 07 | REVISE | 5 figs < 6 |
| 08,09 | PASS | counts met |
| 10 | REVISE | 5 figs < 6 |
| 11-14 | PASS | counts met |
| 15 | REVISE | 5 figs < 6 |
| 16-18 | PASS | counts met |
| 19 | PASS | workshop contract per outline (20 problems+full solutions; no exercises by design) |

## Verbatim-specified REVISE fixes (one figure each; data already produced by committed scripts)
- ch06 (rolling): add pgfplots bar/line figure "finish speed vs beta" from ch06_rolling_race.py outputs (6.261/5.292/5.112/4.427 m/s at beta 0/0.4/0.5/1.0).
- ch07 (resonance): add A(wd) response curve figure from ch07_resonance_sweep.py measured+theory columns (peak at 1.980).
- ch10 (Gauss): add flux-vs-mesh-n convergence figure from ch10_flux_check.py (n=10..270 -> 12.597..12.566).
- ch15 (EM waves): add pulse-propagation positions figure from ch15_em_pulse.py (peaks 0.7->210 cells, v=1.0) or standing-wave snapshots.

## Delivered-state nits (not content defects)
- Shipped main.pdf is 157pp; fresh rebuild from pkg yields 149pp (index/toc state drift).
- docs/notation.md is the verbatim cp shared file — consistent with the set, physics adds no local notation doc; acceptable but note it documents cp concepts (dp, adj, MOD) the physics book never uses.
