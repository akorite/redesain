#include "reroot.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<vector<int>> g(n+1);
    for (int i = 0; i < n-1; i++) { int a,b; scanf("%d %d",&a,&b);
        g[a].push_back(b); g[b].push_back(a); }
    vector<int> down, up;
    reroot(g, 1, down, up);
    for (int i = 1; i <= n; i++)
        printf("%d%c", max(down[i], up[i]), " \n"[i==n]);
}
