// bitmask_dp.h -- (mask,last) template: Elevator Rides as the canonical use.
#include <algorithm>
#include <vector>
using namespace std;
// dp[mask] = {rides used, weight on current last ride} minimized.
inline pair<int,int> elevator(int n, int X, const vector<int>& w) {
    int N = 1 << n;
    vector<pair<int,int>> dp(N, {n + 1, 0});
    dp[0] = {1, 0};
    for (int mask = 1; mask < N; mask++)
        for (int i = 0; i < n; i++) if (mask >> i & 1) {
            auto [r, cap] = dp[mask ^ (1 << i)];
            pair<int,int> cand = (cap + w[i] <= X)
                ? pair<int,int>{r, cap + w[i]}
                : pair<int,int>{r + 1, w[i]};
            dp[mask] = min(dp[mask], cand);
        }
    return dp[N - 1];
}
