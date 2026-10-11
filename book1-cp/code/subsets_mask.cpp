// subsets_mask.cpp -- enumerate all subsets of {1,..,n} with bitmasks.
// mask bit k set <=> element k+1 is in the subset.
#include <iostream>
using namespace std;

int main() {
    int n = 3;
    for (int mask = 0; mask < (1 << n); mask++) {
        cout << "{";
        bool first = true;
        for (int k = 0; k < n; k++)
            if (mask & (1 << k)) {
                cout << (first ? "" : ", ") << k + 1;
                first = false;
            }
        cout << "}\n";
    }
    return 0;
}
