// reroot.h -- down[v]: max depth below; up[v]: max depth via parent.
#include <vector>
using namespace std;
inline void reroot(const vector<vector<int>>& g, int root,
                   vector<int>& down, vector<int>& up) {
    int n = g.size() - 1;
    down.assign(n+1, 0); up.assign(n+1, 0);
    vector<int> ord = {root}, par(n+1, 0);
    for (size_t i = 0; i < ord.size(); i++) {
        int v = ord[i];
        for (int u : g[v]) if (u != par[v]) { par[u] = v; ord.push_back(u); }
    }
    for (int i = ord.size()-1; i > 0; i--) {
        int v = ord[i];
        down[par[v]] = max(down[par[v]], down[v] + 1);
    }
    for (int v : ord) {                    // sibling-max for each child
        vector<int>& ch = *(new vector<int>());
        for (int u : g[v]) if (u != par[v]) ch.push_back(u);
        int m = ch.size();
        vector<int> pre(m+1,0), suf(m+1,0);
        for (int i = 0; i < m; i++) pre[i+1] = max(pre[i], down[ch[i]]+1);
        for (int i = m-1; i >= 0; i--) suf[i] = max(suf[i+1], down[ch[i]]+1);
        for (int i = 0; i < m; i++)
            up[ch[i]] = 1 + max(up[v], max(pre[i], suf[i+1]));
    }
}
