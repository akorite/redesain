// CSES 1091 Concert Tickets: multiset lower_bound is the STL's first_true.
#include <iostream>
#include <set>
using namespace std;
int main(){
    int n, m; cin >> n >> m;
    multiset<int> prices;
    for(int i = 0, x; i < n; i++){ cin >> x; prices.insert(x); }
    while(m--){
        int t; cin >> t;
        auto it = prices.upper_bound(t);          // first element > t
        if(it == prices.begin()){ cout << -1 << '\n'; continue; }
        --it;                                     // last element <= t
        cout << *it << '\n';
        prices.erase(it);
    }
}
