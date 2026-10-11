// course_schedule.cpp -- CSES Course Schedule: Kahn topological order.
#include <iostream>
#include <vector>
#include "toposort.h"
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        g[a].push_back(b);
    }
    auto order = kahn(g);
    if ((int)order.size() < n) { cout << "IMPOSSIBLE\n"; return 0; }
    for (int v : order) cout << v << " ";
    cout << "\n";
}
