// bfs.h -- breadth-first search: layers = unweighted distance.
// dist[] = shortest edge count from s (-1 unreachable); parent[] for
// path reconstruction.
#pragma once
#include <queue>
#include <vector>

struct BFS {
    std::vector<int> dist, parent;
    BFS(const std::vector<std::vector<int>>& g, int s)
        : dist(g.size(), -1), parent(g.size(), -1) {
        std::queue<int> q;
        dist[s] = 0; q.push(s);
        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (int w : g[v])
                if (dist[w] < 0) {
                    dist[w] = dist[v] + 1; parent[w] = v; q.push(w);
                }
        }
    }
};
