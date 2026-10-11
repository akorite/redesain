// weird.cpp -- CSES "Weird Algorithm": simulate until 1. Needs 64 bits.
#include <iostream>
using namespace std;
using ll = long long;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    while (n != 1) {
        cout << n << ' ';
        n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
    }
    cout << 1 << '\n';
}
