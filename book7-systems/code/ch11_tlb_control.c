// ch11_tlb_control.c -- control for ch11_tlb_reach: the SAME number of cache
// lines, but packed contiguously so they live in only a few pages.  If the
// slowdown of ch11_tlb_reach comes from the TLB, these should stay fast.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <sys/mman.h>
static double now_s(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
int main(void){
    char *base = mmap(0, 1 << 26, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANON, -1, 0);
    for (size_t i = 0; i < (1 << 26); i += 4096) base[i] = 1;     /* resident */
    for (int L = 64; L <= 1024; L *= 2) {
        size_t *perm = malloc(L * sizeof *perm);
        for (int i = 0; i < L; i++) perm[i] = i;
        srand(3);
        for (int i = L - 1; i > 0; i--) {
            int j = rand() % (i + 1); size_t t = perm[i]; perm[i] = perm[j]; perm[j] = t;
        }
        uintptr_t *s = (uintptr_t *)base;                          /* 8 words = 1 line */
        for (int i = 0; i < L; i++) s[perm[i] * 8] = (uintptr_t)&s[perm[(i + 1) % L] * 8];
        uintptr_t *p = &s[perm[0] * 8]; long h = 20000000; double t0 = now_s();
        for (long r = 0; r < h; r++) p = (uintptr_t *)*p;
        printf("%4d lines in %2d page(s): %.2f ns/hop (%lu)\n", L,
               (L * 64 + 4095) / 4096, (now_s() - t0) / h * 1e9, (unsigned long)p & 1);
        free(perm);
    }
    return 0;
}
