# ch14_journal_sim.py -- crash a two-block "transfer" at every possible point,
# with and without a write-ahead journal, and check the invariant.
# Disk = dict of blocks.  A write() lands on disk immediately (we model the
# crash as "the machine stops before step k"); each step is one block write.
#   Transfer: move 10 from account block X (60) to Y (40).  Invariant: X+Y == 100.
import copy

START = {"X": 60, "Y": 40, "J": None}          # J = journal area (None = empty)

def plain_steps(d):
    return [lambda: d.__setitem__("X", 50),      # step 1: write X
            lambda: d.__setitem__("Y", 50)]      # step 2: write Y

def journal_steps(d):
    return [lambda: d.__setitem__("J", {"X": 50, "Y": 50, "commit": False}),  # 1: log the new values
            lambda: d["J"].__setitem__("commit", True),                       # 2: commit record
            lambda: d.__setitem__("X", 50),                                   # 3: checkpoint X
            lambda: d.__setitem__("Y", 50),                                   # 4: checkpoint Y
            lambda: d.__setitem__("J", None)]                                 # 5: clear the log

def recover(d):
    j = d["J"]
    if j and j["commit"]:                        # committed: replay (idempotent)
        d["X"], d["Y"] = j["X"], j["Y"]
    d["J"] = None                                # uncommitted or done: discard

def check(name, steps_fn, use_recovery):
    bad = 0
    n = len(steps_fn(copy.deepcopy(START)))
    for k in range(n + 1):                       # crash after k steps
        d = copy.deepcopy(START)
        for s in steps_fn(d)[:k]: s()
        if use_recovery: recover(d)
        ok = d["X"] + d["Y"] == 100
        bad += not ok
        print(f"  {name:8s} crash after step {k}: X={d['X']:2d} Y={d['Y']:2d} sum={d['X']+d['Y']:3d} {'ok' if ok else 'CORRUPT'}")
    return bad

b1 = check("plain", plain_steps, False)
b2 = check("journal", journal_steps, True)
print(f"corrupt states: plain={b1}, journal={b2}")
