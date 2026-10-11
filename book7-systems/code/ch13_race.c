// ch13_race.c -- the lost-update race, unfixed and now visible.
#include <stdio.h>
#include <pthread.h>
static volatile long counter;
#define N 500000
static void *add(void*a){for(long i=0;i<N;i++){
  long t=counter; t=t+1; counter=t;}   /* load-add-store, unprotected */
  return 0;}
int main(void){
    pthread_t t[6];
    for(int i=0;i<6;i++)pthread_create(&t[i],0,add,0);
    for(int i=0;i<6;i++)pthread_join(t[i],0);
    printf("counter=%ld (expected %d, lost %ld)\n",
           counter,6*N,6L*N-counter);
    return 0;}
