// distributing_apples.cpp -- stars and bars: C(n+m-1, n-1).
#include "ncr.h"
#include <cstdio>
int main() {
    int n, m; scanf("%d %d", &n, &m);
    NCR ncr(n + m);
    printf("%lld\n", ncr.choose(n + m - 1, n - 1).v);
}
