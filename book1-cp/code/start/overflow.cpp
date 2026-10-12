#include <iostream>
using namespace std;
int main() {
    int a = 2000000000;
    int b = a + a;                 // too big for 32 bits
    long long c = 2LL * a;         // 64 bits is fine
    cout << b << " " << c << "\n";
}
