// forest_queries.cpp -- CSES Forest Queries (2D prefix on a grid).
#include <iostream>
#include <string>
#include <vector>
#include "prefix.h"
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<ll>> g(n, vector<ll>(n));
    for (int r = 0; r < n; r++) {
        string row; cin >> row;
        for (int c = 0; c < n; c++) g[r][c] = (row[c] == '*');
    }
    Prefix2D pf(g);
    while (q--) {
        int r1, c1, r2, c2;
        cin >> r1 >> c1 >> r2 >> c2;
        cout << pf.sum(r1, c1, r2, c2) << "\n";
    }
}
