#include "bitmask_dp.h"
#include <cstdio>
int main() {
    int n, x; scanf("%d %d", &n, &x);
    vector<int> w(n);
    for (auto& v : w) scanf("%d", &v);
    printf("%d\n", elevator(n, x, w).first);
}
