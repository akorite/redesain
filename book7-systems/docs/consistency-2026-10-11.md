# Full-book consistency + link-rot pass — 2026-10-11 (post-ch19)

## Build state
- `main.pdf` 224 pages; 0 overfull \hbox >3pt; 0 undefined refs/cites; 0 multiply-defined labels (was 16).
- All code test scripts green: test_ch14, test_ch15, test_ch16, test_ch18 (ch17/ch19 are sim-free or shown-not-run by design).

## Link-rot sweep — every \url{} and Watch link across ch01–19 re-curled (58 unique)
- 55/58 live (200/oembed).
- 3 dead-or-blocked, all already or now honest-marked:
  - `fpga4fun.com` — connection failure 000. Cited via `\cite{fpga4fun}` in ch09/11/12/13; bibitem now annotated "(site unreachable at check time; cited on prior verified access)". No content claims depend on it.
  - `allaboutcircuits.com` — 403 to curl (bot-block; browser-reachable, prior verified). bib aacvol1/3/4 + ch17/18 FR keep [unverified] tags; row added to unverified.md.
  - `nandland.com` — 403 (bot-block). ch19 FR kept with [unverified] tag.
- All 15 YouTube Watch-instead links verified via oembed (titles + lengthSeconds captured at chapter time).

## Consistency fixes applied
- 16 multiply-defined labels uniquified: `sec:mistakes` ch01/07–10, `sec:summary`/`sec:exercises` ch07–10, `fig:flow` ch11/13, `fig:wave`/`fig:timing`/`fig:flow` ch13, `fig:charge` ch04, `lst:checktools` ch02 → each suffixed with chapter number. `lst:checktools` semantics preserved: ch02's own listing renamed `lst:checktools02`; both `\ref{lst:checktools}` (ch01:440, ch02:249) still resolve to ch01's original listing.
- No \ref pointed at the renamed sec:*/fig:* duplicates (verified by grep) — renaming was zero-risk.

## Cross-chapter contract checks
- ISA chain consistent: ch14 ALU op-field (000 ADD…111 CMP) == ch16 decoder case statement == asm8.py TWO={'LDI','JMP','JZ'} + MOVA 0xA added ch16. Verified by testbenches playing both roles.
- WB/DST/PC encodings documented identically in ch15 datapath header and ch16.
- Honest-marking pattern uniform: sims real+verbatim, board/P&R/KiCad-GUI described-not-run.

## Still open for reviewer
- `code/ch13_tangnano.cst` pin 18 labelled `tx` — rev-3674 says 18 is FPGA_RX (TX=17). Pre-existing flag from ch13 review.
- ch19's `fig:map` learning-map lists Book 6/7 titles informally — check against the series catalog when Book 7's outline lands.
