// diff.h -- range updates as two point writes.
// To add v to a[l..r]: d[l] += v, d[r+1] -= v.
// The prefix sum of d restores every cell exactly once at the end.
#pragma once
#include <vector>
using ll = long long;

struct Diff1D {
    int n; std::vector<ll> d;
    explicit Diff1D(int n) : n(n), d(n + 2, 0) {}
    void add(int l, int r, ll v) { d[l] += v; d[r + 1] -= v; }
    std::vector<ll> restore() const {
        std::vector<ll> a(n);
        ll cur = 0;
        for (int i = 0; i < n; i++) { cur += d[i]; a[i] = cur; }
        return a;
    }
};

struct Diff2D {
    int n, m; std::vector<std::vector<ll>> d;
    Diff2D(int n, int m) : n(n), m(m), d(n + 2, std::vector<ll>(m + 2, 0)) {}
    void add(int r1, int c1, int r2, int c2, ll v) {  // 1-indexed corners
        d[r1][c1] += v; d[r2 + 1][c1] -= v;
        d[r1][c2 + 1] -= v; d[r2 + 1][c2 + 1] += v;
    }
    std::vector<std::vector<ll>> restore() const {
        std::vector<std::vector<ll>> a(n, std::vector<ll>(m));
        for (int r = 0; r < n; r++) {
            ll row = 0;
            for (int c = 0; c < m; c++) {
                row += d[r][c];
                a[r][c] = row + (r ? a[r - 1][c] : 0);
            }
        }
        return a;
    }
};
