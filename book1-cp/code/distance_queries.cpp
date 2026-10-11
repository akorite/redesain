#include "lca.h"
#include <cstdio>
int main() {
    int n, q; scanf("%d %d", &n, &q);
    vector<vector<int>> g(n+1);
    for (int i = 0; i < n-1; i++) { int a,b; scanf("%d %d",&a,&b);
        g[a].push_back(b); g[b].push_back(a); }
    LCA T(g);
    while (q--) { int a,b; scanf("%d %d",&a,&b);
        printf("%d\n", T.dist(a,b)); }
}
