// stl_tour.cpp -- Listing 1.3: the four STL tools used most, with output.
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {5, 2, 8, 1, 4};
    sort(v.begin(), v.end(), [](int a, int b) {   // custom comparator:
        if ((a & 1) != (b & 1)) return (a & 1) < (b & 1);  // even first,
        return a < b;                                      // then ascending
    });
    cout << "sorted:";
    for (int x : v) cout << ' ' << x;
    cout << '\n';

    set<int> s = {4, 1, 4, 2, 1};                 // dedupe + order
    cout << "set:";
    for (int x : s) cout << ' ' << x;
    cout << '\n';

    map<string, int> freq;                        // frequency table
    for (string w : {"b", "a", "b", "c", "a", "b"}) freq[w]++;
    for (auto& [word, count] : freq)
        cout << word << '=' << count << ' ';
    cout << '\n';

    priority_queue<int> pq;                       // largest on top
    for (int x : {3, 9, 4, 7}) pq.push(x);
    cout << "pop order:";
    while (!pq.empty()) { cout << ' ' << pq.top(); pq.pop(); }
    cout << '\n';
}
