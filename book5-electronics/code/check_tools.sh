#!/bin/sh
# check_tools.sh -- verify the toolchain for this book is installed.
# Run: sh code/check_tools.sh
# Goal: every line says "found". Anything MISSING tells you what to install.

check() {
  # $1 = command to try, $2 = version flag, $3 = what it is for
  if command -v "$1" >/dev/null 2>&1; then
    ver=$("$1" $2 2>/dev/null | grep -m1 -E "[0-9]" | head -n 1)
    printf 'found    %-22s %s\n' "$1" "$ver"
  else
    printf 'MISSING  %-22s %s\n' "$1" "$3"
  fi
}

check iverilog    -V        "Verilog simulation (ch11+)"
check verilator   --version "lint / fast simulation (ch12+)"
check yosys       -V        "synthesis (ch13+)"
check nextpnr-himbaechel --version "place-and-route, Gowin (ch13+)"
check gowin_pack  --help    "bitstream packer, Gowin (ch13+)"
check openFPGALoader --Version  "programming the board (ch13+)"
check gtkwave     --version "viewing waveforms (ch11+)"
check ngspice     --version "analog simulation (ch2+)"
check kicad-cli   version   "PCB work (ch18)"
check python3     --version "scripts and vector generators"

echo "----"
echo "Missing tools come from the OSS CAD Suite (FPGA tools) and your"
echo "package manager (ngspice, KiCad). See code/README.md for versions."
