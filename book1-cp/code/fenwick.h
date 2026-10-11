// fenwick.h -- Fenwick (binary indexed) tree: point add, prefix sum,
// and lower_bound descent (first index with prefix sum >= target).
#include <vector>
using namespace std;
struct Fenwick {
    int n; vector<long long> t;
    Fenwick(int n) : n(n), t(n + 1, 0) {}
    void add(int i, long long v) { for (; i <= n; i += i & -i) t[i] += v; }
    long long sum(int i) const {
        long long s = 0;
        for (; i > 0; i -= i & -i) s += t[i];
        return s;
    }
    long long sum(int l, int r) const { return sum(r) - sum(l - 1); }
    // smallest i with prefix sum >= k (needs non-negative values)
    int lower_bound(long long k) const {
        int i = 0, b = 1;
        for (; b <= n; b <<= 1) ;
        for (int s = b >> 1; s; s >>= 1)
            if (i + s <= n && t[i + s] < k) { i += s; k -= t[i]; }
        return i + 1;
    }
};
