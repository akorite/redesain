# Progress log
| Chapter | Status | Pages | Date |
|---|---|---|---|
- 2026-10-10 — decisions.md recorded (user approval of Wave-1 outlines; all 8 decisions binding).
| ch01 How a program becomes a running thing | DRAFTED | ~12pp (main.pdf 15pp) | 2026-10-11 |
- 2026-10-11 — ch01 drafted: 6 figs, 5 examples, 13 graded + 2 inline exercises, 4 real tool captures (objdump -h/-d/-t/-r, ld.lld link+errors, -O0/-O2 .text deltas 0x76/0x96). Toolchain: Apple clang 21 -target x86_64-linux-gnu + lld 23.1.3 (brew); test_ch01.sh PASS. FR: 5 items, all verified live (incl. Drepper dsohowto.pdf via browser-UA).
| ch02 How the machine sees data | DRAFTED | ~11pp (main.pdf 28pp) | 2026-10-11 |
- 2026-10-11 — ch02 drafted: 6 figs, 5 examples, 12 graded + 2 inline exercises, 4 real C probes (endian byte order, struct padding 24v16, IEEE-754 pi decode, alignment benchmark 151v110ms anomaly taught honestly). All 5 FR + 2 Watch verified live.
| ch03 RV32I assembly I | DRAFTED | ~10pp (main.pdf 38pp) | 2026-10-11 |
- 2026-10-11 — ch03 drafted: 6 figs, 5 examples, 12 graded + 3 inline exercises, 4 real RV32I runs via book-written assembler+interpreter (sum=55, arrsum=15, max=42; mem-vs-reg counts 110 v 57). No riscv toolchain on box — ch03_rv32asm.py/ch03_rv32sim.py built and verified against spec encodings instead. CPUlator marked described-not-captured. 2 Watch videos verified.
| ch04 Functions and the stack | DRAFTED | ~10pp (main.pdf TBD) | 2026-10-11 |
- 2026-10-11 — ch04 drafted: 6 figs, 4 examples + 1 measurement example, 12 graded + 2 inline exercises, real artifacts: fib(7)=13 via real stack frames (565 instrs), call overhead 410v207 (2 instr/call), real clang23 riscv64 -O0/-O2 output (32 v 9 instrs, switch->arithmetic). Watch: Austin's BSP Lab + Godbolt CppCon, oembed-verified.
| ch05 Single-cycle RV32I core | DRAFTED | ~7pp (main.pdf 52pp) | 2026-10-11 |
- 2026-10-11 — ch05 drafted: 6 figs, 5 examples+measurement, 13 graded + 2 inline, real iverilog artifacts: 5 modules (alu/regfile/decode/sc_top), 13-word program self-assembled runs with 8 architectural checks, CPI=1 measured, sim speed ~220k instr/s. Watch: DDCA Ch7 Pt1+Pt2 Sarah Harris.
| ch06 Pipelining | DRAFTED | ~6pp (main.pdf 58pp) | 2026-10-11 |
- 2026-10-11 — ch06 drafted: 5 figs, 5 examples, 11 graded + 2 inline, real iverilog: 5-stage pipe top + tb SHOWING the hazard (a1=3 not 8, real wrong value) + independent stream correct; CPI measured both ways.
| ch07 Hazards: forwarding, stalls, branches | DRAFTED | ~7pp (main.pdf 64pp) | 2026-10-11 |
- 2026-10-11 — ch07 drafted: 6 figs, 5 examples + receipts, 10 graded + 2 inline, real iverilog: fwd_top with forwarding/load-use/flush; measured a1=8, a2=41, a3=42, dmem=42, exactly 1 bubble. Two real bugs kept as receipts (X-prop tag init; hand-hex 0x00002613 decoded as addi not lw).

| ch08 | Traps and MMIO | elec session | complete | 2026-10-11 | 6 figs, 12 exercises, soc+uart+trap sims real |
| ch09 | Memory hierarchy | elec session | complete | 2026-10-11 | 6 figs, 11 ex, mem mountain+stride real |
| ch10 | Caches | elec session | complete | 2026-10-11 | 6 figs, 12 ex, sim+real transpose agree |
| ch11 | Virtual memory | elec session | complete | 2026-10-11 | 6 figs, 11 ex, real 7x fault cost |
| ch12 | Processes & scheduling | elec session | complete | 2026-10-11 | 6 figs, 15 ex, real 3us ctx-switch + sched sim |
| ch13 | Concurrency & sync | elec session | complete | 2026-10-11 | 6 figs, 15 ex, real 83pct lost + lockscale |
| ch14 | File systems & persistence | elec session | complete | 2026-10-11 | 6 figs, 14 ex (now 15 after 2026-10-12 pass), real 17GB/s-cache + fsync tax |
| ch15 | Measuring performance | elec session | complete | 2026-10-11 | 6 figs, 15 ex, folklore audit table |
| ch16 | Vectorisation | elec session | complete | 2026-10-11 | 6 figs, 15 ex, real 4x NEON + 1.00x autovec |
| ch17 | Low-latency patterns | elec session | complete | 2026-10-11 | 6 figs, 15 ex, folklore audit real |
| ch18 | Interpreter & compiler | elec session | complete | 2026-10-11 | 6 figs, 15 ex, real 9-op VM + emitter |

- 2026-10-12 — floors pass (4 parallel authors, merged): ch05-18 each >=5 WE (5..11), >=6 figs, >=15 ex, >=3 listings with captured output, test_chNN.sh for ch01-18 all PASS in a Linux x86_64 container. ch01-smoke removed (it shifted printed chapter numbers by one). Cover/title set. 216pp. Warm beginner voice + Before-you-start/After-this-chapter boxes added to ch05-18. Several pre-existing errors fixed (see review-log).
