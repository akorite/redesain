// min_dist.cpp -- CSES 2194: minimum squared pairwise distance.
// Divide & conquer on x-sorted points; strip merge by y.
#include "geom.h"
#include <cstdio>
#include <functional>
int main() {
    int n; scanf("%d", &n);
    vector<Pt> p(n);
    for (auto& q : p) scanf("%lld %lld", &q.x, &q.y);
    sort(p.begin(), p.end());
    function<ll(int,int)> solve = [&](int l, int r) -> ll {
        if (r - l <= 1) return dist2(p[l], p[r]);
        if (r - l <= 2) {
            ll d = dist2(p[l], p[r]);
            d = min(d, min(dist2(p[l], p[l+1]), dist2(p[l+1], p[r])));
            return d;
        }
        int m = (l + r) / 2;
        ll mx = p[m].x;
        ll d = min(solve(l, m), solve(m, r));
        vector<Pt> strip;
        for (int i = l; i <= r; i++) {
            ll dx = p[i].x - mx;
            if (dx * dx < d) strip.push_back(p[i]);
        }
        sort(strip.begin(), strip.end(),
             [](Pt a, Pt b){ return a.y < b.y; });
        for (size_t i = 0; i < strip.size(); i++)
            for (size_t j = i + 1; j < strip.size() &&
                 (strip[j].y - strip[i].y) * (strip[j].y - strip[i].y) < d; j++)
                d = min(d, dist2(strip[i], strip[j]));
        return d;
    };
    printf("%lld\n", solve(0, n - 1));
}
