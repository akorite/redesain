// histogram.cpp -- largest rectangle: bar i extends to the first
// smaller bar on each side; area = h_i * (R_i - L_i - 1).
#include <iostream>
#include <vector>
#include "monostack.h"
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<ll> h(n);
    for (auto &x : h) cin >> x;
    auto L = nearest_smaller_left(h);
    auto R = nearest_smaller_right(h);
    ll best = 0; int bi = -1;
    for (int i = 0; i < n; i++) {
        ll area = h[i] * (R[i] - L[i] - 1);
        if (area > best) { best = area; bi = i; }
    }
    cout << "best area " << best << " from bar " << bi
         << " (height " << h[bi] << ", spans [" << L[bi] + 1
         << "," << R[bi] - 1 << "])\n";
}
