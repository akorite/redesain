/* ch17_branch_x86.c -- when does "branchless" pay?  Sum the elements >= 128
 * of an int array holding values 0..255, in two orders: random and sorted.
 *   branchy   : if (v >= 128) sum += v;   (an empty asm statement inside the
 *               branch stops gcc from silently turning it into a cmov)
 *   branchless: sum += v & -(v >= 128);   (mask is all-ones or all-zeros)
 * Build: gcc -O2 -fno-tree-vectorize ch17_branch_x86.c
 * (-fno-tree-vectorize so that neither loop is replaced by SIMD code.) */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N (1<<20)
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
__attribute__((noinline)) static long branchy(const int*a){
  long s=0; for(int i=0;i<N;i++){ int v=a[i]; if(v>=128){ __asm__ volatile(""); s+=v; } } return s;}
__attribute__((noinline)) static long branchless(const int*a){
  long s=0; for(int i=0;i<N;i++){ int v=a[i]; s+= v & -(v>=128); } return s;}
static int cmp(const void*p,const void*q){return *(const int*)p-*(const int*)q;}
static double best(long(*f)(const int*),const int*a,long*out){
  double b=1e9; for(int k=0;k<20;k++){ double t=now(); *out=f(a); double d=now()-t; if(d<b)b=d; } return b;}
int main(void){
  int*a=malloc(N*sizeof(int)); srand(7);
  for(int i=0;i<N;i++) a[i]=rand()&255;
  long r1,r2; double tb,tl;
  tb=best(branchy,a,&r1); tl=best(branchless,a,&r2);
  printf("random: branchy %.3f ms  branchless %.3f ms  (sums %ld %ld)\n",tb*1e3,tl*1e3,r1,r2);
  qsort(a,N,sizeof(int),cmp);
  tb=best(branchy,a,&r1); tl=best(branchless,a,&r2);
  printf("sorted: branchy %.3f ms  branchless %.3f ms  (sums %ld %ld)\n",tb*1e3,tl*1e3,r1,r2);
  return 0;}
