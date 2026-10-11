// cowroad.cpp -- USACO 2017 Feb Gold "Why Did the Cow Cross the Road" (visitfj).
// Every crossing costs T; Bessie eats on every 3rd field she lands on
// (moves 3,6,9,...), including FJ's field when arrival is a multiple of 3.
// State (r,c,k), k = moves mod 3; Dijkstra over the 3-layer grid.
#include <queue>
#include <tuple>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;
using W = long long;
const W INF = (W)4e18;

int main() {
    int n; W T;
    if (scanf("%d %lld", &n, &T) != 2) return 0;
    vector<vector<W>> a(n, vector<W>(n));
    for (auto& r : a) for (auto& x : r) scanf("%lld", &x);
    vector dist(n, vector(n, vector<W>(3, INF)));
    using T3 = tuple<W,int,int,int>;
    priority_queue<T3, vector<T3>, greater<T3>> pq;
    dist[0][0][0] = 0; pq.push({0,0,0,0});
    const int dr[4] = {-1,1,0,0}, dc[4] = {0,0,-1,1};
    while (!pq.empty()) {
        auto [d,r,c,k] = pq.top(); pq.pop();
        if (d != dist[r][c][k]) continue;
        for (int i = 0; i < 4; i++) {
            int nr=r+dr[i], nc=c+dc[i];
            if (nr<0||nr>=n||nc<0||nc>=n) continue;
            int nk=(k+1)%3;
            W w = T + (k==2 ? a[nr][nc] : 0);   // landing on move 3k eats
            if (d+w < dist[nr][nc][nk]) { dist[nr][nc][nk]=d+w; pq.push({d+w,nr,nc,nk}); }
        }
    }
    printf("%lld\n", *min_element(dist[n-1][n-1].begin(), dist[n-1][n-1].end()));
}
