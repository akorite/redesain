// ch14_direct.c -- read the same 256 MB file through the page cache and with O_DIRECT.
// O_DIRECT needs an aligned buffer and aligned sizes (here 4096).  Uses ch14_fs_io's file.
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
#define MB (1024*1024)
#define FILE_MB 256
static double read_all(const char *path, int flags, void *buf) {
    int f = open(path, O_RDONLY | flags);
    if (f < 0) { perror("open"); exit(1); }
    double t = now(); long total = 0; ssize_t n;
    while ((n = read(f, buf, MB)) > 0) total += n;
    double dt = now() - t; close(f);
    if (total != (long)FILE_MB * MB) { fprintf(stderr, "short read %ld\n", total); exit(1); }
    return FILE_MB / dt;
}
int main(void) {
#ifdef O_DIRECT
    const char *path = "/tmp/ch14_direct.bin";
    void *buf; if (posix_memalign(&buf, 4096, MB)) return 1;
    int f = open(path, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    for (int i = 0; i < MB; i++) ((char *)buf)[i] = (char)(i * 7);
    for (int i = 0; i < FILE_MB; i++) if (write(f, buf, MB) != MB) return 1;
    fsync(f); close(f);
    printf("buffered read, 1st pass : %8.0f MB/s\n", read_all(path, 0, buf));
    printf("buffered read, 2nd pass : %8.0f MB/s\n", read_all(path, 0, buf));
    printf("O_DIRECT read           : %8.0f MB/s\n", read_all(path, O_DIRECT, buf));
    unlink(path);
    return 0;
#else
    fprintf(stderr, "O_DIRECT not supported on this platform\n");
    return 1;
#endif
}
