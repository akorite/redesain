// ch12_zombie.c -- what a process that exited but was never waited on looks like.
// The child exits at once; the parent reads the child's state from /proc,
// then calls waitpid, then reads /proc again.
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
static char state_of(pid_t p) {          // 3rd field of /proc/PID/stat is the state letter
    char path[64], buf[256];
    snprintf(path, sizeof path, "/proc/%d/stat", (int)p);
    FILE *f = fopen(path, "r");
    if (!f) return '-';                  // no such process any more
    if (!fgets(buf, sizeof buf, f)) { fclose(f); return '?'; }
    fclose(f);
    char *rp = strrchr(buf, ')');        // the name is in parentheses; state follows it
    return rp ? rp[2] : '?';
}
int main(void) {
    pid_t p = fork();
    if (p < 0) { perror("fork"); return 1; }
    if (p == 0) _exit(7);                // child: exit immediately with status 7
    usleep(100000);                      // give the child time to exit
    printf("before waitpid: child state = %c\n", state_of(p));
    int st;
    waitpid(p, &st, 0);
    printf("waitpid returned: exit status = %d\n", WEXITSTATUS(st));
    printf("after  waitpid: child state = %c\n", state_of(p));
    return 0;
}
