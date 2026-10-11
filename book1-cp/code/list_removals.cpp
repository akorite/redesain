#include "orderstat.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) scanf("%lld", &a[i]);
    OrderStat os(n);
    for (int i = 0; i < n; i++) {
        long long k; scanf("%lld", &k);
        int p = os.f.lower_bound(k);
        printf("%lld%c", a[p], " \n"[i + 1 == n]);
        os.f.add(p, -1);
    }
}
