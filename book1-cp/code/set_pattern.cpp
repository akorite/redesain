// set_pattern.cpp -- "best available" with std::set (CSES Concert Tickets).
// For each customer price: sell the most expensive seat <= price.
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    multiset<int> seats;                     // duplicates exist -> multiset
    for (int i = 0, h; i < n; i++) { cin >> h; seats.insert(h); }
    for (int i = 0, t; i < m; i++) {
        cin >> t;
        auto it = seats.upper_bound(t);      // first seat > t
        if (it == seats.begin()) { cout << "-1\n"; continue; }
        --it;                                // largest seat <= t
        cout << *it << "\n";
        seats.erase(it);                     // erase ONE copy via iterator
    }
}
