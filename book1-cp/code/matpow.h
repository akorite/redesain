// matpow.h -- 2x2 matrix power mod 1e9+7: [[a,b],[c,d]].
// Linear recurrences become exponentiation: Fibonacci by [[1,1],[1,0]]^n.
#include "binpow.h"
#include <array>
using M2 = std::array<std::array<long long,2>,2>;
inline M2 mmul(M2 a, M2 b, long long m) {
    M2 r = {};
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++)
                r[i][j] = (r[i][j] + a[i][k] * b[k][j]) % m;
    return r;
}
inline M2 mpow(M2 a, long long b, long long m) {
    M2 r = {{{1,0},{0,1}}};
    for (; b > 0; b >>= 1) {
        if (b & 1) r = mmul(r, a, m);
        a = mmul(a, a, m);
    }
    return r;
}
