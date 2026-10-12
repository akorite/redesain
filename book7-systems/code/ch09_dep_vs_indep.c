// ch09_dep_vs_indep.c -- the same random visiting order, two ways.
//  dependent  : p = a[p]       each load needs the previous result
//  independent: s += a[idx[i]] the addresses are known in advance, so
//               an out-of-order core keeps many loads in flight.
// Latency is only visible in the first. Plain C99, no macOS calls.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>

static double now_s(void) {
    struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}
static uint64_t rng = 88172645463325252ull;           /* xorshift64 */
static uint64_t next(void) {
    rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng;
}
int main(void) {
    const size_t sizes[] = {1u<<15, 1u<<20, 1u<<23, 1u<<27};  /* bytes */
    const long reps = 20000000;
    printf("%10s %12s %12s %8s\n", "bytes", "dep ns/load", "indep ns/load", "ratio");
    for (int s = 0; s < 4; s++) {
        size_t n = sizes[s] / sizeof(uint32_t);
        uint32_t *a = malloc(n * sizeof *a), *idx = malloc(n * sizeof *idx);
        for (size_t i = 0; i < n; i++) idx[i] = (uint32_t)i;
        for (size_t i = n - 1; i > 0; i--) {              /* Fisher-Yates */
            size_t j = next() % (i + 1);
            uint32_t t = idx[i]; idx[i] = idx[j]; idx[j] = t;
        }
        /* a[] is one random cycle through all n slots */
        for (size_t i = 0; i < n; i++) a[idx[i]] = idx[(i + 1) % n];

        uint32_t p = idx[0];
        double t0 = now_s();
        for (long r = 0; r < reps; r++) p = a[p];         /* dependent */
        double dep = (now_s() - t0) / reps * 1e9;

        uint64_t sum = 0; size_t k = 0;
        t0 = now_s();
        for (long r = 0; r < reps; r++) {                 /* independent */
            sum += a[idx[k]];
            if (++k == n) k = 0;
        }
        double ind = (now_s() - t0) / reps * 1e9;
        printf("%10zu %12.2f %12.2f %7.1fx   (check %u %llu)\n", sizes[s], dep, ind,
               dep / ind, p, (unsigned long long)(sum & 1));
        free(a); free(idx);
    }
    return 0;
}
