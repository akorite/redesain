// closing_farm.cpp -- USACO-S Closing the Farm.
// Offline reversal: deletions replayed backwards are insertions.
// ans[i] = connected AFTER barn order[i] closes, i.e. the state
// holding only order[i+1..n-1]: evaluate comps BEFORE inserting.
#include "dsu.h"
int main() {
    int n; scanf("%d", &n);
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a, b; scanf("%d %d", &a, &b);
        g[a].push_back(b); g[b].push_back(a);
    }
    vector<int> order(n);
    for (auto& x : order) scanf("%d", &x);
    vector<char> alive(n + 1, 0), ans(n);
    DSU d(n);
    int comps = 0;
    for (int i = n - 1; i >= 0; i--) {
        ans[i] = (comps <= 1);            // after order[i] closed
        int v = order[i];                 // (empty set: vacuously YES)
        alive[v] = 1; comps++;
        for (int u : g[v])
            if (alive[u] && d.unite(u, v)) comps--;
    }
    for (int i = 0; i < n; i++) puts(ans[i] ? "YES" : "NO");
}
