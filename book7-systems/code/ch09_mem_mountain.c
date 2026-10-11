// ch09_mem_mountain.c -- pointer-chase latency vs working-set size.
// Each element of a random circular linked list hides the next
// pointer; the CPU cannot prefetch across the chain, so each load
// pays the true latency of whichever level holds the set.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdint.h>

static double now_s(void) {
    struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec + ts.tv_nsec * 1e-9;
}
int main(void) {
    const size_t sizes[] = {1<<12, 1<<14, 1<<15, 1<<16, 1<<17, 1<<18,
                            1<<19, 1<<20, 1<<21, 1<<22, 1<<23, 1<<24,
                            1<<25, 1<<26, 1<<27};
    const int ns = sizeof(sizes)/sizeof(sizes[0]);
    printf("%8s %10s\n", "bytes", "ns/load");
    for (int s = 0; s < ns; s++) {
        size_t nbytes = sizes[s];
        size_t n = nbytes / sizeof(uintptr_t);
        uintptr_t *a = malloc(nbytes);
        /* random circular permutation, Fisher-Yates on indices */
        size_t *perm = malloc(n * sizeof(size_t));
        for (size_t i = 0; i < n; i++) perm[i] = i;
        for (size_t i = n - 1; i > 0; i--) {
            size_t j = arc4random_uniform((uint32_t)(i + 1));
            size_t t = perm[i]; perm[i] = perm[j]; perm[j] = t;
        }
        for (size_t i = 0; i < n; i++)
            a[perm[i]] = (uintptr_t)&a[perm[(i + 1) % n]];
        volatile uintptr_t p = (uintptr_t)&a[perm[0]];
        /* warmup */
        for (size_t i = 0; i < n; i++) p = *(volatile uintptr_t *)p;
        double t0 = now_s();
        const long reps = 20000000;
        for (long r = 0; r < reps; r++) p = *(volatile uintptr_t *)p;
        double dt = (now_s() - t0) / reps * 1e9;
        printf("%8zu %10.2f\n", nbytes, dt);
        free(perm); free(a);
        fflush(stdout);
    }
    return 0;
}
