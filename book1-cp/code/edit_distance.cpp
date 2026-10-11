// edit_distance.cpp -- CSES Edit Distance: alignment-grid DP.
#include <algorithm>
#include <cstdio>
using std::min;
#include <cstring>
static int dp[5002][5002];
int main() {
    static char s[5002], t[5002];
    scanf("%s %s", s + 1, t + 1);
    int n = strlen(s + 1), m = strlen(t + 1);
    for (int i = 0; i <= n; i++) dp[i][0] = i;
    for (int j = 0; j <= m; j++) dp[0][j] = j;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            dp[i][j] = min({dp[i-1][j]+1, dp[i][j-1]+1,
                            dp[i-1][j-1]+(s[i]!=t[j])});
    printf("%d\n", dp[n][m]);
}
