// sliding_min.cpp -- CSES Sliding Window Minimum (generated input, xor
// of window minimums).
#include <iostream>
#include <vector>
#include "monodeque.h"
using namespace std;
using ll = long long;

int main() {
    ll n, k, x, a, b, c;
    cin >> n >> k >> x >> a >> b >> c;
    vector<ll> arr(n);
    arr[0] = x;
    for (int i = 1; i < n; i++) arr[i] = (a * arr[i - 1] + b) % c;
    auto mins = sliding_min(arr, (int)k);
    ll acc = 0;
    for (ll v : mins) acc ^= v;
    cout << acc << "\n";
}
