// missing_math.cpp -- CSES "Missing Number" by the sum trick (fixed 64-bit).
#include <iostream>
using namespace std;
using ll = long long;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    ll total = n * (n + 1) / 2;
    ll sum = 0;
    for (int i = 0; i < n - 1; ++i) {
        ll x;
        cin >> x;
        sum += x;
    }
    cout << total - sum << '\n';
}
