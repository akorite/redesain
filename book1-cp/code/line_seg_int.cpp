// line_seg_int.cpp -- CSES 2190: do segments ab and cd intersect?
#include "geom.h"
#include <cstdio>
int main() {
    int t; scanf("%d", &t);
    while (t--) {
        Pt a, b, c, d;
        scanf("%lld %lld %lld %lld %lld %lld %lld %lld",
              &a.x, &a.y, &b.x, &b.y, &c.x, &c.y, &d.x, &d.y);
        puts(seg_int(a, b, c, d) ? "YES" : "NO");
    }
}
