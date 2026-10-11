// ncr.h -- nCk mod p via precomputed factorials and inverse factorials.
#include "modint.h"
#include <vector>
using namespace std;
struct NCR {
    vector<mint> f, fi;
    NCR(int n) : f(n + 1), fi(n + 1) {
        f[0] = 1;
        for (int i = 1; i <= n; i++) f[i] = f[i - 1] * i;
        fi[n] = f[n].inv();
        for (int i = n; i > 0; i--) fi[i - 1] = fi[i] * i;
    }
    mint choose(int n, int k) const {
        if (k < 0 || k > n) return mint(0);
        return f[n] * fi[k] * fi[n - k];
    }
};
