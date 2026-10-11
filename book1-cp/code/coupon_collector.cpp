// coupon_collector.cpp -- coupon collector: E = n*H(n) vs simulation.
#include <cstdio>
#include <random>
int main() {
    int n; scanf("%d", &n);
    double h = 0;
    for (int i = 1; i <= n; i++) h += 1.0 / i;
    printf("exact   %.6f\n", n * h);
    std::mt19937 rng(12345);
    double sim = 0;
    const int T = 200000;
    for (int t = 0; t < T; t++) {
        std::vector<char> seen(n, 0);
        int got = 0, draws = 0;
        while (got < n) { draws++; if (!seen[rng() % n]++) got++; }
        sim += draws;
    }
    printf("simulated %.6f\n", sim / T);
}
