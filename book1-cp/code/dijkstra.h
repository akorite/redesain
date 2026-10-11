// dijkstra.h -- single-source shortest paths, non-negative weights.
#include <functional>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

using W = long long;
const W INF = (W)4e18;

// g[u] = {v, w}; returns dist[] (INF = unreachable).
inline vector<W> dijkstra(int s, const vector<vector<pair<int,int>>>& g) {
    int n = g.size() - 1;
    vector<W> dist(n + 1, INF);
    priority_queue<pair<W,int>, vector<pair<W,int>>,
                   greater<pair<W,int>>> pq;
    dist[s] = 0; pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d != dist[u]) continue;          // stale entry
        for (auto [v, w] : g[u])
            if (d + w < dist[v]) {
                dist[v] = d + w;
                pq.push({dist[v], v});
            }
    }
    return dist;
}
