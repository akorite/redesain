// mss_linear.cpp -- Kadane's algorithm, the submission version.
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
    ll best = a[0], cur = a[0];
    for (int i = 1; i < n; ++i) {
        cur = max(a[i], cur + a[i]);
        best = max(best, cur);
    }
    cout << best << '\n';
}
