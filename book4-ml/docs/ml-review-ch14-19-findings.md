# Re-review findings — textbook-electronics ch14–19 (ml session, 2026-10-11)

Independent depth-pass verification of elec-0006's six merged chapters.
Scope: NEW content only — sim math/Verilog live-run under iverilog-13 +
ngspice-47, FR URLs curled, Watch videos oEmbed+duration verified,
contract counts vs docs/decisions.md floor (≥5 WEs / ≥6 figs in visual
topics / ≥15 exercises).

## Verified live (all chapters)

- `test_ch14.sh` PASS: 64-vector ALU tb + **131,072-vector exhaustive**
  PASS; flag semantics spot-verified against sim rows (0x7f+0x01→
  n=1,v=1; 0x80+0x80→z=1,c=1,v=1; SUB carry = not-borrow, ARM-style —
  internally consistent).
- `test_ch15.sh` PASS: regfile8 12 checks, rom16+ram16 8 checks,
  datapath 8 control-word steps — all live.
- `test_ch16.sh` PASS: cpu8 prints Fibonacci 1..144 then halts (12 OUT
  bytes, pc=14); mult prints 7*6=42; uart RX decodes 0x39.
  CLKS_PER_BIT=234 math verified (27e6/115200 = 234.375 — chapter
  honestly prints the 115,384 Hz / 0.16% error). "302 cells" claim
  matches `ch16_cpu8_synth.out` verbatim. Hint arithmetic verified
  (10-bit frame = 87µs → ~11.5 kHz max OUT rate; div[21] ≈ 6 Hz).
- `test_ch18.sh` PASS: ngspice fc = 1.59226 kHz vs theory 1.5915 kHz
  (chapter says "within 0.1%" — true); gerbers + drill written; DRC
  0 violations.
- ch17 decks (no test script — ran manually): `divider_measured.cir`
  → V(2) = **3.352299 V**, matching quoted 3.352 V; `rc_fade` tau
  = 985·1.08µF = **1.064 ms** as quoted (+6.4% vs ideal). ch19 has no
  sims by design ("reading only").
- FR URLs: 44 unique \url{}s across ch14–19 — 41/44 curl-200; the 3
  403s (allaboutcircuits experiments, docs.arduino.cc Blink,
  nandland.com FPGA-vs-MCU) are Cloudflare bot-blocks — all confirmed
  real pages via fetcher and already recorded in docs/unverified.md.
- Watch: all 12 chapter rulebox videos verified live (oEmbed title +
  channel, approxDurationMs); every claimed duration within ±1 s of
  real; section-match annotations plausible (Ben Eater ALU/bus/control,
  CrashCourse #5/#6/#8, LeftyMaker, SparkFun DMM, Phil's Lab KiCad,
  DIY Hideout, Uplatz, Charles Clayton).
- \cite keys (ddca, tangnano9k, apicula) resolve to real bibitems.
- Contract blocks present in all six: Common mistakes, Summary table,
  Further reading, Watch rulebox, Hints and answers, \index{} terms,
  opening paragraph, \chapternotes{}.
- ch19 datasheet quotes verified: ATmega328 "20 MIPS @ 20 MHz, 32 KB
  flash, 2 KB SRAM, 1 KB EEPROM, 10-bit ADC, 6 PWM" — real values;
  "ten thousand times" = real 10k flash endurance; "three timers"
  (2×8b + 1×16b) correct.
- main.log: 0 overfull > 3pt, 0 undefined refs.

## Findings — floor observations for coordinator arbitration

1. **ch17 — worked examples = 3 < floor 5.** Chapters has 6 figures,
   23 exercises, 6 tripwire boxes, 1 checkpoint — dense with builds,
   but the example count itself is under the decisions.md floor.
   Author could promote two of {the divider build, the RC fade build,
   the transistor-switch build} into full `example` environments, or
   leave as-is if the breadboard chapter's build-walkthroughs are
   counted as the WE equivalent. Coordinator call.
2. **ch18 — worked examples = 3 < floor 5.** Same shape: 6 figures,
   23 exercises, workflow-heavy. The schematic→layout→gerber walk
   functions as the worked example but isn't in `example` envs.
   Coordinator call.
3. **ch19 — exercises = 13 < floor 15; figures = 3.** The chapter
   declares itself reading-only ("no sims, no board, just judgment").
   The "≥6 figures in visual topics" floor may not apply to a closing
   chapter; the 13 < 15 exercise gap is the harder one. Two more
   decision/judgment exercises would close it. Coordinator call.

No REVISE blockers: every claimed number, URL, video, cite, and test
artifact verified real and reproducible.

## Verdicts

| ch14 The 8-bit ALU | ACCEPT — sims + flags live-verified, watch verified, counts at floor |
| ch15 Buses and the datapath | ACCEPT — 3 benches live-verified, watch verified, counts at floor |
| ch16 A small CPU that runs | ACCEPT — fib/mult/uart live-verified, baud + cell-count claims real, counts at floor |
| ch17 The breadboard and the real bench | ACCEPT — sims live-verified, watch verified; WE count 3 < 5 flagged |
| ch18 From schematic to a real board | ACCEPT — ngspice/gerber/DRC live-verified, watch verified; WE count 3 < 5 flagged |
| ch19 Microcontrollers and the road ahead | ACCEPT — datasheet quotes real, watch verified; exercise count 13 < 15 flagged |
