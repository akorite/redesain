// digitdp.h -- count x in [0,N] whose decimal digits satisfy pred.
// States: (pos, tight, leading); skeleton memoized on digits of N.
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
    static long long memo[20][2][2];
    memset(memo, -1, sizeof memo);
    function<long long(int,int,int)> go = [&](int pos, int tight, int leading) -> long long {
        if (pos < 0) return 1;               // counted a valid number
        long long& r = memo[pos][tight][leading];
        if (r >= 0) return r;
        r = 0;
        int hi = tight ? d[pos] : 9;
        for (int dig = 0; dig <= hi; dig++)
            r += go(pos - 1, tight && dig == hi, leading && dig == 0);
        return r;
    };
    return go(L - 1, 1, 1);
}
