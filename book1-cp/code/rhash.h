// rhash.h -- polynomial rolling hash, two moduli, prefix-hash queries.
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
struct RH {
    static const long long B  = 91138233;
    static const long long M1 = 972663749;
    static const long long M2 = 998244353;
    vector<long long> h1, h2, p1, p2;
    int n;
    RH(const string& s) {
        n = (int)s.size();
        h1.assign(n + 1, 0); h2.assign(n + 1, 0);
        p1.assign(n + 1, 1); p2.assign(n + 1, 1);
        for (int i = 0; i < n; i++) {
            h1[i+1] = (h1[i] * B + (unsigned char)s[i]) % M1;
            h2[i+1] = (h2[i] * B + (unsigned char)s[i]) % M2;
            p1[i+1] = p1[i] * B % M1;
            p2[i+1] = p2[i] * B % M2;
        }
    }
    pair<long long,long long> get(int l, int r) const {   // hash of s[l..r)
        long long x1 = (h1[r] - h1[l] * p1[r - l]) % M1; if (x1 < 0) x1 += M1;
        long long x2 = (h2[r] - h2[l] * p2[r - l]) % M2; if (x2 < 0) x2 += M2;
        return {x1, x2};
    }
    int lcp(int i, int j) const {                          // LCP of suffixes i, j
        int lo = 0, hi = min(n - i, n - j);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (get(i, i + mid) == get(j, j + mid)) lo = mid; else hi = mid - 1;
        }
        return lo;
    }
};
