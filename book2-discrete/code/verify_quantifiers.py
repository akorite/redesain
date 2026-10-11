# verify_quantifiers.py -- Chapter 1, Listing 1.1
# why: "for every x there is a y" and "there is a y for every x" are
# different claims. On a finite world both can be checked by brute force.

contestants = ["Ana", "Budi", "Citra", "Dewi"]
problems = ["P1", "P2", "P3", "P4"]


def verdicts(passed):
    # forall x exists y : every contestant has some solved problem
    fe = all(any(p in passed[c] for p in problems) for c in contestants)
    # exists y forall x : some single problem was solved by everyone
    ef = any(all(p in passed[c] for c in contestants) for p in problems)
    return fe, ef


def report(name, passed):
    fe, ef = verdicts(passed)
    print(name)
    print("  every contestant solved some problem :", fe)
    print("  some problem was solved by everyone  :", ef)


# world 1: each contestant solved exactly one, all different
w1 = {"Ana": {"P1"}, "Budi": {"P2"}, "Citra": {"P3"}, "Dewi": {"P4"}}
# world 2: everyone solved P1 and nothing else
w2 = {c: {"P1"} for c in contestants}
# world 3: Dewi solved nothing at all
w3 = dict(w1)
w3["Dewi"] = set()

report("world 1:", w1)
report("world 2:", w2)
report("world 3:", w3)
