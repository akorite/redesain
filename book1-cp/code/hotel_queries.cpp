// hotel_queries.cpp -- first room with capacity >= r via walk-on-tree.
#include "segtree.h"
#include <algorithm>
#include <cstdio>
struct Hotel {
    int n2, n;
    static vector<long long> padded(const vector<long long>& a, int& n2) {
        n2 = 1; while (n2 < (int)a.size()) n2 <<= 1;
        vector<long long> pad(n2, -1);
        for (size_t i = 0; i < a.size(); i++) pad[i] = a[i];
        return pad;
    }
    SegTree<long long> st;
    // walk-on-tree needs leaves on a power-of-two grid: pad to n2
    Hotel(vector<long long>& a)
        : n2(0), n(a.size()),
          st(padded(a, n2),
             [](long long x, long long y){return x>y?x:y;}, -1) {}
    int book(long long r) {
        if (st.t[1] < r) return 0;
        int v = 1;
        while (v < n2) v = st.t[2*v] >= r ? 2*v : 2*v+1;
        int p = v - n2;                       // leaf position
        if (p >= n) return 0;                 // only padding qualified
        st.t[v] -= r;
        for (v >>= 1; v; v >>= 1)
            st.t[v] = st.combine(st.t[2*v], st.t[2*v+1]);
        return p + 1;
    }
};
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<long long> a(n);
    for (auto& v : a) scanf("%lld", &v);
    Hotel h(a);
    while (m--) { long long r; scanf("%lld", &r); printf("%d ", h.book(r)); }
    puts("");
}
