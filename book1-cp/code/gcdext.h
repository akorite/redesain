// gcdext.h -- extended Euclidean algorithm: returns (g, x, y) with
// ax + by = g = gcd(a,b). Invariant: every step's pair is an integer
// combination of (a,b); termination by strictly decreasing remainder.
#include <tuple>
using namespace std;
inline tuple<long long,long long,long long> gcdext(long long a, long long b) {
    if (b == 0) return {a, 1, 0};
    auto [g, x, y] = gcdext(b, a % b);
    return {g, y, x - (a / b) * y};
}
// modular inverse of a mod m (needs gcd(a,m)=1)
inline long long inv(long long a, long long m) {
    auto [g, x, y] = gcdext(a, m);
    (void)y;
    return ((x % m) + m) % m;
}
