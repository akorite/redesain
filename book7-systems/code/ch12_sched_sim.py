# ch12_sched_sim.py -- FIFO / SJF / STCF / RR / MLFQ on one job set.
# Reports average turnaround, average response, context switches.
# turnaround = finish - arrival;  response = first run - arrival.
import sys
JOBS = [("A", 0, 100), ("B", 10, 30), ("C", 20, 10), ("D", 30, 60)]

def simulate(jobs, pol, q=10):
    rem = {n: e for n, a, e in jobs}
    arr = {n: a for n, a, e in jobs}
    done, first = {}, {}
    t, cur, switches, order = 0, None, 0, []
    queue = []                       # RR ready queue / MLFQ levels below
    lvl = {n: 0 for n in rem}        # MLFQ level of each job
    QS = [10, 20, 40]                # MLFQ slice per level
    slice_used = 0
    last_boost = 0
    last_run = {}                    # MLFQ: when each job last ran
    while len(done) < len(jobs):
        ready = [n for n in rem if arr[n] <= t and n not in done]
        if not ready:
            t += 1; cur = None; continue
        if pol == "mlfq" and t - last_boost >= 100:
            for n in lvl: lvl[n] = 0
            last_boost = t; slice_used = 0
        # decide who runs this tick
        keep = cur in ready and pol in ("fifo", "sjf")       # non-preemptive
        if pol == "stcf":
            nxt = min(ready, key=lambda n: (rem[n], arr[n]))
        elif pol == "fifo" or pol == "sjf":
            if keep: nxt = cur
            else:
                key = (lambda n: arr[n]) if pol == "fifo" else (lambda n: (rem[n], arr[n]))
                nxt = min(ready, key=key)
        elif pol == "rr":
            for n in ready:                                  # new arrivals join the queue
                if n not in queue and n != cur: queue.append(n)
            if cur in ready and slice_used < q: nxt = cur
            else:
                if cur in ready and cur not in queue: queue.append(cur)
                nxt = queue.pop(0); slice_used = 0
        else:                                                # mlfq
            if cur in ready and slice_used < QS[lvl[cur]] and \
               all(lvl[n] >= lvl[cur] for n in ready):
                nxt = cur
            else:
                if cur in ready and slice_used >= QS[lvl[cur]]:
                    lvl[cur] = min(lvl[cur] + 1, len(QS) - 1)
                top = min(lvl[n] for n in ready)
                cands = [n for n in ready if lvl[n] == top]
                # round-robin inside a level: least recently run first
                nxt = min(cands, key=lambda n: (last_run.get(n, -1), arr[n]))
                slice_used = 0
        if nxt != cur:
            if cur is not None: switches += 1
            if not order or order[-1] != nxt: order.append(nxt)
        if nxt not in first: first[nxt] = t
        cur = nxt; slice_used += 1
        last_run[nxt] = t
        rem[nxt] -= 1; t += 1
        if rem[nxt] == 0: done[nxt] = t
    tat = sum(done[n] - arr[n] for n in done) / len(jobs)
    resp = sum(first[n] - arr[n] for n in first) / len(jobs)
    return tat, resp, switches, "".join(order)

def table(jobs, title):
    print(title)
    print(f"{'policy':6s} {'turnaround':>10s} {'response':>9s} {'switches':>8s}  first-run/slice order")
    for pol in ["fifo", "sjf", "stcf", "rr", "mlfq"]:
        tat, resp, sw, order = simulate(jobs, pol)
        print(f"{pol:6s} {tat:10.1f} {resp:9.1f} {sw:8d}  {order if len(order) <= 24 else order[:24] + '...'}")

if __name__ == "__main__":
    table(JOBS, "arrivals 0,10,20,30  (A=100 B=30 C=10 D=60)")
    print()
    table([(n, 0, e) for n, a, e in JOBS], "all arrive at t=0")
