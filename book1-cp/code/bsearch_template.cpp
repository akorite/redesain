// bsearch_template.cpp -- the template + lower_bound on a real array.
#include <algorithm>
#include <iostream>
#include <vector>
#include "lib/bsearch.h"
using namespace std;

int main() {
    vector<int> a = {2, 4, 7, 7, 11};
    int t = 7;
    ll i = first_true(0, (ll)a.size() - 1, [&](ll i){ return a[i] >= t; });
    ll j = first_true(0, (ll)a.size() - 1, [&](ll i){ return a[i] >  t; });
    cout << "first >= " << t << " at index " << i
         << " (a[" << i << "]=" << a[i] << ")\n";
    cout << "first >  " << t << " at index " << j
         << " (a[" << j << "]=" << a[j] << ")\n";
    cout << "lower_bound agrees: "
         << (lower_bound(a.begin(), a.end(), t) - a.begin()) << "\n";
}
