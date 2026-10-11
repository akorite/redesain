// prefix.h -- prefix tables: build once, query forever.
// 1D: P[i] = a[1]+...+a[i], sum(l..r) = P[r]-P[l-1].
// 2D: P[r][c] = sum of the (r x c) corner; rect (r1,c1)-(r2,c2) =
//     P[r2][c2] - P[r1-1][c2] - P[r2][c1-1] + P[r1-1][c1-1].
#pragma once
#include <vector>
using ll = long long;

struct Prefix1D {
    int n; std::vector<ll> p;
    explicit Prefix1D(const std::vector<ll>& a) : n(a.size()), p(n + 1) {
        for (int i = 0; i < n; i++) p[i + 1] = p[i] + a[i];
    }
    ll sum(int l, int r) const { return p[r] - p[l - 1]; }  // 1-indexed
};

struct Prefix2D {
    int n, m; std::vector<std::vector<ll>> p;
    Prefix2D(const std::vector<std::vector<ll>>& a)
        : n(a.size()), m(a[0].size()), p(n + 1, std::vector<ll>(m + 1)) {
        for (int r = 1; r <= n; r++)
            for (int c = 1; c <= m; c++)
                p[r][c] = a[r - 1][c - 1] + p[r - 1][c] + p[r][c - 1]
                        - p[r - 1][c - 1];
    }
    ll sum(int r1, int c1, int r2, int c2) const {
        return p[r2][c2] - p[r1 - 1][c2] - p[r2][c1 - 1] + p[r1 - 1][c1 - 1];
    }
};
