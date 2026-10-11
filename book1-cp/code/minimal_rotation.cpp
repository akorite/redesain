// CSES 1110 Minimal Rotation -- lexicographically smallest rotation.
// Compare rotations of s as length-n windows of s+s via double hash
// + binary-search LCP: O(n log n) comparisons, no suffix structures.
#include "rhash.h"
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string s; cin >> s;
    int n = s.size();
    string t = s + s;
    RH H(t);
    int best = 0;
    for (int i = 1; i < n; i++) {
        int d = H.lcp(best, i);
        if (d < n && t[i + d] < t[best + d]) best = i;
    }
    printf("%s\n", (s.substr(best) + s.substr(0, best)).c_str());
}
