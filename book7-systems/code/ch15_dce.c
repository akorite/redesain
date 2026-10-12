// ch15_dce.c -- the dead-code-elimination incident.
//   gcc -O2 ch15_dce.c           -> result never used: the compiler deletes the kernel
//   gcc -O2 -DSINK ch15_dce.c    -> result stored to a volatile: the kernel must run
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static long sum(const int *a, long n){ long s = 0; for (long i = 0; i < n; i++) s += a[i]; return s; }
int main(void){
    long n = 1L << 22;                               // 4M ints = 16 MiB
    int *a = malloc(n * sizeof *a);
    for (long i = 0; i < n; i++) a[i] = i & 0xff;
#ifdef SINK
    volatile long sink;
#endif
    double best = 1e9;
    for (int r = 0; r < 11; r++) {
        double t = now();
#ifdef SINK
        sink = sum(a, n);
#else
        sum(a, n);                                   // result thrown away
#endif
        double dt = now() - t; if (dt < best) best = dt;
    }
    printf("%s: best of 11 = %.4f ms  (%.1f GB/s implied)\n",
#ifdef SINK
           "with sink   ",
#else
           "without sink",
#endif
           best * 1e3, n * 4 / best / 1e9);
    return 0;
}
