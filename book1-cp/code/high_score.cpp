// high_score.cpp -- CSES 1673 High Score: longest path 1->n where a
// positive cycle can make the score unbounded. Negate weights, run
// Bellman-Ford; vertices still relaxing in round n sit downstream of
// a negative cycle. -1 iff any such vertex can reach n.
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
using W = long long;
const W INF = (W)4e18;
struct Edge { int u, v, w; };

int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<Edge> E(m);
    vector<vector<int>> adj(n + 1);
    for (auto& e : E) {
        scanf("%d %d %d", &e.u, &e.v, &e.w);
        e.w = -e.w;                       // longest path via negation
        adj[e.u].push_back(e.v);
    }
    vector<W> d(n + 1, INF); d[1] = 0;
    vector<int> touched;
    for (int i = 0; i < n; i++) {
        touched.clear();
        for (auto& e : E)
            if (d[e.u] < INF && d[e.u] + e.w < d[e.v]) {
                d[e.v] = d[e.u] + e.w;
                touched.push_back(e.v);
            }
    }
    // `touched` = vertices relaxed in the n-th round: reachable from 1
    // AND downstream of a negative cycle. Any of them that reaches n
    // makes the answer unbounded.
    vector<char> bad(n + 1, 0);
    queue<int> q;
    for (int v : touched) if (!bad[v]) { bad[v] = 1; q.push(v); }
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) if (!bad[v]) { bad[v] = 1; q.push(v); }
    }
    printf("%lld\n", bad[n] ? -1 : -d[n]);
}
