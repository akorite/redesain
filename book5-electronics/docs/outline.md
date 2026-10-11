# Outline — Book 5: Electronics and digital design, FPGA (`textbook-electronics`)

Status: Wave-1 proposal, awaiting coordinator/user approval before any chapter is written.
Research log: `docs/sources.md`. Conventions: `docs/notation.md`.
All tool versions and prices date-stamped 2026-10-10.

## 0. Design decisions (read first)

**Audience contract.** Algebra + beginning calculus, strong programmer, zero electronics. Every physical
quantity is defined before use; calculus is used only as far as $dv/dt$ and $\int$ in ch4, with
the intuitive reading given first.

**Six parts, 19 chapters.** Order follows All About Circuits + Harris&Harris (analog fundamentals →
devices → digital logic → HDL → FPGA → machine → physical build). Deliberate deviations from the
seed list, each researched:

1. *MOSFET-as-switch before op-amps.* MIT 6.002 introduces the digital abstraction at lecture 4 and
   the MOS switch model at lecture 5, before small-signal amplifier theory. Ch6 transistors is
   written as the explicit bridge: switches → static discipline → CMOS gate, so Part III (digital)
   lands on physics the reader already owns. Amplifier design depth is deliberately shallow —
   this book's op-amp outcome is *use a comparator/buffer/regulator correctly*, not design one.
2. *Simulation-first, hardware-optional until Part VI.* Platt's experiment-first order is superb
   for a reader with a stocked bench; our reader has a laptop and a ~US$20 budget. Every analog
   circuit in the book ships an ngspice netlist the reader runs and modifies; breadboard anatomy
   is taught in ch1 and optional "build it on your breadboard" checkpoints appear from ch2, but
   no chapter before ch17 *requires* components. The single required purchase is the FPGA board.
3. *HDL after logic, per H&H.* Verilog waits until the reader can draw the circuit on paper —
   Verilog describes hardware, it does not replace the mental model. Testbenches are taught as
   first-class citizens from the first module (brief requirement: every module has a testbench).
4. *The CPU is our own 8-bit ISA, not verbatim Hack and not RISC-V.* Nand2Tetris owns the
   gate→ALU→RAM→CPU→assembler ladder; we borrow the ladder but design a cleaner load/store ISA
   so that (a) it is not a copy, and (b) Book 7 can then introduce real RISC-V as "the same ideas,
   done properly" and carry the capstone to a pipelined core. A tiny Python assembler is a ch16
   code listing.
5. *Merged op-amps + regulators/power into one chapter* (ch7) to stay inside 250 pp; full op-amp
   design theory is out of scope for this reader's goals.
6. *K-maps kept to 2–3 variables, algebra-first.* AAC teaches K-maps through 6 variables; Yosys
   does the minimisation in practice, so we teach the concept and move on.

**Toolchain (pinned 2026-10-10, all in one download):** OSS CAD Suite daily build containing
Icarus Verilog v13.0, Verilator v5.050, Yosys v0.69, nextpnr-himbaechel 0.8, apicula,
openFPGALoader, GTKWave; ngspice-47 (separate install); KiCad 10.0.7 (current stable, verified 2026-10-10 via kicad.org release notes; re-verify
at each writing session and pin in `code/README.md`). Versions recorded in `code/README.md`; the book instructs the reader to note drift on update.

**Target board: Sipeed Tang Nano 9K** (Gowin GW1NR-LV9, 8640 LUT4 / 6480 FF / 468 Kb BSRAM,
onboard USB-JTAG+UART via BL702, HDMI, LEDs, buttons, 27 MHz). ~US$18–23 worldwide; an Ubuy
Indonesia listing exists and SE-Asian marketplaces routinely stock it — **exact Indonesian
street price unverified, flagged as open question**. Chosen over iCE40 boards (fully open
toolchain but 2–5× the price for less logic) and Altera/DE boards (~Rp 4.6 M in-country).

**Two capstones, woven through Parts V–VI:**
- **C1 — the machine:** ch14 8-bit ALU → ch15 datapath → ch16 simple CPU running a real
  assembled program on the Tang Nano 9K (UART output). Verification: self-checking testbenches
  + a real-program run on hardware.
- **C2 — the board:** ch17 breadboard builds → ch18 two-layer sensor board in KiCad
  (MCU/sensor + LDO + header mating to the FPGA board) → Gerbers ready to order; ordering the
  PCB is optional (cost note included).

**Simulation contract:** every circuit in the book has a runnable ngspice netlist in `code/`;
every Verilog module has a testbench whose VCD output is post-processed into the printed
waveform figures (no hand-drawn timing). `make test` re-runs all of them.

**Common mistakes (approved decision 7, 2026-10-10):** every chapter carries a
"Common mistakes" section — seeded above per chapter (floating inputs, missing pull-ups,
inferred latches, clock-domain slips, missing testbench cases, and the like).

**Safety (per §4):** the book never directs the reader at mains. Mains appears only inside
clearly-marked tripwire boxes explaining why it is out of scope (ch1, ch7, ch18); soldering and
lithium-battery notes in ch17–18.

## 1. Page budget

| Block | Pages |
|---|---|
| Front matter (title, ToC, how to use this book, the kit & budget list) | 8 |
| Part I — Foundations (ch1–3) | 36 |
| Part II — Components and analog circuits (ch4–7) | 46 |
| Part III — Digital logic (ch8–10) | 34 |
| Part IV — Verilog and FPGA (ch11–13) | 35 |
| Part V — The machine (ch14–16) | 38 |
| Part VI — The physical build (ch17–19) | 30 |
| Back matter (hints, solutions ≥50%, bibliography, index) | 17 |
| **Total** | **244** |

Cut candidates if a chapter runs long: ch19 folds into ch16 (−6); ch7 op-amp section trims (−3);
appendix B (component buying list) compresses (−2).

## 2. Hardware requirement per chapter

| Chapters | Needs |
|---|---|
| 1–10 | Simulation-only (ngspice). Breadboard checkpoints optional everywhere. |
| 11–12 | Computer only (Icarus/Verilator/GTKWave). |
| 13–16 | Tang Nano 9K board (~US$20, the one required purchase). Ch11–14 fully simulatable without it; ch15–16 degrade gracefully to simulation if the board is late. |
| 17 | Breadboard + small component kit (~US$10–15: resistors, caps, LEDs, 1N4148, 2N7000, LM358, LM7805/LDO, wires, 9V/USB supply). Optional if budget is exhausted — chapter is readable, less learned. |
| 18 | Computer only (KiCad is free). Ordering the PCB optional (~US$5–15 fab + shipping). |
| 19 | Nothing beyond ch13's board; Arduino section is read-only unless reader already has one. |

## 3. Part I — Foundations

### Ch1 — Electricity, circuits and the workbench (12 pp, simulation + optional kit)
Prereq: none.
Sections: What electricity is (charge, fields → voltage as potential difference, one-paragraph
honesty about what we skip); current; resistance and the resistor; a complete circuit and the
schematic as the real object; conventional vs electron flow; the multimeter; the workbench kit
and the budget; **safety: what this book will and will not have you touch**.
Worked examples: (1) reading a simple circuit diagram into a parts list; (2) choosing a resistor
to light an LED from 5 V (forward into ch2, worked only after Ohm's law — posed here, solved
there); (3) estimating battery life for a 20 mA LED.
Figures: F1 atoms→charge→field cartoon; F2 V/I/R water-analogy vs honest version side-by-side;
F3 circuitikz first schematic (battery–resistor–LED); F4 photo-style TikZ of a DMM dial with the
three things we measure; F5 the shopping list as a table-figure.
Code listings: none required (analog sim starts ch2) — a `code/` README + install-check script
counted as listing 1: `check_tools.sh` printing detected versions.
Simulations: none (tooling dry-run only).
Exercises: 3 inline + 10 additional (4 easy / 4 medium / 2 hard: unit conversions, identifying
series vs parallel from photos of real boards, computing resistor colour codes, "why is the
water analogy wrong" essay→rubric).
Safety: the low-voltage-only rule; what mains can do (numbers, no drama); ESD when handling ICs;
LiPo/battery short warning; the "if it plugs into the wall, we do not open it" rulebox.
Common mistakes: reading a schematic as geography not topology; switching conventional vs electron flow mid-argument; assuming the multimeter 'uses up' what it measures.
Sources: AAC vol I ch1–3; SparkFun breadboard/multimeter tutorials; OpenStax vol 2 (charge/field
derivations cited).

### Ch2 — Ohm's law, power and the simulator (12 pp, simulation + optional breadboard)
Prereq: ch1.
Sections: Ohm's law as a definition of R; power P=VI and dissipation ratings; nonlinear loads
(LED preview); resistor networks concept; reading a datasheet's headline numbers; **your first
ngspice netlist** — nodes, elements, `.op`, `.dc` sweeps; why we simulate before we build.
Worked examples: (1) LED resistor sizing for 5 V and 3.3 V, done twice with tolerances;
(2) power-rating check on a 1/4 W resistor carrying 100 mA → fails, choose bigger;
(3) the same circuit three ways: by hand, by ngspice `.op`, by `.dc` sweep plot — cross-check.
Figures: F1 V-I line through origin vs LED curve; F2 resistor colour-code chart; F3 annotated
ngspice run screenshot→re-drawn TikZ of netlist→output flow; F4 the `.dc` sweep plotted
(pgfplots from real output); F5 "predict the output" checkpoint figure.
Code listings: `led.cir` netlist; its `.op` output; `sweep.cir` + matplotlib/PGF figure source;
`check_tools.sh` output.
Simulations: S1 `.op` operating point of battery–resistor; S2 `.dc` sweep V 0–5 V on LED
resistor circuit.
Exercises: 3 inline + 10 (4/4/2; incl. derive the P=I²R forms, write a netlist for a two-resistor
circuit, predict-then-run checkpoints).
Safety: resistor power ratings and "it gets hot"; USB power only.
Common mistakes: applying V=IR to nonlinear loads (LEDs); ignoring power ratings until the resistor browns; treating a .op number as exact (tolerances exist).
Sources: AAC vol I ch2 (+ its own SPICE section), OpenStax vol 2 circuits.

### Ch3 — Series, parallel and Kirchhoff's laws (12 pp, simulation + optional breadboard)
Prereq: ch2.
Sections: series and parallel definitions by node count; equivalent resistance both ways;
voltage divider (the most-used circuit in the book); current divider; KCL and KVL as
conservation laws; the node-voltage method on two nodes; Thévenin/Norton equivalents —
concept and one worked use each (depth-limited); measuring without breaking the circuit
(meter loading).
Worked examples: (1) divider for 3.3 V logic from 5 V; (2) solving a two-loop network by
node-voltage then verifying in ngspice; (3) Thévenin model of a divider and when the
simplification lies.
Figures: F1 series vs parallel redrawn four ways (same circuit); F2 divider annotated;
F3 KCL/KVL loop diagram with signed drops; F4 Thévenin equivalent picture; F5 meter-loading
measurement figure; F6 summary cheat-sheet table.
Code listings: `divider.cir`; `twoloop.cir` + output; `thevenin_check.cir` + output.
Simulations: S1 divider `.op`; S2 two-loop `.op` cross-check; S3 sweep showing Thévenin model
matches original across load resistance.
Exercises: 3 inline + 10 (4/4/2 incl. design a divider under a load current — the classic trap;
derive R_parallel formula; a mesh problem).
Safety: none new.
Common mistakes: applying KVL around the wrong loop / KCL at a node that isn't one; mixing series and parallel formulas mid-redraw; forgetting R_eq changes when the network is redrawn.
Sources: AAC vol I ch5–6, ch10; MIT 6.002 L1–L3.

## 4. Part II — Components and analog circuits

### Ch4 — Capacitors, inductors and RC/RL transients (12 pp, simulation)
Prereq: ch3; calculus reading $dv/dt$, $\int$ informally.
Sections: the capacitor as charge bucket (I = C dv/dt); energy storage; the RC step response —
derivation shown once, intuition always; time constant τ; charging vs discharging; the inductor
dual (V = L di/dt), kept lighter; RL transients; where transients hide: debounce, power-up
reset, decoupling; a starred section on the driven RLC (why ringing happens) marked optional.
Worked examples: (1) 555-style RC delay computation → ngspice `.tran` check; (2) decoupling:
what a 100 nF cap does to a sudden current step, simulated; (3) RL flyback voltage when a relay
coil is opened — computed, simulated, safety-flagged.
Figures: F1 capacitor charge cartoon; F2 RC step response plot (real `.tran` output);
F3 τ marked at 63 %; F4 charging vs discharging curves; F5 inductor flyback waveform (real sim);
F6 decoupling before/after.
Code listings: `rc_step.cir` + plotted output; `decouple.cir`; `relay_flyback.cir` + warning
comment; Python VCD/CSV→figure script.
Simulations: S1 RC `.tran` step; S2 decoupling `.tran` with pulse current; S3 relay flyback
`.tran` (this one motivates the diode in ch5).
Exercises: 3 inline + 10 (4/4/2 incl. derive τ from the ODE, compute a delay, design RC for
50 ms).
Safety: flyback spikes kill transistors (preview of diode protection); capacitor bleeds/charged
caps on unplugged circuits.
Common mistakes: assuming capacitors respond instantly; sign errors in the discharge direction; using steady-state formulas mid-transient.
Sources: AAC vol I ch13–16; 6.002 L13–L16.

### Ch5 — Diodes (10 pp, simulation)
Prereq: ch4.
Sections: the junction diode — I–V curve and the three models (ideal / 0.7 V / Shockley stated
not derived); forward voltage of LEDs; the rectifier; the flyback (freewheel) diode applied to
ch4's relay; the zener and its shunt regulator (honest about when not to use it); the diode in
the wild (ESD protection, reverse-polarity guard).
Worked examples: (1) half-wave rectifier `.tran` and ripple estimate; (2) zener shunt for a
3.3 V reference from 9 V, sized and simulated; (3) reverse-polarity protection — series diode
vs Schottky vs "just don't" trade-offs.
Figures: F1 I–V curve; F2 three models overlaid; F3 half-wave rectifier schematic +
input/output waveforms; F4 flyback diode placement figure; F5 zener shunt.
Code listings: `rectifier.cir` + output waveforms; `zener.cir` + sweep; `reverse_pol.cir`.
Simulations: S1 rectifier ripple vs C; S2 zener regulation vs load; S3 flyback with/without
diode (the spike, tamed).
Exercises: 3 inline + 10 (4/4/2 incl. pick a flyback diode rating, ripple computation, LED
current in a matrix).
Safety: what happens with no flyback diode (real transistor casualty story as remark).
Common mistakes: treating a diode as a zero drop; forgetting reverse-voltage limits; sizing LED current off the ideal model.
Sources: AAC vol III diodes; 6.002 nonlinear lectures (model layering).

### Ch6 — Transistors: the switch and the amplifier (12 pp, simulation) **— the bridge chapter**
Prereq: ch5.
Sections: the MOSFET — terminals, V_GS, the switch (S model) then the switch-resistor (SR
model, 6.002's pedagogy); the NMOS inverter built by hand; the static discipline — what
makes a level a "1" (noise margins); CMOS NAND/NOR/inverter; the BJT as the current-controlled
cousin (conceptual, BJT amplifier design flagged out of scope); the transistor as amplifier —
one small-signal example, honestly labelled "further study lives in AoE"; logic families and
voltage levels (3.3 V vs 5 V, why we stay at 3.3 V).
Worked examples: (1) NMOS + resistor inverter `.dc` transfer curve → noise-margin reading;
(2) CMOS inverter `.dc` — why it draws ~no static power; (3) 2N7000 driving a 12 V LED strip
from 3.3 V logic (gate drive check + high-side/low-side).
Figures: F1 MOSFET symbol/terminals; F2 S vs SR model; F3 inverter transfer curve with V_IL/
V_IH/V_OL/V_OH marked; F4 CMOS inverter + NAND structures; F5 switch driving a load
(low-side/high-side); F6 analog switch→digital abstraction bridge diagram.
Code listings: `nmos_inv.cir` + transfer data; `cmos_inv.cir` + output; `switch_load.cir` +
output.
Simulations: S1 inverter transfer curves (both); S2 power draw comparison NMOS-load vs CMOS;
S3 gate-drive sweep.
Exercises: 3 inline + 10 (4/4/2 incl. compute noise margins from a given curve, design NAND in
CMOS, reason about static power).
Safety: MOSFET gate ESD; high-current switching — why we simulate those and breadboard only
≤1 A.
Common mistakes: assuming a MOSFET conducts from gate voltage without checking V_th; swapping source and drain; forgetting the body diode.
Sources: MIT 6.002 L4–L9 (model ordering); AAC vol III.

### Ch7 — Op-amps and power supplies (12 pp, simulation + safety notes)
Prereq: ch6.
Sections: the op-amp contract (golden rules, negative feedback intuition); the three circuits
that cover 90 % of use — buffer, inverting, non-inverting; the comparator (with hysteresis
mention); where op-amps bite (rails, GBW, slew — awareness not design); regulators: linear
(LM7805, LDO) vs switching concept; USB power as the bench supply; decoupling revisited;
**mains power: why it stays boxed** (tripwire).
Worked examples: (1) non-inverting buffer for a weak sensor `.op`; (2) inverting amplifier
gain-of-10 with saturation shown in `.tran`; (3) comparator + RC = relaxation oscillator,
simulated (sets up the 555 in exercises).
Figures: F1 op-amp symbol and golden rules diagram; F2 the three configs side by side;
F3 saturating amplifier waveform; F4 comparator + hysteresis transfer; F5 regulator block
(9 V→7805→decoupling→load) circuitikz; F6 "inside a wall wart — admire, don't open" figure.
Code listings: `buffer.cir`; `inv_amp.cir` + saturation output; `comparator_osc.cir`.
Simulations: S1 buffer; S2 inverting amp + clipping; S3 relaxation oscillator frequency check.
Exercises: 3 inline + 10 (4/4/2 incl. gain sizing, a comparator threshold design, choosing
between LDO and buck given a current budget — reasoning exercise).
Safety: **mains chapter note — full box**: why 230 V (Indonesia) kills, never open adapters,
buy don't build; high-current USB packs and LiPo handling.
Common mistakes: applying the golden rules with inputs at the rails; forgetting decoupling capacitors; using an op-amp as a comparator without hysteresis.
Sources: AAC vol III op-amp chs; 6.002 L8–L12, L20+; AoE (cited for the reader's next step).

## 5. Part III — Digital logic

### Ch8 — Numbers, bits and Boolean algebra (11 pp, simulation-none; exercises on paper)
Prereq: ch6 (for the "where do gates come from" callbacks).
Sections: why two levels (back to noise margins); binary, hex, two's complement — the
programmer's refresher; truth tables; AND/OR/NOT/XOR and the universal gates; De Morgan;
simplification by algebra then by 2–3 var K-map; from expression to gate network.
Worked examples: (1) signed byte arithmetic three ways; (2) prove a simplification by truth
table then check by algebra; (3) derive the alarm circuit (door + ignition + seatbelt) into
minimal form.
Figures: F1 gate symbols table; F2 truth-table→K-map→expression pipeline; F3 K-map worked
figures (two); F4 universal-gate proofs visual; F5 the "same function three ways" schematic.
Code listings: `gates_tb.v` (behavioral gate truth printer — first Verilog sighting, read-only,
explained line by line, full syntax waits for ch11); its output table; a Python truth-table
checker used by exercises.
Simulations: none (SPICE); the Verilog truth-printer output stands in.
Exercises: 3 inline + 10 (4/4/2 incl. two's complement edge cases, De Morgan transforms,
minimal-SOP derivations; HDLBits "Getting Started"/basic gates named as external drills).
Safety: none.
Common mistakes: misreading place values on multi-digit binary; sign slips in two's complement; off-by-one on representable ranges.
Sources: AAC vol IV ch1–8; H&H ch1–2 (order + exercise style).

### Ch9 — Combinational circuits (11 pp, Verilog begins for real but pre-toolchain — paper+sim)
Prereq: ch8.
Sections: multiplexers and decoders as the two primitive "routers"; half/full adders;
ripple-carry adder and why it is slow (propagation delay, honestly first); comparators;
encoders/priority; ALU concept preview — the combinational heart of ch14; don't-cares in
real designs; from gates to a bus.
Worked examples: (1) build a 4-to-1 mux from gates, then from `assign` (shown, toolchain
formalised in ch11); (2) ripple adder carry-chain timing estimate vs a 2-level sum —
the speed/area trade in miniature; (3) seven-segment decoder truth table → minimal logic.
Figures: F1 mux tree; F2 full-adder gate map; F3 ripple carry annotated with delay;
F4 adder block diagram (CLA teaser, not built); F5 seven-segment map; F6 ALU symbol preview.
Code listings: `full_adder.v`; `adder4.v` + `adder4_tb.v`; `seg7.v` + truth-table output.
Simulations: S1 ripple adder vs expected sums (Icarus run, output printed); S2 seven-segment
truth dump.
Exercises: 3 inline + 10 (4/4/2 incl. design a priority encoder, subtractor from adder+2's
complement, count LUTs for a function).
Common mistakes: K-map adjacency errors (the edges wrap); incomplete truth tables feeding minimisation; treating don't-cares as fixed values.
Sources: H&H ch2, ch5; AAC vol IV combinational; fpga4fun adder examples (concept only).

### Ch10 — Sequential circuits and state machines (12 pp)
Prereq: ch9.
Sections: feedback and memory; SR latch → D latch → D flip-flop (edge vs level, the
transparent-latch trap shown in sim); setup and hold conceptually (not computed — that is
Book 7); registers and buses; counters (binary, then the useful ones: prescaler/enable);
finite state machines — Moore vs Mealy, the always-three-block style; metastability one
honest paragraph + "never clock a button into logic without two-flop sync" (used later).
Worked examples: (1) D-latch vs D-FF in simulation — the classic bug; (2) traffic-light FSM
end to end: state diagram → encoding → tables → Verilog; (3) a divider counter that makes a
1 Hz tick from 27 MHz (real board constraint ahead).
Figures: F1 latch vs FF timing figure (real VCD→pgfplots); F2 register/bus diagram; F3 counter
structure; F4 traffic FSM state diagram (TikZ); F5 Mealy vs Moore templates; F6 the two-flop
synchroniser.
Code listings: `dff.v` + `dff_tb.v` (latch bug demo); `counter.v` + tb; `traffic_fsm.v` + tb
with expected cycle trace.
Simulations: S1 latch transparency demo; S2 counter rollover; S3 FSM full-cycle trace.
Exercises: 3 inline + 10 (4/4/2 incl. pattern-detector FSM, Gray counter reasoning, the
"forgotten else → inferred latch" diagnosis exercise).
Common mistakes: latch vs flip-flop confusion; incomplete sensitivity lists; state machines containing unreachable states.
Sources: H&H ch3; AAC vol IV sequential; HDLBits FSM problems named.

## 6. Part IV — Verilog and FPGA

### Ch11 — Verilog I: describing hardware (13 pp, computer-only)
Prereq: ch10.
Sections: HDL is not a program — the mental reset; modules, ports, wires vs regs; `assign`
for combinational; `always @*` for combinational, `always @(posedge clk)` for sequential —
the two recipes; blocking vs non-blocking, one rule memorised + the why; parameters and
generate peek; the testbench as a module too; Icarus + GTKWave workflow; reading a waveform.
Worked examples: (1) the mux written four legal ways and two wrong ways (with the wrong-way
output shown); (2) counter + self-checking tb printing PASS/FAIL; (3) the traffic FSM from
ch10 re-coded in the book's style, waveform read line by line.
Figures: F1 module/port diagram; F2 the two always-block templates; F3 blocking vs
non-blocking timing cartoon; F4 GTKWave screenshot→annotated figure; F5 sim→wave pipeline.
Code listings: `mux4.v` (+ wrong-way listing w/ output); `counter2.v` + `counter2_tb.v`;
`tb_template.v`; Makefile sim targets.
Simulations: all of the above (Icarus).
Exercises: 3 inline + 10 (4/4/2 incl. predict-the-waveform checkpoints, fix-the-testbench,
write a tb for a given module; HDLBits language track named).
Common mistakes: writing software-style sequential Verilog; blocking vs non-blocking misuse; describing hardware you could not draw first.
Sources: chipverify topic order; HDLBits; Icarus docs (v13.0 notes: declare wires before use).

### Ch12 — Verilog II: testbenches and the classic bugs (10 pp, computer-only)
Prereq: ch11.
Sections: clocked testbench structure (clock gen, stimulus, check, report); `$display`,
`$finish`, `assert`-style checks; writing expectations as tables; Verilator `--lint-only` as
the grumpy reviewer; the hall of fame: inferred latches, off-by-one resets, width mismatches,
blocking-in-sequential, uninitialised state, X propagation, simulation-vs-synthesis lies;
reading warnings properly.
Worked examples: (1) a buggy FSM debugged end-to-end (lint → sim → fix, each output shown);
(2) golden-model testbench — Python generates vectors, tb checks them; (3) self-checking
random stimulus for the adder (seeded, reproducible).
Figures: F1 testbench anatomy diagram; F2 X-propagation waveform; F3 inferred-latch schematic
vs intent; F4 lint output annotated; F5 "sim says yes, hardware says no" cause map.
Code listings: `tb_clocked.v` template; `golden_vectors` Python + tb pair; `buggy_fsm.v` +
fixed version + outputs of each stage.
Simulations: every listing run; wrong outputs printed deliberately.
Exercises: 3 inline + 10 (4/4/2 incl. three find-the-bug problems, write a checker for a
decoder, lint a provided file).
Common mistakes: testbenches that only cover the happy path; not propagating or checking X; races inside the testbench itself.
Sources: Verilator docs; chipverify verification track; HDLBits tb-writing guidance.

### Ch13 — The FPGA flow: from text to silicon (12 pp, **needs board**)
Prereq: ch12.
Sections: what an FPGA is — LUTs, FFs, routing, BRAM, I/O; what the toolchain does —
synthesis→P&R→bitstream→program, each named with its tool (yosys `synth_gowin`,
nextpnr-himbaechel, gowin_pack, openFPGALoader); the constraint file (pins!); the Tang Nano 9K
tour (clock, LEDs, buttons, headers, HDMI teaser); blinky end-to-end with every command's
output shown; button+debounce (the two-flop sync from ch10 appears); where the vendor tools
sit (Gowin EDA — free but we use the open flow; noted honestly).
Worked examples: (1) blinky at 1 Hz from 27 MHz — code, .cst, full build log; (2) two buttons
AND-ed onto an LED — first real pin constraints; (3) the counter on LEDs, then sped up to
"too fast to see" → prescaler lesson reinforced by eye.
Figures: F1 FPGA fabric cartoon (LUT grid + routing + I/O banks); F2 tool-flow pipeline diagram
with real commands; F3 Tang Nano 9K pinout photo-map (drawn); F4 .cst annotated; F5 debounce
waveform.
Code listings: `blinky.v` + `tangnano9k.cst`; `buttons.v`; full Makefile `make prog` target;
build log excerpt.
Simulations: tb for blinky (shortened count) + hardware run.
Exercises: 3 inline + 10 (4/4/2 incl. PWM an LED, button-toggle with debounce, read the P&R
report's utilisation lines).
Safety: USB power only; board-level ESD; don't tie outputs together.
Common mistakes: ignoring timing-constraint warnings; assuming synthesis equals simulation; pin-assignment slips between constraint file and board.
Sources: apicula README/wiki (commands verified); oss-cad-suite docs; fpga4fun.

## 7. Part V — The machine (capstone C1)

### Ch14 — An 8-bit ALU (12 pp, board)
Prereq: ch11–13.
Sections: what an ALU is and the contract (inputs, op field, result, flags); choosing the op
set: add, sub, and, or, xor, shift-left, shift-right, compare — encoded in 3 bits; flags Z, N,
C, V — semantics defined before any code; the design: compute-all-then-mux; the testbench —
vector table + flag checks; onto the board: switches as operand, LEDs as result/flags.
Worked examples: (1) the adder path with carry-out and overflow — the flag truth table derived
not asserted; (2) subtract via A + ~B + 1, proven; (3) the full `alu8` module + tb + hardware
run (switches→LEDs).
Figures: F1 ALU block diagram; F2 op encoding table; F3 flag logic diagram; F4 compute-all-
then-mux structure; F5 board wiring figure (switches, LEDs); F6 waveform of a flag edge case.
Code listings: `alu8.v`; `alu8_tb.v` (+ vectors file); `top_alu9k.v` board wrapper + .cst;
Python vector generator.
Simulations: full tb; hardware: switch/LED demo.
Exercises: 3 inline + 10 (4/4/2 incl. add a fourth op, prove V flag for sub, a trap: what does
op field 111 currently do — define it).
Common mistakes: carry/overflow flag edge cases; ALU op-code off-by-ones; relying on power-up state instead of an explicit reset.
Sources: Nand2Tetris project 2 (contract style, not the ISA); H&H ch5.

### Ch15 — Registers, buses and the datapath (12 pp, board optional-in-parts)
Prereq: ch14.
Sections: the register file — write port, two read ports; the bus and who may drive it
(tri-state concept, mux reality); datapath vs control; a memory — RAM/ROM behavioural models,
what synthesises to BRAM; the cycle: fetch an instruction, move data, write back; assembling
datapath pieces around the ch14 ALU — now it is a processing element, not a calculator.
Worked examples: (1) 8×8 register file + tb; (2) ROM of instructions read by an address counter
— the program is data; (3) one full hand-traced cycle of the datapath moving a value through
the ALU — table of every control signal per step.
Figures: F1 register-file schematic; F2 bus/mux vs tri-state; F3 datapath block diagram
(the figure this book builds toward); F4 memory map of our tiny machine; F5 cycle-by-cycle
control-signal table-figure; F6 RAM/BRAM inference cartoon.
Code listings: `regfile8.v` + tb; `rom.v`/`ram.v` behavioural; `datapath.v` partial + tb.
Simulations: all tbs.
Exercises: 3 inline + 10 (4/4/2 incl. widen the register file, add a write-enable trace bug to
diagnose, compute minimum bits for a control word).
Common mistakes: bus contention from two simultaneous drivers; forgetting tri-state on shared buses; ignoring metastability on asynchronous inputs.
Sources: H&H ch5, ch7 (single-cycle datapath); Nand2Tetris projects 3–5 (ladder, not text).

### Ch16 — A small CPU that runs real programs (14 pp, board) **capstone C1 completion**
Prereq: ch15.
Sections: our ISA — 8 instructions: NOP, LDI, MOV, ADD, SUB, AND, JMP, JZ, OUT, HALT — encoding
table first (2×4-bit fields: opcode|reg|imm-variants); fetch–decode–execute as the master FSM;
the control unit — signal table → logic; the PC and branching; the OUT register to UART/LEDs;
the assembler: 60 lines of Python; program 1: count up forever; program 2: multiply by
repeated addition; program 3 (exercise): Fibonacci; **a short section mapping our 8-instruction
ISA onto a RISC-V RV32I subset** (LDI→addi/lui, MOV→addi rd,rs,0, ADD/SUB/AND→R-type, JMP→jal x0,
JZ→beq, OUT→store to a memory-mapped port, HALT→ebreak) so Book 7 lands as 'the same ideas,
done properly' (approved decision 6); what this CPU is missing (call stack, interrupts,
pipelining — honest list pointing to Book 7).
Worked examples: (1) trace three instructions through fetch-decode-execute by hand before
running; (2) assemble and run "count on the LEDs"; (3) Fibonacci mod-256 printed on UART.
Figures: F1 ISA encoding table; F2 the full datapath+control diagram (the book's centrepiece
figure); F3 control-FSM state diagram; F4 CPU board photo-map; F5 real UART trace/LED count;
F6 "what a pipelined version would look like" teaser.
Code listings: `cpu8.v` (the whole core, ~150 lines, in code/ not the page — page shows the
control unit listing); `cpu8_tb.v` + program ROM; `asm8.py` assembler; UART output listing.
Simulations: full-program tb (Fibonacci to 144 printed); hardware run.
Exercises: 3 inline + 10 (4/4/2 incl. add SUBI instruction end-to-end, write the multiply
program, find the control-table bug we plant).
Safety: none new.
Common mistakes: ISA encoding bugs that the assembler accepts silently; program-counter edge cases (jump to self, halt mid-fetch); a testbench that only ever runs one program.
Sources: Nand2Tetris projects 4–6 (sequence, not text); H&H ch7 (microarchitecture).

## 8. Part VI — The physical build

### Ch17 — Breadboards and the real bench (9 pp, **needs kit**)
Prereq: ch3–7 (it revisits them).
Sections: breadboard anatomy — rails, tie points, the ravine, why DIP straddles it (per the
SparkFun mechanism read in research); wiring that doesn't lie (layout habits); building three
circuits from Part II for real — divider, RC + LED fade, transistor switch; debugging with a
DMM: a method, not luck; when breadboards misbehave (contact resistance, long wires, stray
capacitance — honest limits); from breadboard to "permanent" — perfboard and the PCB bridge
to ch18.
Worked examples: (1) the divider measured at 3 points vs simulated — reconcile the numbers
(tolerance talk); (2) RC LED fade timed vs `.tran`; (3) debugging a planted bad build —
the measurement sequence.
Figures: F1 breadboard anatomy (annotated); F2 good vs bad wiring photos→drawn; F3 build
diagram for divider+LED; F4 measurement-points figure; F5 "same circuit: schematic, breadboard,
netlist" triptych.
Code listings: re-runs of `divider.cir`, `rc_fade.cir` with measured values substituted;
a comparison table listing.
Simulations: the three builds' netlists re-simulated at measured component values.
Exercises: 3 inline + 10 (4/4/2 incl. predict-then-measure checkpoints, tolerance-band
problems, a fault-tree exercise).
Safety: iron-safety defer note (we don't require soldering; if you do: rules); breadboard
current limits; recap of the low-voltage rule.
Common mistakes: floating inputs — the classic; missing pull-ups/pull-downs; split breadboard power rails; shared-ground assumptions across supplies.
Sources: SparkFun breadboard tutorial (mechanism); AAC vol VI Experiments; Platt (style of
build diagrams — ours are schematic-style, like his 3e).

### Ch18 — KiCad: from schematic to a two-layer sensor board (13 pp, computer; PCB order optional) **capstone C2**
Prereq: ch7, ch17.
Sections: the KiCad workflow — schematic → symbols → ERC → footprints → PCB → DRC → Gerbers;
the sensor board spec: LDO 5 V→3.3 V + TMP36-class analog sensor (or photodiode) + RC filter
+ header mating to the Tang Nano (ADC via the FPGA's external comparator? — honestly scoped:
sensor feeds a comparator/threshold, digital out to FPGA header); drawing the schematic;
assigning footprints (we stay 0805/DIP for hand-solderability); two-layer placement and
routing — pour GND, route the rest; DRC and the fab files; ordering (~US$5–15 + shipping —
unverified, date-stamped; alternatives: keep it as a design exercise); what to check when the
board arrives.
Worked examples: (1) the full schematic capture walkthrough; (2) placement rationale — keep
the sensor away from the LDO heat, short analog path; (3) running DRC on a deliberately
broken board → reading violations → fixing.
Figures: F1 workflow pipeline; F2 the board's schematic (the deliverable figure); F3 footprint
selection panel annotated; F4 two-layer stack diagram; F5 routed board front/back figure;
F6 Gerber→fab→assembly flow.
Code listings: exported netlist excerpt; DRC report excerpt; Gerber file listing (what each
layer file is).
Simulations: re-simulate the sensor RC filter + regulator in ngspice to sanity-check the real
BOM values.
Exercises: 3 inline + 10 (4/4/2 incl. add a mounting hole + keepout, reroute for a 1-oz-copper
current limit question, review a peer-style broken layout).
Safety: soldering safety (iron, fume, lead-free); LiPo if powering untethered (rules);
**mains recap — a power supply is bought, never built**.
Common mistakes: unconnected pins ERC flagged but ignored; schematic-footprint pinout mismatches; missing decoupling at ICs; trace width vs. current.
Sources: KiCad 10.0.7 official docs (version-stamped, verified 2026-10-10); AAC vol VI; SparkFun PCB tutorials.

### Ch19 — Microcontrollers and the road ahead (8 pp, read-only)
Prereq: ch16.
Sections: what a microcontroller is — the same CPU idea, shrink-wrapped; MCU vs FPGA — the
honest decision table (when each wins); the Arduino/hello-blink sketch (shown, not required);
the sensor board's natural MCU variant; pointers: RISC-V soft cores on the Tang Nano
(PicoRV32 exists — cited), Book 7 (pipelined RISC-V, caches, hazards), HDLBits as drills,
AoE/H&H as the next texts.
Worked examples: (1) decision exercise — pick MCU or FPGA for three stated products;
(2) the same debounce in C vs Verilog side by side; (3) reading a microcontroller datasheet's
front page honestly.
Figures: F1 MCU-vs-FPGA decision table figure; F2 soft-core-in-FPGA diagram; F3 the learning
map — where each of the eight books takes over.
Code listings: `blink.ino` (shown); `debounce` in C and Verilog side by side; PicoRV32
integration pointer listing.
Exercises: 3 inline + 8 (3/3/2; a lighter tail chapter by design).
Common mistakes: assuming MCU == FPGA; power and clock assumptions carried over from Arduino abstractions; treating library calls as the hardware truth.
Sources: MakerShed/Arduino material; PicoRV32 repo (cited); Book 7 brief (hand-off).

## 9. Appendices and back matter (~17 pp)

- App A — The toolkit and shopping list with rough prices (USD + IDR ranges, date-stamped,
  flagged unverified where applicable); where to buy in Indonesia.
- App B — Every netlist/testbench command in one place (the `make` targets).
- App C — The 8-bit ISA card + control-signal table (the ch16 reference card).
- Hints to all [hard] exercises; solutions to ≥50 % of exercises; numbered bibliography
  (~30 entries drawn from sources.md); index.

## 10. Cross-checks against the brief

- Seed coverage: V/I/R ch1–2 ✓; Kirchhoff ch3 ✓; C/L + RC/RL ch4 ✓; diodes ch5 + transistors
  ch6 ✓; op-amps + regulators/power ch7 ✓; Boolean ch8 ✓; combinational ch9 ✓; sequential/FSM
  ch10 ✓; Verilog+sim ch11–12 ✓; FPGA flow ch13 ✓; ALU ch14 ✓; datapath+CPU ch15–16 ✓;
  KiCad ch18 ✓; MCU ch19 ✓.
- Every circuit → ngspice netlist in `code/` (named per chapter) ✓.
- Every Verilog module → testbench + real waveform figure ✓.
- Safety: ch1 rules; ch4 flyback; ch6 high-current; ch7 + ch18 mains box; ch17 iron/battery ✓.
- Capstones: C1 = ch14–16 (ALU on board by ch14, full CPU by ch16); C2 = ch18 sensor board
  (two-layer, KiCad) ✓.
- Budget: one required purchase (Tang Nano 9K ~US$20); all else simulation or optional ✓.
