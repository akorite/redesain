// painting_barn.cpp -- USACO-S Painting the Barn via 2D difference.
#include <iostream>
#include <vector>
#include "diff.h"
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<vector<ll>> diff(N + 1, vector<ll>(N + 1));
    int x1, y1, x2, y2;
    while (cin >> x1 >> y1 >> x2 >> y2) {      // bottom-left / top-right
        diff[x1][y1]++; diff[x1][y2]--;
        diff[x2][y1]--; diff[x2][y2]++;
    }
    int cnt = 0;
    for (int x = 0; x < N; x++) {
        int run = 0;
        for (int y = 0; y < N; y++) {
            run += diff[x][y];
            diff[x][y] = run + (x ? diff[x - 1][y] : 0);
            if (diff[x][y] == K) cnt++;
        }
    }
    cout << cnt << "\n";
}
