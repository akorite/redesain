// bsearch.h -- the one binary-search template: first true in [lo,hi].
// Contract: pred is monotone on [lo, hi] (F...F T...T) and pred(hi) is true.
// Returns the smallest x with pred(x); undefined if pred is not monotone.
#pragma once
using ll = long long;

template <class F> ll first_true(ll lo, ll hi, F pred) {
    while (lo < hi) {
        ll mid = lo + (hi - lo) / 2;
        if (pred(mid)) hi = mid; else lo = mid + 1;
    }
    return lo;
}
