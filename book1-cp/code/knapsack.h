// knapsack.h -- 0/1 knapsack, descending-capacity inner loop + take table.
#include <algorithm>
#include <vector>
using namespace std;

// w[i],v[i]; returns max value for capacity X; take[i]=used item i.
inline int knapsack(int n, int X, const vector<int>& w,
                    const vector<int>& v, vector<char>& take) {
    vector<vector<int>> dp(n + 1, vector<int>(X + 1, 0));
    for (int i = 1; i <= n; i++)
        for (int x = X; x >= 0; x--) {          // descending: item once
            dp[i][x] = dp[i-1][x];
            if (x >= w[i]) dp[i][x] = max(dp[i][x], dp[i-1][x - w[i]] + v[i]);
        }
    take.assign(n + 1, 0);
    int x = X;
    for (int i = n; i >= 1; i--)
        if (x >= w[i] && dp[i][x] == dp[i-1][x - w[i]] + v[i])
            { take[i] = 1; x -= w[i]; }
    return dp[n][X];
}
