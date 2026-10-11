import re
demo = """## Findings
SMA(20,60) Sharpe +0.28 on 721 bars (run_sma.py, 5bp/2bp).
2024 slice Sharpe +4.08 (yearly_sharpe.py).
The edge is robust across regimes.
Kelly f* = 0.10 (kelly_sims.py).
"""
num = re.compile(r"[+\-]?\d+\.\d+|[+\-]\d+%")
qual = re.compile(r"\b(robust|significant|consistent|stable|strong)\b", re.I)
prov = re.compile(r"\([^\)]*\.py[^\)]*\)")
print("memo lint: claims and their provenance")
ok=0; bad=[]
for i,l in enumerate(demo.splitlines()):
    needs = bool(num.search(l) or qual.search(l))
    if not needs: continue
    has = bool(prov.search(l))
    ok += has
    tag = "OK  " if has else "MISS"
    print(f"  line {i}: {tag} {l.strip()[:72]}")
    if not has: bad.append(i)
print(f"{ok}/{ok+len(bad)} claims cite a script")
for i in bad: print(f"  FIX line {i}: 'robust' is a claim -- attach the regime table or delete the word")
