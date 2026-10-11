// CSES 1733 Finding Periods -- all period lengths k, 1 <= k <= n.
// k is a period of s iff n - k is a border length of s (or k == n).
#include "kmp.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    string s; cin >> s;
    int n = (int)s.size();
    vector<int> pi = prefix_function(s), ans;
    for (int j = pi[n - 1]; j > 0; j = pi[j - 1]) ans.push_back(n - j);
    ans.push_back(n);
    sort(ans.begin(), ans.end());
    for (int i = 0; i < (int)ans.size(); i++) printf("%d%c", ans[i], " \n"[i + 1 == (int)ans.size()]);
}
