#include <iostream>
#include <vector>
using namespace std;
// Find the first index whose value is >= target in a sorted array.
int main() {
    vector<int> a = {1, 3, 5, 7, 9};
    int target = 6;
    int lo = 0, hi = (int)a.size() - 1, steps = 0;
    while (lo < hi && steps < 8) {            // cap added only so this demo stops
        int mid = (lo + hi) / 2;
        if (a[mid] >= target) hi = mid; else lo = mid;   // naive: lo = mid
        cout << "lo=" << lo << " hi=" << hi << "\n";
        steps++;
    }
    cout << (steps == 8 ? "stuck: never terminates" : "done") << "\n";
}
