#include "bellmanford.h"
#include <algorithm>
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<Edge> E(m);
    for (auto& e : E) scanf("%d %d %d", &e.u, &e.v, &e.w);
    vector<int> cyc;
    bellmanford(n, 1, E, cyc);
    if (cyc.empty()) { puts("NO"); return 0; }
    puts("YES");
    for (int i = 0; i < (int)cyc.size(); i++)
        printf("%d%c", cyc[i], " \n"[i + 1 == (int)cyc.size()]);
}
