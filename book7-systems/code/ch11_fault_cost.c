// ch11_fault_cost.c -- first-touch (page fault) vs resident access
// cost via mmap, measured on this machine. The page size is read from
// the OS, so the same source runs on 4 KB (Linux/x86) and 16 KB (macOS/arm64).
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
int main(void){
    size_t pg=(size_t)sysconf(_SC_PAGESIZE);   /* 4096 on Linux/x86, 16384 on macOS/arm64 */
    size_t mb=512, nb=(size_t)mb<<20, np=nb/pg;
    /* first-touch: every page faults */
    char*p=mmap(NULL,nb,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANON,-1,0);
    double t0=now(); volatile char s=0;
    for(size_t i=0;i<nb;i+=pg)s+=p[i];
    double fresh=(now()-t0)/np*1e9;
    /* resident: same walk again */
    t0=now(); for(size_t i=0;i<nb;i+=pg)s+=p[i];
    double res=(now()-t0)/np*1e9;
    printf("page size=%zu bytes\npages=%zu\nfirst-touch %.0f ns/page\nresident    %.1f ns/page\nfault cost %.0fx\n",
           pg,np,fresh,res,fresh/res);
    munmap(p,nb);return 0;}
