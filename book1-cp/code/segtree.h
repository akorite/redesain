// segtree.h -- iterative segment tree (Al.Cash style): tree[2n],
// any associative monoid via combine().
#include <vector>
using namespace std;
template <class T> struct SegTree {
    int n; vector<T> t; T id;
    T (*combine)(T, T);
    SegTree(const vector<T>& a, T (*f)(T,T), T idv)
        : n(a.size()), t(2 * a.size(), idv), id(idv), combine(f) {
        for (int i = 0; i < n; i++) t[n + i] = a[i];
        for (int i = n - 1; i > 0; i--) t[i] = combine(t[2*i], t[2*i+1]);
    }
    void set(int p, T v) {
        for (t[p += n] = v; p > 1; p >>= 1)
            t[p >> 1] = combine(t[p], t[p ^ 1]);
    }
    T query(int l, int r) const {           // [l, r)
        T rl = id, rr = id;
        for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
            if (l & 1) rl = combine(rl, t[l++]);
            if (r & 1) rr = combine(t[--r], rr);
        }
        return combine(rl, rr);
    }
};
inline long long seg_sum(long long a, long long b) { return a + b; }
inline long long seg_min(long long a, long long b) { return a < b ? a : b; }
