// size_ladder.cpp -- measured cost of 2^n enumeration, n = 15..27.
// Each run touches every subset once (subset-sum tally via a Gray-free
// mask loop) so the times track the size of the search space, not IO.
#include <chrono>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    vector<int> ns = {15, 18, 20, 22, 24, 25, 26, 27, 28, 29, 30};
    for (int n : ns) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i + 1;
        auto t0 = chrono::steady_clock::now();
        ll tally = 0;
        for (ll mask = 0; mask < (1LL << n); mask++)
            tally += a[__builtin_ctzll(mask | (1LL << n)) % n];  // touch one element
        auto t1 = chrono::steady_clock::now();
        cout << "n=" << n << "  subsets=" << (1LL << n)
             << "  time=" << chrono::duration<double, milli>(t1 - t0).count()
             << " ms   (tally=" << tally << ")\n";
    }
    return 0;
}
