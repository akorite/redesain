// ferris_wheel.cpp -- pair lightest + heaviest, else heaviest rides alone.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    long long x;
    cin >> n >> x;
    vector<long long> p(n);
    for (auto &w : p) cin >> w;
    sort(p.begin(), p.end());
    int i = 0, j = n - 1, g = 0;
    while (i <= j) {
        if (p[i] + p[j] <= x) i++;           // lightest fits with heaviest
        j--;                                 // heaviest always boards now
        g++;
    }
    cout << g << "\n";
}
