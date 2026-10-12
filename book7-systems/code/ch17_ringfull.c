/* ch17_ringfull.c -- how many items does a 256-slot ring really hold, and
 * what do head and tail look like after wrap-around?  Same push/pop as
 * ch17_ringbuf.c (single thread, indices masked with 255). */
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
  ring_t r={0,0,{0}}; int v,stored=0;
  while(push(&r,stored)==0) stored++;
  printf("pushes accepted before full: %d  (head=%u tail=%u)\n",stored,(unsigned)r.head,(unsigned)r.tail);
  for(int i=0;i<10;i++) pop(&r,&v);
  printf("after 10 pops: head=%u tail=%u\n",(unsigned)r.head,(unsigned)r.tail);
  for(int i=0;i<10;i++) push(&r,1000+i);
  printf("after 10 more pushes: head=%u tail=%u (head wrapped past 255)\n",(unsigned)r.head,(unsigned)r.tail);
  int n=0; while(pop(&r,&v)==0) n++;
  printf("drained %d items, last value %d\n",n,v);
  return 0;}
