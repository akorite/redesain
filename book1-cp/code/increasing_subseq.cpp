#include "lis.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<int> a(n);
    for (auto& x : a) scanf("%d", &x);
    printf("%d\n", lis_len(a));
}
