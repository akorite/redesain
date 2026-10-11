// trie.h -- prefix dictionary: insert words, walk from any position.
#include <array>
#include <vector>
#include <string>
using namespace std;
struct Trie {
    static const int AL = 26;
    struct Node { array<int, AL> ch{}; int cnt = 0; };
    vector<Node> t;
    Trie() : t(1) {}
    void insert(const string& w) {
        int u = 0;
        for (char c : w) {
            int k = c - 'a';
            if (!t[u].ch[k]) { t[u].ch[k] = (int)t.size(); t.push_back(Node()); }
            u = t[u].ch[k];
        }
        t[u].cnt++;
    }
    int next(int u, char c) const { return t[u].ch[c - 'a']; }
    int count(int u) const { return t[u].cnt; }
    int root() const { return 0; }
};
