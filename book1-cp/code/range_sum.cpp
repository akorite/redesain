// range_sum.cpp -- CSES Static Range Sum Queries (1D prefix).
#include <iostream>
#include <vector>
#include "prefix.h"
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;
    Prefix1D pf(a);
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pf.sum(l, r) << "\n";
    }
}
