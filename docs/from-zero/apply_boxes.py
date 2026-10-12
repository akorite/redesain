#!/usr/bin/env python3
"""Insert 'Before you start' / 'After this chapter you can' boxes into chapters.

Usage: python3 docs/from-zero/apply_boxes.py   (run from repo root; idempotent)
Data lives in docs/from-zero/boxes_bookN.py as BOOK = {dir, files: {n: filename}, ch: {n: (before, can)}}.
"""
import importlib.util, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BEGIN, END = "% from-zero:begin", "% from-zero:end"

def render(before, can, think=None):
    out = [BEGIN]
    if before:
        out.append(r"\begin{rulebox}[Before you start]")
        out.append(before[0]); 
        if len(before) > 1:
            out.append(r"\begin{itemize}")
            out += [r"\item " + b for b in before[1:]]
            out.append(r"\end{itemize}")
        out.append(r"\end{rulebox}")
    out.append(r"\begin{wins}[After this chapter you can]")
    out.append(r"\begin{itemize}")
    out += [r"\item " + c for c in can]
    out.append(r"\end{itemize}")
    out.append(r"\end{wins}")
    if think:
        out.append(r"\begin{principle}[How to think about this]")
        out.append(think)
        out.append(r"\end{principle}")
    out.append(END)
    return "\n".join(out) + "\n\n"

def apply(book):
    d = ROOT / book["dir"]
    for n, (before, can) in sorted(book["ch"].items()):
        p = d / book["files"][n]
        s = p.read_text()
        s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n\n?", "", s, flags=re.S)
        m = re.search(r"^\\section\{", s, flags=re.M)
        if not m:
            print("NO SECTION", p); continue
        s = s[:m.start()] + render(before, can, book.get("think", {}).get(n)) + s[m.start():]
        p.write_text(s)

if __name__ == "__main__":
    for f in sorted((ROOT / "docs/from-zero").glob("boxes_book*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        t = f.with_name(f.name.replace("boxes_", "think_"))
        if t.exists():
            ts = importlib.util.spec_from_file_location(t.stem, t)
            tm = importlib.util.module_from_spec(ts); ts.loader.exec_module(tm)
            mod.BOOK["think"] = tm.THINK
        apply(mod.BOOK); print("applied", f.name)
