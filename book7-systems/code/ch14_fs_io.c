// ch14_fs_io.c -- sequential vs random read; buffered write vs fsync-per-write.
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>
#include <sys/stat.h>
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);
  return t.tv_sec+t.tv_nsec*1e-9;}
#define F "/tmp/ch14_big.bin"
#define MB (1024*1024)
int main(void){
  // build a 256MB file
  int f=open(F,O_WRONLY|O_CREAT|O_TRUNC,0644);
  char*w=malloc(MB); for(int i=0;i<MB;i++)w[i]=i;
  for(int i=0;i<256;i++)write(f,w,MB);
  fsync(f); close(f);
  char*b=malloc(MB);
  // sequential read
  f=open(F,O_RDONLY); double t=now();
  while(read(f,b,MB)==MB); close(f);
  printf("sequential read: %.1f MB/s\n",256.0/(now()-t));
  // random read, 4KB blocks
  srand(7); f=open(F,O_RDONLY); t=now(); long n=20000;
  for(long i=0;i<n;i++){off_t off=((long)rand()*4096)%(256L*MB-4096);
    pread(f,b,4096,off);}
  close(f);
  printf("random 4KB read: %.1f MB/s\n",n*4096.0/MB/(now()-t));
  // buffered write vs fsync-per-write
  f=open("/tmp/ch14_buf.bin",O_WRONLY|O_CREAT|O_TRUNC,0644); t=now();
  for(int i=0;i<64;i++)write(f,w,MB); close(f);
  printf("write (no fsync): %.1f MB/s\n",64.0/(now()-t));
  f=open("/tmp/ch14_sync.bin",O_WRONLY|O_CREAT|O_TRUNC,0644); t=now();
  for(int i=0;i<64;i++){write(f,w,MB);fsync(f);} close(f);
  printf("write + fsync per 1MB: %.1f MB/s\n",64.0/(now()-t));
  // fsync per 4KB -- the real tax
  f=open("/tmp/ch14_sync4.bin",O_WRONLY|O_CREAT|O_TRUNC,0644); t=now();
  for(int i=0;i<2000;i++){write(f,w,4096);fsync(f);} close(f);
  printf("fsync per 4KB write: %.2f ms per fsync\n",(now()-t)*1e3/2000);
  return 0;}
