// floyd.h -- all-pairs shortest paths, O(n^3); next[][] reconstructs.
#include <vector>
using namespace std;
using W = long long;
const W FW_INF = (W)4e18;

// dist: n+1 x n+1 matrix (FW_INF = no edge, dist[i][i]=0).
// next[i][j]: first hop from i toward j; -1 when unreachable.
inline void floyd(int n, vector<vector<W>>& dist,
                  vector<vector<int>>& nxt) {
    nxt.assign(n + 1, vector<int>(n + 1, -1));
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (dist[i][j] < FW_INF) nxt[i][j] = j;
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (dist[i][k] < FW_INF && dist[k][j] < FW_INF &&
                    dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                    nxt[i][j] = nxt[i][k];
                }
}
