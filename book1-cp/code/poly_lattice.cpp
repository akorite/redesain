// poly_lattice.cpp -- CSES 2193: interior + boundary lattice points (Pick)
#include "geom.h"
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    vector<Pt> p(n);
    for (auto& q : p) scanf("%lld %lld", &q.x, &q.y);
    ll B = boundary_pts(p);
    ll I = (area2(p) - B + 2) / 2;         // A = I + B/2 - 1
    printf("%lld %lld\n", I, B);
}
