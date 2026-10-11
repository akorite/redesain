#include "dijkstra.h"
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        g[a].push_back({b, c});
    }
    auto d = dijkstra(1, g);
    for (int i = 1; i <= n; i++)
        printf("%lld%c", d[i], " \n"[i == n]);
}
