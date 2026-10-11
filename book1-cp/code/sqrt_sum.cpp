// sqrt_sum.cpp -- sqrt-decomposition range sum with point updates.
#include <iostream>
#include <vector>
#include "sqrtdec.h"
using namespace std;

int main() {
    SqrtDec sd({3, 1, 4, 1, 5, 9, 2, 6, 5, 3});
    cout << "sum[2..6] = " << sd.sum(2, 6) << "\n";   // 4+1+5+9+2 = 21
    sd.set(4, 0);                                     // a[4]: 5 -> 0
    cout << "after set(4,0): sum[2..6] = " << sd.sum(2, 6) << "\n";
    cout << "sum[0..9] = " << sd.sum(0, 9) << "\n";
}
