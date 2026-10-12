#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;                    // read how many numbers follow
    vector<int> a(n);            // a list of n integers
    for (int i = 0; i < n; i++)
        cin >> a[i];
    int total = 0;
    for (int x : a)
        total += x;              // add them up
    sort(a.begin(), a.end());    // smallest first
    cout << "sum = " << total << "\n";
    cout << "smallest = " << a[0] << ", largest = " << a[n - 1] << "\n";
}
