// subsets.h -- complete-search subset enumeration (capstone library).
// Two idioms, pick per task:
//   subsets_rec(n, f)  -- recursive take/leave; f gets the subset as vector<int>
//   for_mask(n, f)     -- bitmask iteration; f gets the mask
// Convention: elements are 0..n-1, bit k <=> element k.
#pragma once
#include <functional>
#include <vector>
using namespace std;

inline void subsets_rec_go(int k, int n, vector<int>& chosen,
                           const function<void(const vector<int>&)>& f) {
    if (k == n) { f(chosen); return; }
    chosen.push_back(k);
    subsets_rec_go(k + 1, n, chosen, f);
    chosen.pop_back();
    subsets_rec_go(k + 1, n, chosen, f);
}

inline void subsets_rec(int n, const function<void(const vector<int>&)>& f) {
    vector<int> chosen;
    subsets_rec_go(0, n, chosen, f);
}

inline void for_mask(int n, const function<void(int)>& f) {
    for (int mask = 0; mask < (1 << n); mask++) f(mask);
}

// Half the work when the objective is symmetric under complement
// (e.g. partition problems): pin element 0, enumerate n-1 free bits.
inline void for_mask_fixed0(int n, const function<void(int)>& f) {
    for (int mask = 0; mask < (1 << (n - 1)); mask++) f(mask);
}
