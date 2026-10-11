// creating_strings.cpp -- CSES Creating Strings.
// All distinct permutations of a word, alphabetically sorted.
// next_permutation visits each distinct permutation of a multiset once,
// so duplicate letters need no special handling -- just sort first.
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string s;
    cin >> s;
    sort(s.begin(), s.end());     // mandatory: start from smallest

    vector<string> out;
    do {
        out.push_back(s);
    } while (next_permutation(s.begin(), s.end()));

    cout << out.size() << "\n";
    for (auto& t : out) cout << t << "\n";
    return 0;
}
