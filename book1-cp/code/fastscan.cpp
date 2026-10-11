// fastscan.cpp -- Listing 1.2: cin+sync off vs raw-buffer scanner, timed.
// Reads N integers from stdin and prints a checksum plus elapsed time.
// Build: clang++ -std=c++17 -O2 -o fastscan fastscan.cpp
#include <chrono>
#include <cstdio>
#include <iostream>
#include "lib/fastscan.h"
using namespace std;

int main(int argc, char** argv) {
    bool use_fast = argc > 1 && argv[1][0] == 'f';
    auto t0 = chrono::steady_clock::now();
    long long sum = 0;
    if (!use_fast) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
        int n; cin >> n;
        for (int i = 0; i < n; ++i) { long long x; cin >> x; sum += x; }
    } else {
        FastScanner fs;
        int n = fs.nextInt();
        for (int i = 0; i < n; ++i) sum += fs.nextLongLong();
    }
    double ms = chrono::duration<double, milli>(
        chrono::steady_clock::now() - t0).count();
    printf("method=%s sum=%lld time_ms=%.1f\n",
           use_fast ? "fread" : "cin", sum, ms);
}
