/* ch16_satadd.c -- an operation the compiler may not find: unsigned 8-bit
 * saturating add (pixel brighten).  Scalar clamp loop vs _mm_adds_epu8
 * (16 lanes of u8 in one instruction).  Also checks both agree. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <emmintrin.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
__attribute__((noinline)) static void sat_scalar(const unsigned char*a,const unsigned char*b,unsigned char*o,long n){
  for(long i=0;i<n;i++){int s=a[i]+b[i]; o[i]= s>255?255:s;}}
__attribute__((noinline)) static void sat_sse2(const unsigned char*a,const unsigned char*b,unsigned char*o,long n){
  long i=0;
  for(;i+16<=n;i+=16)
    _mm_storeu_si128((__m128i*)(o+i),_mm_adds_epu8(_mm_loadu_si128((const __m128i*)(a+i)),_mm_loadu_si128((const __m128i*)(b+i))));
  for(;i<n;i++){int s=a[i]+b[i]; o[i]= s>255?255:s;}}
int main(void){
  long n=1L<<16; unsigned char*a=malloc(n),*b=malloc(n),*o1=malloc(n),*o2=malloc(n);
  srand(1); for(long i=0;i<n;i++){a[i]=rand();b[i]=rand();}
  sat_scalar(a,b,o1,n); sat_sse2(a,b,o2,n);
  printf("outputs identical: %s\n", memcmp(o1,o2,n)==0?"yes":"NO");
  int reps=20000; double best1=1e9,best2=1e9;
  for(int k=0;k<5;k++){
    double t=now(); for(int r=0;r<reps;r++) sat_scalar(a,b,o1,n); double d=(now()-t)/reps; if(d<best1)best1=d;
    t=now(); for(int r=0;r<reps;r++) sat_sse2(a,b,o2,n); d=(now()-t)/reps; if(d<best2)best2=d;}
  printf("scalar clamp: %.4f ms   _mm_adds_epu8: %.4f ms   speedup %.1fx  (n=%ld bytes)\n",best1*1e3,best2*1e3,best1/best2,n);
  return 0;}
