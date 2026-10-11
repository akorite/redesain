// ch13_lockscale.c -- counter increments at 1..8 threads, three ways:
// mutex, C11 atomic add, per-thread partition summed at the end.
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdatomic.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
#define PER 400000
static long mtx_c; static pthread_mutex_t m=PTHREAD_MUTEX_INITIALIZER;
static _Atomic long atm_c; static long *part;
static void *f_mtx(void*a){for(long i=0;i<PER;i++){pthread_mutex_lock(&m);mtx_c++;pthread_mutex_unlock(&m);}return 0;}
static void *f_atm(void*a){for(long i=0;i<PER;i++)atomic_fetch_add(&atm_c,1);return 0;}
static void *f_pt(void*a){long k=(long)a;for(long i=0;i<PER;i++)part[k]++;return 0;}
int main(void){
  printf("%3s %9s %9s %9s\n","T","mutex","atomic","partition");
  part=calloc(8,sizeof(long));
  for(int T=1;T<=8;T*=2){
    pthread_t t[8];double t0;
    mtx_c=0;t0=now();for(int i=0;i<T;i++)pthread_create(&t[i],0,f_mtx,0);
    for(int i=0;i<T;i++)pthread_join(t[i],0);double tm=now()-t0;
    atm_c=0;t0=now();for(int i=0;i<T;i++)pthread_create(&t[i],0,f_atm,0);
    for(int i=0;i<T;i++)pthread_join(t[i],0);double ta=now()-t0;
    for(int i=0;i<8;i++)part[i]=0;t0=now();
    for(int i=0;i<T;i++)pthread_create(&t[i],0,f_pt,(void*)(long)i);
    for(int i=0;i<T;i++)pthread_join(t[i],0);double tp=now()-t0;
    printf("%3d %9.1f %9.1f %9.3f\n",T,tm*1e3,ta*1e3,tp*1e3);}
  return 0;}
