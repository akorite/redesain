// ch09_stride_bw.c -- sequential-read bandwidth vs stride.
// Stride 1 touches every 8-byte word; stride 64 touches one word
// per 512 bytes -- same bytes read per load, wildly different
// bytes moved across the bus.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
static double now_s(void) {
    struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}
int main(void) {
    const size_t nbytes = 1u<<26;             /* 64 MiB -- past caches */
    uint64_t *a = malloc(nbytes);
    size_t n = nbytes / sizeof(uint64_t);
    for (size_t i = 0; i < n; i++) a[i] = i;
    printf("%6s %10s %12s\n", "stride", "ns/acc", "GB/s(eff)");
    for (size_t st = 1; st <= 128; st *= 2) {
        volatile uint64_t sink = 0;
        double t0 = now_s();
        const int reps = 20;
        for (int r = 0; r < reps; r++)
            for (size_t i = 0; i < n; i += st) sink += a[i];
        double dt = (now_s() - t0) / reps;
        double accs = (double)n / st;
        double nspacc = dt / accs * 1e9;
        /* effective bandwidth: useful bytes vs bytes the bus saw */
        double gbs_eff = (accs * 8) / dt / 1e9;
        printf("%6zu %10.3f %12.2f\n", st, nspacc, gbs_eff);
    }
    free(a);
    return 0;
}
