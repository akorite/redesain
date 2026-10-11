// milk_pails.cpp -- USACO Bronze "Milk Pails" (February 2016).
// Pails of size X and Y can be filled any number of times and poured
// into a third pail of capacity M.  Largest measurable amount <= M?
// Complete search over (i fills of X, j fills of Y): the bounds come
// straight from the constraint M <= 1000.
#include <iostream>
using namespace std;

int main() {
    int X, Y, M;
    cin >> X >> Y >> M;

    int best = 0;
    for (int i = 0; i * X <= M; i++)        // i = fills of the X pail
        for (int j = 0; i * X + j * Y <= M; j++)
            best = max(best, i * X + j * Y);
    cout << best << "\n";
    return 0;
}
