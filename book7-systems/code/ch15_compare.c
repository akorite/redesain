// ch15_compare.c -- is B really faster than A?  Two sum kernels, 40 interleaved
// samples each (ABAB... so drift hits both), mean +- standard error, and the
// difference measured against its own noise.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static long sumA(const int *a, long n){ long s = 0; for (long i = 0; i < n; i++) s += a[i]; return s; }
static long sumB(const int *a, long n){            // 4 independent accumulators
    long s0 = 0, s1 = 0, s2 = 0, s3 = 0;
    for (long i = 0; i < n; i += 4){ s0 += a[i]; s1 += a[i+1]; s2 += a[i+2]; s3 += a[i+3]; }
    return s0 + s1 + s2 + s3; }
static void stats(const double *x, int k, double *mean, double *sd){
    double m = 0, v = 0; for (int i = 0; i < k; i++) m += x[i]; m /= k;
    for (int i = 0; i < k; i++) v += (x[i] - m) * (x[i] - m);
    *mean = m; *sd = sqrt(v / (k - 1)); }
#define K 40
int main(void){
    long n = 1L << 22;
    int *a = malloc(n * sizeof *a);
    for (long i = 0; i < n; i++) a[i] = i & 0xff;
    volatile long sink;
    for (int i = 0; i < 3; i++){ sink = sumA(a, n); sink = sumB(a, n); }     // warmup both
    double ta[K], tb[K];
    for (int i = 0; i < K; i++){
        double t = now(); sink = sumA(a, n); ta[i] = (now() - t) * 1e3;
        t = now();        sink = sumB(a, n); tb[i] = (now() - t) * 1e3; }
    double ma, sa, mb, sb; stats(ta, K, &ma, &sa); stats(tb, K, &mb, &sb);
    double sea = sa / sqrt(K), seb = sb / sqrt(K), se = sqrt(sea*sea + seb*seb);
    printf("A: mean %.3f ms  sd %.3f  se %.3f\n", ma, sa, sea);
    printf("B: mean %.3f ms  sd %.3f  se %.3f\n", mb, sb, seb);
    printf("B - A = %+.3f ms  (%.1f%%), se of difference %.3f, |diff|/se = %.1f\n",
           mb - ma, 100 * (mb - ma) / ma, se, fabs(mb - ma) / se);
    printf("verdict: %s\n", fabs(mb - ma) > 2 * se ? "difference is larger than 2 se: believable"
                                                  : "difference is within 2 se: not distinguishable from noise");
    return 0;
}
