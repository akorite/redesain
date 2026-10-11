// toposort.h -- Kahn's algorithm: repeatedly emit in-degree-0
// vertices. Leftover vertices <=> a directed cycle remains.
#pragma once
#include <queue>
#include <vector>

inline std::vector<int> kahn(const std::vector<std::vector<int>>& g) {
    int n = g.size();
    std::vector<int> deg(n), order;
    for (auto& nb : g) for (int w : nb) deg[w]++;
    std::queue<int> q;
    for (int v = 1; v < n; v++) if (deg[v] == 0) q.push(v);
    while (!q.empty()) {
        int v = q.front(); q.pop();
        order.push_back(v);
        for (int w : g[v]) if (--deg[w] == 0) q.push(w);
    }
    return order;   // size < n-1 iff cycle exists (index 0 unused)
}
