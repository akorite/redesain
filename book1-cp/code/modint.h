// modint.h -- modular int for mod 1e9+7: the class you write once.
// PITFALL: (a-b) needs +m before %; a*b needs long long inside.
struct mint {
    static const long long M = 1000000007;
    long long v;
    mint(long long x = 0) : v((x % M + M) % M) {}
    mint operator+(mint o) const { return mint(v + o.v); }
    mint operator-(mint o) const { return mint(v - o.v); }
    mint operator*(mint o) const { return mint(v * o.v % M); }
    mint pow(long long b) const {
        long long r = 1, a = v;
        for (; b > 0; b >>= 1) {
            if (b & 1) r = r * a % M;
            a = a * a % M;
        }
        return mint(r);
    }
    mint inv() const { return pow(M - 2); }      // Fermat: a^{p-2}
    mint operator/(mint o) const { return *this * o.inv(); }
};
