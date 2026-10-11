#include "matpow.h"
#include <cstdio>
int main() {
    long long n; scanf("%lld", &n);
    M2 a = {{{1,1},{1,0}}};
    printf("%lld\n", mpow(a, n, 1000000007)[0][1]);
}
