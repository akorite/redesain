#include "dsu.h"
int main() {
    int n, m; scanf("%d %d", &n, &m);
    DSU d(n);
    int comps = n, biggest = 1;
    while (m--) {
        int a, b; scanf("%d %d", &a, &b);
        a = d.find(a); b = d.find(b);
        if (a != b) {
            if (d.sz[a] < d.sz[b]) swap(a, b);
            d.p[b] = a; d.sz[a] += d.sz[b];
            biggest = max(biggest, d.sz[a]);
            comps--;
        }
        printf("%d %d\n", comps, biggest);
    }
}
