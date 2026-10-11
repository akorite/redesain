// treedp.h -- in/out state pair on a rooted tree (Tree Matching).
#include <algorithm>
#include <vector>
using namespace std;
// in[v]=max matching with v matched to a child; out[v]=v free upward.
inline pair<int,int> tree_match(const vector<vector<int>>& ch, int v) {
    int in = -1e9, out = 0;
    for (int u : ch[v]) {
        auto [ui, uo] = tree_match(ch, u);
        out += max(ui, uo);
        in = max(in, uo - max(ui, uo));
    }
    return {out + std::max(0, in + 1), out};
}
