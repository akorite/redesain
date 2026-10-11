// dsu.h -- disjoint set union: path halving + union by size + sizes.
#include <numeric>
#include <vector>
using namespace std;

struct DSU {
    vector<int> p, sz;
    DSU(int n) : p(n + 1), sz(n + 1, 1) { iota(p.begin(), p.end(), 0); }
    int find(int v) {                        // path halving
        while (p[v] != v) { p[v] = p[p[v]]; v = p[v]; }
        return v;
    }
    bool unite(int a, int b) {               // false if same set
        a = find(a); b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b);
        p[b] = a; sz[a] += sz[b];
        return true;
    }
    int size(int v) { return sz[find(v)]; }
};
