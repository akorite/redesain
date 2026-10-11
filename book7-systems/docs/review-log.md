# Review log
| Chapter | Author | Reviewer | Findings | Resolution |
|---|---|---|---|---|
| ch01 How a program becomes a running thing | elec-0006 | coordinator | REVISE 2026-10-11 — test_ch01.sh was a max-subarray C++ script (wrong book); replaced with real clang/ELF wrapper, PASS — RESOLVED, ACCEPTED |
| ch02 How the machine sees data | elec-0006 | coordinator | ACCEPTED 2026-10-11 — test_ch02.sh PASS (bytes/pad/align/float timings real) |
| ch03 RV32I assembly I | elec-0006 | coordinator | REVISE 2026-10-11 — fig_formats delivered to figures/ch02/ while ch03 \input's it from figures/ch03/; rerouted — RESOLVED, ACCEPTED (test_ch03.sh PASS: 4 programs assembled+run) |
# Review log — textbook-systems ch01–04 (45pp, elec-0006)

Independent reviewer: Devin (book-8 author session). Method: fresh make (45pp),
contract counts vs the book's own outline floors (§line 519: figs ≥4, listings ≥3,
WEs ≥3, additional exercises ≥10 — NOT the 5/6/15 contract other books use), all four
`code/test_chNN.sh` suites executed on this box (Apple clang cross-target
x86_64-linux-gnu + lld — real C17/RISC-V compile+run), all 21 FR/Watch URLs fetched
live, all 8 videos verified via oEmbed + lengthSeconds against watch.md claims,
chapter-printed outputs diffed against captured `.out` files, technical claims
spot-derived (fib(7) call count, .text sizes, alignment delta).

| chapter | verdict | blockers | nits | date |
|---|---|---|---|---|
| ch01 program→running | PASS | — | — | 2026-10-11 |
| ch02 machine sees data | PASS | — | — | 2026-10-11 |
| ch03 RISC-V assembly | PASS | — | sits at the ≥3 WE floor (3 WEs) — flagging, no action required | 2026-10-11 |
| ch04 calls/stack frames | REVISE | **9 exercises < 10** (outline floor). Real gap, needs one more graded exercise | (a) `docs/watch.md` has ZERO ch04 rows — the two Watch picks exist in the chapter and verify (6:35, 75:45) but were never logged; (b) Common mistakes uses plain `itemize` vs `tripwire` envs in ch01–03 (content fine, style inconsistent) | 2026-10-11 |

## Verbatim fixes for ch04

**(a) Exercise shortfall** — insert one graded exercise in `\section*{Exercises}`
(between the medium and hard tiers, ~line 380):

```latex
\begin{exercise}[medium]\label{ex:m04e}
A non-leaf function needs its return address, one callee-saved
register \texttt{s0}, and two 8-byte locals across its calls. How large
must its stack frame be under the RISC-V psABI, and why?
\end{exercise}
\begin{solution}
$8+8+16=32$ bytes: \texttt{ra} and \texttt{s0} are 8 bytes each, the
locals are 16, and 32 keeps \texttt{sp} 16-byte aligned at call sites
(sec:contract04). A 24-byte frame would misalign the ABI boundary.
\end{solution}
```

**(b) Missing watch.md rows** — append:

```markdown
| ch04 | RISC-V General-Purpose Registers: Usage and Calling Convention | Austin's BSP Lab | 6:35 | sec:contract04–sec:ownership04 | 2026-10-11 |
| ch04 | What Has My Compiler Done for Me Lately? | CppCon (Matt Godbolt) | 75:45 | sec:readasm04 | 2026-10-11 |
```

**(c) Style nit (optional)** — wrap ch04's six Common-mistakes items in
`tripwire` envs to match ch01–03, or leave as-is; content is complete either way.

## Checks that passed (record)

- Whole-book make: 45pp, 0 `!` errors, 0 undefined refs, **0 overfull >3pt**.
- All 4 test suites green on this box: ch01 (x86-64 asm emit + ELF object + expected
  link failure via lld), ch02 (endian/padding/float/alignment probes — real timings
  printed), ch03 (4 RV32 programs real-assembled, real-executed: 55/15/42 outputs,
  110-vs-57 instruction counts), ch04 (fib(7)=13 real frames, call tax 2 instrs).
- Printed outputs are genuine: `.text` sizes 0x76 (O0) / 0x96 (O2) in ch01 match
  `code/ch01_sizes.out`; the alignment anomaly (ch02) reproduces on this box —
  misaligned ~25% faster, and the chapter teaches the anomaly honestly with the
  machine spec recorded ("Apple M-series, 32 passes").
- fib(7) call-tree claim verified analytically: 41 total calls, exactly as printed.
- Links: all 21 URLs return 200 (incl. Drepper dsohowto.pdf, riscvbook, diveintosystems,
  cpulator, gcc docs, Compiler Explorer).
- Watch: all 8 videos resolve via oEmbed with exact title/channel; all 8 duration
  spot-checks match the printed claims to the second (1142s=19:02, 3551s=59:11,
  646s=10:46, 556s=9:16, 168s=2:48, 702s=11:42, 395s=6:35, 4545s=75:45).
- unverified.md has zero rows and nothing was left unverified — consistent.
- Venue/claim date-stamping present where needed (toolchain versions, access dates).
