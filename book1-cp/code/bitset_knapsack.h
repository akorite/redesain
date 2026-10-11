// bitset_knapsack.h -- reachable sums via dp |= dp << w.
#include <bitset>
#include <vector>
using namespace std;
template <size_t MAXSUM>
inline bitset<MAXSUM> money_sums(const vector<int>& c) {
    bitset<MAXSUM> dp;
    dp[0] = 1;
    for (int w : c) dp |= dp << w;
    return dp;
}
