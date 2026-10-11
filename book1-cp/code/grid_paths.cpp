// grid_paths.cpp -- CSES Grid Paths I (obstacles, in-place table).
#include <cstdio>
const long long MOD = 1e9+7;
static long long dp[1002][1002];
static char g[1002][1002];
int main() {
    int n; scanf("%d", &n);
    for (int i = 1; i <= n; i++) scanf("%s", g[i] + 1);
    if (g[1][1] == '*' || g[n][n] == '*') { puts("0"); return 0; }
    dp[1][1] = 1;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            if (g[i][j] == '*') { dp[i][j] = 0; continue; }
            if (i > 1 || j > 1)
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD;
        }
    printf("%lld\n", dp[n][n]);
}
