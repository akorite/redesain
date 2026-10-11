#!/usr/bin/env python3
"""ch03_rv32sim.py -- a tiny RV32I interpreter (the ch03 subset).
Executes words produced by ch03_rv32asm.py. Data memory: 4 KiB dict.
Writes to address 0x10000000 print a character (memory-mapped stdout,
the same trick Book 5 ch16's UART used).
Usage: python3 ch03_rv32sim.py file.hex   (hex = one 8-digit word per line)
"""
import sys
from ch03_rv32asm import assemble

MEM_SIZE = 4096
OUT = 0x10000000

def s32(x):  return x - (1 << 32) if x & 0x80000000 else x
def sext(v, n):  return v - (1 << n) if v & (1 << (n - 1)) else v

class CPU:
    def __init__(self, words):
        self.x = [0] * 32
        self.mem = {}
        for i, w in enumerate(words):
            self.mem[i * 4] = w            # text at address 0
        self.pc = 0
        self.out = []
        self.steps = 0

    def _ld(self, a):
        v = 0
        for b in range(4):
            v |= (self.mem.get(a + b, 0) & 0xFF) << (8 * b)
        return v

    def _st(self, a, v):
        if a == OUT:
            self.out.append(chr(v & 0xFF)); return
        for b in range(4):
            self.mem[a + b] = (v >> (8 * b)) & 0xFF

    def run(self, limit=100000):
        while self.steps < limit:
            w = self.mem.get(self.pc, None)
            if w is None or w == 0x00000013:      # nop / fall off
                break
            self.steps += 1
            op, rd, f3 = w & 0x7F, (w >> 7) & 0x1F, (w >> 12) & 7
            rs1, rs2, f7 = (w >> 15) & 0x1F, (w >> 20) & 0x1F, (w >> 25) & 0x7F
            immI = sext((w >> 20) & 0xFFF, 12)
            immS = sext(((w >> 25) << 5) | ((w >> 7) & 0x1F), 12)
            immB = sext((((w >> 31) & 1) << 12) | (((w >> 7) & 1) << 11) |
                       (((w >> 8) & 0xF) << 1) | (((w >> 25) & 0x3F) << 5), 13)
            npc = self.pc + 4
            if op == 0x6F:                      # jal
                immJ = sext((((w >> 31) & 1) << 20) | (((w >> 12) & 0xFF) << 12) |
                           (((w >> 20) & 1) << 11) | (((w >> 21) & 0x3FF) << 1), 21)
                self.x[rd] = self.pc + 4
                npc = (self.pc + immJ) & 0xFFFFFFFF
            elif op == 0x67:                    # jalr
                self.x[rd] = self.pc + 4
                npc = (self.x[rs1] + immI) & 0xFFFFFFFE
            elif op == 0x37:                      # lui
                self.x[rd] = w & 0xFFFFF000
            elif op == 0x33:                      # R-type
                a, b = self.x[rs1], self.x[rs2]
                if f3 == 0: self.x[rd] = (a + b if f7 == 0 else a - b) & 0xFFFFFFFF
                elif f3 == 7: self.x[rd] = a & b
                elif f3 == 6: self.x[rd] = a | b
                elif f3 == 4: self.x[rd] = a ^ b
                elif f3 == 1: self.x[rd] = (a << (b & 31)) & 0xFFFFFFFF
                elif f3 == 5: self.x[rd] = a >> (b & 31)
                elif f3 == 2: self.x[rd] = 1 if s32(a) < s32(b) else 0
            elif op == 0x13:                    # I-type alu
                a = self.x[rs1]
                if f3 == 0: self.x[rd] = (a + immI) & 0xFFFFFFFF
                elif f3 == 7: self.x[rd] = a & (immI & 0xFFFFFFFF)
                elif f3 == 6: self.x[rd] = a | (immI & 0xFFFFFFFF)
                elif f3 == 4: self.x[rd] = a ^ (immI & 0xFFFFFFFF)
                elif f3 == 1: self.x[rd] = (a << (immI & 31)) & 0xFFFFFFFF
                elif f3 == 5: self.x[rd] = a >> (immI & 31)
            elif op == 0x03:                    # loads
                a = (self.x[rs1] + immI) & 0xFFFFFFFF
                if f3 == 2: self.x[rd] = self._ld(a)
                elif f3 == 0: self.x[rd] = s32(self._ld(a) & 0xFF)
            elif op == 0x23:                    # stores
                a = (self.x[rs1] + immS) & 0xFFFFFFFF
                if f3 == 2: self._st(a, self.x[rs2])
                elif f3 == 0: self._st(a, self.x[rs2] & 0xFF)
            elif op == 0x63:                    # branches
                a, b = self.x[rs1], self.x[rs2]
                take = {0: a == b, 1: a != b,
                        4: s32(a) < s32(b), 5: s32(a) >= s32(b)}[f3]
                if take: npc = (self.pc + immB) & 0xFFFFFFFF
            else:
                raise ValueError(f"unimplemented op {op:#x} at {self.pc:#x}")
            self.x[0] = 0
            self.pc = npc
        return self

if __name__ == "__main__":
    words = [w for _, w, _ in assemble(open(sys.argv[1]).read().splitlines())]
    cpu = CPU(words).run()
    print("".join(cpu.out) or f"(no output; {cpu.steps} instructions retired)")
    print(f"# {cpu.steps} instructions retired", file=sys.stderr)
