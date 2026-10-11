// apple_bench.cpp -- measured cost of the "fix element 0" symmetry.
// Same recursive search twice: once free, once with w[0] pinned to
// group A.  Swapping the groups changes nothing, so every solution
// appears twice in the free search -- pinning removes the mirror half.
#include <chrono>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int n;
vector<ll> w;
ll total;

void dfs(int k, ll sumA, ll& best, ll& leaves) {
    if (k == n) { best = min(best, llabs(total - 2 * sumA)); leaves++; return; }
    dfs(k + 1, sumA + w[k], best, leaves);
    dfs(k + 1, sumA, best, leaves);
}

int main() {
    n = 22;
    for (int i = 0; i < n; i++) { w.push_back((i * 37 % 97) + 1); total += w[i]; }

    auto t0 = chrono::steady_clock::now();
    ll best = total, leaves = 0;
    dfs(0, 0, best, leaves);                      // all 2^n assignments
    auto t1 = chrono::steady_clock::now();
    cout << "free:      leaves=" << leaves
         << "  time=" << chrono::duration<double, milli>(t1 - t0).count() << " ms"
         << "  answer=" << best << "\n";

    t0 = chrono::steady_clock::now();
    best = total; leaves = 0;
    dfs(1, w[0], best, leaves);                   // w[0] pinned to group A
    t1 = chrono::steady_clock::now();
    cout << "fixed[0]:  leaves=" << leaves
         << "  time=" << chrono::duration<double, milli>(t1 - t0).count() << " ms"
         << "  answer=" << best << "\n";
    return 0;
}
