// ch14_fsync_sweep.c -- cost of fsync as a function of how much you write before it.
// For each write size, write 8 MB total, calling fsync after every write.
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
int main(void) {
    const long TOTAL = 8L << 20;
    char *buf = malloc(1 << 20);
    for (int i = 0; i < (1 << 20); i++) buf[i] = (char)i;
    printf("%10s %10s %12s %10s\n", "write size", "fsyncs", "ms/fsync", "MB/s");
    for (long sz = 4096; sz <= (1L << 20); sz *= 4) {
        int f = open("/tmp/ch14_sweep.bin", O_WRONLY | O_CREAT | O_TRUNC, 0644);
        long n = TOTAL / sz; if (n > 512) n = 512;       // cap the slow small-size runs
        double t = now();
        for (long i = 0; i < n; i++) { if (write(f, buf, sz) != sz) return 1; fsync(f); }
        double dt = now() - t; close(f);
        printf("%8ld B %10ld %12.3f %10.1f\n", sz, n, dt * 1e3 / n, n * sz / 1048576.0 / dt);
    }
    unlink("/tmp/ch14_sweep.bin");
    return 0;
}
