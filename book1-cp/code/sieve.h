// sieve.h -- smallest-prime-factor table: spf[i] = least prime
// dividing i; factorize in O(log n) per query.
#include <vector>
using namespace std;
inline vector<int> spf_sieve(int n) {
    vector<int> spf(n + 1);
    for (int i = 1; i <= n; i++) spf[i] = i;
    for (int i = 2; (long long)i * i <= n; i++)
        if (spf[i] == i)
            for (long long j = (long long)i * i; j <= n; j += i)
                if (spf[j] == j) spf[j] = i;
    return spf;
}
// factorize x via spf: (prime, exponent) pairs
inline vector<pair<int,int>> factorize(long long x, const vector<int>& spf) {
    vector<pair<int,int>> f;
    while (x > 1) {
        int p = spf[x], e = 0;
        while (x % p == 0) { x /= p; e++; }
        f.push_back({p, e});
    }
    return f;
}
