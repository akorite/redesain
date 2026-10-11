// hash_demo.cpp -- where collisions live: hunt a real colliding pair
// under (B=26, p=97), then show the same pair separates under the
// moduli used by RH. Deterministic search, real output.
#include <cstdio>
#include <string>
#include <map>
using namespace std;
long long h(const string& s, long long B, long long P) {
    long long x = 0;
    for (char c : s) x = (x * B + (c - 'a' + 1)) % P;
    return x;
}
int main() {
    // enumerate all 3-letter strings until (B=26, p=97) collides
    map<long long, string> seen;
    string a, b;
    for (int i = 0; i < 26 * 26 * 26; i++) {
        string w = {char('a' + i / 676), char('a' + (i / 26) % 26), char('a' + i % 26)};
        long long x = h(w, 26, 97);
        if (seen.count(x) && seen[x] != w) { a = seen[x]; b = w; break; }
        seen[x] = w;
    }
    printf("mod 97, base 26: \"%s\" and \"%s\" both hash to %lld\n",
           a.c_str(), b.c_str(), h(a, 26, 97));
    printf("same pair, mod 1e9+7:   %lld vs %lld\n", h(a, 26, 1000000007), h(b, 26, 1000000007));
    printf("same pair, mod 998244353: %lld vs %lld\n", h(a, 26, 998244353), h(b, 26, 998244353));
    // birthday count: 4096 random 8-letter strings, one modulus vs two
    map<long long, int> mid;
    map<pair<long long,long long>, int> both;
    unsigned rng = 1;
    for (int i = 0; i < 8192; i++) {
        string w;
        for (int j = 0; j < 8; j++) { rng = rng * 1103515245 + 12345; w += 'a' + (rng / 65536) % 26; }
        mid[h(w, 91138233, 9726647)]++;
        both[{h(w, 91138233, 972663749), h(w, 91138233, 998244353)}]++;
    }
    int c1 = 0, c2 = 0;
    for (auto& e : mid) c1 += e.second - 1;
    for (auto& e : both) c2 += e.second - 1;
    printf("8192 8-letter strings: %d extra hashes collide mod 9726647 (birthday), %d under the RH pair\n", c1, c2);
}
