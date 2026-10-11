// social_distancing.cpp -- USACO-S Social Distancing: maximise the min gap.
#include <algorithm>
#include <iostream>
#include <vector>
#include "lib/bsearch.h"
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<ll> p(n);
    for (auto &x : p) cin >> x;
    sort(p.begin(), p.end());
    auto fits = [&](ll d) {            // can k cows sit with gaps >= d?
        int placed = 1; ll last = p[0];
        for (int i = 1; i < n; i++)
            if (p[i] - last >= d) { placed++; last = p[i]; }
        return placed >= k;
    };
    // largest d that still fits == last false of "!fits" == first_true-1
    ll d = first_true(0, p.back() - p[0] + 1,
                    [&](ll d){ return !fits(d); }) - 1;
    cout << "fits(4)=" << fits(4) << " fits(5)=" << fits(5) << "\n";
    cout << d << "\n";
}
