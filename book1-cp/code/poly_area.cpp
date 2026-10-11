// poly_area.cpp -- CSES 2191: print twice the polygon area
#include "geom.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<Pt> p(n);
    for (auto& q : p) scanf("%lld %lld", &q.x, &q.y);
    printf("%lld\n", area2(p));
}
