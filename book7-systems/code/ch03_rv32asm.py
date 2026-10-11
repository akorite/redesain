#!/usr/bin/env python3
"""ch03_rv32asm.py -- a two dozen-line RV32I assembler.
Encodes the RV32I subset taught in chapter 3 to real 32-bit words.
Usage: python3 ch03_rv32asm.py file.S  -> prints "addr: hex   # source"
"""
import sys, re

REG = {f"x{i}": i for i in range(32)}
REG.update({r: i for i, r in enumerate(
    "zero ra sp gp tp t0 t1 t2 s0 s1 a0 a1 a2 a3 a4 a5 a6 a7 "
    "s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 t3 t4 t5 t6".split())})

def R(f7, rs2, rs1, f3, rd, op):  return f7<<25 | rs2<<20 | rs1<<15 | f3<<12 | rd<<7 | op
def I(imm, rs1, f3, rd, op):      return (imm&0xFFF)<<20 | rs1<<15 | f3<<12 | rd<<7 | op
def S(imm, rs2, rs1, f3, op):     return ((imm>>5)&0x7F)<<25 | rs2<<20 | rs1<<15 | f3<<12 | (imm&0x1F)<<7 | op
def B(imm, rs2, rs1, f3, op):     return ((imm>>12)&1)<<31 | ((imm>>5)&0x3F)<<25 | rs2<<20 | rs1<<15 | f3<<12 | ((imm>>1)&0xF)<<8 | ((imm>>11)&1)<<7 | op

# name: (kind, f7, f3, opcode)
INS = {
  "add":  (R, 0x00, 0, 0x33), "sub":  (R, 0x20, 0, 0x33),
  "and":  (R, 0x00, 7, 0x33), "or":   (R, 0x00, 6, 0x33),
  "xor":  (R, 0x00, 4, 0x33), "sll":  (R, 0x00, 1, 0x33),
  "srl":  (R, 0x00, 5, 0x33), "slt":  (R, 0x00, 2, 0x33),
  "addi": (I, 0, 0, 0x13),    "andi": (I, 0, 7, 0x13),
  "ori":  (I, 0, 6, 0x13),    "xori": (I, 0, 4, 0x13),
  "slli": (I, 0, 1, 0x13),    "srli": (I, 0, 5, 0x13),
  "lw":   (I, 0, 2, 0x03),    "lb":   (I, 0, 0, 0x03),
  "sw":   (S, 0, 2, 0x23),    "sb":   (S, 0, 0, 0x23),
  "beq":  (B, 0, 0, 0x63),    "bne":  (B, 0, 1, 0x63),
  "blt":  (B, 0, 4, 0x63),    "bge":  (B, 0, 5, 0x63),
  "nop":  (None, 0, 0, 0),    # pseudoinstruction: addi x0,x0,0
  "lui":  ("U", 0, 0, 0x37),    "jal":  ("J", 0, 0, 0x6F),
  "jalr": ("JALR", 0, 0, 0x67), "j":    ("PJ", 0, 0, 0),
  "call": ("CALL", 0, 0, 0),    "ret":  ("RET", 0, 0, 0),
  "li":   ("LI", 0, 0, 0),    # pseudoinstruction: addi rd,x0,imm
}

def U(imm, rd, op):  return (imm & 0xFFFFF000) | (rd << 7) | op

def reg(s): return REG[s.strip().rstrip(",")]

def enc(mn, ops, pc, labels):
    kind, f7, f3, op = INS[mn]
    if kind is None:                            # nop
        return I(0, 0, 0, 0, 0x13)
    if kind == "U":                             # lui rd, imm20
        return U(int(ops[1], 0) << 12, reg(ops[0]), op)
    if kind == "LI":                            # li rd, imm -> addi
        return I(int(ops[1], 0), 0, 0, reg(ops[0]), 0x13)
    if kind == "J":                             # jal rd, label/imm
        imm = (labels[ops[1]] - pc) if ops[1] in labels else int(ops[1], 0)
        return (((imm >> 20) & 1) << 31 | ((imm >> 1) & 0x3FF) << 21 |
                ((imm >> 11) & 1) << 20 | ((imm >> 12) & 0xFF) << 12 |
                reg(ops[0]) << 7 | op)
    if kind == "JALR":                          # jalr rd, off(rs1)
        m = re.match(r"(-?\d+)\((\w+\d*)\)", ops[1])
        return I(int(m.group(1)), reg(m.group(2)), 0, reg(ops[0]), op)
    if kind == "PJ":                            # j label -> jal x0,label
        imm = labels[ops[0]] - pc
        return (((imm >> 20) & 1) << 31 | ((imm >> 1) & 0x3FF) << 21 |
                ((imm >> 11) & 1) << 20 | ((imm >> 12) & 0xFF) << 12 | 0x6F)
    if kind == "CALL":                          # call label -> jal ra,label
        imm = labels[ops[0]] - pc
        return (((imm >> 20) & 1) << 31 | ((imm >> 1) & 0x3FF) << 21 |
                ((imm >> 11) & 1) << 20 | ((imm >> 12) & 0xFF) << 12 |
                1 << 7 | 0x6F)
    if kind == "RET":                           # ret -> jalr x0,0(ra)
        return I(0, 1, 0, 0, 0x67)
    if kind is R:
        return R(f7, reg(ops[2]), reg(ops[1]), f3, reg(ops[0]), op)
    if kind is I:
        if mn in ("lw", "lb"):                      # lw rd, off(rs1)
            m = re.match(r"(-?\d+)\((\w+\d*)\)", ops[1])
            return I(int(m.group(1)), reg(m.group(2)), f3, reg(ops[0]), op)
        return I(int(ops[2], 0), reg(ops[1]), f3, reg(ops[0]), op)
    if kind is S:
        m = re.match(r"(-?\d+)\((\w+\d*)\)", ops[1])
        return S(int(m.group(1)), reg(ops[0]), reg(m.group(2)), f3, op)
    if kind is B:
        tgt = labels[ops[2]]
        return B(tgt - pc, reg(ops[1]), reg(ops[0]), f3, op)
    raise ValueError(mn)

def assemble(lines):
    labels, prog = {}, []
    pc = 0
    for ln in lines:
        ln = re.sub(r"[;#].*$", "", ln).strip()
        if not ln: continue
        while True:
            m = re.match(r"^(\w+):\s*", ln)
            if not m: break
            labels[m.group(1)] = pc
            ln = ln[m.end():].strip()
            if not ln: break
        if ln:
            prog.append((pc, ln)); pc += 4
    out = []
    for pc, ln in prog:
        parts = ln.split(None, 1)
        mn = parts[0].lower()
        ops = [o for o in re.split(r"[,\s]+", parts[1].strip()) if o] if len(parts) > 1 else []
        out.append((pc, enc(mn, ops, pc, labels), ln))
    return out

if __name__ == "__main__":
    src = open(sys.argv[1]).read().splitlines() if len(sys.argv) > 1 else sys.stdin.read().splitlines()
    for pc, w, ln in assemble(src):
        print(f"{pc:08x}: {w:08x}   # {ln}")
