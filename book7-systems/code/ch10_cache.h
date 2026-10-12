/* ch10_cache.h -- the cache model of chapter 10 (header-only).
 * C = S sets x E ways x B bytes.  LRU replacement, write-back,
 * write-allocate.  Addresses are plain 64-bit integers, so the traces
 * are synthetic and the counts are deterministic: no dependence on where
 * the linker or ASLR put an array.                                     */
#ifndef CH10_CACHE_H
#define CH10_CACHE_H
#include <stdint.h>
#include <stdlib.h>

typedef struct { uint64_t tag; int valid, dirty; unsigned lru; } Line;
typedef struct {
    int S, E, B, bbits;            /* sets, ways, line bytes, log2(B)   */
    Line *ln; unsigned clock;
    uint64_t hits, misses, evicts, dirty_ev;
} Cache;

static Cache *cache_new(int S, int E, int B) {
    Cache *c = calloc(1, sizeof *c);
    c->S = S; c->E = E; c->B = B; c->bbits = __builtin_ctz(B);
    c->ln = calloc((size_t)S * E, sizeof(Line));
    return c;
}
static void cache_free(Cache *c) { free(c->ln); free(c); }

/* result bits: 1 = miss, 2 = a valid line was evicted */
static int cache_access(Cache *c, uint64_t addr, int is_write) {
    c->clock++;
    uint64_t block = addr >> c->bbits;        /* drop the offset bits   */
    uint64_t set = block % (uint64_t)c->S;    /* next s bits: the set   */
    uint64_t tag = block / (uint64_t)c->S;    /* the rest: the tag      */
    Line *l = &c->ln[set * c->E];
    for (int i = 0; i < c->E; i++)
        if (l[i].valid && l[i].tag == tag) {
            l[i].lru = c->clock; c->hits++;
            if (is_write) l[i].dirty = 1;
            return 0;
        }
    c->misses++;
    int v = -1; unsigned best = ~0u;
    for (int i = 0; i < c->E; i++) {          /* free way, else oldest  */
        if (!l[i].valid) { v = i; break; }
        if (l[i].lru < best) { best = l[i].lru; v = i; }
    }
    int r = 1;
    if (l[v].valid) { c->evicts++; r |= 2; if (l[v].dirty) c->dirty_ev++; }
    l[v].tag = tag; l[v].valid = 1; l[v].dirty = is_write; l[v].lru = c->clock;
    return r;
}
#endif
