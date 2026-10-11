#include "segtree.h"
#include <cstdio>
int main() {
    int n, q; scanf("%d %d", &n, &q);
    vector<long long> a(n);
    for (auto& v : a) scanf("%lld", &v);
    SegTree<long long> st(a, seg_sum, 0);
    while (q--) {
        int t; scanf("%d", &t);
        if (t == 1) { int k; long long u; scanf("%d %lld", &k, &u); st.set(k - 1, u); }
        else { int a_, b; scanf("%d %d", &a_, &b); printf("%lld\n", st.query(a_ - 1, b)); }
    }
}
