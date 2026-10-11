// ch12_fork_demo.c -- correct fork/exec/wait usage.
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
int main(void){
    printf("parent %d starting\n",getpid());
    pid_t p=fork();
    if(p<0){perror("fork");return 1;}
    if(p==0){
        printf("  child %d exec'ing /bin/echo\n",getpid());
        execl("/bin/echo","echo","  hello from exec'd child",(char*)NULL);
        _exit(127);                    // only reached if exec fails
    }
    int st; pid_t w=waitpid(p,&st,0);
    printf("parent: child %d exited, status=%d\n",
           (int)w,WEXITSTATUS(st));
    return 0;}
