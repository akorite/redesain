// gen_mss.cpp -- random test generator for the stress harness.
// Usage: ./gen_mss SEED -> prints n and n ints in [-20, 20].
#include <cstdio>
#include <cstdlib>
#include <random>
int main(int argc, char** argv) {
    unsigned seed = argc > 1 ? (unsigned)strtoul(argv[1], 0, 10) : 1;
    std::mt19937 rng(seed);
    int n = 1 + rng() % 12;
    printf("%d\n", n);
    for (int i = 0; i < n; i++)
        printf("%d ", (int)(rng() % 41) - 20);
    printf("\n");
}
