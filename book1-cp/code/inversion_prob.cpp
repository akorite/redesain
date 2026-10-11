// inversion_prob.cpp -- CSES 1728: position i uniform on {1..r_i};
// expected inversions = sum over pairs P(x_a > x_b).
#include <cstdio>
int main() {
    int n; scanf("%d", &n);
    int r[105];
    for (int i = 0; i < n; i++) scanf("%d", &r[i]);
    double e = 0;
    for (int a = 0; a < n; a++)
        for (int b = a + 1; b < n; b++) {
            long long cnt = 0;
            for (int va = 1; va <= r[a]; va++)
                cnt += va - 1 < r[b] ? va - 1 : r[b];
            e += (double)cnt / ((double)r[a] * r[b]);
        }
    printf("%.6f\n", e);
}
