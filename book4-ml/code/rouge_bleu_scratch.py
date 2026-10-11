# rouge_bleu_scratch.py -- BLEU (n-gram precisions + brevity penalty)
# and ROUGE-1/ROUGE-L implemented from scratch, then run on candidate
# summaries where the metrics and a human reader disagree.
import math
from collections import Counter

def ngrams(tokens, n):
    return Counter(tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1))

def bleu(cand, ref, max_n=4):
    c, r = cand.split(), ref.split()
    pns = []
    for n in range(1, max_n+1):
        cn, rn = ngrams(c, n), ngrams(r, n)
        match = sum((cn & rn).values())
        total = max(sum(cn.values()), 1)
        pns.append(match / total)
    bp = 1.0 if len(c) > len(r) else math.exp(1 - len(r)/max(len(c),1))
    return bp * math.exp(sum(math.log(max(p,1e-9)) for p in pns)/max_n)

def lcs_len(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = dp[i][j]+1 if a[i]==b[j] else max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

def rouge1(cand, ref):
    cs, rs = Counter(cand.split()), Counter(ref.split())
    return sum((cs & rs).values()) / max(sum(rs.values()), 1)

def rougeL(cand, ref):
    c, r = cand.split(), ref.split()
    return lcs_len(c, r) / max(len(r), 1)

REF = "the cat sat on the mat and slept peacefully all afternoon"
CAND_A = "the cat sat on the mat and slept all afternoon"   # faithful, terse
CAND_B = "the feline companion rested upon the woven surface" # fluent, wrong facts
CAND_C = "the cat the cat the cat sat sat sat on the mat the mat" # degenerate

print(f"reference : {REF}")
for name, c in [("A faithful-terse", CAND_A), ("B fluent-wrong", CAND_B),
                ("C degenerate-repeat", CAND_C)]:
    b, r1, rl = bleu(c, REF), rouge1(c, REF), rougeL(c, REF)
    print(f"{name}: BLEU {b:.3f}  ROUGE-1 {r1:.3f}  ROUGE-L {rl:.3f}")

# a second pair where metric and judgment diverge harder
REF2 = "the new drug reduced tumour growth by 40 percent in mice"
CAND_D = "the new drug reduced tumour growth by 40 percent in rats"  # one wrong word = wrong
CAND_E = "mice treated with the new drug showed 40 percent less tumour growth"
print(f"\nreference2: {REF2}")
for name, c in [("D one-token-error", CAND_D), ("E faithful-rephrase", CAND_E)]:
    b, r1, rl = bleu(c, REF2), rouge1(c, REF2), rougeL(c, REF2)
    print(f"{name}: BLEU {b:.3f}  ROUGE-1 {r1:.3f}  ROUGE-L {rl:.3f}")
