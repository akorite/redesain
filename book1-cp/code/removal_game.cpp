#include "rangedp.h"
#include <numeric>
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<long long> a(n);
    for (auto& v : a) scanf("%lld", &v);
    printf("%lld\n", removal_game(a));
}
