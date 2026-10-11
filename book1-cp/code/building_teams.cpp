// building_teams.cpp -- CSES Building Teams: bipartite 2-colouring.
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        g[a].push_back(b); g[b].push_back(a);
    }
    vector<int> col(n + 1, 0);
    bool ok = true;
    for (int s = 1; s <= n && ok; s++) {
        if (col[s]) continue;
        col[s] = 1;
        queue<int> q; q.push(s);
        while (!q.empty() && ok) {
            int v = q.front(); q.pop();
            for (int w : g[v]) {
                if (col[w] == col[v]) { ok = false; break; }
                if (!col[w]) { col[w] = 3 - col[v]; q.push(w); }
            }
        }
    }
    if (!ok) { cout << "IMPOSSIBLE\n"; return 0; }
    for (int v = 1; v <= n; v++)
        cout << col[v] << " \n"[v == n];
}
