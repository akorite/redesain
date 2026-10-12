/* ch18_vm_bench.c -- what does interpretation cost?  The same countdown
 *   n = N; do { n = n - 1 } while (n != 0);
 * run (a) natively and (b) as stack-VM bytecode:
 *   PUSH N | L: PUSH 1  SUB  DUP  JNZ L | HALT     (L = address 2)
 * Four dispatches per iteration (PUSH, SUB, DUP, JNZ).  Same switch-based
 * dispatch loop as ch18_vm.c.  Build: gcc -O2 ch18_vm_bench.c */
#include <stdio.h>
#include <time.h>
enum{HALT,PUSH,ADD,SUB,MUL,DIV,DUP,OUT,JNZ};
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
static int st[256];
__attribute__((noinline)) static long vm(const int*p){
  int ip=0,sp=0; long ins=0;
  for(;;){ ins++;
    switch(p[ip++]){
      case HALT: return ins;
      case PUSH: st[sp++]=p[ip++]; break;
      case SUB:{int b=st[--sp],a=st[--sp]; st[sp++]=a-b;}break;
      case DUP:{int a=st[sp-1]; st[sp++]=a;}break;
      case JNZ:{int t=p[ip++]; if(st[--sp]) ip=t;}break;}}}
__attribute__((noinline)) static long native(long n){
  volatile long v=n; do { v=v-1; } while(v!=0); return n;}
__attribute__((noinline)) static long native_reg(long n){
  long v=n; do { v=v-1; __asm__ volatile("" : "+r"(v)); } while(v!=0); return n;}   /* counter stays in a register */
int main(void){
  long N=100000000L;
  int prog[]={PUSH,(int)N,PUSH,1,SUB,DUP,JNZ,2,HALT};
  double t=now(); long d=vm(prog); double tv=now()-t;
  t=now(); native(N); double tn=now()-t;
  t=now(); native_reg(N); double tr=now()-t;
  printf("iterations: %ld\n",N);
  printf("native, register counter: %7.1f ms  (%.2f ns/iter)\n",tr*1e3,tr*1e9/N);
  printf("native, memory counter  : %7.1f ms  (%.2f ns/iter)\n",tn*1e3,tn*1e9/N);
  printf("stack VM                : %7.1f ms  (%.2f ns/iter, %ld dispatches, %.2f ns/dispatch)\n",
         tv*1e3,tv*1e9/N,d,tv*1e9/d);
  printf("VM / native(register) = %.1fx    VM / native(memory) = %.1fx\n",tv/tr,tv/tn);
  return 0;}
