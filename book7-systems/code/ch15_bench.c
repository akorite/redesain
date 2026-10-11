// ch15_bench.c -- the honest benchmark harness: warmup, repeated
// samples, p50/p99 tail stats. Used by ch15-17's measurements.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
static int cmpd(const void*a,const void*b){double d=*(const double*)a-*(const double*)b;return d<0?-1:d>0;}
// the workload: sum an array -- a foilable kernel on purpose
static long sum(const int*a,long n){long s=0;for(long i=0;i<n;i++)s+=a[i];return s;}
int main(void){
  long n=1L<<22; int*a=malloc(n*4); for(long i=0;i<n;i++)a[i]=i&0xff;
  volatile long sink;
  for(int i=0;i<3;i++) sink=sum(a,n);           // warmup
  double s[21];
  for(int i=0;i<21;i++){double t=now();sink=sum(a,n);s[i]=now()-t;}
  qsort(s,21,sizeof(double),cmpd);
  printf("n=4M ints sum: p50=%.2fms p99=%.2fms min=%.2fms max=%.2fms spread=%.0fx\n",
         s[10]*1e3,s[20]*1e3,s[0]*1e3,s[20]*1e3,s[20]/s[0]);
  // the foil: remove warmup + reduce to 3 samples
  double s2[3]; for(int i=0;i<3;i++){double t=now();sink=sum(a,n);s2[i]=now()-t;}
  qsort(s2,3,sizeof(double),cmpd);
  printf("same, 3 cold samples: p50=%.2fms (median lies by %.0f%%)\n",
         s2[1]*1e3,100*(s2[1]-s[0])/s[0]);
  return 0;}
