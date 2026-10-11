/* ch02_pad.c -- struct layout probe: real sizeof/offsetof */
#include <stddef.h>
#include <stdio.h>
struct A { char c; double d; int i; };
struct B { double d; int i; char c; };
int main(void) {
    printf("A: sizeof=%zu  c@%zu d@%zu i@%zu\n",
           sizeof(struct A), offsetof(struct A,c),
           offsetof(struct A,d), offsetof(struct A,i));
    printf("B: sizeof=%zu  d@%zu i@%zu c@%zu\n",
           sizeof(struct B), offsetof(struct B,d),
           offsetof(struct B,i), offsetof(struct B,c));
    return 0;
}
