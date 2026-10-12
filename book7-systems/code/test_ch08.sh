#!/bin/bash
# test_ch08.sh -- traps + MMIO UART: runs BOTH testbenches
#   ch08_soc_tb.v   : compute 6*7, MMIO bytes at the store, trap, mret
#   ch08_wire_tb.v  : decodes the bytes back from the tx wire alone
cd "$(dirname "$0")" || exit 1
set -e
SRC="ch08_rv32i_soc_top.v ch08_uart_tx.v ch05_rv32i_decode.v ch05_rv32i_regfile.v ch05_rv32i_alu.v"
OUT=${TMPDIR:-/tmp}
iverilog -o "$OUT/ch08_soc_tb" ch08_soc_tb.v $SRC
vvp "$OUT/ch08_soc_tb" > ch08_soc_tb.out 2>&1
iverilog -o "$OUT/ch08_wire_tb" ch08_wire_tb.v $SRC
vvp "$OUT/ch08_wire_tb" > ch08_wire_tb.out 2>&1
cat ch08_soc_tb.out ch08_wire_tb.out
grep -q "ran 770 cyc, pc=00000058, a2=42" ch08_soc_tb.out
grep -q "MMIO bytes sent: 42K!" ch08_soc_tb.out
grep -q "tx start-bit edges seen: 13" ch08_soc_tb.out
grep -q "^ch08 PASS" ch08_soc_tb.out
grep -q "decoded from tx wire: 42K!" ch08_wire_tb.out
grep -q "falling edges on tx=13" ch08_wire_tb.out
grep -q "^ch08 WIRE PASS" ch08_wire_tb.out
echo "ch08 core ok: 6*7=42, 42K! decoded off the wire, trap+mret round trip"
# --- delay-loop sweep: rewrite "li t1,60" (0x03c00313) to "li t1,N" and
# find the shortest delay that does not drop the second UART store.
sweep() {  # $1 = N ; prints number of frames decoded
  python3 - "$1" "$OUT/ch08_prog_n.hex" <<'PY'
import sys
n=int(sys.argv[1]); w=open("ch08_prog.hex").read().split()
w=["%08x"%((n<<20)|0x313) if x=="03c00313" else x for x in w]
open(sys.argv[2],"w").write("\n".join(w)+"\n")
PY
  vvp "$OUT/ch08_wire_tb" +hex="$OUT/ch08_prog_n.hex" | sed -n 's/^frames=\([0-9]*\) .*/\1/p'
}
f39=$(sweep 39); f40=$(sweep 40)
echo "delay sweep: N=39 -> $f39 frames, N=40 -> $f40 frames"
[ "$f39" = "2" ] && [ "$f40" = "4" ]
echo "ch08 PASS (all): wire decode, trap round trip, delay sweep (smallest safe delay N=40)"
