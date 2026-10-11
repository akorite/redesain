// CSES 2205 Gray Code: reflected construction, one bit position at a time.
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
    int n; cin >> n;
    vector<string> g = {"0","1"};
    for(int len = 2; len <= n; len++){
        vector<string> h;
        h.reserve(1 << len);
        for(int i = 0; i < (int)g.size(); i++) h.push_back("0" + g[i]);
        for(int i = (int)g.size() - 1; i >= 0; i--) h.push_back("1" + g[i]);
        g = h;
    }
    for(auto& c : g) cout << c << '\n';
}
