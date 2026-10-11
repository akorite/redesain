// dice_probability.cpp -- CSES 1725: P(sum of n dice in [a,b]).
// Count compositions by DP; divide by 6^n.
#include <cstdio>
#include <vector>
int main() {
    int n, a, b; scanf("%d %d %d", &n, &a, &b);
    std::vector<double> dp(n * 6 + 1, 0), nd;
    dp[0] = 1.0;
    for (int i = 0; i < n; i++) {
        nd.assign(n * 6 + 1, 0);
        for (int s = 0; s <= 6 * i; s++)
            for (int f = 1; f <= 6 && s + f <= 6 * n; f++)
                nd[s + f] += dp[s] / 6.0;
        dp = nd;
    }
    double p = 0;
    for (int s = a; s <= b; s++) p += dp[s];
    printf("%.6f\n", p);
}
