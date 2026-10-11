// ch17_folklore.c -- 5 low-latency claims audited on real hardware.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
__attribute__((noinline)) static void*myalloc(size_t z){return malloc(z);}
__attribute__((noinline)) static void myfree(void*p){free(p);}
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
#define N (1L<<24)  // 16M
static int*a;
// claim 1: branchless min is faster
static int min_b(int x,int y){return x<y?x:y;}
static int min_bl(int x,int y){int m=x-y;return y+(m&(m>>31));}
// claim 2: binary beats linear on sorted data (size-dependent!)
static long lin(const int*v,long n,int k){long i;for(i=0;i<n&&v[i]!=k;i++);return i;}
static long bin(const int*v,long n,int k){long lo=0,hi=n-1;while(lo<=hi){long m=(lo+hi)/2;if(v[m]==k)return m;if(v[m]<k)lo=m+1;else hi=m-1;}return -1;}
int main(void){
  a=malloc(N*4); for(long i=0;i<N;i++)a[i]=i*2;
  volatile int si; volatile long sl;
  double t;
  // 1: branchless vs branchy min, 100M ops
  t=now(); for(long i=0;i<100000000;i++)si=min_b(i&0xffff,12345); printf("min branchy:  %.1fms\n",(now()-t)*1e3);
  t=now(); for(long i=0;i<100000000;i++)si=min_bl(i&0xffff,12345); printf("min branchless: %.1fms\n",(now()-t)*1e3);
  // 2: linear vs binary at two sizes
  t=now(); for(int r=0;r<200;r++)sl=lin(a,64,127);  printf("linear n=64:  %.3fus\n",(now()-t)*1e6/200);
  t=now(); for(int r=0;r<200;r++)sl=bin(a,64,127);  printf("binary n=64:  %.3fus\n",(now()-t)*1e6/200);
  t=now(); for(int r=0;r<200;r++)sl=lin(a,N,N);     printf("linear n=16M: %.1fms\n",(now()-t)*1e3/200);
  t=now(); for(int r=0;r<200;r++)sl=bin(a,N,N);     printf("binary n=16M: %.3fus\n",(now()-t)*1e6/200);
  // 3: malloc in a hot loop vs pool reuse
  t=now(); {int tot=0;for(int i=0;i<50000;i++){int*q=myalloc(64);q[15]=i;tot+=q[15];myfree(q);}si=tot;} printf("malloc/free: %.3fus each\n",(now()-t)*1e6/50000);
  static int pool[16]; int pc=0;
  t=now(); {int tot=0;for(int i=0;i<50000;i++){int*q=&pool[(pc++)&15];q[15]=i;tot+=q[15];}si=tot;}  printf("pool reuse:  %.3fus each\n",(now()-t)*1e6/50000);
  return 0;}
