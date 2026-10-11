// sqrtdec.h -- square-root decomposition: block sums + point updates.
// Query: O(#blocks + #fringe) = O(sqrt n). Update a point: O(1).
#pragma once
#include <cmath>
#include <vector>
using ll = long long;

struct SqrtDec {
    int n, B;
    std::vector<ll> a, blk;
    explicit SqrtDec(std::vector<ll> v) : n(v.size()), a(std::move(v)) {
        B = (int)std::sqrt(n) + 1;
        blk.assign(B + 1, 0);
        for (int i = 0; i < n; i++) blk[i / B] += a[i];
    }
    void set(int i, ll v) { blk[i / B] += v - a[i]; a[i] = v; }
    ll sum(int l, int r) const {            // inclusive [l, r]
        ll s = 0;
        int bl = l / B, br = r / B;
        if (bl == br)
            for (int i = l; i <= r; i++) s += a[i];
        else {
            for (int i = l; i / B == bl; i++) s += a[i];
            for (int b = bl + 1; b < br; b++) s += blk[b];
            for (int i = br * B; i <= r; i++) s += a[i];
        }
        return s;
    }
};
