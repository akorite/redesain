// ch18_vm.c -- a 9-opcode stack VM: the interpreter half.
#include <stdio.h>
enum{HALT,PUSH,ADD,SUB,MUL,DIV,DUP,OUT,JNZ};
static int ip,sp,st[256]; static long ins;
#define N st[--sp]
static void run(const int*p){
 while(1){ins++;
  switch(p[ip++]){
   case HALT:return;
   case PUSH:st[sp++]=p[ip++];break;
   case ADD:{int b=N,a=N;st[sp++]=a+b;}break;
   case SUB:{int b=N,a=N;st[sp++]=a-b;}break;
   case MUL:{int b=N,a=N;st[sp++]=a*b;}break;
   case DIV:{int b=N,a=N;st[sp++]=a/b;}break;
   case DUP:{int a=N;st[sp++]=a;st[sp++]=a;}break;
   case OUT:printf("%d\n",N);break;
   case JNZ:{int a=p[ip++];if(N)ip=a;}break;}}}
int main(void){
 // (6*7)+8, print -> 50  ; then a countdown 3..1 via JNZ loop
 int prog[]={PUSH,6,PUSH,7,MUL,PUSH,8,ADD,DUP,OUT,
             PUSH,3,DUP,OUT,PUSH,1,SUB,DUP,JNZ,12,OUT,HALT};
 run(prog);
 printf("instructions executed: %ld\n",ins);
 return 0;}
