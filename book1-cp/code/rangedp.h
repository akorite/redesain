// rangedp.h -- by-length order: Removal Game max first-player sum.
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;
inline long long removal_game(const vector<long long>& a) {
    int n = a.size();
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) dp[i][i] = a[i];
    for (int len = 2; len <= n; len++)
        for (int l = 0; l + len <= n; l++) {
            int r = l + len - 1;
            dp[l][r] = max(a[l] - dp[l + 1][r], a[r] - dp[l][r - 1]);
        }
    return (accumulate(a.begin(), a.end(), 0LL) + dp[0][n - 1]) / 2;
}
