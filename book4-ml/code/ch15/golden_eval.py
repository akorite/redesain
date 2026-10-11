# golden_eval.py -- a 30-item golden set for a toy QA task, a rubric
# scorer, and the prompt-regression diff table between two "prompt
# versions" (canned model behaviours -- the harness is what ships).
import json

GOLD = [
    # (prompt, expected, rubric): all answers checkable by rule
    ("reverse 'hello'", "olleh", "exact"),
    ("2+3*4", "14", "exact"),
    ("first letter of 'zebra'", "z", "exact"),
    ("count vowels in 'banana'", "3", "exact"),
    ("uppercase 'cat'", "CAT", "exact"),
    ("sort digits '312'", "123", "exact"),
    ("binary of 5", "101", "exact"),
    ("last char of 'apple'", "e", "exact"),
    ("square of 7", "49", "exact"),
    ("double 'ab'", "abab", "exact"),
    ("7 mod 3", "1", "exact"),
    ("is 11 prime (yes/no)", "yes", "exact"),
    ("hex of 255", "ff", "exact"),
    ("len of 'mississippi'", "11", "exact"),
    ("middle char of 'abcde'", "c", "exact"),
    ("abs of -4.5", "4.5", "exact"),
    ("repeat 'x' 4 times", "xxxx", "exact"),
    ("sqrt of 144", "12", "exact"),
    ("swap case 'Ab'", "aB", "exact"),
    ("10 // 4", "2", "exact"),
    ("strip spaces 'a b'", "ab", "exact"),
    ("min of [3,1,2]", "1", "exact"),
    ("'hello'[1]", "e", "exact"),
    ("ceil of 2.1", "3", "exact"),
    ("floor of 2.9", "2", "exact"),
    ("title-case 'hi there'", "Hi There", "exact"),
    ("first 3 of 'python'", "pyt", "exact"),
    ("last 3 of 'python'", "hon", "exact"),
    ("'xy' in 'xyzzy'", "yes", "exact"),
    ("8 in binary", "1000", "exact"),
]

# two simulated model behaviours: v1 gets most right but stumbles on
# index/reverse items; v2 fixes those but REGRESSES arithmetic.
def model_v1(prompt):
    buggy = {"reverse 'hello'", "'hello'[1]", "first 3 of 'python'"}
    wrong = {p: e for p, e, _ in GOLD}
    if prompt in buggy:
        return "WRONG"
    return wrong[prompt]

def model_v2(prompt):
    buggy = {"2+3*4", "10 // 4", "sqrt of 144", "8 in binary"}
    wrong = {p: e for p, e, _ in GOLD}
    if prompt in buggy:
        return "WRONG"
    return wrong[prompt]

def grade(resp, expected, rubric):
    return resp.strip() == expected

rows, n1, n2 = [], 0, 0
for p, e, r in GOLD:
    s1, s2 = grade(model_v1(p), e, r), grade(model_v2(p), e, r)
    n1 += s1; n2 += s2
    if s1 != s2:
        rows.append((p, 'PASS' if s1 else 'fail', 'PASS' if s2 else 'fail'))

print(f"v1 pass: {n1}/{len(GOLD)} = {n1/len(GOLD):.2f}")
print(f"v2 pass: {n2}/{len(GOLD)} = {n2/len(GOLD):.2f}")
print(f"diff {n2-n1:+d} items, but the TABLE matters:")
print(f"{'item':28s} {'v1':>4s} {'v2':>4s}")
for p, a, b in rows:
    print(f"{p:28s} {a:>4s} {b:>4s}")
print(f"\nregressions v1->v2: {sum(1 for _,a,b in rows if a=='PASS' and b=='fail')}"
      f"  fixes: {sum(1 for _,a,b in rows if a=='fail' and b=='PASS')}")
