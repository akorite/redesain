// coins.cpp -- greedy coin change vs the true optimum on small amounts.
// usage: coins <amount> <denom>...   e.g.  coins 6 1 3 4
// Denominations are sorted descending internally: greedy is only defined
// for largest-first order, so caller order never changes the answer.
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int amount = atoi(argv[1]);
    vector<int> d;
    for (int i = 2; i < argc; i++) d.push_back(atoi(argv[i]));
    sort(d.rbegin(), d.rend());          // largest first -- the definition
    // greedy: largest-first
    int left = amount, gc = 0;
    for (int c : d) { gc += left / c; left %= c; }
    // truth: DP over all amounts (correctness by construction)
    const int INF = 1e9;
    vector<int> best(amount + 1, INF);
    best[0] = 0;
    for (int v = 1; v <= amount; v++)
        for (int c : d) if (c <= v) best[v] = min(best[v], best[v - c] + 1);
    cout << "amount=" << amount << " coins={";
    for (size_t i = 0; i < d.size(); i++)
        cout << d[i] << (i + 1 < d.size() ? "," : "");
    cout << "} greedy=" << gc << " optimal=" << best[amount] << "\n";
}
