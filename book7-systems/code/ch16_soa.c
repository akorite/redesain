// ch16_soa.c -- AoS vs SoA on a 4-field particle update.
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
typedef struct{float x,y,z,m;}P;
int main(void){
  long n=1L<<24;
  P*p=malloc(n*sizeof(P)); float*x=malloc(n*4),*y=malloc(n*4),*z=malloc(n*4),*m=malloc(n*4);
  for(long i=0;i<n;i++){p[i].x=i;m[i]=i*0.1f;}
  double t=now();
  for(int r=0;r<10;r++)for(long i=0;i<n;i++)p[i].x+=p[i].m; // AoS: touches 4 fields to use 2
  printf("AoS x+=m: %.1fms\n",(now()-t)*1e2);
  t=now();
  for(int r=0;r<10;r++)for(long i=0;i<n;i++)x[i]+=m[i];      // SoA: streams 2 arrays
  printf("SoA x+=m: %.1fms\n",(now()-t)*1e2);
  return 0;}
