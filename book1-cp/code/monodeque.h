// monodeque.h -- sliding-window minimum in O(n).
// The deque holds candidate indices, front = current window min.
// On entry i: pop indices with a[idx] >= a[i] (they can never win
// again), push i, drop the front once it leaves the window.
#pragma once
#include <deque>
#include <vector>

template <class T>
std::vector<T> sliding_min(const std::vector<T>& a, int k) {
    std::deque<int> dq;
    std::vector<T> out;
    for (int i = 0; i < (int)a.size(); i++) {
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
        dq.push_back(i);
        if (dq.front() <= i - k) dq.pop_front();
        if (i >= k - 1) out.push_back(a[dq.front()]);
    }
    return out;
}
