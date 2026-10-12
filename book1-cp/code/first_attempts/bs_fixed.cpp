#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int> a = {1, 3, 5, 7, 9};
    int target = 6;
    int lo = 0, hi = (int)a.size() - 1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] >= target) hi = mid; else lo = mid + 1;
        cout << "lo=" << lo << " hi=" << hi << "\n";
    }
    cout << "first index with a[i] >= 6: " << lo << " (value " << a[lo] << ")\n";
}
