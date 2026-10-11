// throwing_dice.cpp -- CSES 1096: compositions of n with parts <= 6,
// n up to 1e18. Linear recurrence f(i)=sum_{j=1..6} f(i-j) via 6x6
// matrix power mod 1e9+7. f(0)=1, f(i<0)=0.
#include <cstdio>
typedef long long ll;
const ll M = 1000000007;
typedef ll Mat[6][6];
void mul(Mat a, Mat b, Mat c) {
    for (int i = 0; i < 6; i++)
        for (int j = 0; j < 6; j++) {
            ll s = 0;
            for (int k = 0; k < 6; k++) s = (s + a[i][k] * b[k][j]) % M;
            c[i][j] = s;
        }
}
int main() {
    ll n; scanf("%lld", &n);
    // companion: row 0 = all ones; row i>0 shifts f down.
    Mat T = {{1, 1, 1, 1, 1, 1},
             {1, 0, 0, 0, 0, 0},
             {0, 1, 0, 0, 0, 0},
             {0, 0, 1, 0, 0, 0},
             {0, 0, 0, 1, 0, 0},
             {0, 0, 0, 0, 1, 0}};
    Mat R = {{1,0,0,0,0,0},{0,1,0,0,0,0},{0,0,1,0,0,0},
             {0,0,0,1,0,0},{0,0,0,0,1,0},{0,0,0,0,0,1}};
    Mat tmp;
    while (n > 0) {
        if (n & 1) { mul(R, T, tmp); for (int i=0;i<6;i++) for (int j=0;j<6;j++) R[i][j]=tmp[i][j]; }
        n >>= 1;
        if (n) { mul(T, T, tmp); for (int i=0;i<6;i++) for (int j=0;j<6;j++) T[i][j]=tmp[i][j]; }
    }
    // state vector [f(0),f(-1),...,f(-5)]^T = [1,0,...,0]: f(n) is entry [0][0].
    printf("%lld\n", R[0][0]);
}
