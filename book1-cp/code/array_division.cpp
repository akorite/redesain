// array_division.cpp -- CSES Array Division: minimise the largest group sum.
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
#include "lib/bsearch.h"
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;
    auto check = [&](ll cap) {         // does cap per group suffice?
        int groups = 1; ll sum = 0;
        for (ll x : a) {
            if (x > cap) return false;
            if (sum + x > cap) { groups++; sum = 0; }
            sum += x;
        }
        return groups <= k;
    };
    ll lo = *max_element(a.begin(), a.end()),
       hi = accumulate(a.begin(), a.end(), 0LL);
    cout << "check(7)=" << check(7) << " check(8)=" << check(8) << "\n";
    cout << first_true(lo, hi, check) << "\n";
}
