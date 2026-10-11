"""euler_check.py -- connectivity + degree parity -> Eulerian trail check.

An undirected graph has:
  an Eulerian CIRCUIT iff connected and every degree is even;
  an Eulerian TRAIL   iff connected and exactly 0 or 2 odd degrees.
Pure-Python DFS, no libraries.
"""
import random


def components(n, adj):
    seen, comps = [False] * n, 0
    for s in range(n):
        if not seen[s] and adj[s]:
            comps += 1
            stack = [s]
            seen[s] = True
            while stack:
                for w in adj[stack.pop()]:
                    if not seen[w]:
                        seen[w] = True
                        stack.append(w)
    return comps


def euler_status(n, edges):
    # multigraph-aware: neighbors for connectivity, multiplicities for degrees
    nbr = [set() for _ in range(n)]
    deg = [0] * n
    for u, v in edges:
        nbr[u].add(v)
        nbr[v].add(u)
        deg[u] += 1
        deg[v] += 1
    odd = sum(d % 2 for d in deg)
    conn = components(n, nbr) <= 1
    if conn and odd == 0:
        return "Eulerian circuit"
    if conn and odd == 2:
        return "Eulerian trail (no circuit)"
    return "no Eulerian trail"


def main():
    konigsberg = [(0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (1, 3), (2, 3)]  # 7 bridges, degrees 5,3,3,3
    print("Konigsberg multigraph:", euler_status(4, konigsberg))
    cycle5 = [(i, (i + 1) % 5) for i in range(5)]
    print("5-cycle:", euler_status(5, cycle5))
    path4 = [(0, 1), (1, 2), (2, 3)]
    print("path of 4:", euler_status(4, path4))
    random.seed(7)
    n, edges = 6, set()
    while len(edges) < 8:
        u, v = random.sample(range(n), 2)
        edges.add((min(u, v), max(u, v)))
    print("random 6v/8e:", euler_status(n, sorted(edges)))


if __name__ == "__main__":
    main()
