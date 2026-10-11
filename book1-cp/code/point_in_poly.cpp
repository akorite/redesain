// point_in_poly.cpp -- CSES 2192: INSIDE / OUTSIDE / BOUNDARY
#include "geom.h"
#include <cstdio>
int main() {
    int n, m; scanf("%d %d", &n, &m);
    vector<Pt> p(n);
    for (auto& q : p) scanf("%lld %lld", &q.x, &q.y);
    while (m--) {
        Pt q; scanf("%lld %lld", &q.x, &q.y);
        puts((const char*[]){"INSIDE", "BOUNDARY", "OUTSIDE"}[in_poly(q, p)]);
    }
}
