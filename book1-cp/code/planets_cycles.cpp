// planets_cycles.cpp -- CSES Planets Cycles.
// Functional graph: every walk is tail + cycle. If path [p0..pk-1]
// next enters vertex v: v already answered -> all of path is tail and
// ans[p_i] = (k-i) + ans[v]. Otherwise v = p_j, the cycle is
// p_j..p_{k-1} (length k-j): cycle members get k-j, tails get k-i.
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> t(n + 1), ans(n + 1, -1);
    vector<int> pos(n + 1, -1), inpath(n + 1, -1);
    for (int i = 1; i <= n; i++) cin >> t[i];
    for (int s = 1; s <= n; s++) {
        if (ans[s] >= 0) continue;
        vector<int> path;
        int v = s;
        while (ans[v] < 0 && inpath[v] != s) {
            inpath[v] = s;
            pos[v] = path.size();
            path.push_back(v);
            v = t[v];
        }
        int k = path.size();
        if (ans[v] >= 0) {                    // all tail
            for (int i = 0; i < k; i++) ans[path[i]] = k - i + ans[v];
        } else {                              // v = p_j: cycle found
            int j = pos[v], cyc = k - j;
            for (int i = j; i < k; i++) ans[path[i]] = cyc;
            for (int i = 0; i < j; i++) ans[path[i]] = k - i;
        }
    }
    for (int i = 1; i <= n; i++)
        cout << ans[i] << " \n"[i == n];
}
