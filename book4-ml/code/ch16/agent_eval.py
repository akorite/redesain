# agent_eval.py -- trajectory scoring for agent runs: success,
# steps, tool errors, cost per trace -- the agent version of ch15's
# eval loop. Traces come from react_minimal-style runs (here: a
# recorded battery of 8 scripted runs).
import json

RUNS = [
    dict(id=1, ok=True,  steps=4, tool_errors=0, tokens=520),
    dict(id=2, ok=True,  steps=6, tool_errors=1, tokens=910),
    dict(id=3, ok=False, steps=8, tool_errors=3, tokens=1400),  # loop
    dict(id=4, ok=True,  steps=3, tool_errors=0, tokens=440),
    dict(id=5, ok=False, steps=8, tool_errors=2, tokens=1350),  # loop
    dict(id=6, ok=True,  steps=5, tool_errors=0, tokens=680),
    dict(id=7, ok=True,  steps=7, tool_errors=1, tokens=1050),
    dict(id=8, ok=False, steps=2, tool_errors=0, tokens=210),  # bad Final
]

n = len(RUNS)
succ = sum(r['ok'] for r in RUNS)
loops = sum(1 for r in RUNS if r['steps'] >= 8)
toks = [r['tokens'] for r in RUNS]
cost = [t * 0.002 / 1000 for t in toks]   # fake $/tok for the table

print(f"{'run':>3} {'ok':>4} {'steps':>5} {'tool_err':>8}"
      f" {'tokens':>6} {'cost$':>7}")
for r, c in zip(RUNS, cost):
    print(f"{r['id']:>3} {str(r['ok']):>4} {r['steps']:>5} "
          f"{r['tool_errors']:>8} {r['tokens']:>6} {c:7.4f}")
print(f"\nsuccess rate {succ}/{n} = {succ/n:.2f}")
print(f"mean steps   {sum(r['steps'] for r in RUNS)/n:.1f}")
print(f"loop-terminations (>=8 steps): {loops} "
      f"-- all were failures" if loops else "none")
print(f"mean cost/run ${sum(cost)/n:.4f}; "
      f"cost-per-success ${sum(cost)/max(succ,1):.4f}")
print("note: run 8 'succeeded' cheaply -- it called Final at step 2 "
      "with a wrong answer; step-count alone won't catch that")
