// mss_timing.cpp -- Listing 1.4: four algorithms for maximum subarray sum,
// timed on inputs each can finish. Deterministic data, chrono measurements.
#include <algorithm>
#include <chrono>
#include <cstdio>
#include <vector>
using namespace std;
using ll = long long;

ll mss_cubic(const vector<ll>& a) {           // check every (l,r) by resumming
    ll best = a[0];
    for (int l = 0; l < (int)a.size(); ++l)
        for (int r = l; r < (int)a.size(); ++r) {
            ll s = 0;
            for (int k = l; k <= r; ++k) s += a[k];
            best = max(best, s);
        }
    return best;
}
ll mss_quad(const vector<ll>& a) {            // same pairs, sum kept running
    ll best = a[0];
    for (int l = 0; l < (int)a.size(); ++l) {
        ll s = 0;
        for (int r = l; r < (int)a.size(); ++r) {
            s += a[r];
            best = max(best, s);
        }
    }
    return best;
}
ll mss_cross(const vector<ll>& a, int l, int m, int r) {
    ll left = LLONG_MIN, s = 0;
    for (int i = m; i >= l; --i) { s += a[i]; left = max(left, s); }
    ll right = LLONG_MIN; s = 0;
    for (int i = m + 1; i <= r; ++i) { s += a[i]; right = max(right, s); }
    return left + right;
}
ll mss_dnc(const vector<ll>& a, int l, int r) {  // divide and conquer, n log n
    if (l == r) return a[l];
    int m = (l + r) / 2;
    return max({mss_dnc(a, l, m), mss_dnc(a, m + 1, r),
                mss_cross(a, l, m, r)});
}
ll mss_kadane(const vector<ll>& a) {          // best suffix ending here
    ll best = a[0], cur = a[0];
    for (int i = 1; i < (int)a.size(); ++i) {
        cur = max(a[i], cur + a[i]);
        best = max(best, cur);
    }
    return best;
}

vector<ll> make_input(int n) {                // deterministic pseudo-random
    vector<ll> a(n);
    unsigned long long x = 88172645463325252ULL;
    for (auto& v : a) {
        x ^= x << 13; x ^= x >> 7; x ^= x << 17;
        v = (ll)(x % 2001) - 1000;            // values in [-1000, 1000]
    }
    return a;
}

template <class F>
void run(const char* name, int n, F f) {
    vector<ll> a = make_input(n);
    auto t0 = chrono::steady_clock::now();
    ll ans = f(a);
    double ms = chrono::duration<double, milli>(
        chrono::steady_clock::now() - t0).count();
    printf("%-9s n=%-7d ans=%lld time_ms=%.1f\n", name, n, ans, ms);
}

int main() {
    run("O(n^3)", 3000, mss_cubic);
    run("O(n^2)", 50000, mss_quad);
    run("O(nlogn)", 200000,
        [](const vector<ll>& a) {
            return mss_dnc(a, 0, (int)a.size() - 1);
        });
    run("O(n)", 200000, mss_kadane);
    run("O(n)", 5000000, mss_kadane);
}
