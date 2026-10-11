// convex_hull.cpp -- CSES 2195: hull size + vertices, boundary included
#include "geom.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<Pt> p(n);
    for (auto& q : p) scanf("%lld %lld", &q.x, &q.y);
    vector<Pt> h = hull(p);
    printf("%d\n", (int)h.size());
    for (auto& q : h) printf("%lld %lld\n", q.x, q.y);
}
