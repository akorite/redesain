// ch11_fault_cost.c -- first-touch (page fault) vs resident access
// cost via mmap, measured on this machine.
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <time.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
int main(void){
    size_t mb=512, nb=(size_t)mb<<20, np=nb/16384;
    /* first-touch: every page faults */
    char*p=mmap(NULL,nb,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANON,-1,0);
    double t0=now(); volatile char s=0;
    for(size_t i=0;i<nb;i+=16384)s+=p[i];
    double fresh=(now()-t0)/np*1e9;
    /* resident: same walk again */
    t0=now(); for(size_t i=0;i<nb;i+=16384)s+=p[i];
    double res=(now()-t0)/np*1e9;
    printf("pages=%zu\nfirst-touch %.0f ns/page\nresident    %.1f ns/page\nfault cost %.0fx\n",
           np,fresh,res,fresh/res);
    munmap(p,nb);return 0;}
