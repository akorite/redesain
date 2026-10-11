// ch12_ctx_switch.c -- ctx-switch cost: each pair gets its OWN two
// pipes; parent round-trips sequentially with every child.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
int main(int argc,char**argv){
    int pairs=argc>1?atoi(argv[1]):1, trips=8000;
    int (*p2c)[2]=malloc(2*pairs*sizeof(int));
    int (*c2p)[2]=malloc(2*pairs*sizeof(int));
    for(int k=0;k<pairs;k++){pipe(p2c[k]);pipe(c2p[k]);}
    double t0=now();
    for(int k=0;k<pairs;k++){
      if(fork()==0){char b;close(p2c[k][1]);close(c2p[k][0]);
        for(int i=0;i<trips;i++)
          {if(read(p2c[k][0],&b,1)!=1)_exit(0);
           if(write(c2p[k][1],&b,1)!=1)_exit(0);}
        _exit(0);}}
    char b='x';
    for(int i=0;i<trips;i++)for(int k=0;k<pairs;k++){
      write(p2c[k][1],&b,1); read(c2p[k][0],&b,1);}
    double dt=now()-t0;
    for(int k=0;k<pairs;k++)wait(NULL);
    printf("pairs=%d  %.2f us per ctx switch (%.0f rtrips/s)\n",
           pairs,dt/trips/pairs/2*1e6,trips*pairs/dt);
    return 0;}
