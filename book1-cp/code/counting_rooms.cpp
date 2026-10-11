// counting_rooms.cpp -- CSES Counting Rooms (iterative flood fill).
#include <iostream>
#include <string>
#include <vector>
#include "floodfill.h"
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> g(n);
    for (auto& row : g) cin >> row;
    cout << count_rooms(g) << "\n";
}
