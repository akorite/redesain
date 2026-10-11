# Notation

Book 7 (*Computer architecture and systems*). Conventions consistent with Book 5
(electronics/FPGA) wherever they overlap — see `shared_notation_proposals` for what
this book needs back from Book 5's `notation.md`. Per the approved global decisions:
`log` = natural log; other bases explicit (`log_2` for address bits, entropy).

| Symbol / macro | Meaning | First used |
|---|---|---|
| **Assembly & registers** | | |
| `x0`–`x31` | Integer register numbers (encoding tables, datapath text) | ch3 |
| `zero`, `ra`, `sp`, `gp`, `tp` | ABI names of x0–x5 — used in all assembly listings | ch3 |
| `t0`–`t6`, `s0`–`s11` (= `s0`=`fp`), `a0`–`a7` | ABI names of temporaries, saved, argument registers | ch3 |
| `pc` | Program counter (current fetch address) | ch3 |
| `imm`, `imm20`, `imm12` | Sign-extended immediate fields of an instruction | ch3 |
| `rd`, `rs1`, `rs2` | Destination / source register fields in an encoding | ch3 |
| `op:` label | Assembler label convention; `label:` defines, plain use references | ch3 |
| `ecall`, `ebreak` | Environment call / breakpoint — the only two system instructions in RV32I core | ch3, ch8 |
| `RV32I`, `RV32IM`, `RV32IMA` | ISA subset names; teaching core = RV32I, optional M/A | ch3 |
| **Memory & addresses** | | |
| `0x1234ABCD` | Hex literal, byte address | ch1 |
| `M[a]` | Contents of memory at byte address `a` (width from context; `M32[a]` explicit) | ch3 |
| `a[7:0]`, `x[31:0]` | Bit slicing, MSB:LSB — Verilog-style, matches Book 5 | ch2 |
| `VA`, `PA` | Virtual / physical address | ch11 |
| `VPN`, `PPN`, `offset` | Page-number / page-offset split of an address: `VA = VPN ∥ offset` | ch11 |
| `PTE` | Page-table entry | ch11 |
| `∥` | Bit-field concatenation (`VPN ∥ offset`) | ch11 |
| little-endian | Byte 0 at lowest address = least significant; RV32 convention; drawn LSB-right | ch2 |
| `KiB/MiB/GiB` | Binary units (1024-based); `KB/MB/GB` reserved for decimal (storage/network) | ch2 |
| `B` | Byte; `b` | bit | ch2 |
| **Processor & pipeline** | | |
| `IF`, `ID`, `EX`, `MEM`, `WB` | The five pipeline stages | ch6 |
| `IF/ID`, `ID/EX`, `EX/MEM`, `MEM/WB` | Pipeline registers, written stage/stage (COD convention) | ch6 |
| `CPI`, `IPC` | Cycles per instruction / its reciprocal | ch5 |
| `T_cycle`, `f_max` | Cycle time and its reciprocal | ch5 |
| `RAW`, `WAR`, `WAW` | Dependence classes; only RAW causes true data hazards | ch7 |
| `T`, `N` | Branch taken / not-taken in trace notation | ch7 |
| `BTB` | Branch target buffer | ch7 |
| `mtvec`, `mepc`, `mcause`, `mstatus` | Trap CSRs used (Zicsr subset only) | ch8 |
| **Cache & memory hierarchy** | | |
| `C = S × E × B` | Cache capacity = sets × ways (lines/set) × block bytes (CS:APP/CAQA convention) | ch10 |
| `s`, `b` | Index bits, block-offset bits; tag = `a − s − b` | ch10 |
| `AMAT = HT + MR × MP` | Average memory access time | ch9 |
| `HT`, `MR`, `MP` | Hit time, miss rate, miss penalty | ch9 |
| `L1`, `L2`, `LLC` | Cache levels; LLC = last-level | ch9 |
| `TLB` | Translation lookaside buffer — "the cache for translations" | ch11 |
| `WSS` | Working-set size | ch9 |
| **OS & concurrency** | | |
| `pid` | Process identifier | ch12 |
| `fork`, `exec`, `wait` | POSIX calls, always monospace | ch12 |
| `MLFQ` | Multi-level feedback queue | ch12 |
| `T_turnaround`, `T_response` | Scheduling metrics (OSTEP definitions) | ch12 |
| `lr.w`/`sc.w`, `amo*` | RISC-V A-extension primitives (read, not built) | ch13 |
| `CV` | Condition variable | ch13 |
| `Q` | Queue in diagrams | ch12 |
| **Performance & time** | | |
| `ns`, `µs`, `ms`, `s` | Wall-clock units; `cycles` spelled out (never `c`) | ch1 |
| `T(n)`, `T_lat`, `T_th` | Time, latency, throughput as functions of size | ch15 |
| `S = T_old/T_new` | Speedup; `E` efficiency where needed | ch15 |
| `f` | Parallel/vectorisable fraction in Amdahl's law: `S ≤ 1/((1−f)+f/p)` | ch15 |
| `p50`, `p99` | Latency percentiles | ch15 |
| `n` | Repetition count of a measurement; always printed beside a result | ch1 |
| `±` | Reported with n and machine spec — this book's honesty convention | ch15 |
| **Verilog (capstone, consistent with Book 5 style)** | | |
| `clk`, `rst_n` | Clock (posedge), active-low synchronous reset — must match Book 5 | ch5 |
| `rv32i_*` | Module prefix for the capstone (`rv32i_fetch`, `rv32i_decode`, `rv32i_alu`, `rv32i_regfile`, `rv32i_pipe_regs`, `rv32i_forward`, `rv32i_hazard`, `rv32i_bp2`, `rv32i_csr`, `rv32i_sc_top`, `rv32i_pipe_top`, `uart_mmio`) | ch5 |
| `i_*`, `o_*` | Port direction prefixes (if Book 5 uses them — to confirm) | ch5 |
| `wire`/`reg`-style declarations | Verilog-2005 style as in Book 5 (no SystemVerilog in listings) | ch5 |
| `D`/`Q` | Register input/output names in datapath figures | ch5 |
| `←` or `:=` | Register-transfer assignment in text — pick Book 5's convention | ch5 |
| **Typography** | | |
| `code font` | Instructions, mnemonics, file names, tool names | ch1 |
| *italic* | New terms at definition (index entry at same point) | ch1 |
| `p.`, `pp` | Page(s) | preface |
