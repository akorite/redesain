# Sources

Research log for Book 7 (*Computer architecture and systems*, `textbook-systems`).
All URLs verified open on 2026-10-10. Table follows the master prompt §3B format.
Nothing was copied; entries record ideas, topic order and exercise types only.

| URL / ISBN | Accessed (2026-10-10) | Licence | What was taken (idea / topic order / exercise type; never text) |
|---|---|---|---|
| **Anchors** | | | |
| https://pages.cs.wisc.edu/~remzi/OSTEP/ (OSTEP v1.10) | 2026-10-10 | Free chapter PDFs on site; print/PDF sold | Three-part framing virtualization/concurrency/persistence; chapter order process→scheduling→address space→paging→TLB→swapping; thread API→locks→CVs→semaphores→bugs; I/O→disk→files→FS impl→journaling→SSD. Homework-via-simulator idea adopted as our per-chapter measurement. Dialogue chapters rejected (wrong register for us). |
| https://craftinginterpreters.com/contents.html | 2026-10-10 | Free to read online; print/ebook sold | Two-pass structure (tree-walk interpreter, then bytecode VM in C) — pattern for our ch18 (interpreter then compiler). "Design Note" side boxes ≈ our `remark`/`principle` environments. Teach-by-running-code register. |
| https://www.csapp.cs.cmu.edu/ + http://csapp.cs.cmu.edu/3e/labs.html | 2026-10-10 | Free student site & lab handouts (self-study allowed); book © Pearson | Programmer's-perspective spine: data repr → machine code → processor (SEQ→PIPE) → optimization → memory hierarchy → linking → exceptions → VM → I/O/concurrency. Lab list as exercise-type inspiration: Bomb Lab (reverse-engineering via objdump), Cache Lab (write a cache *simulator* then optimize transpose against it — we adopt this exercise shape, own code), Arch Lab (tune a pipelined core's CPE). |
| ISBN 9780128203316 — Patterson & Hennessy, *Computer Organization and Design, RISC-V Edition*, 2e (Elsevier page + chapter list) | 2026-10-10 | Commercial | Confirmed the canonical order: instructions (ch2) → processor single-cycle→pipelined (ch4) → memory hierarchy (ch5) → parallel (ch6). Confirms our Part II/III sequencing and the IF/ID/EX/MEM/WB stage names used in notation.md. |
| ISBN 9780128119051 — Hennessy & Patterson, *Computer Architecture: A Quantitative Approach*, 6e (Elsevier page + TOC) | 2026-10-10 | Commercial | Quantitative stance adopted as book policy: every claim paired with a measured number (Amdahl, CPI, AMAT). Appendix "Pipelining: Basic and Intermediate Concepts" confirms hazard-taxonomy order (structural/data/control). |
| ISBN 9780128200643 — Harris & Harris, *Digital Design and Computer Architecture, RISC-V Edition* (Elsevier page + https://pages.hmc.edu/harris/ddca/ddcarv.html companion site) | 2026-10-10 | Commercial; companion appendices free | Confirmed DDCA's single-chapter progression single-cycle→multicycle→pipelined and its build-the-processor-in-HDL method; overlaps Book 5 — we cite it rather than re-teach. Companion site model (free appendices) noted for our appendix A (RV32I green card). |
| https://riscv.org/specifications/ → docs.riscv.org + https://github.com/riscv/riscv-isa-manual/releases | 2026-10-10 | Open ISA manual (CC-family; verify exact licence line at citation time) | Authoritative instruction encodings for appendix A and the capstone. Manual releases are rolling snapshots — latest seen `riscv-isa-release-d8a0c13-2026-10-08`; book pins the release date it cites. |
| **Further comparable resources (§3B, ≥5 required — 16 logged)** | | | |
| https://diveintosystems.org/book/ + single-page TOC | 2026-10-10 | Free online textbook (v1.2), print via No Starch | Vertical-slice ordering for a CS1-level reader; gdb/valgrind debugging as first-class chapters (we adopt "tools as a section in every chapter" instead of a standalone debugging chapter); their x86-64/ARM/IA32 split confirms our single-ISA (RV32I) simplification is the right choice. |
| https://www.nand2tetris.org/ | 2026-10-10 | Materials free for non-profit use; book © MIT Press | Overlap check for Book 5: their Hack CPU + assembler + VM + compiler stack is a smaller version of our ch1→ch18 arc. Deliberate difference: real ISA (RV32I) instead of Hack; their project style (end-to-end build) informs capstone staging. No conflict — cite as further reading. |
| https://computationstructures.org/ (MIT 6.004 notes) | 2026-10-10 | Free MIT course notes (evolving) | Hierarchical design method (gates→combinational→sequential→FSM→processor→system); browser-based lab exercises as a model for "measure in simulation" exercises; students gate-level-design a RISC processor in labs — validates our build-it-yourself capstone. |
| https://pdos.csail.mit.edu/6.1810/2024/xv6/book-riscv-rev4.pdf (xv6 book rev4) | 2026-10-10 | Free draft PDF; xv6 code MIT-licensed | OS-part chapter order: interfaces → organization → page tables → traps → interrupts/drivers → locking → scheduling → file system → concurrency revisited. "Code:" commentary style adopted: our OS chapters include short guided reads of real xv6 source. Confirms RISC-V (sv32, trap machinery) as the teaching vehicle. |
| https://www.agner.org/optimize/ | 2026-10-10 | Free PDFs, © Agner Fog | Measurement-driven microarchitecture facts; instruction tables (optimizing_cpp.pdf modified 2026-09-10, microarchitecture.pdf 2026-05-23 — date-stamped). Exercise type adopted: predict-then-measure instruction latency/throughput loops (his PMCTest approach) — x86-flavoured, we write our own host-agnostic versions. |
| https://www.brendangregg.com/ | 2026-10-10 | Free site; books © Addison-Wesley | Benchmarking methodology: "Evaluating the Evaluation" checklist (2018), USE method, flame graphs — basis for ch15's "measure correctly" checklist. Confirms warm-up/frequency/noise pitfalls list. |
| https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/ | 2026-10-10 | MIT OCW, CC BY-NC-SA | Performance-engineering topic order (analysis → algorithmic → instruction-level → caching → parallel) mirrors our Part V; bit-trick and C-level optimization exercise styles; course language is C — matches reader. |
| https://perfwiki.github.io/main/ | 2026-10-10 | Public wiki | `perf` subcommand map (stat/record/report/annotate/top/bench), hardware counters (cache-misses, branch-misses), top-down analysis — tooling section of ch15. **perf is Linux-only**: drives our "portable fallback for every measurement" rule. |
| https://github.com/compiler-explorer/compiler-explorer + godbolt.org | 2026-10-10 | BSD-2-Clause (repo); free service | 30+ languages incl. C/C++/Rust/Go and RISC-V gcc/clang targets; used in ch3–4 (read compiler output without installing a cross toolchain) and ch16 (diff -O2 vs -O3 codegen). |
| https://cpulator.01xz.net/ | 2026-10-10 | Free browser tool | Zero-install RV32 simulator + debugger (single-step, breakpoints, watchpoints, register/memory view); RV32 support added 2024-03; ~20 Minstr/s. Adopted as the *default* runner for ch3–4 assembly exercises (no install friction); Spike is the local alternative. |
| https://github.com/riscv-software-src/riscv-isa-sim (Spike) | 2026-10-10 | Open source (repo licence field "Other") | Golden ISA sim: RV32I/RV64I v2.1 + M/A/C/F/D/V(1.0) etc. Active (last push 2026-05-16; latest tag v1.1.0 2021 — use master). Adopted as: local RV32I runner + RVV host for ch16 vectorisation measurements. |
| https://github.com/riscv-collab/riscv-gnu-toolchain + https://xpack-dev-tools.github.io/riscv-none-elf-gcc-xpack/ | 2026-10-10 | GNU toolchain (GPL-family); xPack binaries free | Source build ≈6.65 GB clone — too heavy for a student. Chosen path: **xPack `riscv-none-elf-gcc` 15.2.0-1.1** prebuilt (Windows/macOS/Linux, xpm or archive). Alternative distro packages named in appendix B as unverified-variant. |
| https://verilator.org/guide/latest/ | 2026-10-10 | LGPL-3.0 / Artistic-2.0 | Verilator 5.052 docs current; used for capstone lint, `--binary` fast sims and coverage. Bundled inside OSS CAD Suite — no separate install. |
| https://github.com/YosysHQ/oss-cad-suite-build/releases | 2026-10-10 | Mixed open-source licences | Daily builds (latest seen 2026-10-10): Icarus, Verilator, Yosys, nextpnr, GTKWave — same toolchain Book 5 pinned; capstone reuses it unchanged (decision, approved). |
| https://akkadia.org/drepper/cpumemory.pdf (Drepper, *What Every Programmer Should Know About Memory*, 2007) | 2026-10-10 | Free PDF, © Red Hat | Memory-hierarchy deep dive: cache geometry, associativity, prefetch — source of ch9–10 figure ideas (memory pyramid, cache-line anatomy) and the "memory mountain" measurement. Dated (2007, pre-NVMe) — cite for concepts, not current numbers; we re-measure everything on the reader's machine. |
| https://pdos.csail.mit.edu/6.1810/ (MIT 6.1810 course page, Fall 2025/2026) | 2026-10-10 | Free course site | Confirms xv6 is live teaching material in 2025–26 (not a dead project); lab pointers for OS exercises. |

## Findings that shape the outline

### RISC-V subset taught
- **Core: RV32I** (base integer ISA v2.1 — frozen/ratified). Rationale: matches Book 5's
  ch16 mapping table (addi/lui/R-type/jal/beq/store/ebreak), is CPUlator's teaching ISA,
  fits the Tang Nano 9K's ~8640-LUT fabric for the capstone soft core, and is the subset
  PicoRV32-style cores implement.
- **M extension** (mul/div) covered in one section — toolchain emits it by default;
  capstone lists it as an optional exercise.
- **Zicsr** introduced in ch8 only as far as traps need (mtvec, mepc, mcause).
- **A** (lr.w/sc.w, AMOs) referenced in ch13 for hardware atomics — read, not built.
- **F/D/V**: named and skipped (no FPU in capstone; V covered on the *host* side in ch16
  via Spike's RVV 1.0 support + host SIMD).
- **C** (compressed): one remark only — decoder complexity not worth the pages.
- Deliberately **RV32I not RV64I**: matches Book 5, halves datapath width, and every
  real-world RV teaching stack (xv6 targets rv64 but its code is width-agnostic) works.

### Open tools verified today (all date-stamped 2026-10-10)
- **Assembly/simulation:** CPUlator (browser, free, RV32IMAFD+); Spike (riscv-isa-sim
  master); xPack riscv-none-elf-gcc 15.2.0-1.1 (prebuilt, 3 OSes); Compiler Explorer
  (browser; RISC-V gcc/clang). Building riscv-gnu-toolchain from source = 6.65 GB clone —
  documented as the "if all else fails" path only.
- **Verilog/FPGA:** OSS CAD Suite (daily builds, latest 2026-10-10): Icarus, Verilator
  5.052, Yosys, nextpnr, GTKWave — inherited unchanged from Book 5's toolchain decision.
- **Profiling on the reader's laptop:** `perf` is **Linux-only** (perfwiki). macOS
  alternatives named but flagged: Instruments/xctrace, `sample`. Therefore every
  measurement is designed **portable-first** (self-timing C programs via
  `clock_gettime`, plus a tiny software counter/simulator where hardware counters are
  unavailable); perf appears as the "if you are on Linux" deeper cut.
- **Host ISA caveat stated in book:** measurements in ch7–17 run on the *reader's own
  machine* (x86-64 or ARM64) — the book says so honestly and explains why the effects
  (cache, branch prediction, TLB) are ISA-independent.

### How the sources sequence assembly → datapath → pipeline (consensus)
COD RISC-V (ch2→ch4→ch5), CS:APP (ch3→ch4→ch5–6), DDCA (arch chapters), Dive into
Systems (ch5→6–9→11), MIT 6.004 all converge on:
**ISA/asm first → single-cycle datapath → pipelined datapath → hazards
(data: forwarding/stall; control: branch prediction) → memory hierarchy (cache→VM).**
This book keeps that spine, differs in that the reader *builds* each stage in Verilog
(spinning off from Book 5's custom CPU) and *measures* each effect on real hardware —
the two things no single anchor does at once.

### Overlap deliberately left to Book 5 (checked against approved Book 5 map)
Verilog language & testbenches (Book 5 ch11–12), Boolean algebra/K-maps (ch9),
FSMs (ch10), ALU internals (ch14), basic datapath/bus concepts (ch15), and the *idea* of
a single-cycle CPU (ch16). Book 7 opens from Book 5's RV32I mapping table, builds a
real RV32I single-cycle core as a one-chapter bridge (ch5), then goes where Book 5's
"honest list" pointed: pipelining, hazards, caches, VM, OS.
