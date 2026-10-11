// movie_festival.cpp -- interval scheduling by earliest end time.
// argv[1] = "start" switches to the (wrong) earliest-start greedy.
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    bool by_start = argc > 1 && !strcmp(argv[1], "start");
    int n;
    cin >> n;
    vector<pair<int,int>> m(n);
    for (auto &[a, b] : m) cin >> a >> b;
    sort(m.begin(), m.end(), [by_start](const auto &x, const auto &y) {
        return by_start ? x.first < y.first : x.second < y.second;
    });
    int taken = 0, free_at = 0;
    for (auto &[a, b] : m)
        if (a >= free_at) { taken++; free_at = b; }
    cout << taken << "\n";
}
