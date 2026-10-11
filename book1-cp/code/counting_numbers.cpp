#include "digitdp.h"
#include <cstdio>
int main() {
    long long a, b; scanf("%lld %lld", &a, &b);
    printf("%lld\n", count_digits(b) - count_digits(a - 1));
}
