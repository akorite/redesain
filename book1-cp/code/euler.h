// euler.h -- tin/tout: subtree of v = contiguous [tin[v], tout[v]).
#include <vector>
using namespace std;
inline void euler(const vector<vector<int>>& g, int root,
                  vector<int>& tin, vector<int>& tout, vector<int>& dep) {
    int n = g.size() - 1, t = 0;
    tin.assign(n+1,0); tout.assign(n+1,0); dep.assign(n+1,0);
    vector<pair<int,int>> st = {{root, 0}};   // (v, next child idx)
    tin[root] = t++;
    while (!st.empty()) {
        auto& [v, i] = st.back();
        if (i < (int)g[v].size()) {
            int u = g[v][i++];
            if (u != (st.size() > 1 ? st[st.size()-2].first : 0) &&
                tin[u] == 0 && u != root) {
                dep[u] = dep[v] + 1; tin[u] = t++;
                st.push_back({u, 0});
            }
        } else { tout[v] = t; st.pop_back(); }
    }
}
