# Code

All tool versions below were verified from official release pages on 2026-10-10.
Re-verify at each writing session and date-stamp changes.

## Pinned versions

| Tool | Pinned version | Install route | First used |
|---|---|---|---|
| Icarus Verilog (`iverilog`) | v13.0 (2026-03-02) | OSS CAD Suite | ch11 |
| Verilator | v5.050 | OSS CAD Suite | ch12 |
| Yosys | v0.69 (2026-09) | OSS CAD Suite | ch13 |
| nextpnr-himbaechel | 0.8 | OSS CAD Suite | ch13 |
| gowin_pack / apicula | with nextpnr | OSS CAD Suite | ch13 |
| openFPGALoader | (suite build) | OSS CAD Suite | ch13 |
| GTKWave | (suite build) | OSS CAD Suite | ch11 |
| ngspice | 47 (2026-08-11) | package manager | ch2 |
| KiCad (`kicad-cli`) | 10.0.7 | kicad.org | ch18 |
| Python | ≥3.9 | system | ch1 |

The FPGA flow (yosys `synth_gowin` → `nextpnr-himbaechel` → `gowin_pack` →
openFPGALoader) targets the Sipeed Tang Nano 9K (Gowin GW1NR-LV9) — see ch13.

## Layout

- `chNN/` holds the listings of chapter NN.
- `make test` runs `code/test_*.sh`; each checks the chapter's code works.
- `make figures` regenerates top-level `figures/*.py` outputs; chapter figure
  sources live in `figures/chNN/` and are TikZ/circuitikz (no regeneration
  needed — they compile with the document).
