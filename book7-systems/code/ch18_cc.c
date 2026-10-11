// ch18_cc.c -- the compiler half: same AST to x86-64-ish asm text.
#include <stdio.h>
// compile  (a+b)*c  where a,b,c are immediates in vars
int main(void){
 int a=6,b=7,c=8;
 printf("# ch18_cc out: compile (a+b)*c with a=%d b=%d c=%d\n",a,b,c);
 printf("  mov  w0, #%d\n",a);
 printf("  mov  w1, #%d\n",b);
 printf("  add  w0, w0, w1\n");
 printf("  mov  w1, #%d\n",c);
 printf("  mul  w0, w0, w1\n");
 printf("# eval at compile time: %d\n",(a+b)*c);
 return 0;}
