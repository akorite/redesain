/* link demo: two files, one unresolved symbol */
int sum(int *a, int n);              /* lives in ch01_sum.c */
extern int missing(void);            /* declared, never defined */
int main(void) {
    static int v[] = {1,2,3,4,5};
    return sum(v, 5) + missing();    /* link will fail HERE */
}
