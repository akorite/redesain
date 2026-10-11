// sparse.h -- sparse table for idempotent range queries (min/max/gcd):
// O(n log n) build, O(1) query via two overlapping levels.
// Requires the operation satisfy f(f(x)) = f(x) -- overlapping pieces
// may double-count nothing.
#pragma once
#include <algorithm>
#include <vector>

template <class T, class F>
struct SparseTable {
    std::vector<std::vector<T>> st;
    F f;
    SparseTable(const std::vector<T>& a, F f) : f(f) {
        int n = a.size(), L = 32 - __builtin_clz(n);
        st.assign(L, std::vector<T>(n));
        st[0] = a;
        for (int j = 1; j < L; j++)
            for (int i = 0; i + (1 << j) <= n; i++)
                st[j][i] = f(st[j - 1][i], st[j - 1][i + (1 << (j - 1))]);
    }
    T query(int l, int r) const {           // inclusive [l, r]
        int j = 31 - __builtin_clz(r - l + 1);
        return f(st[j][l], st[j][r - (1 << j) + 1]);
    }
};
