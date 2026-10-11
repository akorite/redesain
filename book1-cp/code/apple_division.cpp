// apple_division.cpp -- CSES Apple Division.
// Split n apples into two groups minimizing |sum A - sum B|.
// Bitmask enumeration: 2^(n-1) candidates (element 0 fixed in group A).
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    int n;
    cin >> n;
    vector<ll> w(n);
    ll total = 0;
    for (ll& x : w) { cin >> x; total += x; }

    ll best = total;   // |sumA - sumB| = |total - 2*sumA|
    for (int mask = 0; mask < (1 << (n - 1)); mask++) {
        ll sumA = w[0];                      // element 0 fixed in A
        for (int k = 0; k < n - 1; k++)
            if (mask & (1 << k)) sumA += w[k + 1];
        best = min(best, llabs(total - 2 * sumA));
    }
    cout << best << "\n";
    return 0;
}
