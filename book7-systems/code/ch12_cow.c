// ch12_cow.c -- fork returns twice, and the child gets a COPY of memory.
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
int x = 100;                              // one variable, two processes
int main(void) {
    pid_t p = fork();
    if (p < 0) { perror("fork"); return 1; }
    if (p == 0) {                         // this branch runs only in the child (fork returned 0)
        x += 1;
        printf("child : fork returned %d, x=%d, &x=%p\n", (int)p, x, (void *)&x);
        return 0;
    }
    waitpid(p, NULL, 0);                  // this branch: fork returned the child's pid
    printf("parent: fork returned child pid > 0: %s, x=%d, &x=%p\n", p > 0 ? "yes" : "no", x, (void *)&x);
    return 0;
}
