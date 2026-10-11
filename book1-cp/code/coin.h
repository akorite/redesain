// coin.h -- coin DP both ways: memo (top-down) and table (bottom-up).
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
const int CINF = 1e9;

// memo[x] = min coins for x; -1 uncomputed.
inline int coin_memo(int x, const vector<int>& c, vector<int>& memo) {
    if (x == 0) return 0;
    if (x < 0) return CINF;
    int& r = memo[x];
    if (r >= 0) return r;
    r = CINF;
    for (int v : c) r = min(r, coin_memo(x - v, c, memo));
    if (r < CINF) r++;
    return r;
}
// tab[x] = min coins for x, filled bottom-up.
inline vector<int> coin_tab(int X, const vector<int>& c) {
    vector<int> tab(X + 1, CINF);
    tab[0] = 0;
    for (int x = 1; x <= X; x++)
        for (int v : c)
            if (x - v >= 0) tab[x] = min(tab[x], tab[x - v] + 1);
    return tab;
}
