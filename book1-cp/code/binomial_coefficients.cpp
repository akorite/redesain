#include "ncr.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    NCR ncr(1000000);
    while (n--) {
        int a, b; scanf("%d %d", &a, &b);
        printf("%lld\n", ncr.choose(a, b).v);
    }
}
