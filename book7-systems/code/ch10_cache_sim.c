// ch10_cache_sim.c -- exact miss counts of a C = S x E x B cache
// (LRU, write-back, write-allocate) driven by the naive and the
// blocked transpose of an N x N matrix of 4-byte floats.
//   A: miss rate vs associativity       (N=256,  S=32, B=64)
//   B: naive vs blocked, toy 16 KB L1   (N=256,  S=64, E=4, B=64)
//   C: same, on this container's L1d    (N=2048, S=64, E=8, B=64 = 32 KB)
//   D: the three Cs of the naive transpose in B
//   G: the toy L1 again with rows padded from 256 to 272 floats
//   F: next-line prefetch on every miss, naive transpose, toy L1
//   E: two levels (L1 32 KB 8-way + L2 1 MiB 16-way), N=2048: what L2 absorbs
// Build: cc -O2 -o ch10_cache_sim ch10_cache_sim.c
#include <stdio.h>
#include "ch10_cache.h"

#define ES 4                           /* sizeof(float)                 */
#define A_BASE 0x10000000ull           /* synthetic address of a[0][0]  */
static int N, P;                       /* matrix size, row pitch in floats */
static uint64_t B_BASE;                /* b follows a in memory         */
static uint64_t a_at(int i, int j) { return A_BASE + ((uint64_t)i * P + j) * ES; }
static uint64_t b_at(int i, int j) { return B_BASE + ((uint64_t)i * P + j) * ES; }

/* every driver reports each access through this hook */
typedef void (*Sink)(void *ctx, uint64_t addr, int wr);
static void run_naive(Sink f, void *ctx) {
    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) {
        f(ctx, a_at(i, j), 0);         /* read  a[i][j] */
        f(ctx, b_at(j, i), 1);         /* write b[j][i] */
    }
}
static void run_blocked(Sink f, void *ctx, int bs) {
    for (int ii = 0; ii < N; ii += bs) for (int jj = 0; jj < N; jj += bs)
        for (int i = ii; i < ii + bs; i++) for (int j = jj; j < jj + bs; j++) {
            f(ctx, a_at(i, j), 0);
            f(ctx, b_at(j, i), 1);
        }
}
static void to_cache(void *ctx, uint64_t a, int w) { cache_access(ctx, a, w); }

static void report(const char *name, int S, int E, int bs) {
    Cache *c = cache_new(S, E, 64);
    if (bs) run_blocked(to_cache, c, bs); else run_naive(to_cache, c);
    printf("%-8s misses=%-8llu evictions=%-8llu miss rate=%.1f%%\n", name,
           (unsigned long long)c->misses, (unsigned long long)c->evicts,
           100.0 * c->misses / (c->hits + c->misses));
    cache_free(c);
}

/* ---- D: classify every miss: compulsory / capacity / conflict ---- */
typedef struct { Cache *real, *fa; unsigned char *seen;
                 uint64_t comp, cap, conf; } Cls;
static void to_cls(void *ctx, uint64_t addr, int wr) {
    Cls *k = ctx;
    uint64_t line = (addr - A_BASE) >> 6;
    int real_miss = cache_access(k->real, addr, wr) & 1;
    int fa_miss   = cache_access(k->fa,   addr, wr) & 1;  /* 1 set, all ways */
    int first     = !k->seen[line]; k->seen[line] = 1;
    if (!real_miss) return;
    if (first) k->comp++; else if (fa_miss) k->cap++; else k->conf++;
}
static void classify(const char *name, int bs) {
    Cls k = { cache_new(64, 4, 64), cache_new(1, 64 * 4, 64),
              calloc((size_t)2 * N * P * ES / 64 + 1, 1), 0, 0, 0 };
    if (bs) run_blocked(to_cls, &k, bs); else run_naive(to_cls, &k);
    printf("%-8s compulsory=%-6llu capacity=%-7llu conflict=%-7llu total=%llu\n",
           name, (unsigned long long)k.comp, (unsigned long long)k.cap,
           (unsigned long long)k.conf, (unsigned long long)(k.comp + k.cap + k.conf));
    cache_free(k.real); cache_free(k.fa); free(k.seen);
}

/* ---- E: two levels; an L1 miss becomes an L2 access (write-backs ignored) ---- */
typedef struct { Cache *l1, *l2; } Two;
static void to_two(void *ctx, uint64_t addr, int wr) {
    Two *t = ctx;
    if (cache_access(t->l1, addr, wr) & 1) cache_access(t->l2, addr, wr);
}
static void two_level(const char *name, int bs) {
    Two t = { cache_new(64, 8, 64), cache_new(1024, 16, 64) };
    if (bs) run_blocked(to_two, &t, bs); else run_naive(to_two, &t);
    printf("%-8s L1 misses=%-8llu L2 misses=%-8llu\n", name,
           (unsigned long long)t.l1->misses, (unsigned long long)t.l2->misses);
    cache_free(t.l1); cache_free(t.l2);
}

/* ---- F: on a demand miss, also fetch the next line (counted separately) ---- */
typedef struct { Cache *c; uint64_t demand; } Pf;
static void to_pf(void *ctx, uint64_t addr, int wr) {
    Pf *p = ctx;
    if (cache_access(p->c, addr, wr) & 1) {
        p->demand++;
        cache_access(p->c, addr + 64, 0);       /* the prefetch */
    }
}

int main(void) {
    N = 256; P = 256; B_BASE = A_BASE + (uint64_t)N * P * ES;
    puts("== A: miss rate vs associativity (N=256 floats, S=32 sets, B=64)");
    for (int E = 1; E <= 8; E *= 2) {
        char nm[24]; snprintf(nm, sizeof nm, "E=%d", E);
        report(nm, 32, E, 0);
    }
    puts("== B: toy L1 S=64 E=4 B=64 (16 KB), N=256 floats (256 KB per matrix)");
    report("naive", 64, 4, 0);
    for (int bs = 2; bs <= 32; bs *= 2) {
        char nm[24]; snprintf(nm, sizeof nm, "block%d", bs);
        report(nm, 64, 4, bs);
    }
    puts("== D: three Cs, same toy L1 as B (fully-assoc. LRU shadow, same 16 KB)");
    classify("naive", 0); classify("block8", 8); classify("block16", 16);
    classify("block32", 32);
    { Pf p = { cache_new(64, 4, 64), 0 }; run_naive(to_pf, &p);
      puts("== F: toy L1 with next-line prefetch on miss, naive, N=256");
      printf("naive    demand misses=%llu (without prefetch: 69632)\n",
             (unsigned long long)p.demand); cache_free(p.c); }
    puts("== G: toy L1 again, but each row padded to 272 floats (pitch 1088 B = 17 lines)");
    P = 272; B_BASE = A_BASE + (uint64_t)N * P * ES;
    report("naive", 64, 4, 0);
    for (int bs = 8; bs <= 32; bs *= 2) {
        char nm[24]; snprintf(nm, sizeof nm, "block%d", bs);
        report(nm, 64, 4, bs);
    }
    N = 2048; P = 2048; B_BASE = A_BASE + (uint64_t)N * P * ES;
    puts("== C: S=64 E=8 B=64 (32 KB, like this container's L1d), N=2048 floats");
    report("naive", 64, 8, 0);
    for (int bs = 4; bs <= 64; bs *= 2) {
        char nm[24]; snprintf(nm, sizeof nm, "block%d", bs);
        report(nm, 64, 8, bs);
    }
    puts("== E: L1 (S=64 E=8) backed by L2 (S=1024 E=16, 1 MiB), N=2048 floats");
    two_level("naive", 0);
    for (int bs = 4; bs <= 64; bs *= 2) {
        char nm[24]; snprintf(nm, sizeof nm, "block%d", bs);
        two_level(nm, bs);
    }
    return 0;
}
