// prefix_map.cpp -- Subarray Sums II (negatives allowed) and
// Subarray Divisibility: prefix + map counting.
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    int n; ll x;
    cin >> n >> x;
    vector<ll> a(n);
    for (auto &v : a) cin >> v;
    // exact sum x: count pairs (P[i], P[j]) with P[j]-P[i] = x
    map<ll, int> seen;
    ll P = 0, cnt = 0;
    seen[0] = 1;
    for (ll v : a) {
        P += v;
        cnt += seen[P - x];
        seen[P]++;
    }
    cout << "sum=" << x << ": " << cnt << "\n";
    // divisibility by n itself (Subarray Divisibility): equal residues
    map<ll, int> rem;
    ll Q = 0; ll d = 0;
    rem[0] = 1;
    for (ll v : a) {
        Q = ((Q + v) % n + n) % n;
        d += rem[Q];
        rem[Q]++;
    }
    cout << "divisible by n=" << n << ": " << d << "\n";
}
