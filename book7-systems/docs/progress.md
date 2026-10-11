# Progress log
| Chapter | Status | Pages | Date |
|---|---|---|---|
- 2026-10-10 — decisions.md recorded (user approval of Wave-1 outlines; all 8 decisions binding).
| ch01 How a program becomes a running thing | DRAFTED | ~12pp (main.pdf 15pp) | 2026-10-11 |
- 2026-10-11 — ch01 drafted: 6 figs, 5 examples, 13 graded + 2 inline exercises, 4 real tool captures (objdump -h/-d/-t/-r, ld.lld link+errors, -O0/-O2 .text deltas 0x76/0x96). Toolchain: Apple clang 21 -target x86_64-linux-gnu + lld 23.1.3 (brew); test_ch01.sh PASS. FR: 5 items, all verified live (incl. Drepper dsohowto.pdf via browser-UA).
| ch02 How the machine sees data | DRAFTED | ~11pp (main.pdf 28pp) | 2026-10-11 |
- 2026-10-11 — ch02 drafted: 6 figs, 5 examples, 12 graded + 2 inline exercises, 4 real C probes (endian byte order, struct padding 24v16, IEEE-754 pi decode, alignment benchmark 151v110ms anomaly taught honestly). All 5 FR + 2 Watch verified live.
