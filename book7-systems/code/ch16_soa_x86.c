/* ch16_soa_x86.c -- AoS vs SoA, x86_64 rewrite of ch16_soa.c.
 * Differences from the Mac program: every array is fully written before timing
 * (no first-touch page faults inside the timed region), and each pass is a
 * separate noinline call so the compiler cannot interchange the repeat loop
 * into the element loop.  Kernel: x[i] += m[i] over n = 2^24 particles.
 * Build: gcc -O3 ch16_soa_x86.c   (add -fno-tree-vectorize for the scalar build) */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
typedef struct{float x,y,z,m;}P;               /* 16 bytes per particle */
__attribute__((noinline)) static void aos_pass(P*p,long n){
  for(long i=0;i<n;i++) p[i].x+=p[i].m;}
__attribute__((noinline)) static void soa_pass(float*restrict x,const float*restrict m,long n){
  for(long i=0;i<n;i++) x[i]+=m[i];}
int main(void){
  long n=1L<<24; int reps=10;
  P*p=malloc(n*sizeof(P)); float*x=malloc(n*4),*y=malloc(n*4),*z=malloc(n*4),*m=malloc(n*4);
  for(long i=0;i<n;i++){p[i]=(P){i*1e-3f,0,0,1e-3f}; x[i]=i*1e-3f; y[i]=0; z[i]=0; m[i]=1e-3f;}
  aos_pass(p,n); soa_pass(x,m,n);                          /* warm-up pass */
  double best_a=1e9,best_s=1e9;
  for(int k=0;k<reps;k++){
    double t=now(); aos_pass(p,n); double d=now()-t; if(d<best_a)best_a=d;
    t=now(); soa_pass(x,m,n); d=now()-t; if(d<best_s)best_s=d;}
  printf("AoS x+=m: %.2f ms/pass  (touches %ld MB)\n",best_a*1e3,n*16>>20);
  printf("SoA x+=m: %.2f ms/pass  (touches %ld MB)\n",best_s*1e3,n*8>>20);
  printf("ratio AoS/SoA = %.2fx   (checksum %g)\n",best_a/best_s,(double)p[n-1].x+x[n-1]+y[0]+z[0]);
  return 0;}
