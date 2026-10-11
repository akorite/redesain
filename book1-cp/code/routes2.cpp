#include "floyd.h"
int main() {
    int n, m, q; scanf("%d %d %d", &n, &m, &q);
    vector<vector<W>> d(n + 1, vector<W>(n + 1, FW_INF));
    for (int i = 1; i <= n; i++) d[i][i] = 0;
    for (int i = 0; i < m; i++) {
        int a, b, c; scanf("%d %d %d", &a, &b, &c);
        d[a][b] = d[b][a] = min(d[a][b], (W)c);
    }
    vector<vector<int>> nxt;
    floyd(n, d, nxt);
    while (q--) {
        int a, b; scanf("%d %d", &a, &b);
        printf("%lld\n", d[a][b] >= FW_INF ? -1 : d[a][b]);
    }
}
