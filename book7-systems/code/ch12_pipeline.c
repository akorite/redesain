// ch12_pipeline.c -- what a shell does for  `echo ... | tr a-z A-Z | wc -c`:
// 3 forks, 2 pipes, dup2 to wire stdin/stdout, 3 execs, 3 waits.
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
static void spawn(char *const argv[], int in_fd, int out_fd, int close_a, int close_b, int close_c, int close_d) {
    pid_t p = fork();
    if (p < 0) { perror("fork"); exit(1); }
    if (p == 0) {
        if (in_fd  != 0) dup2(in_fd, 0);       // make the pipe end become stdin
        if (out_fd != 1) dup2(out_fd, 1);      // ...or stdout
        close(close_a); close(close_b); close(close_c); close(close_d);
        execvp(argv[0], argv);
        perror(argv[0]); _exit(127);
    }
}
int main(void) {
    int p1[2], p2[2];
    if (pipe(p1) < 0 || pipe(p2) < 0) { perror("pipe"); return 1; }
    char *a1[] = {"echo", "hello systems", NULL};
    char *a2[] = {"tr", "a-z", "A-Z", NULL};
    char *a3[] = {"wc", "-c", NULL};
    spawn(a1, 0,     p1[1], p1[0], p1[1], p2[0], p2[1]);
    spawn(a2, p1[0], p2[1], p1[0], p1[1], p2[0], p2[1]);
    spawn(a3, p2[0], 1,     p1[0], p1[1], p2[0], p2[1]);
#ifndef LEAK                                   // -DLEAK builds the buggy version: it hangs
    close(p1[0]); close(p1[1]); close(p2[0]); close(p2[1]);   // parent must close ALL ends
#endif
    int st, n = 0;
    while (wait(&st) > 0) n++;
    printf("parent reaped %d children\n", n);
    return 0;
}
