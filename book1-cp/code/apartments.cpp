// apartments.cpp -- two pointers after sorting both lists.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

int main() {
    int n, m;
    ll k;
    cin >> n >> m >> k;
    vector<ll> a(n), b(m);
    for (ll &x : a) cin >> x;
    for (ll &x : b) cin >> x;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int i = 0, j = 0, given = 0;
    while (i < n && j < m) {
        if (b[j] < a[i] - k) j++;            // too small for everyone left
        else if (b[j] > a[i] + k) i++;       // too big for this applicant
        else { given++; i++; j++; }          // match: take it
    }
    cout << given << "\n";
}
