// perms_demo.cpp -- the next_permutation idiom, up close.
// Prints every distinct permutation of two words.
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

void all_perms(string s) {
    sort(s.begin(), s.end());
    int count = 0;
    do {
        cout << "  " << s << "\n";
        count++;
    } while (next_permutation(s.begin(), s.end()));
    cout << "count: " << count << "\n";
}

int main() {
    cout << "abc:\n"; all_perms("cba");   // unsorted input is fine, we sort
    cout << "aab:\n"; all_perms("aab");   // duplicates: distinct only
    return 0;
}
