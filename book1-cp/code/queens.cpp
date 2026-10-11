// queens.cpp -- CSES Chessboard and Queens, with an instrumented counter.
// 'leaves' = arrivals at depth 8.  With all checks on, every leaf is a
// valid solution; with checks off it is just a surviving permutation.
// Place one queen per row; prune a branch as soon as a column, diagonal,
// or reserved square is violated.  'mode' toggles which checks are on so
// the counter can show what each pruning rule buys.
#include <iostream>
#include <string>
using namespace std;

const int N = 8;
string board[N];
bool col[N], d1[2 * N - 1], d2[2 * N - 1];
long long nodes = 0, pruned = 0, sols = 0;
bool useDiag = true, useCell = true;

void search(int r) {
    nodes++;
    if (r == N) { sols++; return; }
    for (int c = 0; c < N; c++) {
        bool bad = col[c]
            || (useDiag && (d1[r + c] || d2[r - c + N - 1]))
            || (useCell && board[r][c] == '*');
        if (bad) { pruned++; continue; }      // dead branch: counted, never explored
        col[c] = d1[r + c] = d2[r - c + N - 1] = true;
        search(r + 1);
        col[c] = d1[r + c] = d2[r - c + N - 1] = false;
    }
}

void run(const char* label) {
    nodes = pruned = sols = 0;
    for (int i = 0; i < N; i++) col[i] = false;
    for (int i = 0; i < 2 * N - 1; i++) d1[i] = d2[i] = false;
    search(0);
    cout << label << "  nodes=" << nodes
         << "  pruned=" << pruned << "  leaves=" << sols << "\n";
}

int main(int argc, char** argv) {
    for (int i = 0; i < N; i++) board[i] = "........";
    if (argc > 1 && string(argv[1]) == "stdin")
        for (int i = 0; i < N; i++) cin >> board[i];

    useDiag = true;  useCell = true;
    run("full checks (col+diag+cells): ");
    useDiag = false; useCell = true;
    run("columns only:                ");
    return 0;
}
