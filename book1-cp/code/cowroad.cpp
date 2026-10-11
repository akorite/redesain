// cowroad.cpp -- USACO-G Why Did the Cow Cross the Road.
// Boundary between different labels consumes a crossing ticket;
// each ticket covers 3 crossings.  State (r,c,k) k=ticket crossings used.
#include <queue>
#include <tuple>
#include <vector>
using namespace std;
using W = long long;
const W INF = (W)4e18;

int main() {
    int n; W T;
    if (scanf("%d %lld", &n, &T) != 2) return 0;
    vector<vector<int>> a(n, vector<int>(n));
    for (auto& r : a) for (auto& x : r) scanf("%d", &x);
    // dist[r][c][k]
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
            if (a[nr][nc] == a[r][c]) {              // same pasture
                if (d+1 < dist[nr][nc][k]) { dist[nr][nc][k]=d+1; pq.push({d+1,nr,nc,k}); }
            } else if (k < 2) {                    // same ticket, k-th crossing
                if (d+1 < dist[nr][nc][k+1]) { dist[nr][nc][k+1]=d+1; pq.push({d+1,nr,nc,k+1}); }
            } else {                               // third crossing pays toll T
                if (d+1+T < dist[nr][nc][0]) { dist[nr][nc][0]=d+1+T; pq.push({d+1+T,nr,nc,0}); }
            }
        }
    }
    W ans = *min_element(dist[n-1][n-1].begin(), dist[n-1][n-1].end());
    printf("%lld\n", ans);
}
