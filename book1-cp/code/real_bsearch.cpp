// real_bsearch.cpp -- 60 fixed iterations find sqrt(2); no eps needed.
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double lo = 0, hi = 2;
    for (int it = 1; it <= 60; it++) {
        double mid = (lo + hi) / 2;
        if (mid * mid < 2) lo = mid; else hi = mid;
        if (it == 10 || it == 20 || it == 60)
            cout << "it=" << it << " bracket=[" << setprecision(17)
                 << lo << ", " << hi << "]\n";
    }
}
