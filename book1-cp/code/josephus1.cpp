// CSES 2162 Josephus Problem I: queue rotation removes every second child.
#include <iostream>
#include <queue>
using namespace std;
int main(){
    int n; cin >> n;
    queue<int> q;
    for(int i = 1; i <= n; i++) q.push(i);
    bool skip = false;
    while(!q.empty()){
        int c = q.front(); q.pop();
        if(skip) cout << c << ' ';
        else q.push(c);
        skip = !skip;
    }
    cout << '\n';
}
