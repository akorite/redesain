// ch09_volatile_cost.c -- how much does the "volatile p" in the mountain
// loop cost?  Same 4 KiB random pointer chain (always an L1 hit), timed
// with a plain pointer and with a volatile one.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
static double now_s(void){struct timespec ts;clock_gettime(CLOCK_MONOTONIC,&ts);
  return ts.tv_sec+ts.tv_nsec*1e-9;}
int main(void){
    size_t n = 4096 / sizeof(uintptr_t);                /* 512 slots */
    uintptr_t *a = malloc(n * sizeof *a);
    size_t *perm = malloc(n * sizeof *perm);
    for (size_t i = 0; i < n; i++) perm[i] = i;
    srand(1);
    for (size_t i = n - 1; i > 0; i--) {
        size_t j = (size_t)rand() % (i + 1);
        size_t t = perm[i]; perm[i] = perm[j]; perm[j] = t;
    }
    for (size_t i = 0; i < n; i++)
        a[perm[i]] = (uintptr_t)&a[perm[(i + 1) % n]];
    const long reps = 100000000;

    uintptr_t p = (uintptr_t)&a[perm[0]];
    double t0 = now_s();
    for (long r = 0; r < reps; r++) p = *(uintptr_t *)p;
    double plain = (now_s() - t0) / reps * 1e9;

    volatile uintptr_t q = (uintptr_t)&a[perm[0]];
    t0 = now_s();
    for (long r = 0; r < reps; r++) q = *(volatile uintptr_t *)q;
    double vol = (now_s() - t0) / reps * 1e9;

    printf("plain pointer   : %.2f ns/load  (%lu)\n", plain, (unsigned long)(p & 1));
    printf("volatile pointer: %.2f ns/load\n", vol);
    return 0;
}
