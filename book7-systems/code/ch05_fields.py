#!/usr/bin/env python3
"""ch05_fields.py -- split RV32I words into fields the way the decoder
and immediate generator do, and show what a WRONG choice of immediate
would give.  Usage: python3 ch05_fields.py prog.hex
Columns: address, word, format, mnemonic, rd/rs1/rs2, the immediate the
hardware uses (immI/immS/immB/immU/immJ chosen by opcode) and immI, the
immediate you would get by treating every word as I-type."""
import sys

def sext(v, n): return v - (1 << n) if v & (1 << (n - 1)) else v

def decode(w):
    op, rd, f3 = w & 0x7F, (w >> 7) & 31, (w >> 12) & 7
    rs1, rs2, f7 = (w >> 15) & 31, (w >> 20) & 31, w >> 25
    immI = sext(w >> 20, 12)
    immS = sext((f7 << 5) | rd, 12)
    immB = sext(((w >> 31) << 12) | (((w >> 7) & 1) << 11) |
                (((w >> 25) & 0x3F) << 5) | (((w >> 8) & 0xF) << 1), 13)
    immU = w & 0xFFFFF000
    immJ = sext(((w >> 31) << 20) | (((w >> 12) & 0xFF) << 12) |
                (((w >> 20) & 1) << 11) | (((w >> 21) & 0x3FF) << 1), 21)
    if op == 0x33: return "R", {0: "add/sub", 7: "and", 6: "or", 4: "xor",
        1: "sll", 5: "srl", 2: "slt"}[f3] if f3 != 0 else ("sub" if f7 else "add"), rd, rs1, rs2, None, immI
    if op == 0x13: return "I", {0: "addi", 7: "andi", 6: "ori", 4: "xori",
        1: "slli", 5: "srli", 2: "slti"}[f3], rd, rs1, None, immI, immI
    if op == 0x03: return "I", "lw", rd, rs1, None, immI, immI
    if op == 0x23: return "S", "sw", None, rs1, rs2, immS, immI
    if op == 0x63: return "B", {0: "beq", 1: "bne"}[f3], None, rs1, rs2, immB, immI
    if op == 0x37: return "U", "lui", rd, None, None, immU, immI
    if op == 0x6F: return "J", "jal", rd, None, None, immJ, immI
    raise ValueError("opcode %#x" % op)

def f(v): return "-" if v is None else str(v)

def main():
    print("addr word     fmt op     rd rs1 rs2  imm(used)    immI(wrong)")
    for i, line in enumerate(open(sys.argv[1])):
        line = line.strip()
        if not line: continue
        w = int(line, 16)
        fmt, name, rd, rs1, rs2, imm, wrong = decode(w)
        imm_s = "-" if imm is None else (hex(imm) if fmt == "U" else str(imm))
        print("%04x %08x  %s   %-6s %2s %3s %3s  %-12s %d" % (
            4 * i, w, fmt, name, f(rd), f(rs1), f(rs2), imm_s, wrong))


if __name__ == "__main__":
    main()
