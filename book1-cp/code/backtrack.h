// backtrack.h -- backtracking skeleton with instrumentation (capstone lib).
// Write three lambdas, get a counted search for free:
//   dead(k)      -> true if the partial state cannot extend to a solution
//   place(k)     -> commit choice at depth k (loop inside)
//   is_goal(k)   -> true at a leaf
// The struct counts nodes (states entered) and pruned (dead ends skipped),
// so tuning a pruning rule has a number attached, not a guess.
#pragma once
#include <functional>
using namespace std;

struct Backtrack {
    long long nodes = 0, pruned = 0, sols = 0;
    function<void()> go;   // set by init

    // domain(r) iterates candidate moves at depth r as ints
    void init(int depth,
              const function<bool(int)>& is_goal,
              const function<void(int, const function<void(int)>&)>& domain,
              const function<bool(int, int)>& dead,
              const function<void(int, int, bool)>& apply) {
        go = [&, this] {
            function<void(int)> rec = [&](int r) {
                nodes++;
                if (is_goal(r)) { sols++; return; }
                domain(r, [&](int mv) {
                    if (dead(r, mv)) { pruned++; return; }
                    apply(r, mv, true);
                    rec(r + 1);
                    apply(r, mv, false);
                });
            };
            rec(0);
        };
    }
};
