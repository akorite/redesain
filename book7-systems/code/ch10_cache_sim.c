// ch10_cache_sim.c -- cycle-accurate-enough cache model:
// C = S x E x B, LRU replacement, write-back+write-allocate.
// Drives (a) miss-rate vs E sweep and (b) naive vs blocked
// transpose miss counts -- all numbers real.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef struct { uint64_t tag; int valid, dirty; unsigned lru; } Line;
typedef struct { int S, E, B; Line *ln; unsigned clock;
                 uint64_t hits, misses, evicts, dirty_ev; } Cache;

static Cache *mk(int S,int E,int B){
    Cache*c=calloc(1,sizeof* c);c->S=S;c->E=E;c->B=B;
    c->ln=calloc((size_t)S*E,sizeof(Line));return c;}
static void access(Cache*c,uint64_t addr,int wr){
    c->clock++;
    int b=c->B>0?__builtin_ctz(c->B):0;
    uint64_t set=(addr/b)%c->S, tag=addr/b/c->S;
    Line*l=&c->ln[set*c->E];
    for(int i=0;i<c->E;i++)if(l[i].valid&&l[i].tag==tag){
        l[i].lru=c->clock;c->hits++;if(wr)l[i].dirty=1;return;}
    c->misses++;
    int v=-1;unsigned best=~0u;
    for(int i=0;i<c->E;i++){if(!l[i].valid){v=i;break;}
        if(l[i].lru<best){best=l[i].lru;v=i;}}
    if(l[v].valid){c->evicts++;if(l[v].dirty)c->dirty_ev++;}
    l[v].tag=tag;l[v].valid=1;l[v].dirty=wr;l[v].lru=c->clock;}

#define N 256
static uint8_t img[N][N], out[N][N];
static void trans_naive(Cache*c){
    for(int i=0;i<N;i++)for(int j=0;j<N;j++){
        access(c,(uint64_t)&img[i][j],0);
        access(c,(uint64_t)&out[j][i],1);}}
static void trans_blocked(Cache*c,int bs){
    for(int ii=0;ii<N;ii+=bs)for(int jj=0;jj<N;jj+=bs)
     for(int i=ii;i<ii+bs&&i<N;i++)for(int j=jj;j<jj+bs&&j<N;j++){
        access(c,(uint64_t)&img[i][j],0);
        access(c,(uint64_t)&out[j][i],1);}}

int main(void){
    puts("-- miss rate vs associativity (transpose N=256, S=32,B=64)");
    for(int E=1;E<=8;E*=2){Cache*c=mk(32,E,64);trans_naive(c);
        printf("E=%d  misses=%llu  rate=%.1f%%\n",E,
          (unsigned long long)c->misses,
          100.0*c->misses/(c->hits+c->misses));free(c->ln);free(c);}
    puts("-- naive vs blocked (S=64,E=4,B=64)");
    Cache*a=mk(64,4,64);trans_naive(a);
    printf("naive   : misses=%llu evictions=%llu\n",
        (unsigned long long)a->misses,(unsigned long long)a->evicts);
    for(int bs=4;bs<=32;bs*=2){Cache*c=mk(64,4,64);trans_blocked(c,bs);
        printf("block%2d : misses=%llu evictions=%llu\n",bs,
          (unsigned long long)c->misses,(unsigned long long)c->evicts);
        free(c->ln);free(c);}
    free(a->ln);free(a);return 0;}
