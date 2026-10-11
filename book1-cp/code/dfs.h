// dfs.h -- recursive DFS with visited set. Depth = component size;
// see tripwire on grid recursion (use iterative flood fill).
#pragma once
#include <vector>

inline void dfs(const std::vector<std::vector<int>>& g, int v,
                std::vector<char>& seen) {
    seen[v] = 1;
    for (int w : g[v])
        if (!seen[w]) dfs(g, w, seen);
}
