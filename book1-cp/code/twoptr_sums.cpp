// twoptr_sums.cpp -- CSES Subarray Sums I: all values must be positive.
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n; long long x;
    cin >> n >> x;
    vector<long long> a(n);
    for (auto &v : a) cin >> v;
    int cnt = 0; long long sum = 0;
    for (int l = 0, r = 0; r < n; r++) {
        sum += a[r];
        while (sum > x) sum -= a[l++];
        if (sum == x) cnt++;
    }
    cout << cnt << "\n";
}
