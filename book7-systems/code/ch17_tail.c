/* ch17_tail.c -- mean vs tail: per-call latency of malloc vs a fixed pool.
 * Each call is timed individually with clock_gettime, so every row includes
 * the timer's own cost; the "empty" row measures that cost alone.
 * Workload: 4096 live blocks of random size 16..2048 bytes; each step frees
 * a random live block and allocates a new random-size one (fragmenting the
 * heap).  Pool: the same churn on fixed 2048-byte slots taken from a free
 * stack.  Build: gcc -O2 ch17_tail.c */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define LIVE 4096
#define STEPS 2000000
static inline long ns(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec*1000000000L+t.tv_nsec;}
static int cmpl(const void*a,const void*b){long x=*(const long*)a,y=*(const long*)b;return (x>y)-(x<y);}
static void report(const char*name,long*lat,long n){
  double sum=0; for(long i=0;i<n;i++) sum+=lat[i];
  qsort(lat,n,sizeof(long),cmpl);
  printf("%-12s mean %7.1f  p50 %5ld  p99 %6ld  p99.9 %7ld  max %9ld  (ns)\n",
         name,sum/n,lat[n/2],lat[n*99/100],lat[n*999/1000],lat[n-1]);}
static unsigned rs=12345; static unsigned rnd(void){rs=rs*1664525u+1013904223u;return rs>>8;}
int main(void){
  long*lat=malloc(STEPS*sizeof(long)); void*live[LIVE]={0};
  /* empty: two back-to-back timer reads */
  for(long i=0;i<STEPS;i++){long a=ns(),b=ns();lat[i]=b-a;} report("empty timer",lat,STEPS);
  /* malloc: time only the malloc call */
  for(long i=0;i<STEPS;i++){
    int k=rnd()%LIVE; free(live[k]);
    size_t sz=16+rnd()%2033;
    long a=ns(); void*p=malloc(sz); long b=ns();
    if(p)((char*)p)[0]=1; live[k]=p; lat[i]=b-a;}
  report("malloc",lat,STEPS);
  for(int k=0;k<LIVE;k++){free(live[k]);live[k]=0;}
  /* pool: fixed 2048-byte slots, free stack */
  static char slab[LIVE][2048]; static int stk[LIVE]; int top=0;
  for(int k=0;k<LIVE;k++) stk[top++]=k;
  static int slot[LIVE]; for(int k=0;k<LIVE;k++) slot[k]=-1;
  for(long i=0;i<STEPS;i++){
    int k=rnd()%LIVE; if(slot[k]>=0) stk[top++]=slot[k];
    long a=ns(); int s=stk[--top]; long b=ns();
    slab[s][0]=1; slot[k]=s; lat[i]=b-a; }
  report("pool",lat,STEPS);
  return 0;}
