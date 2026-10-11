// missing_int.cpp -- the deliberately broken submission of Worked Example 1.4.
// Bug: every quantity is int; n*(n+1)/2 overflows once n > ~46000.
#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int total = n * (n + 1) / 2;
    int sum = 0;
    for (int i = 0; i < n - 1; ++i) {
        int x;
        cin >> x;
        sum += x;
    }
    cout << total - sum << '\n';
}
