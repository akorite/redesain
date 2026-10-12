// ch13_prodcons.c -- producer/consumer with a mutex + condition variable.
//   ./prodcons while   : consumers re-check the predicate in a while loop (correct)
//   ./prodcons if      : consumers check once with `if`  (the classic bug)
// The producer pushes N items one at a time and wakes ALL waiting consumers
// (broadcast), so several consumers can be woken for one item.
#include <stdio.h>
#include <string.h>
#include <pthread.h>
#define N 200000
#define CONSUMERS 3
static int queue_len, produced, consumed, bad_wakeups, done;
static pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
static pthread_cond_t  cv = PTHREAD_COND_INITIALIZER;
static int use_while;
static void *producer(void *a){
    for (int i = 0; i < N; i++) {
        pthread_mutex_lock(&m);
        queue_len++; produced++;
        pthread_cond_broadcast(&cv);
        pthread_mutex_unlock(&m);
    }
    pthread_mutex_lock(&m); done = 1; pthread_cond_broadcast(&cv); pthread_mutex_unlock(&m);
    return 0;
}
static void *consumer(void *a){
    pthread_mutex_lock(&m);
    for (;;) {
        if (use_while) { while (queue_len == 0 && !done) pthread_cond_wait(&cv, &m); }
        else           { if    (queue_len == 0 && !done) pthread_cond_wait(&cv, &m); }
        if (queue_len == 0) {
            if (done) break;
            bad_wakeups++;            // woke up, queue empty: a real pop would underflow here
            continue;
        }
        queue_len--; consumed++;
    }
    pthread_mutex_unlock(&m);
    return 0;
}
int main(int argc, char **argv){
    use_while = !(argc > 1 && strcmp(argv[1], "if") == 0);
    pthread_t p, c[CONSUMERS];
    for (int i = 0; i < CONSUMERS; i++) pthread_create(&c[i], 0, consumer, 0);
    pthread_create(&p, 0, producer, 0);
    pthread_join(p, 0);
    for (int i = 0; i < CONSUMERS; i++) pthread_join(c[i], 0);
    printf("mode=%-5s produced=%d consumed=%d empty-queue wakeups=%d\n",
           use_while ? "while" : "if", produced, consumed, bad_wakeups);
    return 0;
}
