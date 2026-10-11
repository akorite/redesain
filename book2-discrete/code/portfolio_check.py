"""portfolio_check.py -- a proof-file linter, NOT a grader.

Scans .tex files for the elements a grader looks for:
  claim first    -- a theorem/lemma/proposition environment
  named lemmas   -- \begin{lemma} with a [Title]
  proof env      -- \begin{proof}
  qed            -- \qed or \end{proof} present
Reports MISSING items per file. Exit 0 always: lint, don't judge.
"""
import re
import sys
import glob

NEED = {
    "claim first": r"\\begin\{(theorem|lemma|proposition|claim)\}",
    "named lemma": r"\\begin\{lemma\}\[[^\]]+\]",
    "proof env":   r"\\begin\{proof\}",
    "qed":         r"\\qed",
}

def lint(path):
    text = open(path).read()
    missing = [name for name, pat in NEED.items() if not re.search(pat, text)]
    return missing

def main():
    files = sorted(glob.glob("sample_proofs/*.tex"))
    for f in files:
        miss = lint(f)
        if miss:
            print(f"{f}:")
            for m in miss:
                print(f"   missing: {m}")
        else:
            print(f"{f}: OK")

if __name__ == "__main__":
    main()
