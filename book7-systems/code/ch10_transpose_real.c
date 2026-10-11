// ch10_transpose_real.c -- wall-clock naive vs blocked transpose
// on the real machine (time, not sim counts).
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 2048
#define REPS 4
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
static float a[N][N], b[N][N];
int main(void){
    for(int i=0;i<N;i++)for(int j=0;j<N;j++)a[i][j]=i+j;
    volatile float sink;
    double t0=now();
    for(int r=0;r<REPS;r++)for(int i=0;i<N;i++)for(int j=0;j<N;j++)b[j][i]=a[i][j];
    sink=b[0][0]+b[N-1][N-1];
    printf("naive   %dx%d: %.2f ms\n",N,N,(now()-t0)*1000/REPS);
    for(int bs=8;bs<=64;bs*=2){t0=now();
     for(int ii=0;ii<N;ii+=bs)for(int jj=0;jj<N;jj+=bs)
      for(int r=0;r<REPS;r++)for(int i=ii;i<ii+bs;i++)for(int j=jj;j<jj+bs;j++)b[j][i]=a[i][j];
     printf("block%2d %dx%d: %.1f ms\n",bs,N,N,(now()-t0)*1000);}
    return 0;}
