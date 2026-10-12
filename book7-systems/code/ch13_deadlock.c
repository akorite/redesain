// ch13_deadlock.c -- two locks, two threads, opposite order => deadlock.
//   ./deadlock bad   : T1 takes A then B, T2 takes B then A
//   ./deadlock good  : both take A then B (a global lock order)
// A sleep between the two acquisitions forces the bad interleaving every time.
// timedlock turns the hang into a report so the program can print and exit.
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>
static pthread_mutex_t A = PTHREAD_MUTEX_INITIALIZER, B = PTHREAD_MUTEX_INITIALIZER;
static int ordered, stuck;
static pthread_barrier_t gate;                         // both threads decide before either unlocks
static int lock_timeout(pthread_mutex_t *m){
    struct timespec ts; clock_gettime(CLOCK_REALTIME, &ts); ts.tv_sec += 1;
    return pthread_mutex_timedlock(m, &ts);          // 0 on success, ETIMEDOUT otherwise
}
static void *worker(void *arg){
    int id = (int)(long)arg;
    pthread_mutex_t *first  = (id == 1 || ordered) ? &A : &B;
    pthread_mutex_t *second = (id == 1 || ordered) ? &B : &A;
    pthread_mutex_lock(first);
    usleep(100000);                                   // let the other thread take its first lock
    int got = (lock_timeout(second) == 0);
    if (got) printf("T%d: got both locks\n", id);
    else {
        printf("T%d: holds %s, waited 1 s for %s -> deadlock\n", id,
               first == &A ? "A" : "B", second == &A ? "A" : "B");
        __sync_fetch_and_add(&stuck, 1);
    }
    if (!ordered) pthread_barrier_wait(&gate);        // both decide before either unlocks
    if (got) pthread_mutex_unlock(second);
    pthread_mutex_unlock(first);
    return 0;
}
int main(int argc, char **argv){
    ordered = argc > 1 && strcmp(argv[1], "good") == 0;
    pthread_t t1, t2;
    pthread_barrier_init(&gate, 0, 2);
    pthread_create(&t1, 0, worker, (void*)1L);
    pthread_create(&t2, 0, worker, (void*)2L);
    pthread_join(t1, 0); pthread_join(t2, 0);
    printf("%s order: %d thread(s) stuck\n", ordered ? "global" : "opposite", stuck);
    return 0;
}
