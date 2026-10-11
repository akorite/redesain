// christmas_party.cpp -- derangements: D_n = (n-1)(D_{n-1}+D_{n-2}).
#include "modint.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    mint d0 = 1, d1 = 0;
    for (int i = 2; i <= n; i++) {
        mint d2 = mint(i - 1) * (d1 + d0);
        d0 = d1; d1 = d2;
    }
    printf("%lld\n", (n == 1 ? d1 : (n == 0 ? d0 : d1)).v);
}
