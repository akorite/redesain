// moving_robots.cpp -- CSES 1726: 8x8 grid, one robot per square,
// each turn every robot moves to a uniform random neighbour.
// E[empty squares] = sum_s prod_t (1 - p_{t->s}).
#include <cstdio>
#include <vector>
using namespace std;
int main() {
    int k; scanf("%d", &k);
    const int N = 64;
    vector<vector<int>> adj(N);
    auto id = [](int r, int c) { return r * 8 + c; };
    const int dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1};
    for (int r = 0; r < 8; r++) for (int c = 0; c < 8; c++)
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (0 <= nr && nr < 8 && 0 <= nc && nc < 8)
                adj[id(r, c)].push_back(id(nr, nc));
        }
    double expect = 0;
    for (int t = 0; t < N; t++) {          // robot starting at t
        vector<double> cur(N, 0), nxt;
        cur[t] = 1.0;
        for (int step = 0; step < k; step++) {
            nxt.assign(N, 0);
            for (int s = 0; s < N; s++)
                for (int v : adj[s]) nxt[v] += cur[s] / adj[s].size();
            cur = nxt;
        }
        // cur[s] = P(robot from t is on s).  We need prod over t of
        // (1 - p_{t->s}); accumulate per square.
        static double notempty[64] = {}; 
        if (t == 0) for (int s = 0; s < N; s++) notempty[s] = 1.0;
        for (int s = 0; s < N; s++) notempty[s] *= (1.0 - cur[s]);
        if (t == N - 1) for (int s = 0; s < N; s++) expect += notempty[s];
    }
    printf("%.6f\n", expect);
}
