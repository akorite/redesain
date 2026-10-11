// monostack.h -- monotonic stack for nearest-smaller queries.
// Invariant: the stack holds indices with strictly increasing values;
// each index is pushed once and popped once -> O(n) amortized.
#pragma once
#include <stack>
#include <vector>

// ans[i] = index of nearest position LEFT of i with a smaller value,
// or -1. Swap the comparison for "nearest greater" or right-side scans.
template <class T>
std::vector<int> nearest_smaller_left(const std::vector<T>& a) {
    int n = a.size();
    std::vector<int> ans(n, -1);
    std::stack<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        ans[i] = st.empty() ? -1 : st.top();
        st.push(i);
    }
    return ans;
}

template <class T>
std::vector<int> nearest_smaller_right(const std::vector<T>& a) {
    int n = a.size();
    std::vector<int> ans(n, n);
    std::stack<int> st;
    for (int i = n - 1; i >= 0; i--) {
        while (!st.empty() && a[st.top()] >= a[i]) st.pop();
        ans[i] = st.empty() ? n : st.top();
        st.push(i);
    }
    return ans;
}
