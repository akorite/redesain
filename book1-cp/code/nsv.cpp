// nsv.cpp -- CSES Nearest Smaller Values (1-indexed output, 0 if none).
#include <iostream>
#include <vector>
#include "monostack.h"
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (auto &x : a) cin >> x;
    auto L = nearest_smaller_left(a);
    for (int i = 0; i < n; i++)
        cout << L[i] + 1 << " \n"[i + 1 == n];
}
