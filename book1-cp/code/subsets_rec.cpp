// subsets_rec.cpp -- enumerate all subsets of {1,..,n} by recursion.
// Search tree: each level decides "take k" or "leave k".
#include <iostream>
#include <vector>
using namespace std;

int n;
vector<int> chosen;

void search(int k) {
    if (k == n + 1) {
        cout << "{";
        for (int i = 0; i < (int)chosen.size(); i++)
            cout << (i ? ", " : "") << chosen[i];
        cout << "}\n";
        return;
    }
    chosen.push_back(k);   // take k
    search(k + 1);
    chosen.pop_back();
    search(k + 1);         // leave k
}

int main() {
    n = 3;
    search(1);
    return 0;
}
