#include "knapsack.h"
#include <cstdio>
int main() {
    int n, x; scanf("%d %d", &n, &x);
    vector<int> w(n+1), v(n+1);
    for (int i = 1; i <= n; i++) scanf("%d", &w[i]);
    for (int i = 1; i <= n; i++) scanf("%d", &v[i]);
    vector<char> take;
    printf("%d\n", knapsack(n, x, w, v, take));
    int first = 1;
    for (int i = 1; i <= n; i++)
        if (take[i]) { printf("%s%d", first ? "" : " ", i); first = 0; }
    printf("\n");
}
