// CSES 1732 Finding Borders -- all border lengths, ascending.
#include "kmp.h"
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    string s; cin >> s;
    vector<int> pi = prefix_function(s), b;
    for (int j = pi[(int)s.size() - 1]; j > 0; j = pi[j - 1]) b.push_back(j);
    sort(b.begin(), b.end());
    for (int i = 0; i < (int)b.size(); i++) printf("%d%c", b[i], " \n"[i + 1 == (int)b.size()]);
}
