# Notation — textbook-electronics

Conventions for every chapter. Where a choice exists, we state it once here and never deviate.
Units are typeset with `siunitx` (loaded in `main.tex`, never in `lifeos.sty`): `\qty{4.7}{\kilo\ohm}`,
`\qty{3.3}{\volt}`, `\qty{100}{\nano\farad}`; numbers use a decimal point, engineering prefixes
(k, M, m, µ→u in code, n, p).

## Electrical quantities

| Symbol / macro | Meaning | First used |
|---|---|---|
| $V$, $v(t)$ | voltage; uppercase for DC/operating point, lowercase-$v$ for time-varying | ch1 |
| $V_{DD}$, $V_{CC}$, GND | positive supply (3.3 V unless stated) and ground node | ch1 (GND), ch6 (V_DD) |
| $v_s$ | source voltage | ch2 |
| $I$, $i(t)$ | current, same case convention | ch1 |
| $R$, $r$ | resistance; $r$ for small internal/on resistances ($r_{DS(on)}$) | ch1, ch6 |
| $G$ | conductance $=1/R$ (only where it pays) | ch3 |
| $P$ | power, $P=VI=I^2R=V^2/R$ | ch2 |
| $C$ | capacitance; $i=C\,dv/dt$ | ch4 |
| $L$ | inductance; $v=L\,di/dt$ | ch4 |
| $\tau$ | time constant, $\tau=RC$ or $L/R$ | ch4 |
| $Z$ | impedance (complex, $Z=R+jX$); introduced informally, full phasor deferred | ch4 (starred) |
| $X_C$, $X_L$ | reactance | ch4 (starred) |
| $V_F$ | diode/LED forward voltage | ch5 |
| $V_{GS}$, $V_{TH}$, $r_{DS(on)}$ | MOSFET gate-source voltage, threshold, on-resistance | ch6 |
| $V_{IL},V_{IH},V_{OL},V_{OH}$ | static-discipline thresholds; noise margins NM_L/NM_H | ch6 |
| $f$, $T$ | frequency and period, $T=1/f$; clock period $T_{clk}$ | ch4, ch10 |
| $t_{su}$, $t_h$, $t_{pd}$ | setup, hold, propagation delay (conceptual) | ch10 |

## Schematic and netlist conventions

| Convention | Meaning | First used |
|---|---|---|
| circuitikz only | every schematic drawn with `circuitikz`; no pasted images | ch1 |
| GND symbol, +3V3 / +5V rails | ground and supply drawn as power symbols, not batteries | ch1 |
| Net names | functional names in schematic (`SENSE`, `EN`), numeric or `n1` nodes in SPICE | ch2 |
| SPICE element names | first letter = type (`V1`, `R1`, `C1`, `D1`, `M1`, `X1`); values in SI | ch2 |
| Signal arrows | arrows = current direction chosen; signed values may be negative | ch3 |
| +5V vs 5V\_SW | unswitched vs switched/supplied nets distinguished in name | ch7 |

## Digital and Verilog conventions

| Convention | Meaning | First used |
|---|---|---|
| 1/0, H/L | logic levels; `1` = asserted, `0` = deasserted unless `_n` suffix | ch8 |
| `8'h1F`, `4'b1010`, `8'd255` | sized literals, always sized | ch9 |
| `[7:0]` | bus order MSB-first; `A[3]` = bit 3 of A | ch9 |
| module names | `lower_snake` (`alu8`, `traffic_fsm`); testbenches `<name>_tb` | ch9, ch11 |
| port prefixes | `i_` input, `o_` output, `io_` inout: `i_clk`, `i_rst`, `i_a`, `o_y` | ch11 |
| clock/reset | exactly one `i_clk`; `i_rst` synchronous, active-high; active-low nets end `_n` (`i_uart_rx_n` never happens in this book — we stay active-high) | ch11 |
| state regs | `state_q` registered value, `state_d` next-state combinational | ch10/11 |
| parameters | `parameter NAME = val`, ALL_CAPS; instances `inst_` or descriptive | ch11 |
| blocking/non-blocking | `=` inside `always @*` (comb); `<=` inside `always @(posedge i_clk)` — the one rule | ch11 |
| filename = module | `alu8.v` holds `module alu8`; one module per file (except small tb-only helpers) | ch11 |

## Diagrams

| Convention | Meaning | First used |
|---|---|---|
| Timing diagrams | generated from real VCD/sim output (matplotlib→PDF); clock drawn; transitions vertical; X = hatched region; cause→effect arrows | ch10 |
| State machines | circle = state, label = name/code; edge label `condition / output` (Mealy); Moore outputs inside the state node | ch10 |
| Block diagrams | boxes with name inside, arrows left-to-right for data, control dashed; widths marked `/8` on buses | ch9 |
| Memory maps | address on left, contents right, low addresses top | ch15 |

## CPU / machine conventions (shared — see shared_notation_proposals)

| Symbol | Meaning | First used |
|---|---|---|
| `PC` | program counter | ch15 |
| `IR` | instruction register | ch15 |
| `R0`–`R7`, `Rn` | register file; `R[i]` contents of register i | ch15 |
| `M[a]` | memory location at address a | ch15 |
| `FLAGS{N,Z,C,V}` | flag bits: Negative, Zero, Carry, oVerflow | ch14 |
| `op field` | instruction encoding written `[7:4]=op [3:0]=rd/imm` tables | ch16 |
| fetch–decode–execute | the three phases; cycle counter `k` in traces | ch16 |

## Text conventions

| Convention | Meaning |
|---|---|
| `definition` env | first use of every defined term, `\index{}`'d |
| `tripwire` env | safety/danger content |
| `checkpoint` env | predict-before-you-run prompts |
| `[easy]/[medium]/[hard]` | exercise grading, per §3 |
| `Listing` | code; every listing has caption+label and a printed real output |
