// factory_machines.cpp -- CSES Factory Machines via binary search on time.
#include <iostream>
#include <vector>
#include "lib/bsearch.h"
using namespace std;

int main() {
    ll n, t;
    cin >> n >> t;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;
    auto check = [&](ll T) {           // can we make t products by time T?
        ll made = 0;
        for (ll x : a) { made += T / x; if (made >= t) return true; }
        return made >= t;
    };
    cout << "check(7)=" << check(7) << " check(8)=" << check(8) << "\n";
    cout << first_true(1, (ll)4e18, check) << "\n";
}
