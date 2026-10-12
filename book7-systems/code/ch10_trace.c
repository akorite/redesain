// ch10_trace.c -- run a short hand-made trace through the chapter-10
// cache model and print what happened to every access.
//   usage: ch10_trace S E B addr [addr ...]      (decimal or 0x.. byte addresses)
//          prefix an address with w to make it a write, e.g. w40
#include <stdio.h>
#include <string.h>
#include "ch10_cache.h"
int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s S E B addr...\n", argv[0]); return 2; }
    int S = atoi(argv[1]), E = atoi(argv[2]), B = atoi(argv[3]);
    Cache *c = cache_new(S, E, B);
    printf("S=%d E=%d B=%d  (C=%d bytes)\n", S, E, B, S * E * B);
    printf("%-4s %-8s %-4s %-4s  %s\n", "#", "addr", "set", "tag", "result");
    for (int k = 4; k < argc; k++) {
        const char *t = argv[k]; int w = (t[0] == 'w'); if (w) t++;
        uint64_t a = strtoull(t, NULL, 0);
        uint64_t blk = a / B;
        int r = cache_access(c, a, w);
        printf("%-4d %-8llu %-4llu %-4llu  %s%s\n", k - 3, (unsigned long long)a,
               (unsigned long long)(blk % S), (unsigned long long)(blk / S),
               r & 1 ? "MISS" : "hit ", r & 2 ? " (evicted a line)" : "");
    }
    printf("hits=%llu misses=%llu evictions=%llu dirty_evictions=%llu\n", (unsigned long long)c->hits,
           (unsigned long long)c->misses, (unsigned long long)c->evicts,
           (unsigned long long)c->dirty_ev);
    cache_free(c); return 0;
}
