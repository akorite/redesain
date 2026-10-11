// range_update_queries.cpp -- range-update/point-query via diff on BIT.
#include "fenwick.h"
#include <cstdio>
int main() {
    int n, q; scanf("%d %d", &n, &q);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    Fenwick f(n);
    while (q--) {
        int t; scanf("%d", &t);
        if (t == 1) { int l, r, x; scanf("%d %d %d", &l, &r, &x);
            f.add(l, x); f.add(r + 1, -x); }
        else { int k; scanf("%d", &k); printf("%lld\n", a[k] + f.sum(k)); }
    }
}
