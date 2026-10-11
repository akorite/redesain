// floodfill.h -- iterative 4-direction flood fill on a grid.
// Explicit stack: recursion depth here can reach n*m.
#pragma once
#include <stack>
#include <string>
#include <utility>
#include <vector>

inline int count_rooms(std::vector<std::string> grid) {
    int n = grid.size(), m = grid[0].size(), rooms = 0;
    const int dr[4] = {-1, 1, 0, 0}, dc[4] = {0, 0, -1, 1};
    for (int r = 0; r < n; r++)
        for (int c = 0; c < m; c++) {
            if (grid[r][c] != '.') continue;
            rooms++;
            std::stack<std::pair<int,int>> st;
            st.push({r, c});
            std::vector<std::vector<char>> seen(n, std::vector<char>(m));
            seen[r][c] = 1;
            while (!st.empty()) {
                auto [x, y] = st.top(); st.pop();
                grid[x][y] = '#';
                for (int k = 0; k < 4; k++) {
                    int nx = x + dr[k], ny = y + dc[k];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < m
                        && grid[nx][ny] == '.' && !seen[nx][ny]) {
                        seen[nx][ny] = 1;
                        st.push({nx, ny});
                    }
                }
            }
        }
    return rooms;
}
