// window_demo.cpp -- sliding window: distinct count + deque min preview.
#include <deque>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main() {
    vector<int> a = {1, 2, 1, 3, 2, 3};
    int k = 3;
    map<int, int> cnt; deque<int> dq;
    for (int i = 0; i < (int)a.size(); i++) {
        cnt[a[i]]++;
        while (!dq.empty() && a[dq.back()] >= a[i]) dq.pop_back();
        dq.push_back(i);
        if (i >= k) {
            if (--cnt[a[i - k]] == 0) cnt.erase(a[i - k]);
            if (dq.front() <= i - k) dq.pop_front();
        }
        if (i >= k - 1)
            cout << "window[" << i - k + 1 << ".." << i << "] distinct="
                 << cnt.size() << " min=" << a[dq.front()] << "\n";
    }
}
