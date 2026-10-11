// lazyseg.h -- recursive lazy segtree: range add, range sum.
#include <vector>
using namespace std;
struct LazySeg {
    int n; vector<long long> sum, tag;
    LazySeg(const vector<long long>& a) : n(a.size()) {
        sum.assign(4 * n, 0); tag.assign(4 * n, 0);
        build(a, 1, 0, n - 1);
    }
    void build(const vector<long long>& a, int v, int l, int r) {
        if (l == r) { sum[v] = a[l]; return; }
        int m = (l + r) / 2;
        build(a, 2*v, l, m); build(a, 2*v+1, m+1, r);
        sum[v] = sum[2*v] + sum[2*v+1];
    }
    void push(int v, int l, int r) {
        if (!tag[v]) return;
        int m = (l + r) / 2;
        apply(2*v, l, m, tag[v]); apply(2*v+1, m+1, r, tag[v]);
        tag[v] = 0;
    }
    void apply(int v, int l, int r, long long d) {
        sum[v] += d * (r - l + 1); tag[v] += d;
    }
    void add(int v, int l, int r, int ql, int qr, long long d) {
        if (ql <= l && r <= qr) { apply(v, l, r, d); return; }
        push(v, l, r); int m = (l + r) / 2;
        if (ql <= m) add(2*v, l, m, ql, qr, d);
        if (qr > m) add(2*v+1, m+1, r, ql, qr, d);
        sum[v] = sum[2*v] + sum[2*v+1];
    }
    long long query(int v, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return sum[v];
        push(v, l, r); int m = (l + r) / 2;
        long long s = 0;
        if (ql <= m) s += query(2*v, l, m, ql, qr);
        if (qr > m) s += query(2*v+1, m+1, r, ql, qr);
        return s;
    }
    void add(int l, int r, long long d) { add(1, 0, n - 1, l, r, d); }
    long long query(int l, int r) { return query(1, 0, n - 1, l, r); }
};
