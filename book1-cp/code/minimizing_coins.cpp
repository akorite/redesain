#include "coin.h"
int main() {
    int n, x; scanf("%d %d", &n, &x);
    vector<int> c(n);
    for (auto& v : c) scanf("%d", &v);
    auto tab = coin_tab(x, c);
    printf("%d\n", tab[x] >= CINF ? -1 : tab[x]);
}
