// point_location.cpp -- CSES 2189: which side of line p1->p2 is p3?
#include "geom.h"
#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        Pt p, q, r;
        scanf("%lld %lld %lld %lld %lld %lld", &p.x, &p.y, &q.x, &q.y, &r.x, &r.y);
        ll o = orient(p, q, r);
        puts(o > 0 ? "LEFT" : o < 0 ? "RIGHT" : "TOUCH");
    }
}
