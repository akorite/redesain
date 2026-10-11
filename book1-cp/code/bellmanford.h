// bellmanford.h -- n-1 relaxation rounds; negative-cycle detect + rebuild.
#include <utility>
#include <vector>
using namespace std;
using W = long long;
const W BF_INF = (W)4e18;

struct Edge { int u, v; int w; };

// fills `cycle` with one negative cycle anywhere in the graph if any
// (all-zero seed = implicit super-source; seed s alone instead to
// restrict to cycles reachable from s). dist[] is 0 when none exists.
inline vector<W> bellmanford(int n, int s, const vector<Edge>& E,
                             vector<int>& cycle) {
    (void)s;
    vector<W> dist(n + 1, 0);
    vector<int> par(n + 1, -1);
    int x = -1;
    for (int i = 0; i < n; i++) {
        x = -1;
        for (auto [u, v, w] : E)
            if (dist[u] < BF_INF && dist[u] + w < dist[v]) {
                dist[v] = max(dist[u] + w, -BF_INF);
                par[v] = u;
                x = v;
            }
    }
    if (x < 0) return dist;                   // no negative cycle
    for (int i = 0; i < n; i++) x = par[x];   // walk into the cycle
    for (int v = x;; v = par[v]) {
        cycle.push_back(v);
        if (v == x && cycle.size() > 1) break;
    }
    reverse(cycle.begin(), cycle.end());
    return dist;
}
