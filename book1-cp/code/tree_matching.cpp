#include "treedp.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<vector<int>> ch(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int a, b; scanf("%d %d", &a, &b);
        ch[a].push_back(b); ch[b].push_back(a);
    }
    // build rooted children lists first
    vector<vector<int>> rc(n + 1);
    vector<int> par(n + 1, 0), st = {1};
    par[1] = -1;
    while (!st.empty()) {
        int v = st.back(); st.pop_back();
        for (int u : ch[v]) if (!par[u]) { par[u] = v; rc[v].push_back(u); st.push_back(u); }
    }
    auto [in, out] = tree_match(rc, 1);
    printf("%d\n", max(in, out));
}
