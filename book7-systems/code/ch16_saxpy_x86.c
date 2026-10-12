/* ch16_saxpy_x86.c -- SAXPY (y = a*x + y) on x86_64: scalar vs SSE2 (4 lanes)
 * vs AVX2 (8 lanes).  Build twice to see what the compiler does by itself:
 *   gcc -O3 -fno-tree-vectorize -mavx2 -mfma ...   (honest scalar baseline)
 *   gcc -O3                     -mavx2 -mfma ...   (compiler allowed to vectorise)
 * The SSE2/AVX2 kernels are hand-written intrinsics in both builds.
 * Usage: ./prog [max_log2_n]   Prints one line per n: times in ms per call. */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <immintrin.h>

static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}

__attribute__((noinline))
static void sax_scalar(const float*restrict x,float*restrict y,float a,long n){
  for(long i=0;i<n;i++) y[i]+=a*x[i];}

__attribute__((noinline))
static void sax_sse2(const float*x,float*y,float a,long n){
  __m128 va=_mm_set1_ps(a); long i=0;
  for(;i+4<=n;i+=4){
    __m128 vx=_mm_loadu_ps(x+i), vy=_mm_loadu_ps(y+i);
    _mm_storeu_ps(y+i,_mm_add_ps(vy,_mm_mul_ps(va,vx)));}
  for(;i<n;i++) y[i]+=a*x[i];}          /* scalar tail */

__attribute__((noinline,target("avx2")))
static void sax_avx2(const float*x,float*y,float a,long n){
  __m256 va=_mm256_set1_ps(a); long i=0;
  for(;i+8<=n;i+=8){
    __m256 vx=_mm256_loadu_ps(x+i), vy=_mm256_loadu_ps(y+i);
    _mm256_storeu_ps(y+i,_mm256_add_ps(vy,_mm256_mul_ps(va,vx)));}
  for(;i<n;i++) y[i]+=a*x[i];}

typedef void (*fn)(const float*,float*,float,long);
static double bench(fn f,const float*x,float*y,long n){
  int reps = (int)((1L<<26)/n); if(reps<5) reps=5; if(reps>20000) reps=20000;
  f(x,y,0.0f,n);                               /* warm caches, y unchanged */
  double best=1e9;
  for(int k=0;k<5;k++){                        /* best of 5 batches */
    double t=now(); for(int r=0;r<reps;r++) f(x,y,1e-6f,n);
    double d=(now()-t)/reps; if(d<best) best=d;}
  return best;}

static int check(void){            /* all three kernels agree on a ragged n */
  long n=1003; float x[1003],y0[1003],y1[1003],y2[1003],y3[1003];
  for(long i=0;i<n;i++){x[i]=i*0.25f;y0[i]=y1[i]=y2[i]=y3[i]=(float)(i%7);}
  sax_scalar(x,y1,3.0f,n); sax_sse2(x,y2,3.0f,n); sax_avx2(x,y3,3.0f,n);
  for(long i=0;i<n;i++) if(y1[i]!=y2[i]||y1[i]!=y3[i]) return 0;
  return 1;}

int main(int argc,char**argv){
  long maxlog = argc>1 ? atol(argv[1]) : 25;
  printf("correctness (n=1003, ragged tail): %s\n", check()?"ok":"MISMATCH");
  printf("%-6s %10s %10s %10s %8s %8s\n","n","scalar_ms","sse2_ms","avx2_ms","sse2_x","avx2_x");
  for(long lg=10; lg<=maxlog; lg+=3){
    long n=1L<<lg;
    float*x=aligned_alloc(64,n*4),*y=aligned_alloc(64,n*4);
    for(long i=0;i<n;i++){x[i]=i*0.001f;y[i]=0;}
    double a=bench(sax_scalar,x,y,n), b=bench(sax_sse2,x,y,n), c=bench(sax_avx2,x,y,n);
    printf("2^%-4ld %10.5f %10.5f %10.5f %7.2fx %7.2fx\n",lg,a*1e3,b*1e3,c*1e3,a/b,a/c);
    free(x);free(y);}
  return 0;}
