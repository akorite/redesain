#!/usr/bin/env python3
"""ch05_golden.py -- reference ("golden") model for the Verilog cores.
Usage: python3 ch05_golden.py prog.S prog.hex
 * assembles prog.S with the book's ch03 assembler,
 * writes prog.hex (64 words, padded with nops) for $readmemh,
 * runs the ch03 instruction-set simulator on the program (everything
   before the final `halt: j halt`) and prints the final state in the
   same format as the Verilog testbenches:
       I=<instructions executed>  HALT=<byte address of the halt jal>
       x10=00000037 ...   (nonzero registers, ascending)
       m0=00000037 ...    (nonzero data words 0..15, ascending)
"""
import sys
from ch03_rv32asm import assemble
from ch03_rv32sim import CPU

class HCPU(CPU):
    """Harvard variant: data lives at +0x1000 in the simulator's one
    dictionary, so stores never overwrite program text (the Verilog
    testbenches keep instruction and data memory separate too)."""
    def _ld(self, a): return CPU._ld(self, a + 0x1000)
    def _st(self, a, v): CPU._st(self, a + 0x1000, v)

src = open(sys.argv[1]).read().splitlines()
prog = assemble(src)
words = [w for _, w, _ in prog]
with open(sys.argv[2], "w") as f:
    for i in range(64):
        f.write("%08x\n" % (words[i] if i < len(words) else 0x13))
halt = 4 * (len(words) - 1)
cpu = HCPU(words[:-1]).run()          # stops when pc runs off the end
print("I=%d HALT=%d" % (cpu.steps, halt))
for r in range(1, 32):
    if cpu.x[r]:
        print("x%d=%08x" % (r, cpu.x[r] & 0xFFFFFFFF))
for m in range(16):
    v = cpu._ld(4 * m)
    if v:
        print("m%d=%08x" % (m, v))
