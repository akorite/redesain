// CSES 1069 Repetitions: longest run of equal characters.
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    string s; cin >> s;
    int best = 0, cur = 0; char prev = 0;
    for(char c : s){
        cur = (c == prev) ? cur + 1 : 1;
        best = max(best, cur); prev = c;
    }
    cout << best << '\n';
}
