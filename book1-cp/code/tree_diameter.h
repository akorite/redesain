// tree_diameter.h -- two-DFS diameter: farthest from anywhere is an end.
#include <queue>
#include <vector>
using namespace std;

inline pair<int,vector<int>> farthest(int s, const vector<vector<int>>& g) {
    int n = g.size() - 1;
    vector<int> dist(n + 1, -1);
    queue<int> q; q.push(s); dist[s] = 0;
    int far = s;
    while (!q.empty()) {
        int v = q.front(); q.pop();
        if (dist[v] > dist[far]) far = v;
        for (int u : g[v]) if (dist[u] < 0) { dist[u] = dist[v]+1; q.push(u); }
    }
    return {far, dist};
}
inline int tree_diameter(const vector<vector<int>>& g) {
    int a = farthest(1, g).first;           // one endpoint
    auto [b, dist] = farthest(a, g);        // other endpoint + dists
    return dist[b];
}
