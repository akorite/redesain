/* ch16_tail.c -- the loop-tail bug: a 4-lane loop over n=10 floats.
 *   ./ch16_tail naive   -> steps i=0,4,8 and touches y[8..11]; y has only 10
 *   ./ch16_tail fixed   -> vector body for i+4<=n, then a scalar tail
 * Build with -fsanitize=address to make the out-of-bounds access visible. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <emmintrin.h>
static void sax_naive(const float*x,float*y,float a,long n){
  __m128 va=_mm_set1_ps(a);
  for(long i=0;i<n;i+=4)                      /* BUG: assumes n % 4 == 0 */
    _mm_storeu_ps(y+i,_mm_add_ps(_mm_loadu_ps(y+i),_mm_mul_ps(va,_mm_loadu_ps(x+i))));}
static void sax_fixed(const float*x,float*y,float a,long n){
  __m128 va=_mm_set1_ps(a); long i=0;
  for(;i+4<=n;i+=4)
    _mm_storeu_ps(y+i,_mm_add_ps(_mm_loadu_ps(y+i),_mm_mul_ps(va,_mm_loadu_ps(x+i))));
  for(;i<n;i++) y[i]+=a*x[i];}
int main(int argc,char**argv){
  long n=10; float*x=malloc(n*sizeof(float)),*y=malloc(n*sizeof(float));
  for(long i=0;i<n;i++){x[i]=(float)i;y[i]=1.0f;}
  if(argc>1&&!strcmp(argv[1],"naive")) sax_naive(x,y,2.0f,n); else sax_fixed(x,y,2.0f,n);
  for(long i=0;i<n;i++) printf("%g ",y[i]);
  printf("\n"); free(x);free(y); return 0;}
