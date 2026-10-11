# Sources — textbook-electronics (Wave 1 research log)

All entries accessed 2026-10-10. "Read" means the page content was actually opened and read
(fetched page or full search-result extract); a failed fetch is marked as such, never invented.
Nothing is copied; entries say what was taken (idea / topic order / exercise type / fact).

## Anchors

| URL / ISBN | Accessed | Licence | What was taken |
|---|---|---|---|
| https://www.allaboutcircuits.com/textbook/ | 2026-10-10 | Design Science License (DSL), Tony R. Kuphaldt | Confirmed six-volume structure: DC, AC, Semiconductors, Digital, Reference, Experiments. Licence identified for citation. |
| https://www.allaboutcircuits.com/textbook/direct-current/ | 2026-10-10 | DSL | Topic order taken: concepts → Ohm's law → **safety as chapter 3** → metric prefixes → series/parallel → dividers + KVL/KCL → meters → network analysis (Thevenin/Norton/superposition) → batteries → conductors → capacitors → magnetism → inductors → RC/LR time constants. Key idea: SPICE simulation is introduced inside the *Ohm's law* chapter and reused thereafter — directly supports our "every circuit gets an ngspice run" rule. |
| https://www.allaboutcircuits.com/textbook/digital/ | 2026-10-10 | DSL | Topic order: numeration/binary → switches + contact bounce → gates → Boolean algebra → Karnaugh maps (incl. don't-care) → combinational → multivibrators → counters → shift registers (SISO/SIPO/PISO/ring) → digital-analog → principles of digital computing. Confirms: bounce/switch reality before abstraction; K-maps kept (we will teach 2–3 var only, algebra-first). |
| https://www.allaboutcircuits.com/textbook/semiconductors/ | 2026-10-10 | DSL | Partial TOC read (page truncated): amplifiers/active devices → solid-state theory → diodes → BJT → JFET (incl. LTspice sim page) onward. Taken: device theory presented as physics-lite before circuits; JFET/BJT before MOSFET in their order — we invert to MOSFET-first (reader's goal is CMOS/digital). |
| https://www.ibiblio.org/kuphaldt/electricCircuits/ | 2026-10-10 | DSL | Read via search-result extract: upstream "Lessons in Electric Circuits" home; edition/revision table (Vol I DC 5th ed., Vol IV Digital 4th ed., Vol VI Experiments 1st ed., minor revisions 2021–2023). Confirms canonical naming for bibliography. |
| https://www.nand2tetris.org/ and https://www.nand2tetris.org/course | 2026-10-10 | Free for non-profit use (Nisan/Schocken) | 12 projects, Part I hardware: 1 Boolean Logic → 2 Boolean Arithmetic → 3 Memory → 4 Machine Language → 5 Computer Architecture → 6 Assembler. Taken: the **gate→ALU→memory→CPU→assembler ladder built entirely in an HDL simulator**, zero hardware — our Part V mirrors this but in Verilog on a real FPGA. |
| https://pages.hmc.edu/harris/ddca/ddca2e.html and /ddcarv.html | 2026-10-10 | Companion pages, free materials | Thin pages; confirm companion site exists, EdX MOOCs for the RISC-V edition, errata contact. Chapter-level structure cross-checked via Elsevier companion (next row). |
| https://shop.elsevier.com/books/book-companion/9780123944245 (DDCA 2e companion) | 2026-10-10 | Free student materials | Read via search extract: hosts odd-numbered exercise solutions, lab materials, HDL files, lecture slides, chapter figure sets Ch1–Ch8. Taken: exercise-style model (concept + HDL exercises per chapter); HDL taught *after* combinational+sequential logic (their ch4) — validates our order. |

## Further comparable resources (§3B — well beyond the required 5)

| URL / ISBN | Accessed | Licence | What was taken |
|---|---|---|---|
| https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/syllabus/ and /pages/calendar/ | 2026-10-10 | CC BY-NC-SA 4.0 | Lecture order taken as evidence: KVL/KCL → nodal analysis → Thevenin/superposition → **digital abstraction at lecture 4** → MOSFET S/SR switch model → nonlinear → small-signal/amplifiers → C/L first-order → digital memory → second-order → sinusoidal steady state/impedance. Course uses Agarwal & Lang, *Foundations of Analog and Digital Electronic Circuits* (ISBN 9781558607354). Key takeaway: introduce the MOSFET-as-switch early — it is the bridge from analog to digital; our ch6 does exactly this. |
| https://artofelectronics.net/ | 2026-10-10 | Commercial (cite only) | AoE 3e facts: 1220 pp, 1470 figures, 90 oscilloscope screenshots, 80 tables ≈1650 real components. Taken: proof that figure-dense, real-part-number presentation is the right register for electronics; bibliography entry; ch5 covers "every circuit artifact" (used to justify our nonideal-effects remarks). |
| https://api.pageplace.de/preview/DT0400.9781680456851_A49421020/preview-9781680456851_A49421020.pdf | 2026-10-10 | Commercial preview | Make: Electronics 3e actual TOC read: Section One "The Basics" = Experiments 1–5 (battery/LED/resistor by discovery), Section Two "Switching" = relay experiments… ISBN 978-1-68045-687-5, US$34.99, released Fall 2021. Taken: **experiment-first sequencing** (burn an LED before theory) — we adopt "hardware checkpoint" boxes inside early chapters but stay theory+simulation-first because of reader budget. |
| https://www.makershed.com/products/make-electronics-3rd-edition-print | 2026-10-10 | Commercial | Confirms 3rd-edition changes (single-bus breadboards, schematic-style build diagrams, Arduino focus, new circuits: burglar alarm, dice, reaction timer). NOTE: Wikipedia and O'Reilly product pages failed to fetch — this plus the pageplace preview used instead. |
| https://openstax.org/details/books/university-physics-volume-2 | 2026-10-10 | CC BY 4.0 | Free calculus-based text; Vol 2 covers thermodynamics + electricity & magnetism (authors Ling/Moebs/Sanny). Taken: backup reference for E-field/potential derivations our physics-light ch1 and ch4 cite; example-style model (approach → work → check). |
| https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all | 2026-10-10 | CC BY-SA (learn.sparkfun) | Breadboard anatomy read in full: internal tie points, ravine/DIP channel, power rails (not cross-connected), rows/columns numbering, binding posts. Taken: exact mechanism we draw in ch17's breadboard anatomy figure + the "power rails not connected" tripwire. |
| https://www.fpga4fun.com/ | 2026-10-10 | Free tutorials | Read: project-driven FPGA learning (retro video, OPL2 sound, breakout). Taken: "one small real project per concept" model; HDMI output as a stretch goal on Tang Nano 9K's HDMI connector. |
| https://hdlbits.01xz.net/wiki/Main_Page | 2026-10-10 | Free | Exercise engine read: small Verilog problems, immediate sim feedback, topic order Getting Started → Verilog Language → Circuits (incl. FSMs, larger circuits), non-synthesizable testbench guidance, web Icarus runner. Taken: **exercise style** — tiny self-checking problems; our digital chapters cite HDLBits problem names as external drills. |
| https://www.chipverify.com/ | 2026-10-10 | Free tutorials (+browser lab) | Read: Verilog/SystemVerilog/digital-design tracks, Yosys+SkyWater synthesis lab, browser-based Icarus/Verilator. Taken: ordering of Verilog topics (data types → operators → always blocks → FSM coding); browser lab as zero-install fallback for readers. |

## Tool versions and target board (date-stamped facts for the book)

| URL / ISBN | Accessed | Licence | What was taken |
|---|---|---|---|
| https://github.com/steveicarus/iverilog/releases and https://steveicarus.github.io/iverilog/releases/v13-0-release-note.html | 2026-10-10 | GPLv2+ | **Icarus Verilog v13.0 released 2026-03-02** (v12.0 2025-06-11; snapshot s20251012). V13 note: wires must be declared before use. Version pinned for code/README.md. |
| https://github.com/verilator/verilator/tags | 2026-10-10 | LGPL-3.0/Perl | **Latest tag v5.050** (2026-10-10). Used for lint/static checks in ch12; version pinned. |
| https://github.com/YosysHQ/yosys/releases | 2026-10-10 | ISC | **Yosys v0.69 released Sep 2026** (0.68 Aug, 0.67 Jul…). Release notes confirm active Gowin support: "DSP inference for Gowin GW1N/GW2A", "hardware latch support for Gowin". Pinned. |
| https://github.com/YosysHQ/nextpnr/releases | 2026-10-10 | ISC | **nextpnr-0.8 latest release** (top of releases list; 0.5 Feb). Note: many users build from git; oss-cad-suite build pins a snapshot. |
| https://github.com/YosysHQ/apicula and wiki Nextpnr‐Himbaechel-Gowin | 2026-10-10 | MIT/ISC | Confirmed **Tang Nano 9K (GW1NR-LV9QN88PC6/I5, family GW1N-9C) supported** end-to-end: yosys `synth_gowin` → `nextpnr-himbaechel --vopt family=GW1N-9C --vopt cst=tangnano9k.cst` → `gowin_pack -d GW1N-9C` → openFPGALoader. Commands taken verbatim for ch13 worked example. |
| https://github.com/YosysHQ/oss-cad-suite-build/releases + README | 2026-10-10 | Mixed OSS | Daily builds; latest **2026-10-10**. Bundles yosys, nextpnr (ice40/ecp5/gowin/himbaechel), iverilog, verilator, GTKWave, Surfer, openFPGALoader, apicula. **One download = whole toolchain; this is the book's install path.** |
| https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/ and https://docs.kicad.org/10.0/en/introduction/introduction.html | 2026-10-10 | GPLv3 | **KiCad 10.0.0 released 2026-03-01**; manual tracks 10.0.7. New: design variants, local power symbols, lasso select, importers, length-tuning overhaul. Book targets KiCad 10.x, date-stamped. (9.0.9 2026-04-28 was last 9.0 bugfix.) |
| https://ngspice.sourceforge.io/news.html | 2026-10-10 | GPLv2 | **ngspice-47 released 2026-08-11** (46: 2026-03-29, 45: 2025-09-01). Pinned; .op/.dc/.tran/.ac analyses used throughout. |
| https://www.ubuy.co.id/id/product/7MJRSMMM2-… (Ubuy Indonesia, Tang Nano 9K) | 2026-10-10 | — | Tang Nano 9K listed "in stock" for Indonesia (price displayed in KWD on that listing — **IDR price unverified**). |
| https://staging.probots.co.in/sipeed-tang-nano-9k-… (India) + sistastore price history | 2026-10-10 | — | Street price **US$18–23** for Tang Nano 9K (bare board; kits with 1.14" LCD ~US$25–40). Specs confirmed: GW1NR-LV9, 8640 LUT4, 6480 FF, 468 Kb BSRAM, HDMI, 27 MHz xtal, USB-C BL702 JTAG/UART. |
| https://www.ftcelectronics.id/product/Olimex/ICE40HX1K-EVB and /ICE40UP5K-MDP-EVN | 2026-10-10 | — | Indonesian distributor pricing for iCE40 boards: Olimex iCE40HX1K-EVB ≈US$26.7; iCE40UP5K MDP-EVN ≈US$100 — confirms iCE40 route is 2–5× the Gowin board's cost here. |
| https://invoklab.com/product/de0-nano-fpga-development-and-education-kit/ | 2026-10-10 | — | Indonesian shop price check: Terasic DE0-Nano (Cyclone IV) Rp 4 650 000 — confirms classic Altera boards are ~10× budget; reject as target. |

| https://www.nand2tetris.org/project02 | 2026-10-11 | 200 | Hack ALU contract: zr/ng flag vocabulary (no C/V) — ours diverges deliberately to ARM-style Z N C V; compute-all-then-mux confirmed as canonical teaching structure. |
| https://pages.hmc.edu/harris/ddca/ | 2026-10-11 | 200 | H&H DDCA companion site (slides/lab PDFs); ch14 ALU + flag conventions follow its §5.2.4. |
| https://hdlbits.01xz.net | 2026-10-11 | 200 | Combinational arithmetic drills matching our adder/overflow idioms; linked for reader practice. |
| https://www.chipverify.com/tutorials/verilog | 2026-10-11 | 200 | Reference for case/mux and $readmemh testbench idioms used in ch14 listings. |
| https://en.wikipedia.org/wiki/Arithmetic_logic_unit | 2026-10-11 | 200 | Historical + terminology reference for ALU intro. |
| https://en.wikipedia.org/wiki/Two%27s_complement | 2026-10-11 | 200 | Second derivation of subtraction/overflow rules. |

| https://www.youtube.com/watch?v=QzWW-CBugZo | 2026-10-11 | oembed 200 | Ben Eater 8-bit register Part 1 (9:35): bus architecture + register transfers — ch15 watch-instead. |
| https://www.youtube.com/watch?v=fpnE6UAfbtU | 2026-10-11 | oembed 200 | CrashCourse #6 Registers and RAM (12:16): latch→regfile→RAM ladder — ch15 watch-instead. |
| https://www.nand2tetris.org/project03 | 2026-10-11 | 200 | Nand2Tetris project 3 (sequential logic): DFF→register→RAM ladder behind ch15 memory section. |
| https://www.nand2tetris.org/project05 | 2026-10-11 | 200 | Nand2Tetris project 5 (computer architecture): Hack CPU datapath/control-word conventions. |
| https://en.wikipedia.org/wiki/Datapath | 2026-10-11 | 200 | Terminology + taxonomy for datapath section. |
| https://en.wikipedia.org/wiki/Register_file | 2026-10-11 | 200 | Register-file port taxonomy (1W2R) reference. |

| https://www.youtube.com/watch?v=dXdoim96v5A | 2026-10-11 | oembed 200 | Ben Eater 8-bit CPU control logic Part 1 (27:52) — ch16 watch-instead. |
| https://www.youtube.com/watch?v=zltgXvg6r3k | 2026-10-11 | oembed 200 | CrashCourse #8 Instructions & Programs (10:36) — ch16 watch-instead. |
| https://www.coursera.org/learn/build-a-computer | 2026-10-11 | 200 | Nand2Tetris Part I Coursera course — ch16 FR. |
| https://en.wikipedia.org/wiki/Central_processing_unit | 2026-10-11 | 200 | CPU terminology — ch16 FR. |
| https://en.wikipedia.org/wiki/Instruction_cycle | 2026-10-11 | 200 | fetch-decode-execute vocabulary — ch16 FR. |

| https://www.youtube.com/watch?v=W6mixXsn-Vc | 2026-10-11 | oembed 200 | LeftyMaker breadboard tutorial (4:16) — ch17 watch-instead. |
| https://www.youtube.com/watch?v=SLkPtmnglOI | 2026-10-11 | oembed 200 | SparkFun multimeter howto (10:33) — ch17 watch-instead. |
| https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard | 2026-10-11 | 200 | Breadboard anatomy + layout — ch17 FR. |
| https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter | 2026-10-11 | 200 | DMM modes + probe method — ch17 FR. |
| https://en.wikipedia.org/wiki/Breadboard | 2026-10-11 | 200 | Spring-clip mechanics — ch17 FR. |

| https://www.youtube.com/watch?v=d9_-lQq8ShE | 2026-10-11 | oembed 200 | DIY Hideout KiCad beginner tutorial (23:37) — ch18 watch-instead. |
| https://www.youtube.com/watch?v=aVUqaB0IMh4 | 2026-10-11 | oembed 200 | Phil's Lab #65 KiCad STM32 PCB tutorial (1:40:05) — ch18 watch-instead. |
| https://docs.kicad.org/10.0/en/getting_started_in_kicad/getting_started_in_kicad.html | 2026-10-11 | 200 | Official KiCad 10 getting-started — ch18 FR. |
| https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad | 2026-10-11 | 200 | SparkFun KiCad guide — ch18 FR. |
| https://jlcpcb.com | 2026-10-11 | 200 | Budget fab for Gerber bundle — ch18 FR. |
| https://en.wikipedia.org/wiki/KiCad | 2026-10-11 | 200 | KiCad project scope — ch18 FR. |

| https://www.ibm.com/think/topics/fpga-vs-microcontroller | 2026-10-11 | 200 | IBM Think FPGA-vs-MCU explainer — ch19 FR. |
| https://docs.arduino.cc/built-in-examples/basics/Blink/ | 2026-10-11 | 200 | Arduino Blink canonical sketch — ch19 FR. |
| https://github.com/YosysHQ/picorv32 | 2026-10-11 | 200 | PicoRV32 RV32I soft core — ch19 FR. |
| https://hdlbits.01xz.net | 2026-10-11 | 200 | HDLBits Verilog drills — ch19 FR. |
| https://en.wikipedia.org/wiki/Microcontroller | 2026-10-11 | 200 | MCU definition — ch19 FR. |
| https://www.youtube.com/watch?v=i1ObzbkVfSA | 2026-10-11 | oembed 200 | Uplatz FPGA-vs-MCU (7:48) — ch19 watch-instead. |
| https://www.youtube.com/watch?v=iHg0mmIg0UU | 2026-10-11 | oembed 200 | Charles Clayton "What's an FPGA?" (1:25) — ch19 watch-instead. |

## Decisions the research drove

1. **Target board: Sipeed Tang Nano 9K** (Gowin GW1NR-9). ~US$20, USB-C programmable, fully supported by open-source flow (yosys `synth_gowin` + nextpnr-himbaechel + gowin_pack + openFPGALoader — all in oss-cad-suite), 8640 LUTs is enough for the 8-bit CPU capstone, HDMI/LEDs/buttons onboard for visible output. iCE40 alternative is 2–5× price in-region for less logic; Altera/DE boards ~10×. Indonesian availability: Ubuy-ID listing live + routine marketplace imports; exact IDR street price left **unverified** (flag for the outline).
2. **Toolchain pinned (2026-10-10):** oss-cad-suite daily build (contains iverilog v13.0, verilator v5.050, yosys v0.69, nextpnr-himbaechel 0.8+, apicula, openFPGALoader, GTKWave); ngspice-47; KiCad 10.0.x.
3. **Sequencing (per §3B comparison):** analog fundamentals → devices → digital → HDL → FPGA → machine → physical build, mirroring AAC+H&H. From 6.002: MOSFET-as-switch taught *before* op-amps and used as the explicit bridge into the digital abstraction. From Platt: hands-on checkpoints early (but hardware optional). From Nand2Tetris: the whole Part V ladder is simulation→FPGA, no soldering needed.
4. **Exercise style:** AAC worked examples + HDLBits-style tiny self-checking Verilog problems + Nand2Tetris interface contracts ("build X, the test bench must pass").
