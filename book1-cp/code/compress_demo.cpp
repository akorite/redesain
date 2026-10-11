// compress_demo.cpp -- coordinate compression with lib/compress.h.
#include "compress.h"
#include <iostream>
using namespace std;

int main() {
    vector<long long> v = {4000000000LL, 10, 10, 80, 4000000000LL};
    vector<long long> vals;
    vector<int> r = compress(v, vals);
    for (size_t i = 0; i < v.size(); i++)
        cout << v[i] << " -> " << r[i] << "\n";
    cout << "distinct values: " << vals.size() << "\n";
}
