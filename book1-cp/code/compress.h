// compress.h -- coordinate compression: values -> ranks 0..k-1.
// Requires the WHOLE list up front; ranks preserve all order comparisons.
#pragma once
#include <algorithm>
#include <vector>
using namespace std;

// Returns ranks in the same positions as v: rank[i] = index of v[i]
// among the distinct sorted values. Also fills `vals` (rank -> value).
inline vector<int> compress(const vector<long long> &v,
                            vector<long long> &vals) {
    vals = v;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    vector<int> r(v.size());
    for (size_t i = 0; i < v.size(); i++)
        r[i] = int(lower_bound(vals.begin(), vals.end(), v[i]) - vals.begin());
    return r;
}
