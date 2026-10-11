#!/usr/bin/env python3
# ch14_alu8_vec_gen.py -- golden-model vector generator for ch14_alu8_tb.v.
# Emits one packed 31-bit vector per line into ch14_alu8_vectors.dat:
#   {op[2:0], a[7:0], b[7:0], y[7:0], z, n, c, v}  -> 8 hex digits/line.
# The flag rules are the chapter's contract, written once here and once in
# Verilog -- the testbench compares the two.

OPS = {"ADD": 0b000, "SUB": 0b001, "AND": 0b010, "OR": 0b011,
       "XOR": 0b100, "SHL": 0b101, "SHR": 0b110, "CMP": 0b111}

def golden(op, a, b):
    if op == OPS["ADD"]:
        full = a + b
        y, c = full & 0xFF, (full >> 8) & 1
        v = int((a >> 7) == (b >> 7) and (y >> 7) != (a >> 7))
    elif op in (OPS["SUB"], OPS["CMP"]):
        full = a + (b ^ 0xFF) + 1           # a - b, ARM-style C = no borrow
        y, c = full & 0xFF, (full >> 8) & 1
        v = int((a >> 7) != (b >> 7) and (y >> 7) != (a >> 7))
    elif op == OPS["AND"]:
        y, c, v = a & b, 0, 0
    elif op == OPS["OR"]:
        y, c, v = a | b, 0, 0
    elif op == OPS["XOR"]:
        y, c, v = a ^ b, 0, 0
    elif op == OPS["SHL"]:
        y, c, v = (a << 1) & 0xFF, (a >> 7) & 1, 0
    elif op == OPS["SHR"]:
        y, c, v = a >> 1, a & 1, 0
    z, n = int(y == 0), (y >> 7) & 1
    return y, z, n, c, v

def pack(op, a, b):
    y, z, n, c, v = golden(op, a, b)
    return (op << 28) | (a << 20) | (b << 12) | (y << 4) | \
           (z << 3) | (n << 2) | (c << 1) | v

# directed vectors: every op once, then the flag edge cases that bite
VECTORS = []
def add_vec(opname, a, b):
    VECTORS.append((OPS[opname], a, b))

# arithmetic basics
add_vec("ADD", 0x00, 0x00); add_vec("ADD", 0x01, 0x01)
add_vec("ADD", 0x55, 0xAA); add_vec("ADD", 0x42, 0x17)
# flag edge cases -- the rows the chapter derives by hand
add_vec("ADD", 0x7F, 0x01)   # signed overflow, V=1
add_vec("ADD", 0x80, 0x80)   # negative + negative -> 0, V=1, C=1
add_vec("ADD", 0xFF, 0x01)   # wraps to 0: Z=1, C=1
add_vec("ADD", 0x40, 0x40)   # +64 + +64 = -128 signed: V=1
add_vec("ADD", 0xC0, 0x40)   # mixed signs can never overflow: V=0, C=1
add_vec("SUB", 0x05, 0x03)   # no borrow: C=1
add_vec("SUB", 0x03, 0x05)   # borrow: C=0, N=1
add_vec("SUB", 0x00, 0x00)   # 0-0 = 0 but C=1 (no borrow happened)
add_vec("SUB", 0x80, 0x01)   # -128 - 1 = +127 signed: V=1
add_vec("SUB", 0x7F, 0xFF)   # +127 - -1 = +128 -> -128 signed: V=1
add_vec("SUB", 0x0A, 0x0A)   # equal operands: Z=1
# logic ops: C and V forced to 0
add_vec("AND", 0xF0, 0x0F); add_vec("AND", 0x55, 0xFF); add_vec("AND", 0xAA, 0xAA)
add_vec("OR",  0x50, 0x05); add_vec("OR",  0x00, 0x00); add_vec("OR",  0x80, 0x01)
add_vec("XOR", 0xFF, 0xFF); add_vec("XOR", 0xA5, 0x5A); add_vec("XOR", 0x3C, 0xC3)
# shifts: C catches the bit that falls off the end
add_vec("SHL", 0x01, 0x00); add_vec("SHL", 0x80, 0x00); add_vec("SHL", 0x55, 0x00)
add_vec("SHR", 0x02, 0x00); add_vec("SHR", 0x01, 0x00); add_vec("SHR", 0x80, 0x00)
# compare: same flags as subtract, result is the difference
add_vec("CMP", 0x05, 0x05); add_vec("CMP", 0x03, 0x09); add_vec("CMP", 0x80, 0x7F)

# pad to the bench's 64-deep memory so $readmemh has no x rows;
# the pad rows are real checks too (ADD 0 + 0)
while len(VECTORS) < 64:
    VECTORS.append((OPS["ADD"], 0x00, 0x00))

with open("ch14_alu8_vectors.dat", "w") as f:
    for op, a, b in VECTORS:
        f.write(f"{pack(op, a, b):08x}\n")

print(f"wrote {len(VECTORS)} vectors to ch14_alu8_vectors.dat")
for name in OPS:
    n = sum(1 for op, _, _ in VECTORS if op == OPS[name])
    print(f"  {name}: {n} vectors")
