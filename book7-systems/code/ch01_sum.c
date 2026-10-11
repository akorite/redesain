/* freestanding: no libc — this is how the machine sees code */
int sum(int *a, int n) { int s = 0; for (int i = 0; i < n; i++) s += a[i]; return s; }
int main(void) { static int v[] = {1,2,3,4,5}; return sum(v, 5); }
