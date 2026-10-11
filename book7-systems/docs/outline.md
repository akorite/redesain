# Outline — Book 7: *Computer Architecture and Systems* (`textbook-systems`)

(to be approved by the user before any chapter is written)

**Reader:** C or C++; Book 5 in progress (Verilog, testbenches, ALU, custom-ISA
single-cycle CPU, RV32I mapping table).
**Premise:** the reader already built a small CPU once. This book builds the *real*
machine around it — a pipelined RV32I core, then the memory hierarchy, the OS that
mediates it, and the measurement discipline that separates performance fact from
folklore. Capstone: a pipelined RV32I core in Verilog, documented, benchmarked and
explained (progressive build across ch5–ch8).
**Conventions kept from Book 5:** every chapter ends with a *Common mistakes* section;
every circuit/Verilog module has a self-checking testbench; measurement chapters are
portable-first with a Linux `perf` deeper cut.

---

## Page budget

| Block | Pages |
|---|---|
| Front matter (preface, how to use, toolchain setup pointer) | ~10 |
| Part I From source to machine code (ch1–4) | 46 |
| Part II The processor — the capstone build (ch5–8) | 52 |
| Part III Memory (ch9–11) | 38 |
| Part IV The operating system (ch12–14) | 38 |
| Part V Performance craft (ch15–17) | 32 |
| Part VI Language runtimes (ch18) | 12 |
| Back matter (appendices A–C, hints, solutions ≥half, bibliography, index) | ~16 |
| **Total** | **~244** |

Compression order if the draft runs long (per approved process): merge ch3+ch4 into
one 18pp assembly chapter; fold ch8 into ch7+ch12 (traps with hazards, drivers with
files); trim ch16 to a section of ch15. Never cut figures, code outputs, worked
examples, or Common-mistakes sections.

Seed-topic deviations: (a) *pipelining and hazards* split into two chapters (6, 7)
plus a traps/IO chapter (8) — the hazard chapter needs its own timing diagrams and the
capstone needs forwarding before it is usable; (b) *performance measurement* is
teased into an early thread (every chapter already has its own measurement) plus the
methodology chapter 15; (c) interpreter-and-compiler moved to the very end (ch18) so
the reader compiles to RV32I, closing the book's arc; (d) networking omitted — not in
the seed, over budget; NFS/distributed pointers live in ch14 Notes.

---

## Part I — From source to machine code

### Ch1. How a program becomes a running thing — *12 pp*

- **Sections:** the four-stage journey (preprocess → compile → assemble → link →
  load); object files and ELF sections; symbols and relocation; the loader and
  `execve`; where Book 5's CPU meets real silicon — the RV32I mapping table from
  Book 5 ch16 revisited; a map of the book.
- **Prerequisites:** Book 5 ch8 (numbers/bits), ch16 (simple CPU + RV32I mapping).
- **Worked examples:** (1) compile `sum.c` to an ELF on the reader's machine and walk
  each tool's output; (2) find `main`'s machine code with `objdump -d`; (3) trace a
  static vs dynamic symbol through `nm`/`readelf -s`.
- **Figures:** compilation pipeline diagram; ELF section map of a real binary;
  address-space overview (text/data/heap/stack/mmap); book-part roadmap.
- **Code listings:** `hello.c` → `gcc -S` output excerpt; `objdump -d` excerpt of
  `main`; `readelf -h/-S` output; a two-file link demo with an unresolved symbol.
- **Measurement:** *binary anatomy* — measure text/data/bss sizes of the same program
  at `-O0` vs `-O2` (`size`, `nm --print-size`), table the deltas.
- **Exercises:** inline checkpoints ×2 (predict which section a `const` lands in).
  Additional ×11 [4 easy / 4 medium / 3 hard]; signature [hard]: hand-link two object
  files and explain each relocation error that appears.
- **Sources:** CS:APP ch7 (linking), Drepper §1, Compiler Explorer docs.

### Ch2. How the machine sees data — *12 pp*

- **Sections:** bytes, words and addresses; two's complement recap (one page — Book 5
  ch8 assumed); endianness and why RV32 is little-endian; alignment and struct
  layout/padding; IEEE-754 in one breath (formats, rounding, the `.5 ulp` idea);
  pointers as typed addresses; arrays vs pointers in generated code.
- **Prerequisites:** ch1; Book 5 ch8.
- **Worked examples:** (1) decode a float's bit pattern by hand then verify in C;
  (2) compute the real size of a 3-field struct vs the naive sum; (3) read the same
  4 bytes as `uint32`, `int32`, `float` — three different worlds.
- **Figures:** little vs big endian byte layout of `0x0A0B0C0D`; IEEE-754 bit-field
  anatomy; struct padding map for two layouts; C type-size table (LP64 vs ILP32).
- **Code listings:** byte-dump program (`union`/pointer casts); `offsetof`/`sizeof`
  padding probe; IEEE-754 hex-to-value decoder.
- **Measurement:** *alignment tax* — sum an array via aligned vs deliberately
  misaligned pointers, time both (predict-then-run: many machines hide it — that is
  a finding too).
- **Exercises:** inline ×2. Additional ×10 [4/4/2]; signature [hard]: write a
  standards-strict float-bits printer without type-punning UB.
- **Sources:** CS:APP ch2; Dive into Systems ch4; CAQA §1 data paths.

### Ch3. RV32I assembly I — arithmetic, memory, control — *12 pp*

- **Sections:** the register file (ABI names `a0–a7`, `s0–s11`, `t0–t6`, `sp`,
  `ra`, `zero` — x-names in a table); R/I/S/B/U/J formats and why the encodings are
  shaped so; loads/stores and addressing modes; branches and comparisons;
  pseudoinstructions vs real instructions; assembler directives; running code on
  CPUlator (browser) and Spike (local).
- **Prerequisites:** ch1–2; Book 5 ch16 mapping table (opened *from* it).
- **Worked examples:** (1) write `max(a,b)` and a sum-1..n loop in asm, run on
  CPUlator; (2) hand-assemble `addi` and `beq` to their 32-bit encodings, verify
  against the assembler; (3) translate a C `for` over an array into asm, check by
  diffing against `gcc -S` output on Compiler Explorer.
- **Figures:** register file + ABI convention table; the six encoding formats as
  bit-field diagrams; load/store addressing diagram; CPUlator screenshot annotated
  (registers, memory, single-step) — *only chapter allowed a UI screenshot, per style*.
- **Code listings:** sum loop (`rv32i_sum.S`); array-sum with `lw`+pointer bump;
  `max` with `bge`; corresponding C originals.
- **Measurement:** *dynamic instruction count* — run the same loop on CPUlator/Spike
  at `-O0` vs `-O2`-equivalent handwritten asm; count instructions retired per
  iteration; predict the ratio first.
- **Exercises:** inline ×3 (predict next PC). Additional ×12 [4/5/3]; signature
  [hard]: implement `strlen`, `memcpy`, `memset` in asm, self-checking on CPUlator.
- **Sources:** RISC-V unprivileged spec; CS:APP ch3 (structure, not ISA); COD ch2;
  CPUlator docs.

### Ch4. RV32I assembly II — functions and reading real compiler output — *10 pp*

- **Sections:** the calling convention (who saves what); the stack frame;
  `ra`/`sp` discipline and leaf vs non-leaf functions; recursion; position-
  independent code in one page; reading `-O0`/`-O2`/`-O3` output on Compiler
  Explorer; when the compiler deletes your code (and how to stop it for benchmarks).
- **Prerequisites:** ch3.
- **Worked examples:** (1) annotate a stack frame for a recursive `fib`; (2) predict
  then read the `-O2` codegen for a 4-way if-else vs switch (jump table); (3) find
  where `volatile`/inline asm is needed to keep a benchmark loop alive.
- **Figures:** stack-frame anatomy (caller's vs callee's view); caller/callee-saved
  register ownership diagram; jump-table memory layout; `-O0` vs `-O2` side-by-side
  codegen for one function.
- **Code listings:** recursive `fib.S` with correct save/restore; a struct-argument
  call in asm; Compiler Explorer excerpt of `-O2` output for the same C.
- **Measurement:** *calling overhead* — time a trivial function called N times vs its
  inlined body on the host; compare `-O0` vs `-O2` (function-call cost is real but
  small: quantify it).
- **Exercises:** inline ×2. Additional ×10 [3/4/3]; signature [hard]: write a
  variadic-style `sum4(a,b,c,d)` chain in asm and prove register preservation with a
  test harness.
- **Sources:** RISC-V psABI (cited via spec site); CS:APP ch3 procedures; Compiler
  Explorer.

---

## Part II — The processor (capstone build, ch5–ch8)

**Capstone spine.** Ch5 builds a correct single-cycle RV32I core (subset: arithmetic,
logic, loads/stores, branches, `jal/jalr`, `lui/auipc`, `ecall/ebreak` — ~40
instructions). Ch6 pipelines it in five stages. Ch7 adds forwarding, load-use stalls
and a branch predictor; benchmarks CPI. Ch8 adds traps + a memory-mapped UART, runs a
real program end-to-end, and synthesizes for the Tang Nano 9K (board optional — every
capstone step also runs in Verilator/Icarus).

### Ch5. A single-cycle RV32I datapath — *14 pp*

- **Sections:** fetch–decode–execute again, done properly; instruction fetch and PC;
  decode and the immediate generator; the register file and ALU (Book 5 ch14–15
  assumed — reused, not re-derived); control as a decoder table; loads/stores and the
  data-memory interface; why single-cycle wastes time (critical path) → forward to
  pipelining.
- **Prerequisites:** ch3–4 (asm fluency); Book 5 ch11–16 (Verilog, testbenches, ALU,
  datapath, custom CPU).
- **Worked examples:** (1) trace `addi x5,x0,1; sw x5,0(x6)` through the datapath
  block-by-block; (2) extend control for `jalr` — what muxes change; (3) find the
  critical path on the diagram and estimate fmax.
- **Figures:** complete single-cycle datapath (main figure, TikZ, also capstone's
  architecture reference); control-truth-table figure; immediate-generator bit-field
  diagram; cycle-flow strip for one `sw`; critical-path highlight overlay.
- **Code listings:** `rv32i_decode.v` (control decoder); `rv32i_regfile.v`;
  `rv32i_alu.v` (adapted from Book 5); `rv32i_sc_top.v` + self-checking testbench
  running a 5-instruction program.
- **Measurement:** *CPI = 1 by construction* — run a program on the sim core vs
  Spike; verify instruction counts match exactly, cycles = instructions; measure sim
  speed (instr/s in Icarus vs Verilator).
- **Exercises:** inline ×2. Additional ×11 [3/5/3]; signature [hard]: add `slti`+
  `slt` with a documented control-table change and tests.
- **Sources:** COD ch4; DDCA RISC-V ch7; Book 5 ch14–16 (bridged).

### Ch6. Pipelining — one instruction per cycle (usually) — *12 pp*

- **Sections:** why pipeline (throughput vs latency); the five stages
  IF/ID/EX/MEM/WB; pipeline registers and what each carries; timing diagrams; where
  it breaks — hazards previewed honestly (naive pipeline gives wrong answers: shown,
  not hidden); ideal CPI and speedup bound.
- **Prerequisites:** ch5 (the core exists in Verilog).
- **Worked examples:** (1) fill a timing diagram for a 5-instruction sequence;
  (2) compute the theoretical speedup of 5-stage vs single-cycle on a given path
  delay profile; (3) run the naive pipeline on a data-dependent sequence and show the
  wrong register value — motivate ch7.
- **Figures:** single vs pipelined timeline (laundry-style); 5-stage datapath with
  pipeline registers; timing-diagram conventions figure; occupancy/utilisation
  diagram showing overlap.
- **Code listings:** `rv32i_pipe_regs.v` (IF/ID, ID/EX, EX/MEM, MEM/WB);
  `rv32i_pipe_top.v`; a GTKWave/Verilator trace excerpt as a listing + figure.
- **Measurement:** *pipeline throughput in sim* — instructions retired per cycle on
  independent-instruction streams (CPI ≈ 1) vs dependent streams (CPI ≫ 1, wrong
  values) — quantifies the hazard bill before we pay it.
- **Exercises:** inline ×2. Additional ×10 [3/5/2]; signature [hard]: derive the
  optimal stage count given per-stage delay + pipeline-register overhead, minimax
  style.
- **Sources:** COD ch4; CAQA app. C; CS:APP ch4 (SEQ→PIPE pedagogical shape).

### Ch7. Hazards: forwarding, stalls, and the branch question — *14 pp*

- **Sections:** data hazards taxonomy (RAW first — the only true dependence);
  forwarding (bypassing) and where it cannot reach; the load-use stall; control
  hazards; static vs dynamic prediction, 1-bit and 2-bit predictors, BTB idea;
  precise exceptions deferred to ch8; implementing forwarding + hazard unit on the
  capstone.
- **Prerequisites:** ch6; host perf tooling (ch15 forward-referenced for Linux
  counters).
- **Worked examples:** (1) mark every dependence in a 6-instruction window and
  classify forwardable vs stall; (2) design the load-use interlock rule, prove why 1
  cycle is necessary and sufficient; (3) simulate a 2-bit predictor's state on the
  sequence T,T,N,T,T,T and compute accuracy.
- **Figures:** forwarding paths on the datapath; load-use stall timing diagram;
  branch-resolution points (EX vs ID) cost diagram; 2-bit saturating-counter FSM;
  measured CPI vs predictor-accuracy curve (own sim data).
- **Code listings:** `rv32i_forward.v`; `rv32i_hazard.v` (interlock); predictor
  module `rv32i_bp2.v`; host branch microbenchmark `branch_pred.c`.
- **Measurement:** *branch-misprediction cost* — host: predictable vs unpredictable
  binary-search loop timed (and `perf stat` branch-misses on Linux); capstone sim:
  CPI before/after forwarding and with/without predictor — the numbers must explain
  each other.
- **Exercises:** inline ×3. Additional ×12 [3/6/3]; signature [hard]: prove a
  claimed "always forward, no stalls" design is broken or fix it.
- **Sources:** CAQA app. C + ch3 (predictor taxonomy); COD ch4; Agner Fog
  microarchitecture (branch section).

### Ch8. Traps, interrupts and the capstone on real silicon — *12 pp*

- **Sections:** synchronous exceptions vs interrupts; the trap frame and
  `mtvec/mepc/mcause` (Zicsr essentials); `ecall` as the user→kernel door (forward-
  references Part IV); a memory-mapped timer and UART; the capstone complete:
  free-running "hello world" program on the core; synthesis for Tang Nano 9K
  (Yosys/nextpnr — Book 5 ch13 flow reused); what real CPUs add on top.
- **Prerequisites:** ch5–7; Book 5 ch13 (FPGA flow).
- **Worked examples:** (1) wire a timer interrupt and handler in asm on the core;
  (2) implement `print(char)` via the mmio UART; (3) read the Yosys report: LUTs,
  FFs, and the fmax estimate; find the critical path in *your* core.
- **Figures:** trap-handling timeline (user→trap→handler→resume); mmio address map;
  capstone full-system block diagram (core + timer + UART + memory); utilization/
  fmax table for the GW1NR-9.
- **Code listings:** `rv32i_csr.v` + trap glue; `uart_mmio.v`; `hello.S` running on
  the core; synthesis TCL/Makefile fragment.
- **Measurement:** *capstone benchmark* — CPI on three small programs (arithmetic,
  memory, branch-heavy) in sim, plus measured fmax/resource count on the FPGA
  (or Verilator-only path if no board) — the documented benchmark the brief requires.
- **Exercises:** inline ×2. Additional ×10 [3/4/3]; signature [hard]: add the M
  extension (`mul` only) and measure the LUT cost vs a software multiply.
- **Sources:** RISC-V privileged spec (trap CSRs only); xv6 ch4 (trap machinery);
  Book 5 ch13.

---

## Part III — Memory

### Ch9. The memory hierarchy — *12 pp*

- **Sections:** the latency/capacity pyramid and why it exists; SRAM vs DRAM vs
  storage; spatial and temporal locality; the levels as a contract (each level
  exploits the one below); latency and bandwidth numbers *measured*, not assumed;
  NUMA/multi-core in one page.
- **Prerequisites:** ch2 (addresses), ch5 (what a cycle costs).
- **Worked examples:** (1) order-of-magnitude table: register→L1→L2→LLC→DRAM→SSD,
  filled by measurement not citation; (2) compute effective access time for a two-
  level hierarchy at 95% hit; (3) explain stride-1 vs stride-64 array sums.
- **Figures:** memory pyramid (annotated with *reader's* measured numbers);
  latency-vs-working-set "memory mountain" plot (generated from own run); locality
  heat map (addresses × time); bandwidth roofline sketch.
- **Code listings:** `mem_mountain.c` (pointer-chase latency sweep); `stride_bw.c`
  (bandwidth vs stride); the Python plotter that produced the mountain figure.
- **Measurement:** *the memory mountain* — access latency vs working-set size and
  stride; identify every cache level's knee on the reader's own machine.
- **Exercises:** inline ×2. Additional ×11 [4/4/3]; signature [hard]: infer L1 line
  size and associativity from stride experiments alone.
- **Sources:** Drepper cpumemory; CS:APP ch6; CAQA ch2; Agner Fog.

### Ch10. Caches — *14 pp*

- **Sections:** cache anatomy (tag/index/offset, `C = S×E×B`); direct-mapped →
  set-associative; replacement policies (LRU and friends) and write policies
  (write-back/write-through, allocate); the three Cs of misses (compulsory, capacity,
  conflict); a cycle-accurate cache model in C (the chapter's own simulator);
  software-visible effects: blocking/tiling, alignment, false sharing preview.
- **Prerequisites:** ch9.
- **Worked examples:** (1) classify every access of a tiny trace as hit/miss by C-type
  on a given geometry; (2) compute misses for naive vs 4×4-blocked transpose on the
  model; (3) pick the geometry: solve for S,E,B given constraints and a trace.
- **Figures:** address split diagram; one-way → 4-way layout map; hit/miss state
  diagram; miss-rate vs associativity plot (own simulator data); transpose access
  pattern grids (naive vs blocked, step-multiples).
- **Code listings:** `cache_sim.c` (parameterized model, CS:APP Cache-Lab-style but
  own); `transpose_naive.c` / `transpose_blocked.c`; `miss_parse.py` trace tool.
- **Measurement:** *miss-count sweep* — naive vs blocked matrix transpose at
  32..2048² on the own simulator (exact counts) and on hardware (`perf stat` on
  Linux, time-based elsewhere); show sim predicts the real ranking.
- **Exercises:** inline ×2. Additional ×12 [4/5/3]; signature [hard]: implement
  LRU + dirty bits in `cache_sim` and verify against a hand-checked trace.
- **Sources:** CS:APP ch6 + Cache Lab shape; CAQA ch2; Drepper.

### Ch11. Virtual memory — *12 pp*

- **Sections:** why virtualize memory (isolation, relocation, sparse use); pages,
  VPN/PPN, page-table entries; the walk (sv32 two-level walk as the concrete case);
  TLBs as translation caches; demand paging, page faults, working set and thrashing;
  `fork` + copy-on-write; protection bits as the OS's fence (bridge to Part IV).
- **Prerequisites:** ch9–10 (caches make TLBs obvious); ch8 (traps make page faults
  obvious).
- **Worked examples:** (1) walk a 4-entry page table for a sv32 address by hand;
  (2) compute TLB reach for given page size/entry counts; (3) trace `fork`+COW for
  one write-heavy parent.
- **Figures:** VA→PA translation flow; sv32 page-table-walk diagram; TLB+page-table+
  cache interaction chain; working-set vs fault-rate curve (own measurement).
- **Code listings:** `tlb_reach.c` (stride over huge region); `fault_cost.c`
  (mmap-touch timing); a toy multi-level page-table walker in C.
- **Measurement:** *page-fault and TLB cost* — first-touch vs resident access time
  via `mmap`; TLB-miss penalty vs page-table depth from measured data.
- **Exercises:** inline ×2. Additional ×10 [3/5/2]; signature [hard]: simulate
  CLOCK/second-chance replacement and compare against LRU on a synthetic trace.
- **Sources:** OSTEP ch13–23 (ordering adapted); CS:APP ch9; xv6 ch3; sv32 spec.

---

## Part IV — The operating system

### Ch12. Processes and scheduling — *14 pp*

- **Sections:** the process abstraction and what the kernel owes you; fork/exec/wait
  semantics (with correct code — the classic bugs as Common mistakes); the context
  switch step-by-step (ties to ch8 traps); scheduling goals (turnaround vs response);
  FIFO/SJF/STCF/MLFQ with worked timelines; reading real kernel source: a guided walk
  of xv6 `proc.c` (this is the "read OS source" outcome — two similar guided reads
  follow in ch13–14).
- **Prerequisites:** ch8 (traps), ch11 (address spaces).
- **Worked examples:** (1) timeline for SJF vs STCF on a 3-job set; (2) trace a
  fork→exec→wait session, count the forks needed for a shell pipeline; (3) compute
  context-switch cost from a ping-pong measurement.
- **Figures:** process state machine; context-switch sequence (registers, stacks,
  PC); MLFQ queue diagram; measured context-switch cost vs thread count plot.
- **Code listings:** `fork_demo.c` (correct wait handling); `ctx_switch.c`
  (pipe ping-pong); xv6 `swtch`/`scheduler` excerpt (quoted ≤15 lines, cited);
  `sched_sim.py` (FIFO/SJF/STCF/MLFQ simulator).
- **Measurement:** *context-switch cost* — pipe ping-pong round trips; scale with
  number of processes; discuss cache warmth confound (measured, stated honestly).
- **Exercises:** inline ×2. Additional ×11 [3/5/3]; signature [hard]: implement
  MLFQ in `sched_sim` and reproduce the "game-the-scheduler" workload.
- **Sources:** OSTEP ch4–11 (simulator-style homework adopted); xv6 ch2,7; CS:APP ch8.

### Ch13. Concurrency and synchronisation — *14 pp*

- **Sections:** threads vs processes (shared address space); races and atomicity —
  what *can* go wrong between two instructions; mutual exclusion and the
  test-and-set/`amo`/`lr-sc` mechanisms (RISC-V A extension, read not built); mutex
  vs spinlock; condition variables done right (Mesa semantics, while-not-if);
  semaphores; deadlock and lock ordering; lock-free in one honest page; Amdahl's
  revenge — what concurrency actually buys.
- **Prerequisites:** ch12; ch4 (asm, for the atomic primitive reading).
- **Worked examples:** (1) reproduce a lost-update race and count the losses;
  (2) fix it three ways (mutex, atomic add, per-thread accumulation) and measure
  all three; (3) solve producer–consumer with CVs, then break it with `if` instead
  of `while` and show the failure.
- **Figures:** race timeline (two threads, one counter); lock-contention scaling
  curve (own data); CV wait/signal state diagram; deadlock wait-for graph.
- **Code listings:** `race.c` (deliberate bug, shown failing); `spinlock.c` with
  `atomic_flag`; `pc_cv.c` producer–consumer; `lr_sc.S` RISC-V atomic read-along.
- **Measurement:** *lock scaling* — counter increments under mutex/atomic/partitioned
  at 1..8 threads; the graph is the lesson (and usually non-monotonic on a laptop:
  discuss why honestly).
- **Exercises:** inline ×2. Additional ×12 [4/5/3]; signature [hard]: prove or
  repair a submitted "lock-free" counter (Dekker-style reasoning, memory ordering
  argued informally).
- **Sources:** OSTEP ch26–33 (ordering + bug taxonomy); xv6 ch6,9; CS:APP ch12.

### Ch14. File systems and persistence — *10 pp*

- **Sections:** what a file system promises (names, durability, crash behaviour);
  files/inodes/directories and the API (`open/read/write/fsync/close`); allocation
  strategies (contiguous, linked, indexed, extents); the buffer cache; journaling
  and crash consistency; SSDs and why random writes hurt; measured I/O truths vs
  folklore.
- **Prerequisites:** ch9 (memory hierarchy), ch12.
- **Worked examples:** (1) trace `write()` through buffer cache → journal → disk;
  (2) compute max file size for a given inode scheme; (3) measure sequential vs
  random read throughput on the reader's disk.
- **Figures:** inode/extent layout diagram; journal transaction timeline; sequential
  vs random throughput bar chart (own data); fsync latency histogram.
- **Code listings:** `fs_seq_rand.c` throughput test; `fsync_cost.c`; guided xv6
  `log.c`/`file.c` reading excerpt (cited); `ls_inodes.py` walker.
- **Measurement:** *storage sweep* — sequential vs random read/write MB/s and
  fsync-per-write cost on the reader's machine; contrast with ch9's pyramid.
- **Exercises:** inline ×2. Additional ×10 [3/5/2]; signature [hard]: design the
  inode for 1 GB max file with 4 KB blocks, smallest metadata that works.
- **Sources:** OSTEP ch36–46; xv6 ch8; CS:APP ch10.

---

## Part V — Performance craft

### Ch15. Measuring performance correctly — *10 pp*

- **Sections:** latency vs throughput, mean vs tail (p50/p99); CPI/IPC, Amdahl,
  speedup law; the benchmark-hygiene checklist (warm-up, cache state, frequency
  scaling, compiler elimination, noise, min-vs-mean debates — each named, each with
  a fix); `perf` on Linux, Instruments/`xctrace` on macOS, `clock_gettime` as the
  portable floor; flame graphs; reporting a number honestly (error bars, n, machine
  spec — this book's own convention).
- **Prerequisites:** everything to ch14 informs; formally ch4 (asm reading).
- **Worked examples:** (1) take ch7's branch benchmark, run it naively, list every
  methodology bug, fix, rerun; (2) compute Amdahl bound for a 70%-vectorizable
  kernel; (3) read one flame graph and locate the 3 real hotspots.
- **Figures:** measurement-checklist flow figure; p50 vs p99 latency distributions;
  flame-graph anatomy; Amdahl curves at several fractions.
- **Code listings:** `bench_harness.c` (portable timer + warm-up + stats);
  `bench_bad.c` → `bench_fixed.c` pair; `perf stat/record` session transcript
  (Linux) with macOS alternative note.
- **Measurement:** *the honest benchmark* — reproduce ch7's result with and without
  each hygiene fix; quantify how wrong the naive version was.
- **Exercises:** inline ×2. Additional ×10 [3/4/3]; signature [hard]: find and
  document a real-world "benchmark" online that violates ≥3 checklist items.
- **Sources:** Brendan Gregg (checklist, flame graphs); perfwiki; MIT 6.172; CAQA ch1.

### Ch16. Vectorisation and data parallelism — *10 pp*

- **Sections:** SIMD as the other parallelism (data-level vs thread-level); lanes and
  width on the host ISA (AVX2/NEON — the book states host-dependence honestly);
  auto-vectorisation: what the compiler needs (aliasing, alignment, trip counts);
  intrinsics as the manual path; SoA vs AoS layouts; RVV's scalable-vector idea in
  one page (run on Spike); when SIMD does not help.
- **Prerequisites:** ch9–10 (memory effects dominate), ch15 (measure it).
- **Worked examples:** (1) SAXPY: scalar → auto-vec → intrinsics, three measured
  generations; (2) make auto-vec fail (`restrict` missing) then fix; (3) AoS→SoA
  transform on a particle struct, measure both.
- **Figures:** lane-wise execution diagram; AoS vs SoA memory map; speedup-vs-width
  measured plot; compiler-vectorisation report excerpt.
- **Code listings:** `saxpy.c` three ways; `soa_aos.c`; `rvv_sum.S`/rvv-intrinsics
  demo on Spike (one page); Compiler Explorer codegen excerpt proving the vector
  loop exists.
- **Measurement:** *the vectorization sweep* — scalar vs vector kernels at n=1e3..1e8;
  bandwidth saturation point identified from the reader's own machine (ties ch9).
- **Exercises:** inline ×2. Additional ×10 [3/4/3]; signature [hard]: vectorize a
  prefix-sum (requires scan strategy, not element-wise).
- **Sources:** Agner Fog optimizing_cpp + vector manuals; MIT 6.172; RISC-V V-spec
  (concepts); Compiler Explorer.

### Ch17. Low-latency design patterns — *12 pp*

- **Sections:** what "low latency" actually costs (jitter, not just mean); branchless
  idioms (`cmov`-style, arithmetic selection) and when they lose; cache-friendly
  layouts (hot/cold splitting, packing); prefetching (hardware already does it —
  when software hints pay); batching and avoiding syscalls/allocations in hot paths;
  false sharing; the pattern → the measured effect → the trade-off table.
- **Prerequisites:** ch7, ch9–10, ch15–16 (this chapter spends their measurements).
- **Worked examples:** (1) branchless `min`/clamp vs branchy — measured with
  mispredict counts; (2) linear vs binary vs branchless search across sizes — the
  crossover measured, not asserted; (3) allocation-free ring-buffer queue vs
  per-node queue.
- **Figures:** branchy vs branchless time-vs-predictability surface; AoS/SoA/packed
  layout comparison; hot-path annotated loop figure; pattern→effect→tradeoff summary
  table (the chapter's cheat-sheet).
- **Code listings:** `search_cmp.c` (three searches); `ringbuf.c` allocation-free
  queue; `cmov_pred.c` branchless select; measured outputs as listings.
- **Measurement:** *the folklore audit* — take 5 common low-latency claims, measure
  each on the reader's machine, print a verdict table (some survive, some die).
- **Exercises:** inline ×2. Additional ×11 [3/5/3]; signature [hard]: find a case
  where a "faster" pattern from this chapter is actually slower, and explain it from
  measured counters.
- **Sources:** Agner Fog; Brendan Gregg; MIT 6.172; own measured data (primary).

---

## Part VI — Language runtimes

### Ch18. An interpreter and a compiler in miniature — *12 pp*

- **Sections:** why a toy language closes the loop (source → bytes → silicon, one
  book later); a 4-op stack/bytecode VM in C (fetch–decode–execute — the reader will
  notice it is ch5's datapath in software); a compiler for a small expression language
  that emits RV32I; running compiled output on Spike and on the ch5–8 core;
  interpretation vs compilation measured; where JITs and real compilers go next
  (pointing at Crafting Interpreters and Compiler Explorer for the road).
- **Prerequisites:** ch3–4 (asm), ch5 (the core), ch15 (measurement).
- **Worked examples:** (1) hand-compile `x = (a+3)*(b-1)` to RV32I, verify on Spike;
  (2) trace the VM executing the same program bytecode-by-byte; (3) the shootout:
  interpreter vs compiled vs native — measure all three.
- **Figures:** lexer→parser→bytecode pipeline; AST for the example program;
  interpreter vs compiled instruction-count bars (own data); the book's full arc
  recap diagram (source→ISA→core→OS→language).
- **Code listings:** `vm.c` (bytecode VM ~120 lines, exerpt); `mini_compiler.py`
  (emits `.S`); generated `prog.S` on the capstone core; shootout harness.
- **Measurement:** *interpreter vs compiler* — bytecode VM vs RV32I-compiled (on
  Spike + on the capstone core in sim) vs host-native — three rungs of the same
  ladder, quantified.
- **Exercises:** inline ×2. Additional ×10 [3/4/3]; signature [hard]: add a
  register-allocated (not stack) code path for locals and measure the win.
- **Sources:** Crafting Interpreters (structure); CS:APP arc; RISC-V spec.

---

## Appendices and back matter (~16 pp)

- **Appendix A.** RV32I green card: every instruction, encoding, format — 4 pp
  (source: RISC-V spec, own layout).
- **Appendix B.** Toolchain recipes: CPUlator, Spike build, xPack gcc, OSS CAD
  Suite, perf/Instruments — OS-by-OS, date-stamped — 4 pp.
- **Appendix C.** Capstone reference: module list, testbench conventions,
  benchmark harness description — 4 pp.
- Hints for all [hard]; full solutions ≥ half of all exercises; bibliography
  (numbered, all sources from `docs/sources.md`); index.

---

## Consistency notes

- Book 5 boundary held: no Verilog teaching, no Boolean algebra, no FSMs, no ALU
  internals — all assumed. Ch1 opens *from* Book 5's RV32I mapping table verbatim
  (reprinted with attribution as a bridge).
- Register naming: ABI names in all assembly (`a0`, `sp`, `ra`), x-numbers in the
  encoding tables only (see `notation.md`).
- Every measurement names hardware/OS and is reproducible from `code/`; perf used
  where available, portable timing everywhere.
- Figures ≥4, listings ≥3, worked examples ≥3, additional exercises ≥10 per chapter
  (spread across [easy]/[medium]/[hard]); Common mistakes + one-page summary table
  + Notes every chapter.
