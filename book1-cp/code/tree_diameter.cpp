#include "tree_diameter.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<vector<int>> g(n+1);
    for (int i = 0; i < n-1; i++) { int a,b; scanf("%d %d",&a,&b);
        g[a].push_back(b); g[b].push_back(a); }
    printf("%d\n", tree_diameter(g));
}
