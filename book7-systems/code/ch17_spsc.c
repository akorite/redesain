/* ch17_spsc.c -- a real two-thread SPSC ring buffer with C11 atomics.
 * One producer thread pushes 0..N-1, one consumer thread pops and checks
 * that the values arrive in order and unchanged.  Two layouts:
 *   packed: head and tail share one 64-byte cache line (false sharing)
 *   padded: head and tail each get their own cache line
 * release/acquire ordering: the producer's store to head "publishes" the
 * slot written just before it; the consumer's acquire load of head makes
 * that slot visible.  Build: gcc -O2 -pthread ch17_spsc.c */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdatomic.h>
#include <pthread.h>
#include <sched.h>
#include <time.h>
#define SLOTS 256
#define N 20000000L
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}

typedef struct { _Atomic uint32_t head, tail; int buf[SLOTS]; } ring_packed;
typedef struct { _Alignas(64) _Atomic uint32_t head; _Alignas(64) _Atomic uint32_t tail;
                 _Alignas(64) int buf[SLOTS]; } ring_padded;

/* the same code for both layouts: a macro keeps them identical */
#define DEFINE_RING_FUNCS(T) \
static void T##_push(T*r,int v){ \
  uint32_t h=atomic_load_explicit(&r->head,memory_order_relaxed), n=(h+1)&(SLOTS-1); \
  while(n==atomic_load_explicit(&r->tail,memory_order_acquire)) ; /* full: spin */ \
  r->buf[h]=v; \
  atomic_store_explicit(&r->head,n,memory_order_release); } \
static int T##_pop(T*r){ \
  uint32_t t=atomic_load_explicit(&r->tail,memory_order_relaxed); \
  while(t==atomic_load_explicit(&r->head,memory_order_acquire)) ; /* empty: spin */ \
  int v=r->buf[t]; \
  atomic_store_explicit(&r->tail,(t+1)&(SLOTS-1),memory_order_release); return v; }
DEFINE_RING_FUNCS(ring_packed)
DEFINE_RING_FUNCS(ring_padded)

static void pin(int cpu){cpu_set_t s;CPU_ZERO(&s);CPU_SET(cpu,&s);
  pthread_setaffinity_np(pthread_self(),sizeof s,&s);}
static void*prod_packed(void*a){pin(0);for(long i=0;i<N;i++)ring_packed_push(a,(int)i);return 0;}
static void*prod_padded(void*a){pin(0);for(long i=0;i<N;i++)ring_padded_push(a,(int)i);return 0;}

int main(void){
  static ring_packed rp; static ring_padded rq;
  for(int variant=0;variant<2;variant++){
    pthread_t th; long bad=0;
    double t=now();
    pthread_create(&th,0,variant?prod_padded:prod_packed,variant?(void*)&rq:(void*)&rp);
    pin(1);
    for(long i=0;i<N;i++){ int v=variant?ring_padded_pop(&rq):ring_packed_pop(&rp); if(v!=(int)i)bad++; }
    pthread_join(th,0);
    double d=now()-t;
    printf("%-6s: %ld items, %ld out of order, %.1f ms, %.1f M items/s\n",
           variant?"padded":"packed",N,bad,d*1e3,N/d/1e6);}
  printf("sizeof packed=%zu padded=%zu\n",sizeof(ring_packed),sizeof(ring_padded));
  return 0;}
