// mss_brute.cpp -- O(n^3) reference for stress tests. Reads n then n ints.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<ll> a(n);
    for (auto& v : a) cin >> v;
    ll best = a[0];
    for (int l = 0; l < n; ++l)
        for (int r = l; r < n; ++r) {
            ll s = 0;
            for (int k = l; k <= r; ++k) s += a[k];
            best = max(best, s);
        }
    cout << best << '\n';
}
