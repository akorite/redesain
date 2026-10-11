// flight_discount.cpp -- CSES Flight Discount.
// Expanded graph: vertex (city, used-coupon?); Dijkstra over it.
#include "dijkstra.h"
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<vector<pair<int,int>>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        g[a].push_back({b, c});
    }
    // dist[v][u] : u=0 coupon unused, u=1 used.
    const W INF = (W)4e18;
    vector<array<W,2>> dist(n + 1, {INF, INF});
    using T = tuple<W,int,int>;
    priority_queue<T, vector<T>, greater<T>> pq;
    dist[1][0] = 0; pq.push({0, 1, 0});
    while (!pq.empty()) {
        auto [d, u, c] = pq.top(); pq.pop();
        if (d != dist[u][c]) continue;
        for (auto [v, w] : g[u]) {
            if (d + w < dist[v][c]) {
                dist[v][c] = d + w; pq.push({dist[v][c], v, c});
            }
            if (!c && d + w / 2 < dist[v][1]) {   // spend coupon
                dist[v][1] = d + w / 2; pq.push({dist[v][1], v, 1});
            }
        }
    }
    printf("%lld\n", dist[n][1]);
}
