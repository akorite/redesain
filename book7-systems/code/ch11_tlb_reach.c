// ch11_tlb_reach.c -- how many pages can the TLB cover?  Chase a random
// cycle that visits exactly ONE cache line in each of P pages.  Cost per hop
// rises when P pages no longer fit in the TLB (every hop then needs a page
// walk).  To keep cache effects small the line used in page k is chosen
// as (k*64) mod 4096, so the lines spread over all cache sets.
// usage: ./ch11_tlb_reach [n|h] [hops=20000000]
// Caveat: P lines are also P cache lines, so for large P the cache
// misses too; the experiment cannot cleanly separate the two (see chapter).
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
static double now_s(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
static uint64_t rng = 0x9E3779B97F4A7C15ull;
static uint64_t next(void){rng^=rng<<13;rng^=rng>>7;rng^=rng<<17;return rng;}
int main(int argc, char **argv) {
    int huge = argc > 1 && argv[1][0] == 'h';        /* ask for transparent huge pages */
    size_t pg = (size_t)sysconf(_SC_PAGESIZE);
    size_t maxp = 1u << 16;                          /* up to 65536 pages = 256 MiB */
    size_t nb = maxp * pg;
    char *base = mmap(NULL, nb + (2u << 20), PROT_READ | PROT_WRITE,
                      MAP_PRIVATE | MAP_ANON, -1, 0);
    base = (char *)(((uintptr_t)base + (2u << 20) - 1) & ~(uintptr_t)((2u << 20) - 1));
    if (huge) madvise(base, nb, MADV_HUGEPAGE);
    for (size_t i = 0; i < nb; i += pg) base[i] = 1; /* make every page resident */
    long hp_kb = -1; char line[256];                 /* how much did the kernel really back with huge pages? */
    FILE *f = fopen("/proc/self/smaps_rollup", "r");
    while (f && fgets(line, sizeof line, f)) if (sscanf(line, "AnonHugePages: %ld kB", &hp_kb) == 1) break;
    if (f) fclose(f);
    printf("%s pages, page size %zu, AnonHugePages %ld kB\n", huge ? "huge-page-advised" : "normal", pg, hp_kb);
    printf("%8s %10s %12s\n", "pages", "region", "ns/hop");
    size_t *perm = malloc(maxp * sizeof *perm);
    for (size_t P = 8; P <= maxp; P *= 2) {
        for (size_t i = 0; i < P; i++) perm[i] = i;
        for (size_t i = P - 1; i > 0; i--) {
            size_t j = next() % (i + 1); size_t t = perm[i]; perm[i] = perm[j]; perm[j] = t;
        }
        #define SLOT(k) ((uintptr_t *)(base + (k) * pg + ((k) * 64) % pg))
        for (size_t i = 0; i < P; i++) *SLOT(perm[i]) = (uintptr_t)SLOT(perm[(i + 1) % P]);
        uintptr_t *p = SLOT(perm[0]);
        for (size_t i = 0; i < 2 * P; i++) p = (uintptr_t *)*p;      /* warm up */
        long hops = argc > 2 ? atol(argv[2]) : 20000000; double t0 = now_s();
        for (long r = 0; r < hops; r++) p = (uintptr_t *)*p;
        double ns = (now_s() - t0) / hops * 1e9;
        printf("%8zu %7zu KiB %12.2f   (%lu)\n", P, P * pg >> 10, ns, (unsigned long)((uintptr_t)p & 1));
    }
    return 0;
}
