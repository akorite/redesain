// labyrinth.cpp -- CSES Labyrinth: BFS + parent reconstruction.
#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    int ar = -1, ac = -1, br = -1, bc = -1;
    for (int r = 0; r < n; r++) {
        cin >> g[r];
        for (int c = 0; c < m; c++) {
            if (g[r][c] == 'A') { ar = r; ac = c; }
            if (g[r][c] == 'B') { br = r; bc = c; }
        }
    }
    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<vector<pair<int,int>>> par(n, vector<pair<int,int>>(m, {-1,-1}));
    const int dr[4] = {0, 0, -1, 1}, dc[4] = {-1, 1, 0, 0};
    const char mv[4] = {'L', 'R', 'U', 'D'};
    queue<pair<int,int>> q;
    dist[ar][ac] = 0; q.push({ar, ac});
    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int k = 0; k < 4; k++) {
            int nr = r + dr[k], nc = c + dc[k];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            if (g[nr][nc] == '#' || dist[nr][nc] >= 0) continue;
            dist[nr][nc] = dist[r][c] + 1;
            par[nr][nc] = {r, c};
            q.push({nr, nc});
        }
    }
    if (dist[br][bc] < 0) { cout << "NO\n"; return 0; }
    cout << "YES\n" << dist[br][bc] << "\n";
    string path;
    for (int r = br, c = bc; par[r][c].first >= 0; ) {
        auto [pr, pc] = par[r][c];
        for (int k = 0; k < 4; k++)
            if (pr + dr[k] == r && pc + dc[k] == c) path += mv[k];
        r = pr; c = pc;
    }
    reverse(path.begin(), path.end());
    cout << path << "\n";
}
