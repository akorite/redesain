// prim.h -- pq frontier MST; good when the graph is dense.
#include <functional>
#include <queue>
#include <vector>
using namespace std;
using W = long long;

inline W prim(int n, const vector<vector<pair<int,int>>>& g, int s = 1) {
    vector<char> seen(n + 1, 0);
    priority_queue<pair<int,int>, vector<pair<int,int>>,
                   greater<>> pq;
    W total = 0;
    seen[s] = 1;
    for (auto [v, w] : g[s]) pq.push({w, v});
    while (!pq.empty()) {
        auto [w, u] = pq.top(); pq.pop();
        if (seen[u]) continue;
        seen[u] = 1; total += w;
        for (auto [v, wv] : g[u])
            if (!seen[v]) pq.push({wv, v});
    }
    return total;
}
