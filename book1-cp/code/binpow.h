// binpow.h -- a^b mod m in O(log b): square-and-multiply by bits.
inline long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long r = 1;
    for (; b > 0; b >>= 1) {
        if (b & 1) r = r * a % m;
        a = a * a % m;
    }
    return r;
}
