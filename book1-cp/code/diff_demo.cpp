// diff_demo.cpp -- range updates, then one prefix-restore.
#include <iostream>
#include "diff.h"
using namespace std;

int main() {
    Diff1D d(8);
    cout << "updates: [2,4]+3, [1,3]+5, [6,7]+2\n";
    d.add(2, 4, 3); d.add(1, 3, 5); d.add(6, 7, 2);
    auto a = d.restore();
    cout << "restored:";
    for (ll v : a) cout << ' ' << v;
    cout << "\n";
}
