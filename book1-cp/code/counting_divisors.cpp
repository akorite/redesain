#include "sieve.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<int> spf = spf_sieve(1000000);
    while (n--) {
        long long x; scanf("%lld", &x);
        long long d = 1;
        for (auto& [p, e] : factorize(x, spf)) d *= e + 1;
        printf("%lld\n", d);
    }
}
