// mss_buggy.cpp -- a subtly wrong Kadane's, for the stress demo.
// Bug: resets the running sum to 0 instead of restarting at a[i],
// which silently allows empty segments on all-negative arrays.
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
    ll best = 0, cur = 0;              // BUG: 'empty segment allowed'
    for (int i = 0; i < n; ++i) {
        cur = max(0LL, cur + a[i]);    // should be max(a[i], cur+a[i])
        best = max(best, cur);
    }
    cout << best << '\n';
}
