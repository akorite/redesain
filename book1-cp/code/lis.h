// lis.h -- longest increasing subsequence, O(n log n).
#include <algorithm>
#include <vector>
using namespace std;
inline int lis_len(const vector<int>& a) {
    vector<int> L;                            // L[i]=smallest tail of len i+1
    for (int x : a) {
        auto it = lower_bound(L.begin(), L.end(), x);
        if (it == L.end()) L.push_back(x); else *it = x;
    }
    return L.size();
}
