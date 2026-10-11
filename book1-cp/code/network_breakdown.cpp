// CSES 1677 Network Breakdown: read removals, play them backwards with DSU.
#include <iostream>
#include <vector>
#include <set>
#include <utility>
using namespace std;
int par[100005], sz[100005];
int find(int x){ return par[x] == x ? x : par[x] = find(par[x]); }
bool uni(int a, int b){
    a = find(a); b = find(b);
    if(a == b) return false;
    if(sz[a] < sz[b]) swap(a, b);
    par[b] = a; sz[a] += sz[b]; return true;
}
int main(){
    int n, m, q; cin >> n >> m >> q;
    vector<pair<int,int>> qr(q);
    set<pair<int,int>> alive;
    for(int i = 0, a, b; i < m; i++){
        cin >> a >> b; if(a > b) swap(a,b); alive.insert({a,b});
    }
    for(auto& [a,b] : qr){
        cin >> a >> b; if(a > b) swap(a,b); alive.erase({a,b});
    }
    for(int i = 1; i <= n; i++){ par[i] = i; sz[i] = 1; }
    int comps = n;
    for(auto [a,b] : alive) comps -= uni(a,b);   // edges that never break
    vector<int> ans(q);
    for(int i = q - 1; i >= 0; i--){
        ans[i] = comps;
        comps -= uni(qr[i].first, qr[i].second); // "un-remove" the edge
    }
    for(int x : ans) cout << x << ' ';
    cout << '\n';
}
