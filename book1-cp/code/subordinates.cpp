#include <vector>
#include <cstdio>
using namespace std;
int main() {
    int n; scanf("%d", &n);
    vector<vector<int>> ch(n+1);
    for (int v = 2; v <= n; v++) { int b; scanf("%d",&b); ch[b].push_back(v); }
    vector<int> sz(n+1,0), st = {1}, ord;
    while (!st.empty()) { int v = st.back(); st.pop_back(); ord.push_back(v);
        for (int u : ch[v]) st.push_back(u); }
    for (int i = ord.size()-1; i >= 0; i--) {
        sz[ord[i]] = 0; for (int u : ch[ord[i]]) sz[ord[i]] += 1 + sz[u]; }
    for (int i = 1; i <= n; i++) printf("%d%c", sz[i], " \n"[i==n]);
}
