// candy_lottery.cpp -- CSES 1727: E[max] of n iid uniforms on {1..k}.
// Tail-sum: E[max] = sum_v P(max >= v) = sum_v (1 - ((v-1)/k)^n).
#include <cstdio>
#include <cmath>
int main() {
    int n, k; scanf("%d %d", &n, &k);
    double e = 0;
    for (int v = 1; v <= k; v++)
        e += 1.0 - pow((v - 1.0) / k, n);
    printf("%.6f\n", e);
}
