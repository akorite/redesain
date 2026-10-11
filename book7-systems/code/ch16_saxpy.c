// ch16_saxpy.c -- SAXPY three ways on arm64: scalar, compiler
// auto-vectorised (-O3 -mcpu), and NEON intrinsics. All real.
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <arm_neon.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
static void sax_scalar(const float*x,float*y,float a,long n){
  for(long i=0;i<n;i++) y[i]+=a*x[i];}
static void sax_neon(const float*x,float*y,float a,long n){
  float32x4_t va=vdupq_n_f32(a);
  for(long i=0;i<n;i+=4){
    float32x4_t vx=vld1q_f32(x+i), vy=vld1q_f32(y+i);
    vst1q_f32(y+i,vmlaq_f32(vy,va,vx));}}
int main(void){
  for(long n=1L<<10;n<=1L<<26;n*=8){
    float*x=malloc(n*4),*y=calloc(n,4);
    for(long i=0;i<n;i++)x[i]=i*0.001f;
    volatile float sink;
    sax_scalar(x,y,2,n); sink=y[0];  // warm
    double t=now(); for(int r=0;r<5;r++)sax_scalar(x,y,2,n);
    double ts=(now()-t)/5;
    t=now(); for(int r=0;r<5;r++)sax_neon(x,y,2,n);
    double tv=(now()-t)/5;
    printf("n=2^%ld: scalar %.3fms neon %.3fms speedup %.1fx\n",
      ({long k=0,v=n;while(v>1){v>>=1;k++;}k;}),ts*1e3,tv*1e3,ts/tv);
    free(x);free(y);}
  return 0;}
