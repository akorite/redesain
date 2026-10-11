#include "bitset_knapsack.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<int> c(n);
    for (auto& v : c) scanf("%d", &v);
    auto dp = money_sums<100001>(c);
    vector<int> ans;
    for (int i = 1; i <= 100000; i++) if (dp[i]) ans.push_back(i);
    printf("%zu\n", ans.size());
    for (size_t i = 0; i < ans.size(); i++)
        printf("%d%c", ans[i], " \n"[i+1==ans.size()]);
}
