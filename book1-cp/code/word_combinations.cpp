// CSES 1731 Word Combinations -- number of ways to split s into dict
// words, mod 1e9+7. dp[i] counts splittings of s[i..n); a trie walk
// from i adds dp[i + len] for every word found on the path.
#include "trie.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
const long long MOD = 1000000007;
int main() {
    string s; int k; cin >> s >> k;
    Trie tr;
    for (int i = 0; i < k; i++) { string w; cin >> w; tr.insert(w); }
    int n = s.size();
    vector<long long> dp(n + 1, 0); dp[n] = 1;
    for (int i = n - 1; i >= 0; i--) {
        int u = tr.root();
        for (int j = i; j < n; j++) {
            u = tr.next(u, s[j]);
            if (!u) break;
            dp[i] = (dp[i] + (long long)tr.count(u) * dp[j + 1]) % MOD;
        }
    }
    printf("%lld\n", dp[0]);
}
