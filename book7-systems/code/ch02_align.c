/* ch02_align.c -- alignment tax: sum via aligned vs misaligned pointer */
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#define N (1u<<22)
static uint32_t a[N + 1];
int main(void) {
    volatile uint64_t s = 0;
    struct timespec t0, t1;
    for (int off = 0; off <= 1; off++) {
        uint32_t *p = (uint32_t *)((char *)a + off);   /* off=1: misaligned */
        memset(a, 1, N * 4);
        clock_gettime(CLOCK_MONOTONIC, &t0);
        for (int r = 0; r < 32; r++)
            for (uint32_t k = 0; k < N; k++) s += p[k];
        clock_gettime(CLOCK_MONOTONIC, &t1);
        double ms = (t1.tv_sec - t0.tv_sec) * 1e3 + (t1.tv_nsec - t0.tv_nsec) / 1e6;
        printf("offset %d: %.1f ms  (s=%llu)\n", off, ms, (unsigned long long)s);
    }
    return 0;
}
