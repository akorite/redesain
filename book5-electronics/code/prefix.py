#!/usr/bin/env python3
"""prefix.py -- metric-prefix converter used in Chapter 1 exercises.

Given a value like 0.0047 it prints engineering notation (4.7 m).
Why: datasheets and meters never agree on the prefix; being able to
shift between them fluently is the first practical skill.
"""

PREFIXES = [
    (1e9, "G"), (1e6, "M"), (1e3, "k"),
    (1.0, ""), (1e-3, "m"), (1e-6, "u"), (1e-9, "n"), (1e-12, "p"),
]

def to_eng(value):
    """Format a plain number in engineering (prefix-aligned) notation."""
    if value == 0:
        return "0"
    for factor, sym in PREFIXES:
        if abs(value) >= factor:
            return f"{value / factor:g} {sym}".rstrip()
    return f"{value:g}"

if __name__ == "__main__":
    for v in [4700, 0.0047, 0.0000001, 20e-3, 3.3]:
        print(f"{v:g}  ->  {to_eng(v)}")
