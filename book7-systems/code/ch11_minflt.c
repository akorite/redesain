// ch11_minflt.c -- count real page faults with getrusage(ru_minflt), and
// watch fork's copy-on-write happen.  Linux/macOS, plain C.
//   part 1: demand paging: read pass, second read pass, write pass
//   part 2: fork + COW: child reads (no copies), child writes (one fault each)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/resource.h>
#include <sys/wait.h>
#include <unistd.h>

static long minflt(void) { struct rusage r; getrusage(RUSAGE_SELF, &r); return r.ru_minflt; }
static long rss_pages(void) {                /* resident set size, in pages (Linux) */
    long size = -1, res = -1; FILE *f = fopen("/proc/self/statm", "r");
    if (f) { if (fscanf(f, "%ld %ld", &size, &res) != 2) res = -1; fclose(f); }
    return res;
}
int main(void) {
    size_t pg = (size_t)sysconf(_SC_PAGESIZE), np = 16384, nb = np * pg;
    char *p = mmap(NULL, nb, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    volatile char s = 0;
    printf("page size %zu bytes, region %zu pages (%zu MiB)\n", pg, np, nb >> 20);
    printf("after mmap, before any touch: faults=%ld  rss=%ld pages\n", minflt(), rss_pages());

    long f0 = minflt();
    for (size_t i = 0; i < nb; i += pg) s += p[i];            /* first READ of each page */
    printf("read pass 1   : +%ld faults   rss=%ld pages\n", minflt() - f0, rss_pages());
    f0 = minflt();
    for (size_t i = 0; i < nb; i += pg) s += p[i];            /* same pages again */
    printf("read pass 2   : +%ld faults\n", minflt() - f0);
    f0 = minflt();
    for (size_t i = 0; i < nb; i += pg) p[i] = (char)(i / pg); /* first WRITE of each page */
    printf("write pass 1  : +%ld faults   rss=%ld pages\n", minflt() - f0, rss_pages());
    f0 = minflt();
    for (size_t i = 0; i < nb; i += pg) p[i] = (char)(i / pg + 1);
    printf("write pass 2  : +%ld faults\n", minflt() - f0);

    /* ---- part 2: copy on write ---- */
    size_t k = 256;                       /* pages the children will look at */
    p[0] = 42;
    fflush(stdout);
    pid_t pid = fork();
    if (pid == 0) {
        long a = minflt();
        for (size_t i = 0; i < k * pg; i += pg) s += p[i];
        long b = minflt();
        for (size_t i = 0; i < k * pg; i += pg) p[i] = 99;
        long c = minflt();
        printf("child  reads %zu shared pages: +%ld faults; then writes them: +%ld faults\n",
               k, b - a, c - b);
        fflush(stdout);
        _exit(0);
    }
    waitpid(pid, NULL, 0);
    printf("parent still sees p[0]=%d (child wrote 99 into its own copy)\n", p[0]);
    long a = minflt();
    for (size_t i = 0; i < k * pg; i += pg) p[i] = 7;
    printf("parent writes the same %zu pages after the child exited: +%ld faults\n",
           k, minflt() - a);
    return 0;
}
