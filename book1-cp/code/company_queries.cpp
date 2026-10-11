#include "lca.h"
#include <cstdio>
int main() {
    int n, q; scanf("%d %d", &n, &q);
    vector<vector<int>> g(n+1);
    for (int v = 2; v <= n; v++) { int b; scanf("%d",&b); g[b].push_back(v); }
    LCA T(g);
    while (q--) { int v, k; scanf("%d %d",&v,&k);
        printf("%d\n", T.kth(v,k) ? : -1); }
}
