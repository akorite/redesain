// ch13_partition.c -- the "partitioned counter" measured honestly.
// ch13_lockscale.c's partition loop is optimised to ONE add by gcc -O2, so it
// times thread start-up only.  Here the counters are volatile (the compiler must
// really do 400M loads+stores), in two layouts:
//   adjacent: counter k lives at slot k          (several counters per 64-byte line)
//   padded  : counter k lives at slot k*8        (8 longs = 64 bytes: one line each)
#include <stdio.h>
#include <pthread.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
#define PER 100000000L
static volatile long slot[8*8] __attribute__((aligned(64)));
static int stride;
static void *work(void *a){
    volatile long *c = &slot[(long)a * stride];
    for (long i = 0; i < PER; i++) (*c)++;
    return 0;
}
static double run(int T, int st){
    pthread_t t[8]; stride = st;
    for (int i = 0; i < 64; i++) slot[i] = 0;
    double t0 = now();
    for (long i = 0; i < T; i++) pthread_create(&t[i], 0, work, (void*)i);
    for (int i = 0; i < T; i++) pthread_join(t[i], 0);
    return (now() - t0) * 1e3;
}
int main(void){
    printf("%3s %14s %14s\n", "T", "adjacent (ms)", "padded (ms)");
    for (int T = 1; T <= 4; T *= 2)
        printf("%3d %14.1f %14.1f\n", T, run(T, 1), run(T, 8));
    return 0;
}
