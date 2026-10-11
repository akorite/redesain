#include "kruskal.h"
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<KEdge> E(m);
    for (auto& e : E) scanf("%d %d %d", &e.u, &e.v, &e.w);
    vector<KEdge> mst;
    W total = kruskal(n, E, &mst);
    if ((int)mst.size() < n - 1) { puts("IMPOSSIBLE"); return 0; }
    printf("%lld\n", total);
}
