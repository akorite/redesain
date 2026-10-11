// permutations.h -- distinct permutations via next_permutation (capstone lib).
// Contract: always sort() first -- next_permutation only walks "upward"
// from the current arrangement, so an unsorted start silently drops perms.
// Duplicates are free: equal elements produce no duplicate permutations.
#pragma once
#include <algorithm>
#include <functional>
#include <string>
using namespace std;

template <class It>
inline void for_perm(It first, It last, const function<void()>& f) {
    sort(first, last);
    do { f(); } while (next_permutation(first, last));
}

inline void for_perm_str(string s, const function<void(const string&)>& f) {
    sort(s.begin(), s.end());
    do { f(s); } while (next_permutation(s.begin(), s.end()));
}
