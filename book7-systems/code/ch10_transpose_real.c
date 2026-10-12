// ch10_transpose_real.c -- wall-clock naive vs blocked transpose, 2048x2048
// floats (16 MiB per matrix).  Each variant does ONE full sweep per trial,
// timed separately; we report the best of TRIALS sweeps and verify every
// variant produces the same b[][] as the naive one (checksum).
// Build: cc -O2 -o ch10_transpose_real ch10_transpose_real.c
//
// Revision note: an earlier harness ran REPS sweeps inside each tile (so
// later sweeps hit a hot tile) but divided only the naive time by REPS.
// That flattered the blocked loops; this version times equal work.
#include <stdio.h>
#include <string.h>
#include <time.h>
#define N 2048
#define TRIALS 7
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
static float a[N][N], b[N][N];
static void naive(void){
    for(int i=0;i<N;i++)for(int j=0;j<N;j++)b[j][i]=a[i][j];}
static void blocked(int bs){
    for(int ii=0;ii<N;ii+=bs)for(int jj=0;jj<N;jj+=bs)
      for(int i=ii;i<ii+bs;i++)for(int j=jj;j<jj+bs;j++)b[j][i]=a[i][j];}
static double check(void){   /* sample b[][]; depends on every variant's output */
    double s=0;for(int i=0;i<N;i+=97)for(int j=0;j<N;j+=89)s+=b[j][i]*(i-j);
    return s;}
int main(void){
    for(int i=0;i<N;i++)for(int j=0;j<N;j++)a[i][j]=(float)(i*3+j);
    naive(); double ref=check(); double t_naive=0;
    for(int bs=0;bs<=64;bs=bs?bs*2:4){
        double best=1e9;
        for(int t=0;t<TRIALS;t++){
            memset(b,0,sizeof b);
            double t0=now(); if(bs)blocked(bs);else naive();
            double dt=now()-t0; if(dt<best)best=dt;}
        if(!bs)t_naive=best;
        printf("%s%2d  %dx%d: %6.2f ms  (%.2fx vs naive)  %s\n",
               bs?"block":"naive",bs,N,N,best*1000,t_naive/best,
               check()==ref?"result ok":"WRONG RESULT");}
    return 0;}
