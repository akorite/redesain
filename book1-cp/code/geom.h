// geom.h -- integer-geometry primitives for contests.
// Everything is exact: orientation via the cross product, no floats
// until the very last digit of an answer truly demands one.
#include <algorithm>
#include <numeric>
#include <vector>
#include <cstdlib>
using namespace std;
using ll = long long;

struct Pt {
    ll x, y;
    bool operator<(const Pt& o) const { return x != o.x ? x < o.x : y < o.y; }
    bool operator==(const Pt& o) const { return x == o.x && y == o.y; }
};
inline Pt operator-(Pt a, Pt b) { return {a.x - b.x, a.y - b.y}; }
inline ll cross(Pt a, Pt b) { return a.x * b.y - a.y * b.x; }
// orientation of (o->a, o->b): >0 left turn, <0 right turn, 0 collinear
inline ll orient(Pt o, Pt a, Pt b) { return cross(a - o, b - o); }

// p on segment ab (assumes collinearity is handled/checked)
inline bool on_seg(Pt p, Pt a, Pt b) {
    return min(a.x, b.x) <= p.x && p.x <= max(a.x, b.x) &&
           min(a.y, b.y) <= p.y && p.y <= max(a.y, b.y);
}

// proper or touching intersection of segments ab and cd
inline bool seg_int(Pt a, Pt b, Pt c, Pt d) {
    ll o1 = orient(a, b, c), o2 = orient(a, b, d);
    ll o3 = orient(c, d, a), o4 = orient(c, d, b);
    // touching: an endpoint lies on the other segment (covers collinear overlap)
    if (o1 == 0 && on_seg(c, a, b)) return true;
    if (o2 == 0 && on_seg(d, a, b)) return true;
    if (o3 == 0 && on_seg(a, c, d)) return true;
    if (o4 == 0 && on_seg(b, c, d)) return true;
    if (o1 == 0 || o2 == 0 || o3 == 0 || o4 == 0) return false;
    return ((o1 > 0) != (o2 > 0)) && ((o3 > 0) != (o4 > 0));
}

// twice signed polygon area (CCW positive)
inline ll area2(const vector<Pt>& p) {
    ll s = 0;
    int n = p.size();
    for (int i = 0; i < n; i++) {
        Pt u = p[i], v = p[(i + 1) % n];
        s += u.x * v.y - v.x * u.y;
    }
    return s > 0 ? s : -s;               // absolute value version
}

// lattice points on the boundary: sum over edges of gcd(|dx|,|dy|)
inline ll boundary_pts(const vector<Pt>& p) {
    ll B = 0;
    int n = p.size();
    for (int i = 0; i < n; i++) {
        Pt d = p[(i + 1) % n] - p[i];
        ll g = std::gcd(std::abs(d.x), std::abs(d.y));
        B += g;
    }
    return B;
}

// point in polygon: 0 inside, 1 boundary, 2 outside  (ray cast +x)
inline int in_poly(Pt q, const vector<Pt>& p) {
    int n = p.size();
    bool inside = false;
    for (int i = 0; i < n; i++) {
        Pt a = p[i], b = p[(i + 1) % n];
        if (orient(a, b, q) == 0 && on_seg(q, a, b)) return 1;
        // does edge (a,b) cross the horizontal ray q -> +inf ?
        if ((a.y > q.y) != (b.y > q.y) &&
            orient(q, a, b) > 0 == (a.y > q.y)) inside = !inside;
    }
    return inside ? 0 : 2;
}

// Andrew monotone chain, CCW hull including collinear boundary points
inline vector<Pt> hull(vector<Pt> p) {
    sort(p.begin(), p.end());
    p.erase(unique(p.begin(), p.end()), p.end());
    int n = p.size();
    if (n <= 2) return p;
    vector<Pt> h;
    for (int half = 0; half < 2; half++) {
        int base = h.size();
        for (int i = 0; i < n; i++) {
            Pt q = p[half ? n - 1 - i : i];
            while (h.size() > (size_t)base + 1 &&
                   orient(h[h.size() - 2], h.back(), q) < 0)
                h.pop_back();
            h.push_back(q);
        }
        h.pop_back();
    }
    return h;
}

// squared distances -- the only distances integer geometry needs
inline ll dist2(Pt a, Pt b) {
    ll dx = a.x - b.x, dy = a.y - b.y;
    return dx * dx + dy * dy;
}
// point-to-segment squared distance as an exact fraction:
// returns (num, den) with the real distance = sqrt(num/den).
// Compare num1*den2 vs num2*den1 to order two distances with no floats.
inline pair<ll,ll> seg_dist2(Pt q, Pt a, Pt b) {
    Pt ab = b - a, aq = q - a;
    ll den = dist2(a, b);
    if (den == 0) return {dist2(q, a), 1};
    ll num = aq.x * ab.x + aq.y * ab.y;  // dot product
    if (num <= 0) return {dist2(q, a), 1};
    if (num >= den) return {dist2(q, b), 1};
    ll c = cross(ab, aq);                // height = |cross| / |ab|
    return {c * c, den};
}
