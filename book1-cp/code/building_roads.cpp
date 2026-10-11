#include "dsu.h"
int main() {
    int n, m; scanf("%d %d", &n, &m);
    DSU d(n);
    while (m--) {
        int a, b; scanf("%d %d", &a, &b);
        d.unite(a, b);
    }
    vector<int> roots;
    for (int v = 1; v <= n; v++)
        if (d.find(v) == v) roots.push_back(v);
    printf("%d\n", (int)roots.size() - 1);
    for (int i = 1; i < (int)roots.size(); i++)
        printf("%d %d\n", roots[i - 1], roots[i]);
}
