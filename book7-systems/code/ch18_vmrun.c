/* ch18_vmrun.c -- the chapter's 9-opcode stack VM, as a program loader:
 * reads the bytecode as whitespace-separated integers from stdin and runs it.
 *   ./ch18_vmrun        run, print OUT values, then the dispatch count
 *   ./ch18_vmrun -t     also print a trace line per dispatched instruction
 * Unlike ch18_vm.c this version bounds-checks the stack and the ip, so a
 * bad program stops with an error instead of corrupting memory.
 * Opcodes (same numbering as ch18_vm.c):
 *   0 HALT  1 PUSH n  2 ADD  3 SUB  4 MUL  5 DIV  6 DUP  7 OUT  8 JNZ addr */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
enum{HALT,PUSH,ADD,SUB,MUL,DIV,DUP,OUT,JNZ};
static const char*NAME[]={"HALT","PUSH","ADD","SUB","MUL","DIV","DUP","OUT","JNZ"};
#define STK 256
static int prog[4096], plen, st[STK], sp, ip; static long ins;
static void die(const char*m){printf("VM error at ip=%d: %s\n",ip,m);exit(1);}
static int pop(void){ if(sp<=0) die("stack underflow"); return st[--sp]; }
static void push(int v){ if(sp>=STK) die("stack overflow"); st[sp++]=v; }
int main(int argc,char**argv){
  int trace = argc>1 && !strcmp(argv[1],"-t"), x;
  while(plen<4096 && scanf("%d",&x)==1) prog[plen++]=x;
  for(;;){
    if(ip<0||ip>=plen) die("ip out of range");
    int at=ip, op=prog[ip++]; ins++;
    if(op<0||op>JNZ) die("bad opcode");
    if(trace){ printf("%3ld  ip=%-3d %-4s",ins,at,NAME[op]);
      if(op==PUSH||op==JNZ) printf(" %-3d",prog[ip]); else printf("    ");
      printf("  stack before:"); for(int i=0;i<sp;i++) printf(" %d",st[i]); printf("\n"); }
    switch(op){
      case HALT: printf("instructions executed: %ld\n",ins); return 0;
      case PUSH: if(ip>=plen) die("missing operand"); push(prog[ip++]); break;
      case ADD:{int b=pop(),a=pop();push(a+b);}break;
      case SUB:{int b=pop(),a=pop();push(a-b);}break;
      case MUL:{int b=pop(),a=pop();push(a*b);}break;
      case DIV:{int b=pop(),a=pop(); if(b==0) die("divide by zero"); push(a/b);}break;
      case DUP:{int a=pop();push(a);push(a);}break;
      case OUT: printf("%d\n",pop()); break;
      case JNZ:{ if(ip>=plen) die("missing operand"); int t=prog[ip++]; if(pop()) ip=t; }break;}}}
