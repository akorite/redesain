// ch15_cdf.c -- latency is a distribution.  1000 timings of one small kernel
// (sum of 256K ints = 1 MiB, fits in cache): print the first samples, the
// percentiles, and a histogram of the sorted values.
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static int cmpd(const void *a, const void *b){ double d = *(const double*)a - *(const double*)b; return d < 0 ? -1 : d > 0; }
static long sum(const int *a, long n){ long s = 0; for (long i = 0; i < n; i++) s += a[i]; return s; }
#define NS 1000
int main(void){
    long n = 1L << 18;
    int *a = malloc(n * sizeof *a);
    for (long i = 0; i < n; i++) a[i] = i & 0xff;
    volatile long sink;
    double s[NS], sorted[NS];
    for (int i = 0; i < NS; i++){ double t = now(); sink = sum(a, n); s[i] = (now() - t) * 1e6; sorted[i] = s[i]; }
    printf("first 5 samples (us): ");
    for (int i = 0; i < 5; i++) printf("%.1f ", s[i]);
    printf("\n");
    qsort(sorted, NS, sizeof(double), cmpd);
    printf("p50=%.1f  p90=%.1f  p99=%.1f  p99.9=%.1f  max=%.1f  (us)\n",
           sorted[NS/2], sorted[NS*9/10], sorted[NS*99/100], sorted[NS*999/1000], sorted[NS-1]);
    double tot = 0; for (int i = 0; i < NS; i++) tot += s[i];
    printf("mean=%.1f us  (mean/p50 = %.2f)\n", tot / NS, tot / NS / sorted[NS/2]);
    // histogram: 8 equal-width buckets between p50 and p99.9 (+ overflow bucket)
    double lo = sorted[NS/2], hi = sorted[NS*999/1000]; int cnt[10] = {0};
    for (int i = 0; i < NS; i++){
        int b = s[i] < lo ? 0 : s[i] >= hi ? 9 : 1 + (int)((s[i] - lo) / (hi - lo) * 8);
        cnt[b]++; }
    printf("histogram (count of 1000 samples):\n");
    printf("  < p50           : %d\n", cnt[0]);
    for (int b = 1; b <= 8; b++) printf("  %6.1f..%6.1f us : %d\n", lo + (hi-lo)*(b-1)/8, lo + (hi-lo)*b/8, cnt[b]);
    printf("  >= p99.9        : %d\n", cnt[9]);
    return 0;
}
