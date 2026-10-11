// lca.h -- binary lifting: 2^k ancestors, k-th ancestor, LCA.
#include <vector>
using namespace std;

struct LCA {
    int n, LOG;
    vector<vector<int>> up;      // up[k][v] = 2^k-th ancestor (0=none)
    vector<int> depth;
    LCA(const vector<vector<int>>& g, int root = 1) {
        n = g.size() - 1;
        LOG = 1; while ((1 << LOG) <= n) LOG++;
        up.assign(LOG, vector<int>(n + 1, 0));
        depth.assign(n + 1, 0);
        vector<int> ord = {root};
        up[0][root] = 0;
        for (size_t i = 0; i < ord.size(); i++) {
            int v = ord[i];
            for (int u : g[v]) if (u != up[0][v]) {
                up[0][u] = v; depth[u] = depth[v] + 1;
                ord.push_back(u);
            }
        }
        for (int k = 1; k < LOG; k++)
            for (int v = 1; v <= n; v++)
                up[k][v] = up[k-1][up[k-1][v]];
    }
    int kth(int v, int k) const {
        for (int j = 0; j < LOG && v; j++)
            if (k & (1 << j)) v = up[j][v];
        return v;
    }
    int lca(int a, int b) const {
        if (depth[a] < depth[b]) swap(a, b);
        a = kth(a, depth[a] - depth[b]);
        if (a == b) return a;
        for (int j = LOG - 1; j >= 0; j--)
            if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
        return up[0][a];
    }
    int dist(int a, int b) const {
        return depth[a] + depth[b] - 2 * depth[lca(a, b)];
    }
};
