// ch17_ringbuf.c -- allocation-free SPSC ring buffer, the
// low-latency workhorse. No malloc, no lock, fixed size.
#include <stdio.h>
#include <stdint.h>
typedef struct{volatile uint32_t head,tail; int buf[256];}ring_t;
static int push(ring_t*r,int v){
  uint32_t n=(r->head+1)&255;
  if(n==r->tail) return -1;            /* full */
  r->buf[r->head]=v; r->head=n; return 0;}
static int pop(ring_t*r,int*v){
  if(r->tail==r->head) return -1;      /* empty */
  *v=r->buf[r->tail]; r->tail=(r->tail+1)&255; return 0;}
int main(void){
  ring_t r={0,0,{0}}; int v,bad=0;
  for(long i=0;i<1000000;i++){ push(&r,i); if(pop(&r,&v)||v!=i) bad++; }
  printf("ringbuf: 1M push/pop pairs, %d mismatches\n",bad);
  return 0;}
