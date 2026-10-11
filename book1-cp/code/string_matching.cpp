// CSES 1753 String Matching -- count occurrences of p in s, twice:
// (1) KMP automaton on p#s, (2) Z-function on the same concatenation.
#include "kmp.h"
#include "zfunc.h"
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;
int main() {
    string s, p; cin >> s >> p;
    int m = p.size();
    string cat = p + "#" + s;
    int c1 = 0, c2 = 0;
    for (int x : prefix_function(cat)) if (x == m) c1++;
    vector<int> z = z_function(cat);
    for (int i = m + 1; i < (int)cat.size(); i++) if (z[i] == m) c2++;
    printf("%d %d\n", c1, c2);          // both methods, one line
}
