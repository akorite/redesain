# ch08_truth_check.py -- compare Boolean expressions over named vars.
# Usage: python3 ch08_truth_check.py "I&D | I&~B" "I&(D|~B)"
# Prints every truth-table row, then EQUIVALENT or DIFFERENT (first counterexample).
import sys, itertools, re

def tokenize(s):
    return re.findall(r"[A-Za-z][A-Za-z0-9_]*|[&|^~()!]|&&|\|\|", s)

def to_py(tokens):
    out = []
    for t in tokens:
        if t in ("&", "&&"):  out.append(" and ")
        elif t in ("|", "||"): out.append(" or ")
        elif t == "^":         out.append(" != ")
        elif t in ("~", "!"):  out.append(" not ")
        elif t == "(":         out.append("(")
        elif t == ")":         out.append(")")
        else:                  out.append(t)
    return "".join(out)

def evaluate(expr, env):
    return bool(eval(to_py(tokenize(expr)), {}, env))

def main():
    exprs = sys.argv[1:]
    if len(exprs) < 1:
        sys.exit("usage: ch08_truth_check.py EXPR [EXPR2 ...]")
    names = sorted({t for e in exprs for t in tokenize(e)
                    if re.match(r"[A-Za-z]", t)})
    print("vars:", " ".join(names))
    header = " ".join(names) + " | " + "   ".join(exprs)
    print(header); print("-" * len(header))
    tables = []
    for bits in itertools.product([0, 1], repeat=len(names)):
        env = dict(zip(names, bits))
        row = [int(evaluate(e, env)) for e in exprs]
        tables.append(row)
        print(" ".join(str(b) for b in bits) + " |   "
              + "   ".join(str(r) for r in row))
    if len(exprs) > 1:
        for i, bits_row in enumerate(itertools.product([0, 1], repeat=len(names))):
            vals = tables[i]
            if len(set(vals)) > 1:
                print("DIFFERENT at", dict(zip(names, bits_row)))
                return
        print("EQUIVALENT on all", 2 ** len(names), "input rows")

if __name__ == "__main__":
    main()
