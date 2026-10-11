# contam_demo.py -- the contamination mechanism as a runnable demo:
# a "model" that memorised the benchmark verbatim, then a paraphrased
# test set it never saw. The collapse is the mechanism.
import re

# the leaked benchmark: 60 QA items the model "trained on"
BENCH = [("what is 2+3?", "5"), ("capital of france?", "paris"),
         ("reverse 'abc'", "cba")] * 20

class Memoriser:
    """learns verbatim pairs only -- a stand-in for a contaminated
    model. generalises to nothing."""
    def __init__(self, pairs):
        self.mem = {q.strip().lower(): a for q, a in pairs}
    def answer(self, q):
        return self.mem.get(q.strip().lower(), "")

def paraphrase(q):
    """mechanical paraphrase: word-order variation + synonym swap."""
    swaps = {"what is": "tell me:", "capital": "main city",
             "reverse": "write backwards", "?": " please"}
    p = q.lower()
    for a, b in swaps.items():
        p = p.replace(a, b)
    return p

m = Memoriser(BENCH)
verbatim = sum(m.answer(q) == a for q, a in BENCH) / len(BENCH)
para = [paraphrase(q) for q, _ in BENCH]
para_acc = sum(m.answer(q2) == a for q2, (_, a) in zip(para, BENCH)) / len(BENCH)
print(f"verbatim benchmark accuracy:   {verbatim:.2f}  (the headline)")
print(f"paraphrased same items:        {para_acc:.2f}  (the truth)")
print(f"collapse: {verbatim - para_acc:.2f} of apparent skill was memory")
