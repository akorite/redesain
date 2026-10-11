// kruskal.h -- sort edges, DSU-filter, accept. Returns MST weight.
#include "dsu.h"
#include <algorithm>
#include <vector>
using namespace std;
using W = long long;
struct KEdge { int u, v; int w; };

inline W kruskal(int n, vector<KEdge> E, vector<KEdge>* mst = nullptr) {
    sort(E.begin(), E.end(),
         [](const KEdge& a, const KEdge& b) { return a.w < b.w; });
    DSU d(n);
    W total = 0;
    for (auto& e : E)
        if (d.unite(e.u, e.v)) {
            total += e.w;
            if (mst) mst->push_back(e);
        }
    return total;
}
