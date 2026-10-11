// exponentiation2.cpp -- a^(b^c) mod 1e9+7: Fermat reduces the
// exponent's exponent mod (m-1) when gcd(a,m)=1.
#include "binpow.h"
#include <cstdio>
int main() {
    const long long M = 1000000007;
    int n; scanf("%d", &n);
    while (n--) {
        long long a, b, c; scanf("%lld %lld %lld", &a, &b, &c);
        printf("%lld\n", binpow(a, binpow(b, c, M - 1), M));
    }
}
