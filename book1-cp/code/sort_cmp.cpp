// sort_cmp.cpp -- sorting with a lambda comparator + structured bindings.
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<pair<string,int>> team = {
        {"anni", 7}, {"bella", 9}, {"cato", 9}, {"dele", 4}
    };
    // by score descending, then name ascending on ties
    sort(team.begin(), team.end(),
         [](const auto &a, const auto &b) {
             return a.second != b.second ? a.second > b.second
                                         : a.first < b.first;
         });
    for (auto &[name, score] : team)            // structured bindings
        cout << name << " " << score << "\n";
}
