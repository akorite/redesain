// orderstat.h -- k-th element by descent on a Fenwick of counts:
// delete position k => find i with count-prefix == k, then add(i,-1).
#include "fenwick.h"
struct OrderStat {
    Fenwick f;
    OrderStat(int n) : f(n) { for (int i = 1; i <= n; i++) f.add(i, 1); }
    int kth(long long k) const { return f.lower_bound(k); }
    void erase_at(long long k) { int i = f.lower_bound(k); f.add(i, -1); }
};
