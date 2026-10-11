// digitdp.h -- count x in [0,N] with no two adjacent equal digits.
// States: (pos, tight, leading, prev-digit); memoized on digits of N.
// `leading` marks "no real digit emitted yet" so shorter numbers are
// handled uniformly and a leading zero is never compared as a digit.
#include <cstring>
#include <functional>
#include <vector>
using namespace std;
inline long long count_digits(long long N) {
    if (N < 0) return 0;
    vector<int> d;
    for (long long t = N; t; t /= 10) d.push_back(t % 10);
    if (d.empty()) return 1;                 // N=0 counts the number 0
    int L = d.size();
    static long long memo[20][2][2][11];
    memset(memo, -1, sizeof memo);
    function<long long(int,int,int,int)> go =
        [&](int pos, int tight, int leading, int prev) -> long long {
        if (pos < 0) return 1;               // counted a valid number
        long long& r = memo[pos][tight][leading][prev];
        if (!tight && r >= 0) return r;      // only loose states memoize
        long long res = 0;
        int hi = tight ? d[pos] : 9;
        for (int dig = 0; dig <= hi; dig++) {
            if (!leading && dig == prev) continue;   // adjacent repeat
            res += go(pos - 1, tight && dig == hi,
                      leading && dig == 0, dig);
        }
        if (!tight) r = res;
        return res;
    };
    return go(L - 1, 1, 1, 0);
}
