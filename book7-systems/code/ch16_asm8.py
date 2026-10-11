#!/usr/bin/env python3
# ch16_asm8.py -- the C1 assembler: 60 lines, one pass per line.
# Usage: python3 ch16_asm8.py prog.asm > prog.hex
# Syntax: LABEL:, MNEMONIC [operand], ; comments. LDI/JMP/JZ take a
# number or a label (immediate byte follows the opcode).
import re, sys

OPS = {'NOP':0x0,'LDI':0x1,'MOV':0x2,'ADD':0x3,'SUB':0x4,'AND':0x5,
       'JMP':0x6,'JZ':0x7,'OUT':0x8,'HALT':0x9,'MOVA':0xA}
TWO = {'LDI','JMP','JZ'}                      # ops with an imm byte
REG = re.compile(r'[rR]([0-7])$')

def main():
    src = [l.split(';')[0].strip() for l in open(sys.argv[1])]
    src = [l for l in src if l]
    labels, pc, body = {}, 0, []
    for l in src:                             # pass 1: addresses
        if l.endswith(':'):
            labels[l[:-1]] = pc
        else:
            body.append(l)
            pc += 2 if l.split()[0] in TWO else 1
    out = []
    for l in body:                            # pass 2: bytes
        parts = l.replace(',', ' ').split()
        op = OPS[parts[0].upper()]
        operand = 0
        imm = None
        if len(parts) > 1:
            arg = parts[-1] if parts[0].upper() == 'LDI' else parts[1]
            m = REG.match(arg)
            if m: operand = int(m.group(1))
            elif arg in labels: imm = labels[arg]
            else: imm = int(arg, 0)
        out.append((op << 4) | operand)
        if parts[0].upper() in TWO:
            out.append(0 if imm is None else imm & 0xFF)
    print(' '.join(f'{b:02x}' for b in out))

main()
