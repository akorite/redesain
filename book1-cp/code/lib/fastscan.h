// fastscan.h -- read integers straight from stdin's buffer.
// Usage: FastScanner fs; ll x = fs.nextLongLong();
#pragma once
#include <cstdio>

struct FastScanner {
    static const int BUFSIZE = 1 << 16;
    char buf[BUFSIZE];
    int idx = 0, size = 0;

    inline char getch() {
        if (idx >= size) {
            size = (int)fread(buf, 1, BUFSIZE, stdin);
            idx = 0;
            if (size == 0) return 0;
        }
        return buf[idx++];
    }
    long long nextLongLong() {
        char c; long long x = 0, sign = 1;
        do { c = getch(); } while (c <= ' ' && c);
        if (c == '-') { sign = -1; c = getch(); }
        for (; c > ' '; c = getch()) x = x * 10 + (c - '0');
        return x * sign;
    }
    int nextInt() { return (int)nextLongLong(); }
};
