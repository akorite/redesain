// rmq.cpp -- CSES Static Range Minimum Queries via sparse table.
#include <algorithm>
#include <iostream>
#include <vector>
#include "sparse.h"
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    SparseTable st(a, [](long long u, long long v) { return min(u, v); });
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << st.query(l - 1, r - 1) << "\n";
    }
}
