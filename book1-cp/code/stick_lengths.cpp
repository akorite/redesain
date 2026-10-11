// stick_lengths.cpp -- the median minimises sum |p_i - m|.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<ll> p(n);
    for (ll &x : p) cin >> x;
    sort(p.begin(), p.end());
    ll m = p[n / 2], cost = 0;
    for (ll x : p) cost += llabs(x - m);
    cout << cost << "\n";
}
