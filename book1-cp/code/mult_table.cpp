// mult_table.cpp -- CSES Multiplication Table: median of n^2 products.
#include <iostream>
#include "lib/bsearch.h"
using namespace std;

int main() {
    ll n;
    cin >> n;
    auto le = [&](ll x) {              // count products <= x, row by row
        ll c = 0;
        for (ll i = 1; i <= n; i++) c += min(n, x / i);
        return c;
    };
    ll k = (n * n + 1) / 2;            // middle position (1-indexed)
    cout << first_true(1, n * n, [&](ll x){ return le(x) >= k; }) << "\n";
}
