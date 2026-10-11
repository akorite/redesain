// missing_set.cpp -- CSES "Missing Number" by marking: no formula needed.
#include <iostream>
#include <vector>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<char> seen(n + 1, 0);
    for (int i = 0; i < n - 1; ++i) {
        int x;
        cin >> x;
        seen[x] = 1;
    }
    for (int v = 1; v <= n; ++v)
        if (!seen[v]) {
            cout << v << '\n';
            break;
        }
}
