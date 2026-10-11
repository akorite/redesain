// coin_combos.cpp -- CSES Coin Combinations I (ordered) vs II (unordered).
#include <cstdio>
const long long MOD = 1e9+7;
int main() {
    int n, x; scanf("%d %d", &n, &x);
    int c[105];
    for (int i = 0; i < n; i++) scanf("%d", &c[i]);
    static long long a[1000006], b[1000006];
    a[0] = 1;
    for (int s = 1; s <= x; s++)               // ordered: sum outer
        for (int i = 0; i < n; i++)
            if (s >= c[i]) a[s] = (a[s] + a[s - c[i]]) % MOD;
    b[0] = 1;
    for (int i = 0; i < n; i++)                // unordered: coin outer
        for (int s = c[i]; s <= x; s++)
            b[s] = (b[s] + b[s - c[i]]) % MOD;
    printf("%lld %lld\n", a[x], b[x]);
}
