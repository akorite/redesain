#!/usr/bin/env python3
"""ch18_expr.py -- a complete little compiler: integer expression -> code.

    python3 ch18_expr.py [--naive] [--fold] --target T "expression"

Targets:
  ast     print the syntax tree
  vm      bytecode for the 9-opcode stack VM (ch18_vmrun), as integers
  vmlist  the same bytecode, one mnemonic per line
  rv32    RISC-V assembly text, register-based, no stack at runtime
          (+ - use add/sub = RV32I; * / use mul/div = RV32M)
Flags:
  --fold   constant folding: evaluate constant subtrees at compile time
  --naive  WRONG on purpose: all operators same precedence, left to right
Grammar (precedence climbing, the standard fix for the naive version):
  expr   := term   (('+'|'-') term)*
  term   := factor (('*'|'/') factor)*
  factor := INTEGER | '(' expr ')'
"""
import re, sys

def tokenize(src):
    toks = re.findall(r"\d+|[-+*/()]|\S", src)
    for t in toks:
        if not (t.isdigit() or t in "+-*/()"):
            raise SyntaxError(f"unexpected character {t!r}")
    return toks

class Parser:
    def __init__(self, toks, naive=False):
        self.t, self.i, self.naive = toks, 0, naive
    def peek(self): return self.t[self.i] if self.i < len(self.t) else None
    def eat(self, want=None):
        tok = self.peek()
        if tok is None or (want and tok != want):
            raise SyntaxError(f"expected {want or 'token'}, got {tok!r}")
        self.i += 1; return tok
    def parse(self):
        n = self.expr()
        if self.peek() is not None: raise SyntaxError(f"trailing {self.peek()!r}")
        return n
    def binary(self, sub, ops):
        n = sub()
        while self.peek() is not None and self.peek() in ops:
            op = self.eat(); n = (op, n, sub())
        return n
    def expr(self):
        if self.naive:                       # every operator at one level
            return self.binary(self.factor, "+-*/")
        return self.binary(self.term, "+-")
    def term(self): return self.binary(self.factor, "*/")
    def factor(self):
        tok = self.peek()
        if tok == "(":
            self.eat("("); n = self.expr(); self.eat(")"); return n
        if tok is not None and tok.isdigit(): self.eat(); return int(tok)
        raise SyntaxError(f"expected a number or '(', got {tok!r}")

def apply(op, a, b):
    if op == "+": r = a + b
    elif op == "-": r = a - b
    elif op == "*": r = a * b
    else:
        if b == 0: raise ZeroDivisionError("division by zero")
        r = abs(a) // abs(b) * (1 if (a < 0) == (b < 0) else -1)   # C truncation
    if not -2**31 <= r < 2**31: raise OverflowError(f"{a} {op} {b} overflows int32")
    return r

def evaluate(n):
    return n if isinstance(n, int) else apply(n[0], evaluate(n[1]), evaluate(n[2]))

def fold(n):
    if isinstance(n, int): return n
    l, r = fold(n[1]), fold(n[2])
    return apply(n[0], l, r) if isinstance(l, int) and isinstance(r, int) else (n[0], l, r)

HALT, PUSH, ADD, SUB, MUL, DIV, DUP, OUT, JNZ = range(9)
OPC = {"+": ADD, "-": SUB, "*": MUL, "/": DIV}
NAMES = ["HALT", "PUSH", "ADD", "SUB", "MUL", "DIV", "DUP", "OUT", "JNZ"]

def gen_vm(n, out):                      # postorder walk = stack code
    if isinstance(n, int): out += [PUSH, n]
    else: gen_vm(n[1], out); gen_vm(n[2], out); out.append(OPC[n[0]])

TEMPS = ["t0", "t1", "t2", "t3", "t4", "t5", "t6"]
RVOP = {"+": "add", "-": "sub", "*": "mul", "/": "div"}
def gen_rv(n, free, out):                # returns the register holding the value
    if isinstance(n, int):
        if not free: raise RuntimeError("out of temporary registers (no spilling)")
        r = free.pop(0); out.append(f"        li   {r}, {n}"); return r
    ra = gen_rv(n[1], free, out); rb = gen_rv(n[2], free, out)
    out.append(f"        {RVOP[n[0]]:<4} {ra}, {ra}, {rb}"); free.insert(0, rb); return ra

def show(n):
    return str(n) if isinstance(n, int) else f"({show(n[1])} {n[0]} {show(n[2])})"

def main(argv):
    naive, dofold, target, src = False, False, "vm", None
    it = iter(argv)
    for a in it:
        if a == "--naive": naive = True
        elif a == "--fold": dofold = True
        elif a == "--target": target = next(it)
        else: src = a
    tree = Parser(tokenize(src), naive).parse()
    if dofold: tree = fold(tree)
    if target == "ast": print(show(tree)); print("value:", evaluate(tree))
    elif target in ("vm", "vmlist"):
        code = []; gen_vm(tree, code); code += [OUT, HALT]
        if target == "vm": print(*code)
        else:
            i = 0
            while i < len(code):
                if code[i] in (PUSH, JNZ): print(f"{i:3}  {NAMES[code[i]]} {code[i+1]}"); i += 2
                else: print(f"{i:3}  {NAMES[code[i]]}"); i += 1
    elif target == "rv32":
        out = []; r = gen_rv(tree, list(TEMPS), out)
        out.append(f"        addi a0, {r}, 0      # result in a0")
        print("\n".join(out))
    else: raise SystemExit(f"unknown target {target}")

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except (SyntaxError, ZeroDivisionError, OverflowError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr); sys.exit(1)
