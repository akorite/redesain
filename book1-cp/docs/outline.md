# Outline (to be approved by the user before any chapter is written)

Book: *Competitive Programming and Algorithms* (`textbook-cp`). Reader: comfortable with basic C++ syntax, below 1000 on Codeforces. Outcomes: solves USACO Gold problems, reaches Codeforces ~1600 with a marked route to 1900. Model for structure and register: Sannemo's PAPS; curriculum checked against Laaksonen's CPH, the USACO Guide (Bronze→Gold), the CSES problem set, cp-algorithms, and MIT 6.006 — see `docs/sources.md`.

Every algorithm in this book is presented with three things: a C++17 snippet that runs, a correctness argument (exchange argument, invariant, or induction), and a complexity bound. Every chapter ends its main text with a one-page cheat-sheet table and a "Notes" section citing sources by bibliography number. Exercises are placed inline where the text assumes them solved; each chapter also has an Additional Exercises section of at least 10 problems split `[easy]` / `[medium]` / `[hard]`. Problems from public archives are cited by name only, never copied (per master prompt §3).

## Page budget

| Block | Pages |
|---|---|
| Front matter (title, preface, how to use, contest landscape 2026, notation summary) | ~10 |
| Chapters 1–18 (per-chapter estimates below) | ~221 |
| Back matter: hints for all `[hard]` exercises, full solutions for ≥ half of all exercises, numbered bibliography, makeindex index | ~19 |
| **Core total (target 245, hard cap 250)** | **≈250** |
| Optional chapters 16–17 (approved decision 3: marked `[optional]`, excluded from the core budget) | ~20, additional |

If the draft runs long, the compression order is: Ch 14 (NT/combinatorics), Ch 12 (DP II), Ch 10 (trees), then Ch 18 (contest craft).

## Deviations from the seed list

The seed's 16 topics are all covered. Reordering, for pedagogy:
1. **Binary search moved before graphs** (it is an array technique and the reader's first "search on the answer" pattern).
2. **Topological sort, cycle detection and functional graphs** folded into the graph-traversal chapter (they are traversal applications, not a separate topic at this level).
3. **DSU and MST merged into one chapter** (Kruskal needs DSU; the cut property is taught once for both Kruskal and Prim).
4. **"Amortized structures"** (monotonic stack, monotone deque, sparse table, sqrt decomposition) promoted to an early Part II chapter — it completes the array-technique picture before graphs, matching CPH's "Amortized analysis" placement.
5. **DP optimisation** (CHT, divide-and-conquer DP, Knuth, SOS) is *named and routed*, not fully taught — flagged as the 1900+ horizon inside Ch 12 and Appendix B rather than a full chapter (consistent with the 1600 target; CPH treats these as advanced topics).
6. **Game theory** reduced to a section of the probability/games chapter (Nim/mex) — full Sprague–Grundy is beyond the target band.

# Front matter (~10 pp)

- Preface: who this book is for, what "1600" and "USACO Gold" mean, how to use the book (chapters build forward; solve inline exercises as you meet them; every algorithm has code + proof + complexity; the capstone library grows chapter by chapter).
- The contest landscape in 2026 (date-stamped, marked for re-verification): Codeforces divisions and ratings, USACO 2025–26 season structure (3 online contests + proctored US Open, certified-score rule, platinum reset), CSES problem set, how online judges score (ICPC vs IOI styles).
- How a problem statement is structured; how solutions are judged (AC/WA/TLE/RE/MLE/PE).
- Notation and conventions summary (points to `docs/notation.md`).

# Part I — Foundations

## Chapter 1 — The contest machine and the cost model (≈14 pp)

*Prerequisites:* none beyond the reader brief (basic C++ syntax).

Sections (teaching order):
1.1 How a judge sees your program — stdin/stdout, verdicts, limits, scoring styles.
1.2 The C++17 starter kit — the template file, fast I/O, integer types and overflow, `vector`/`sort`, `set`/`map`/`priority_queue`, `string`, pairs/tuples, structured bindings, macros we allow (`using ll`, `rep`, `all`) and why we keep them few.
1.3 Time complexity — counting operations, the RAM model, \(O\), \(\Theta\), \(\Omega\) with proofs, common classes and the ~10⁸ simple-operations-per-second heuristic.
1.4 From constraints to a plan — reading \(N\) to guess the required complexity class (the table every contestant internalises), worst case vs typical case, constant factors and when they matter.
1.5 The submit loop — compiling with warnings on, testing locally against samples, the first Wrong Answer checklist, what "accepted" does and doesn't mean.

Worked examples (named):
- WE 1.1 CSES *Weird Algorithm* — read, simulate, submit; the full workflow end to end.
- WE 1.2 CSES *Maximum Subarray Sum* — same problem at \(O(n^3)\), \(O(n^2)\), \(O(n \log n)\), \(O(n)\); measured runtimes at each stage vs the theory.
- WE 1.3 CSES *Missing Number* — two solutions (math vs set) and how to choose under pressure.
- WE 1.4 The first bug hunt — a deliberately broken submission, its WA verdict, and the local-testing fix (worked example of the submit loop).

Figures (named):
- F 1.1 Verdict flowchart — submit → compile → run → AC/WA/TLE/RE, what each means.
- F 1.2 Anatomy of a problem statement — a real statement annotated (constraints, I/O, subtasks).
- F 1.3 Growth curves — \(\log n\), \(n\), \(n\log n\), \(n^2\), \(2^n\) on one pgfplots axis with the 1-second budget line at \(n\) for each.
- F 1.4 Constraint-to-complexity decision table (as a figure, not prose).
- F 1.5 Timeline of one contest minute — read → think → code → test → submit (reused in Ch 18).

Code listings (named):
- L 1.1 `template.cpp` — the starter file used for the whole book (capstone seed, lives in `code/lib/template.cpp`).
- L 1.2 Fast input scanner + `ios::sync_with_stdio(false)` — with a measured speed comparison output.
- L 1.3 STL tour — `set`, `map`, `priority_queue`, `sort` with a custom comparator, each with real output.
- L 1.4 A run of WE 1.2's four solutions on \(n=2\cdot10^5\) with timing output.

Exercises: 4 inline (predict outputs; count operations in a given loop; pick a complexity class from constraints; fix a WA program). Additional (12): [easy] CSES Repetitions, Increasing Array, Bit Strings, Number Spiral, Palindrome Reorder, USACO-B The Cow-Signal, USACO-B Speeding Ticket; [medium] CSES Trailing Zeros, Coin Piles, USACO-B The Bucket List, USACO-B The Bovine Shuffle; [hard] CSES Two Sets.
Named archive problems for the chapter: CSES Introductory set + USACO-B The Cow-Signal, Speeding Ticket, The Lost Cow, The Bovine Shuffle, The Bucket List, Shell Game, Mixing Milk.
Band: CF 800–1100 (Div 2 A/B) — USACO Bronze.
Lib: `template.cpp`, fast scanner.

Common-mistakes seed: `endl` vs `'\n'`; `int` overflow at \(10^9\); reading all input before knowing the format; assuming the sample proves correctness.

## Chapter 2 — Complete search (≈12 pp)

*Prerequisites:* Ch 1 (cost model, complexity reading).

Sections:
2.1 The exhaustive idea — enumerate the whole answer space; when \(n \le 20\) is a feature.
2.2 Enumerating subsets — recursion and bitmasks, \(2^n\) and its cost.
2.3 Enumerating permutations — `next_permutation`, lexicographic order.
2.4 Backtracking — pruning dead branches; counting what we saved.
2.5 Search-space sketches — drawing the state tree before coding.

Worked examples:
- WE 2.1 CSES *Apple Division* — recursive subset enumeration, then the bitmask version; measured speedup from the "fix the last element" symmetry.
- WE 2.2 CSES *Creating Strings* — permutations with `next_permutation` and duplicates handling.
- WE 2.3 CSES *Chessboard and Queens* — backtracking with three pruning rules; instrumented counter of pruned vs visited nodes.
- WE 2.4 USACO-B *Milk Pails* — nested-loop complete search and how to bound it from constraints.

Figures:
- F 2.1 Recursion tree for \(n=3\) subsets (small multiple over calls).
- F 2.2 Bitmask ↔ subset table for \(n=3\).
- F 2.3 Unpruned vs pruned search tree on the 4-queens board (small multiple).
- F 2.4 The size ladder: \(n\), \(2^n\), \(n!\) feasibility bands vs the 1-second budget.

Code listings:
- L 2.1 Recursive subset enumeration (skeleton reused in the lib).
- L 2.2 Bitmask iteration `for mask in [0, 2^n)`.
- L 2.3 Backtracking skeleton with prune counter (prints visited-node count).
- L 2.4 `next_permutation` idiom + duplicate-safe handling.

Exercises: 3 inline (subset count; trace the recursion tree; where does the prune fire). Additional (11): [easy] CSES Tower of Hanoi, Gray Code, USACO-B Diamond Collector, USACO-B Daisy Chains, USACO-B Counting Liars; [medium] CSES Raab Game I, Mex Grid Construction, USACO-B Cow Gymnastics, USACO-B Triangles; [hard] CSES Digit Queries, CSES Grid Path Description.
Named archive problems: CSES Apple Division, Creating Strings, Chessboard and Queens + USACO-B Milk Pails, Diamond Collector, Bovine Genomics, Lifeguards, Guess the Animal, Contaminated Milk, Cow Checkups.
Band: CF 800–1200 — USACO Bronze.
Lib: `subsets.h`, `permutations.h`, `backtrack.h` skeletons.

## Chapter 3 — Sorting and greedy algorithms (≈12 pp)

*Prerequisites:* Ch 1–2.

Sections:
3.1 Sorting as a tool — what `std::sort` does, stability, custom comparators, coordinate compression.
3.2 The greedy method — local choices that survive globally.
3.3 How to argue correctness — the exchange argument, "greedy stays ahead", induction; where each applies.
3.4 When greedy fails — non-canonical coin systems; the obligation to disprove before trusting.
3.5 Sets and maps as greedy tools — `set` as "best available" structure.

Worked examples:
- WE 3.1 CSES *Movie Festival* — interval scheduling, the exchange argument written out fully, and the counter-example showing earliest-start fails.
- WE 3.2 CSES *Stick Lengths* — median minimises \(\sum |a_i - m|\); the pairing proof.
- WE 3.3 CSES *Apartments* + *Ferris Wheel* — two-pointer-after-sort greedy with the "stays ahead" argument.
- WE 3.4 Coin systems — greedy on \{1,5,10,25\} vs \{1,3,4\}: a counter-example and the lesson "prove or distrust".

Figures:
- F 3.1 Interval-scheduling timeline: sorting by end time, accepting/rejecting (small multiple).
- F 3.2 The exchange argument illustrated: an optimal schedule and the greedy schedule side by side with the swapped pair marked.
- F 3.3 Median proof picture — contributions of paired elements as distances on a number line.
- F 3.4 Coordinate compression diagram — values → ranks.
- F 3.5 Coin-system decision tree where greedy picks wrong.

Code listings:
- L 3.1 Sorting with a lambda comparator + structured bindings.
- L 3.2 Coordinate compression utility.
- L 3.3 Greedy-vs-counterexample harness: runs the wrong greedy on \{1,3,4\} and prints the failure.
- L 3.4 `set`-based "best available" pattern (priority queue alternative).

Exercises: 3 inline (find the counter-example; which exchange step; does sorting help). Additional (12): [easy] CSES Distinct Numbers, Sum of Two Values, Collecting Numbers, USACO-B Cow College, USACO-B Even More Odd Photos, USACO-S Lemonade Line; [medium] CSES Restaurant Customers, Tasks and Deadlines, USACO-S High Card Wins, USACO-S Rest Stops, USACO-B Out of Place; [hard] CSES Josephus Problem I.
Named archive problems: + USACO-B Watching Mooloo, Cow Tipping, Photoshoot, Race; USACO-S Berry Picking, Bovine Acrobatics; USACO-G High Card Low Card; CSES Playlist, Towers, Sum of Three Values.
Band: CF 900–1400 — USACO Bronze→Silver.
Lib: `compress.h`.

# Part II — Array methods

## Chapter 4 — Binary search (≈11 pp)

*Prerequisites:* Ch 1–3.

Sections:
4.1 Binary search on a sorted array — the one correct template (`while lo < hi`, half-open intervals) and `lower_bound`.
4.2 Monotone predicates — the true/false frontier picture; "binary search on the answer".
4.3 Real-valued search — iteration counts vs `eps` comparison.
4.4 The pattern's limits — when the predicate isn't monotone.

Worked examples:
- WE 4.1 CSES *Factory Machines* — minimise makespan; predicate "can we finish by time T" built from scratch.
- WE 4.2 CSES *Array Division* — minimise the largest subarray sum; the greedy feasibility check and why it's correct.
- WE 4.3 USACO-S *Social Distancing* — maximise the minimum gap; the same pattern inverted.
- WE 4.4 CSES *Multiplication Table* — counting \(\le x\) per row; \(O(n\log n)\) answer-space search.

Figures:
- F 4.1 The predicate frontier — F…F T…T and where the boundary search lands.
- F 4.2 Interval shrinkage small-multiple (4 steps) on an array.
- F 4.3 Answer-space vs input-space diagram: searching "the answer" not the array.
- F 4.4 Feasibility check for WE 4.2 drawn as a timeline of machine completions.

Code listings:
- L 4.1 The binary-search template (first true) with assertions.
- L 4.2 `check(x)` + search driver for WE 4.1.
- L 4.3 Real-valued binary search with fixed 60 iterations.

Exercises: 3 inline (boundary choices; is this predicate monotone; write the check). Additional (12): [easy] CSES Sum of Three Values, USACO-S Cow Dance Show, USACO-S Convention; [medium] CSES Reading Books, Movie Festival II, USACO-S Loan Repayment, USACO-S Bakery, CF Guess the K-th Zero (interactive); [hard] CSES Maximum Subarray Sum II, CF The Meeting Place Cannot Be Changed, Baltic OI 2012 Mobile.
Named archive problems: + USACO-S Angry Cows (the classic), CF Magic Ship, Packmen, Max Median, Grouped Carriages; CSES Nested Ranges Check/Count, Room Allocation.
Band: CF 1100–1600 — USACO Silver.
Lib: `bsearch.h` (`first_true(lo,hi,pred)`).

## Chapter 5 — Prefix sums, difference arrays, and two pointers (≈12 pp)

*Prerequisites:* Ch 1–3 (Ch 4 helps but isn't required).

Sections:
5.1 Prefix sums — the range-sum trick, build once query forever.
5.2 Difference arrays — range updates as two point writes; the inverse direction.
5.3 Two dimensions — 2D prefix sums, inclusion–exclusion rectangles, 2D difference.
5.4 Two pointers — the telescoping window; when monotonicity licenses it.
5.5 Sliding windows with bookkeeping — sum, count-distinct, and min/max (deque preview of Ch 6).

Worked examples:
- WE 5.1 CSES *Static Range Sum Queries* + *Forest Queries* — 1D then 2D, the rectangle algebra drawn.
- WE 5.2 CSES *Subarray Sums I* — two pointers; the monotonicity requirement stated as a lemma.
- WE 5.3 CSES *Subarray Sums II* / *Subarray Divisibility* — prefix-sum + `map` counting, the mod-remainder trick.
- WE 5.4 USACO-S *Painting the Barn* — 2D difference array from an update-list statement.

Figures:
- F 5.1 Prefix cells → range sum as geometric subtraction.
- F 5.2 2D inclusion–exclusion rectangle diagram.
- F 5.3 Two-pointer march on a sample array (small multiple, 4 frames).
- F 5.4 Difference-array update → point writes → prefix-restore pipeline.
- F 5.5 Prefix-remainder counting: a hash-bucket diagram for Subarray Sums II.

Code listings:
- L 5.1 `prefix.h` 1D + 2D prefix tables.
- L 5.2 Difference-array range updates.
- L 5.3 Two-pointer subarray-sum template.
- L 5.4 Prefix+map counting with real output.

Exercises: 3 inline (compute a prefix range by hand; which problems need nonnegative; the remainder trick). Additional (13): [easy] USACO-S Breed Counting, USACO-S Hoof, Paper, Scissors, CSES Maximum Subarray Sum, CF Karen and Coffee; [medium] CSES Subarray Sums I/II, Subarray Divisibility, USACO-S Subsequences Summing to Sevens, SPOJ Haybale Stacking, CSES Distinct Values Subarrays; [hard] USACO-S Rectangular Pasture, USACO-G Haybale Feast, CF Queries for Number of Palindromes.
Named archive problems: + CSES Static Range Sum Queries, Forest Queries, Sliding Window Sum, USACO-P Modern Art [route to 1900], CF Good Subarrays, Little Girl and Maximum Sum, Counting Rectangles.
Band: CF 1100–1600 — USACO Silver.
Lib: `prefix.h`, `diff.h`, `twoptr.h` patterns.

## Chapter 6 — Amortized structures: stacks, deques, sparse tables (≈10 pp)

*Prerequisites:* Ch 5.

Sections:
6.1 Amortized analysis — each element pays once; the accounting argument.
6.2 The monotonic stack — nearest smaller/greater element everywhere it's used (histograms, subarray maximums).
6.3 The monotonic deque — sliding-window min/max in \(O(n)\).
6.4 Static range queries — sparse tables: \(O(n\log n)\) build, \(O(1)\) idempotent queries.
6.5 Square roots — bucketing as the "good enough" structure; when \(O(\sqrt n)\) beats \(O(\log n)\) in simplicity.

Worked examples:
- WE 6.1 CSES *Nearest Smaller Values* — the stack that pops to its answer; amortized bound argued per push.
- WE 6.2 Largest rectangle in a histogram — the canonical monotonic-stack application, built slowly.
- WE 6.3 CSES *Sliding Window Minimum* — deque indices front/back, the trace drawn.
- WE 6.4 CSES *Static Range Minimum Queries* — sparse table; why min is idempotent and sum isn't.

Figures:
- F 6.1 Monotonic-stack pop trace on the NSV example (small multiple).
- F 6.2 Histogram → nearest-smaller bounds as horizontal rays.
- F 6.3 Deque window sliding (4 frames) with expired indices marked.
- F 6.4 Sparse-table level layout over a 16-element array.
- F 6.5 sqrt-bucket diagram: block sums + partial scans.

Code listings:
- L 6.1 Monotonic stack (NSV both directions).
- L 6.2 Monotonic deque sliding minimum.
- L 6.3 Sparse table for idempotent RMQ.
- L 6.4 sqrt-decomposition range-sum with point updates.

Exercises: 3 inline (amortized counting; deque vs stack; idempotency check). Additional (11): [easy] CSES Towers, Concert Tickets, USACO-S Convention II, LC IPO; [medium] CSES Traffic Lights, Josephus Problem II, USACO-S Milk Measurement, CF William and Robot; [hard] CSES Stick Division, USACO-S Deforestation, USACO-G Job Completion.
Named archive problems: + CSES Bubble Sort Rounds II, Sliding Window Median/Cost, USACO-G Haybale Feast, CF Serval and Kaitenzushi Buffet.
Band: CF 1200–1700 — USACO Silver→Gold.
Lib: `monostack.h`, `monodeque.h`, `sparse.h`, `sqrtdec.h`.

# Part III — Graphs

## Chapter 7 — Graphs: traversal and order (≈14 pp)

*Prerequisites:* Ch 1–2 (recursion review inside).

Sections:
7.1 Graph vocabulary — vertices, edges, degrees, paths, cycles, components; directed vs undirected; weighted vs not.
7.2 Representations — adjacency lists only (why); the tiny edge cases (self-loops, multi-edges, 1-indexing).
7.3 Depth-first search — recursion, visited set, the three applications that fall out for free.
7.4 Breadth-first search — layers as unweighted distance; parent reconstruction.
7.5 Flood fill — grids as implicit graphs; connected-component counting.
7.6 Bipartite checks — two-colouring as a DFS/BFS application.
7.7 Directed graphs — topological order (Kahn), cycle detection via three colours, the DAG as the "safe" graph.
7.8 Functional graphs — successor structure = tail + cycle; where it appears (permutations, successor problems).

Worked examples:
- WE 7.1 CSES *Counting Rooms* — flood fill; the "four directions" discipline.
- WE 7.2 CSES *Labyrinth* — BFS + parent array → path reconstruction.
- WE 7.3 CSES *Building Teams* — bipartite check, with the odd-cycle failure argument.
- WE 7.4 CSES *Course Schedule* + *Round Trip II* — Kahn's algorithm, then directed cycle extraction.
- WE 7.5 CSES *Planets Cycles* — functional-graph cycle finding (fast-forward + retrace).

Figures:
- F 7.1 Adjacency list layout vs the graph it encodes.
- F 7.2 DFS recursion stack growing and unwinding (small multiple).
- F 7.3 BFS layer expansion (small multiple — 4 waves).
- F 7.4 Grid → graph mapping: one cell, its four edges.
- F 7.5 Kahn's queue evolution on a course DAG.
- F 7.6 Functional graph anatomy: the ρ (rho) shape — tail + cycle.

Code listings:
- L 7.1 Recursive DFS with the adjacency-list idiom.
- L 7.2 BFS with `dist` + `parent` arrays.
- L 7.3 Iterative flood fill (explicit stack — recursion-depth tripwire).
- L 7.4 Kahn's algorithm + leftover-vertices-equals-cycle check.

Exercises: 4 inline (spot the edge case; BFS vs DFS order; why does Kahn stop early; functional-graph entry point). Additional (13): [easy] CSES Building Roads, Message Route, USACO-S Closing the Farm, USACO-B Family Tree; [medium] CSES Round Trip, Game Routes, USACO-S Icy Perimeter, USACO-S Build Gates, USACO-S Mooyo Mooyo, USACO-S Visits; [hard] CSES Monsters, USACO-B The Great Revegetation, USACO-S Snow Boots.
Named archive problems: + USACO-S Moocast, Fence Planning, Comfortable Cows, Switching on the Lights, Multiplayer Moo, Cowntagion, Grass Planting, The Bovine Shuffle; USACO-G Timeline; CF Directing Edges, Fox and Names, Connected Components?, Solve The Maze; Kattis Birthday Party; CSES Subarray Sum Constraints [hard preview].
Band: CF 1300–1700 — USACO Silver→Gold.
Lib: `bfs.h`, `dfs.h`, `floodfill.h`, `toposort.h`.

## Chapter 8 — Shortest paths (≈13 pp)

*Prerequisites:* Ch 7.

Sections:
8.1 Relaxation — the operation everything is built from.
8.2 BFS, revisited — the unit-weight special case restated as shortest paths.
8.3 Bellman–Ford — \(n-1\) relaxation rounds, correctness by path-length induction, negative-cycle detection.
8.4 Dijkstra — the greedy frontier; correctness by the exchange/cut argument; *why it dies on negative edges* (shown, not stated).
8.5 Floyd–Warshall — all-pairs DP over the intermediate set; transitive closure; path reconstruction.
8.6 State expansion — shortest paths on derived graphs (the "discount coupon" trick); 0-1 BFS named.

Worked examples:
- WE 8.1 CSES *Shortest Routes I* — Dijkstra end to end; the `pq` stale-entry trick.
- WE 8.2 CSES *Cycle Finding* — Bellman–Ford with reconstruction of a negative cycle.
- WE 8.3 CSES *Shortest Routes II* — Floyd–Warshall; when \(n \le 500\) makes \(O(n^3)\) the right choice.
- WE 8.4 CSES *Flight Discount* — doubling the graph: state (city, coupon-used) as a worked example of state expansion.
- WE 8.5 USACO-G *Why Did the Cow Cross the Road* — weighted BFS-flavoured variant.

Figures:
- F 8.1 One relaxation step annotated.
- F 8.2 Dijkstra's settled set growing (small multiple, 5 frames).
- F 8.3 The negative-edge failure: a graph where Dijkstra settles wrong, marked.
- F 8.4 Floyd–Warshall \(k\)-expansion: the matrix after each intermediate vertex joins.
- F 8.5 State-expanded graph for Flight Discount — two layers and the coupon edges between them.

Code listings:
- L 8.1 Dijkstra with `priority_queue` + skip-stale.
- L 8.2 Bellman–Ford + negative-cycle flag and one-cycle reconstruction.
- L 8.3 Floyd–Warshall (the 15-line core) + `next` table for paths.
- L 8.4 State-expanded Dijkstra (coupon state in the node).

Exercises: 4 inline (relaxation order; when does early-exit lie; why pq; spot the state). Additional (13): [easy] CSES Shortest Routes I/II, USACO-S Milk Pails; [medium] CSES Flight Discount, Flight Routes, Investigation, USACO-G Milk Pumping, USACO-G Shortcut; [hard] CSES High Score, Cycle Finding reconstruction, USACO-G Lasers and Mirrors, USACO-G A Pie for a Pie, USACO-G Telephone.
Named archive problems: + USACO-G Fine Dining, Telephone, Moortal Cowmbat, Cow at Large, Replication; CSES Graph Girth, Swap Game; IOI 2009 Mecho; CF Not Escaping.
Band: CF 1500–1900 — USACO Gold.
Lib: `dijkstra.h`, `bellmanford.h`, `floyd.h`.

## Chapter 9 — Disjoint sets and spanning trees (≈12 pp)

*Prerequisites:* Ch 7; sorting (Ch 3).

Sections:
9.1 The connectivity problem — what DSU buys and when offline beats online.
9.2 The forest representation — `find` with path compression, `union` by size.
9.3 The amortized bound — inverse Ackermann stated; the proof idea (charged ranks) sketched, not required.
9.4 Minimum spanning trees — the cut property (the one theorem that makes all MST algorithms correct), exchange proof.
9.5 Kruskal — sort edges, DSU-filter, accept; complexity sorted.
9.6 Prim — the pq frontier; when dense graphs prefer it.

Worked examples:
- WE 9.1 CSES *Road Construction* — tracking component sizes online.
- WE 9.2 CSES *Building Roads* — counting components, then connecting them.
- WE 9.3 CSES *Road Reparation* — Kruskal end to end on the cut property.
- WE 9.4 USACO-G *Closing the Farm* — offline deletion = online insertion in reverse; the timeline trick.

Figures:
- F 9.1 Forest before/after path compression on the same find.
- F 9.2 Union-by-size: the shallow vs deep merge shapes.
- F 9.3 The cut property: any crossing light edge can be exchanged — diagram.
- F 9.4 Kruskal accept/reject small-multiple over a 6-vertex graph.
- F 9.5 Closing the Farm timeline reversal: deletions read backwards become insertions.

Code listings:
- L 9.1 `DSU` struct (path halving + union by size + component size).
- L 9.2 Kruskal on top of `DSU`.
- L 9.3 Offline-reversal pattern (Closing the Farm skeleton).
- L 9.4 Prim with `priority_queue` (named; full treatment is secondary).

Exercises: 3 inline (find vs union order; which cut; reverse or not). Additional (12): [easy] CSES Road Reparation, USACO-S Closing the Farm, USACO-G MooTube; [medium] USACO-S Wormhole Sort, USACO-G Moocast (alt solution), USACO-G I Would Walk 500 Miles, CF Design Tutorial: Inverse the Problem; [hard] CSES New Roads Queries, USACO-G Portals, USACO-G Fenced In, USACO-OS Ski Course Rating, Baltic OI 2016 Park.
Named archive problems: + USACO-G Strongest Friendship Group, Favorite Colors, Reachable Pairs, Valleys [route], Tractor, Superbull, Moo Network; JOI 2015 Inheritance; COCI Sirni; APIO 2013 Toll; CSES Necessary Roads/Cities [named as articulation preview], Dynamic Connectivity [route].
Band: CF 1400–1800 — USACO Gold.
Lib: `dsu.h`, `kruskal.h`, `prim.h`.

## Chapter 10 — Tree algorithms: subtrees, diameters, LCA (≈13 pp)

*Prerequisites:* Ch 7 (traversal); Ch 11's DP ideas help but a preview is given inline.

Sections:
10.1 The shape of a tree — \(n-1\) edges, unique paths, rooting as a design choice.
10.2 Subtree aggregates — post-order accumulation; *Subordinates*.
10.3 Diameter — the two-DFS algorithm with its proof (why farthest-from-anything is an endpoint).
10.4 Rerooting — computing for every root by passing two aggregates (down + up).
10.5 The Euler tour — `tin`/`tout`, subtree-as-subarray, paths as range queries.
10.6 Binary lifting — \(2^k\) ancestors, k-th ancestor, LCA; the Euler-tour RMQ alternative named.
10.7 Distance queries — `dist(u,v) = depth[u]+depth[v]−2·depth[lca]`.

Worked examples:
- WE 10.1 CSES *Subordinates* — the post-order pattern that everything builds on.
- WE 10.2 CSES *Tree Diameter* — the two-DFS method with the correctness proof spelled out (the common wrong-proof flagged).
- WE 10.3 CSES *Company Queries I & II* — binary lifting for k-th ancestor, then LCA by lifting both ends.
- WE 10.4 CSES *Tree Distances II* — the canonical reroot: `down[v]`, then `up[v]` via the sibling-max trick.
- WE 10.5 CSES *Distance Queries* — LCA + depth formula.

Figures:
- F 10.1 `tin`/`tout` Euler tour intervals nested on a sample tree.
- F 10.2 Binary-lifting table: \(up[v][k]\) = \(2^k\)-th ancestor, drawn over a path.
- F 10.3 Two-DFS diameter: the farthest-point argument illustrated.
- F 10.4 Reroot arrows: what travels from parent to child at the second pass.
- F 10.5 LCA by equal-depth lift then binary search (two-column walk).

Code listings:
- L 10.1 Subtree DP skeleton.
- L 10.2 Two-DFS diameter.
- L 10.3 `LCA` class via binary lifting (+ optional Euler-RMQ note).
- L 10.4 Reroot DP template.

Exercises: 4 inline (rooted vs unrooted; why farthest works; lift table fill; subtree→subarray). Additional (13): [easy] CSES Tree Diameter, Tree Distances I, Subordinates, USACO-S MooTube, USACO-B Family Tree; [medium] CSES Tree Matching, Company Queries II, USACO-S Milk Visits, AC Count Descendants, CF Minimize the Diameter; [hard] CSES Finding a Centroid, Counting Paths, Fixed-Length Paths I, USACO-G Cow Land.
Named archive problems: + USACO-G Directory Traversal, Cow at Large, Delegation [DP cross-ref], USACO-S Ski Slope, Clock Tree; DMOPC Victor Takes Over Canada; POI 2014 Hotels [route].
Band: CF 1500–2000 — USACO Gold→Platinum edge.
Lib: `lca.h`, `tree_diameter.h`, `reroot.h`, `euler.h`.

# Part IV — Dynamic programming

## Chapter 11 — Dynamic programming I: the method and the classics (≈14 pp)

*Prerequisites:* Ch 2 (recursion/subsets), Ch 5 (prefix thinking), Ch 7 (DAGs help — review given inline).

Sections:
11.1 The same problem twice — memoization vs tabulation; when each is safer.
11.2 The DP recipe — state, transition, base case, order, answer; the five-line checklist.
11.3 Coin problems — minimising coins, counting ways; *the ordered-vs-unordered trap that wrong-answers more submissions than any other*.
11.4 Knapsack — 0/1 and unbounded; the inner-loop direction as the whole trick; reconstruction.
11.5 LIS — \(O(n^2)\) then \(O(n\log n)\) with the patience-tableau proof.
11.6 Grid DP — paths, obstacles, edit distance's grid cousin.
11.7 Push vs pull — two directions to write the same recurrence.

Worked examples:
- WE 11.1 CSES *Minimizing Coins* — top-down then bottom-up; why they compute the same set.
- WE 11.2 CSES *Dice Combinations* → *Coin Combinations I vs II* — the ordered/unordered contrast written as the central worked example (swap the loops, break the answer).
- WE 11.3 CSES *Book Shop* — 0/1 knapsack; the descending-capacity inner loop and what goes wrong without it.
- WE 11.4 CSES *Increasing Subsequence* — LIS in \(O(n\log n)\) with the \(L_i\)-monotonicity lemmas (the USACO-Guide-style three-lemma presentation).
- WE 11.5 CSES *Grid Paths I* — obstacles and the in-place table.

Figures:
- F 11.1 The subproblem DAG for coin DP (states as nodes, transitions as edges — DP = DP on a DAG, made literal).
- F 11.2 dp-table filling small-multiple (Book Shop, 4 frames).
- F 11.3 The ordered/unordered bug: two loop-nestings side by side with their counted outcomes.
- F 11.4 The \(L_i\) patience array evolving over one sequence.
- F 11.5 Grid DP dependency arrows (which cells feed cell (i,j)).

Code listings:
- L 11.1 Coin DP memo (top-down).
- L 11.2 Coin DP table (bottom-up) — same recurrence, iterative.
- L 11.3 0/1 knapsack with reconstruction (`take` table).
- L 11.4 LIS \(O(n\log n)\) with `lower_bound`.

Exercises: 4 inline (define the state; ordered or not; which loop direction; predict the bug). Additional (14): [easy] CSES Coin Combinations I/II, Removing Digits, Money Sums, USACO-G Fruit Feast; [medium] CSES Array Description, Two Sets II, Rectangle Cutting, USACO-G Hoof, Paper, Scissors, USACO-G Time is Mooney, USACO-G Teamwork; [hard] CSES Projects, USACO-G Snakes, USACO-G Talent Show.
Named archive problems: + CSES Counting Towers, Minimal Grid Path, Increasing Subsequence II; USACO-G Circular Barn Revisited, Taming the Herd, Drought, Stamp Painting; AC DP-contest A–E named.
Band: CF 1300–1800 — USACO Gold entry. (DP is *the* rating-maker at this band: CF `dp` tag p25 ≈ 1800 per sources.md.)
Lib: `lis.h`, `knapsack.h`, `coin.h` patterns.

## Chapter 12 — Dynamic programming II: masks, digits, ranges, and trees (≈14 pp)

*Prerequisites:* Ch 11; Ch 10 for §12.5; bitmask basics reviewed inline.

Sections:
12.1 Subsets as states — bitmask DP; enumerating masks and submasks.
12.2 The canonical shape — assignment/TSP-style DP over (mask, last).
12.3 Digit DP — counting integers with a property; the tight/loose automaton.
12.4 Range DP — cost over every subarray; the by-length order.
12.5 DP on trees — in/out states on rooted trees; rerooting for all roots (builds on Ch 10.4).
12.6 The optimisation horizon — bitset knapsack (taught), and *named for the route to 1900*: convex hull trick, divide-and-conquer DP, Knuth, SOS DP, profile DP. One worked bitset example; the rest are signposts with pointers to CPH/cp-algorithms.

Worked examples:
- WE 12.1 CSES *Elevator Rides* — the canonical bitmask DP (best-ride-count + residual capacity state).
- WE 12.2 CSES *Counting Numbers* — digit DP skeleton (tight flag, leading-zero flag).
- WE 12.3 CSES *Removal Game* — range DP by length; the min/max over splitting points.
- WE 12.4 CSES *Edit Distance* — alignment-grid DP revisited as the string-DP anchor (LCS contrasted).
- WE 12.5 Tree DP — *Tree Matching* and the AC *Independent Set*: in/out state pairs; then all-roots rerooting on *Tree Distances II* (callback to Ch 10.4).
- WE 12.6 Bitset knapsack — *Money Sums* in \(O(n \cdot C/64)\); the shift-and-or trick explained.

Figures:
- F 12.1 Mask ↔ subset lattice for \(n=4\) (the Hasse diagram the DP walks).
- F 12.2 Digit-DP automaton: states (position, tight, leading-zero) with transitions.
- F 12.3 Range-DP by-length filling order on a 5×5 triangle.
- F 12.4 Edit-distance grid with the optimal alignment path traced.
- F 12.5 Tree-DP in/out state diagram on a rooted tree.
- F 12.6 The bitset trick: `dp |= dp << w` drawn as shifting a bitmask.

Code listings:
- L 12.1 Bitmask TSP/assignment template.
- L 12.2 Digit-DP counter skeleton.
- L 12.3 Range-DP template (Removal Game).
- L 12.4 Tree-DP in/out skeleton + reroot all-roots.
- L 12.5 Bitset knapsack (`std::bitset` / `unsigned long long` blocks).

Exercises: 4 inline (mask iteration; why tight flag; by-length order; what reroot carries). Additional (14): [easy] AC Matching, AC Grouping, CSES Edit Distance, USACO-G Barn Painting; [medium] CSES Elevator Rides, Rectangle Cutting, Minimal Grid Path, USACO-G Uddered but not Herd, AC Independent Set, CF Team Building; [hard] CSES Counting Tilings (profile DP preview), Counting Numbers, Longest Common Subsequence, USACO-G Lights Off.
Named archive problems: + USACO-G Cow Poetry, Exercise, Bovine Genetics, Bessie's Function, Directory Traversal; YS Max Indep Set; IZhO 2014 Bank; Kattis Cat & Mice; POI 2004 Spies [route].
Band: CF 1600–2100 — USACO Gold→Platinum edge.
Lib: `bitmask_dp.h`, `digitdp.h`, `rangedp.h`, `treedp.h`, `bitset_knapsack.h`.

# Part V — Range data structures

## Chapter 13 — Fenwick and segment trees (≈14 pp)

*Prerequisites:* Ch 5 (prefix sums), Ch 6 (amortized thinking helps).

Sections:
13.1 The range-query family — point-update/range-query vs range-update/point-query vs both; a decision table.
13.2 The Fenwick (binary indexed) tree — the lowbit trick, the binary decomposition of indices, prefix-sum in \(O(\log n)\); inversion counting.
13.3 The segment tree — the \(2n\) array, point updates, range queries over any associative monoid; iterative and recursive forms.
13.4 Lazy propagation — range updates deferred; the add-tag + sum-query pair as the canonical combination.
13.5 Walking the tree — first element ≥ x, k-th element; the descent pattern.
13.6 Order statistics — finding the k-th smallest in a BIT/segtree; `List Removals`-style deletions.

Worked examples:
- WE 13.1 CSES *Dynamic Range Sum Queries* — solved twice (BIT, then segtree) with the trade-off table.
- WE 13.2 CSES *Dynamic Range Minimum Queries* — segtree over min; why BIT can't.
- WE 13.3 CSES *Range Update Queries* — range-update/point-query via the difference trick, then lazy segtree for the general case.
- WE 13.4 CSES *Hotel Queries* — walk-on-tree descent (first room with enough capacity).
- WE 13.5 CSES *List Removals* — k-th element by descent; the order-statistic pattern.

Figures:
- F 13.1 Fenwick index → covered-range diagram (the powers-of-two staircase).
- F 13.2 Segment tree over an 8-element array: node ↔ segment labels.
- F 13.3 Query descent: how a range decomposes into ≤ 2·log n nodes.
- F 13.4 Lazy propagation small-multiple: tag set → deferred → pushed.
- F 13.5 Walk-on-tree descent path for Hotel Queries.

Code listings:
- L 13.1 `Fenwick` (add, sum, lower_bound).
- L 13.2 Iterative segment tree (Al.Cash-style, `tree[2n]`).
- L 13.3 Recursive lazy segment tree (range add, range sum).
- L 13.4 Order-statistic descent (k-th element).

Exercises: 4 inline (which of the four query/update combos; why min breaks BIT; tag push order; descent invariant). Additional (13): [easy] CSES Static Range Sum/Minimum Queries, Range Xor Queries, USACO-G Haircut, USACO-G Balanced Photo; [medium] CSES Dynamic Range Sum/Minimum Queries, Salary Queries, USACO-G Sleepy Cow Sorting, USACO-G Why Did the Cow Cross the Road III, Kattis Mega Inversions; [hard] CSES Prefix Sum Queries, Range Updates and Sums, Distinct Values Queries, CF Irrigation.
Named archive problems: + CSES Forest Queries II, Pizzeria Queries, Subarray Sum Queries, Increasing Array Queries, Polynomial Queries, Range Queries and Copies, Missing Coin Sum Queries, Movie Festival Queries, Pyramid Array [route], USACO-P Why Did the Cow Cross the Road [route].
Band: CF 1600–2100 — USACO Gold→Platinum.
Lib: `fenwick.h`, `segtree.h`, `lazyseg.h`, `orderstat.h`.

# Part VI — Contest mathematics

## Chapter 14 — Number theory and combinatorics (≈13 pp)

*Prerequisites:* Ch 1; Ch 11 for the counting-DP cross-references.

Sections:
14.1 Divisibility and gcd — the Euclidean algorithm and its proof by invariant; extended gcd and Bézout.
14.2 Primes — sieve of Eratosthenes, trial division to \(\sqrt n\), prime factorization via smallest-prime-factor table.
14.3 Modular arithmetic — the four rules, why mod-everything-at-every-step is legal, modular inverse via \(a^{p-2}\) (Fermat) and via extended gcd.
14.4 Binary exponentiation — \(a^b \bmod m\) in \(O(\log b)\).
14.5 The `modint` struct — the class you write once and reuse forever (overflow pitfalls inside).
14.6 Counting — factorials and \(n \choose k\) mod p (precompute + inverse), stars and bars, derangements, inclusion–exclusion, Catalan numbers (the reflection/ballot argument).
14.7 Linear recurrences — Fibonacci by matrix exponentiation (named pattern, worked).

Worked examples:
- WE 14.1 CSES *Counting Divisors* — SPF sieve → factorization → divisor count.
- WE 14.2 CSES *Exponentiation II* — Fermat's little theorem reducing the exponent's exponent (the classic trap).
- WE 14.3 CSES *Binomial Coefficients* — precomputed factorials + modular inverses.
- WE 14.4 CSES *Distributing Apples* — stars and bars with the walls/children mapping drawn.
- WE 14.5 CSES *Christmas Party* — derangements via inclusion–exclusion, with the recurrence.
- WE 14.6 CSES *Fibonacci Numbers* — matrix power; the linear-recurrence pattern for later use.

Figures:
- F 14.1 Sieve marking on \(n=30\) (small multiple, primes 2,3,5).
- F 14.2 Binary exponentiation's squaring tree for \(a^{13}\).
- F 14.3 Stars-and-bars: apples and walls as a string diagram.
- F 14.4 Inclusion–exclusion Venn for three sets (the Christmas Party count).
- F 14.5 The Catalan/ballot reflection picture.
- F 14.6 Matrix-power recurrence: the 2×2 Fibonacci matrix and why squaring it works.

Code listings:
- L 14.1 `binpow` (mod exponentiation).
- L 14.2 Sieve + SPF table + factorize.
- L 14.3 `modint` struct (add/sub/mul/div via Fermat).
- L 14.4 \(n \choose k\) precomputation + stars-and-bars formula.

Exercises: 4 inline (extend gcd; why does inverse need prime; which counting model; matrix dimension). Additional (14): [easy] CSES Exponentiation, Counting Divisors, Common Divisors, Throwing Dice; [medium] CSES Exponentiation II, Sum of Divisors, Binomial Coefficients, Distributing Apples, Creating Strings II, Permutation Rounds, Fibonacci Numbers; [hard] CSES Prime Multiples, Counting Coprime Pairs, Christmas Party, Bracket Sequences I, Divisor Analysis, Graph Paths I/II.
Named archive problems: + CSES Next Prime, Josephus Queries, Bracket Sequences II, Counting Necklaces, Counting Grids, System of Linear Equations, Sum of Four Squares, Triangle Number Sums; CF Santa's Bot, Make it One, Round Subset.
Band: CF 1300–1900 — USACO Gold. (CF `number theory` p25 ≈ 1300, `combinatorics` p25 ≈ 1900 — the honest split is noted in-text.)
Lib: `binpow.h`, `sieve.h`, `gcdext.h`, `modint.h`, `ncr.h`, `matpow.h`.

## Chapter 15 — Strings: hashing, KMP, Z (≈12 pp)

*Prerequisites:* Ch 5 (prefix sums), Ch 14 (modular arithmetic for hashing).

Sections:
15.1 Terminology — prefix, suffix, substring, subsequence, border, period.
15.2 Polynomial rolling hash — the hash as a base-\(B\) number mod \(p\); substring equality in \(O(1)\) after prefix hashes; collision probability, why two hashes or a 64-bit modulus.
15.3 The prefix function (KMP) — borders of prefixes, failure links, the automaton for pattern matching.
15.4 The Z-function — the Z-box invariant, linear time by maintaining the window; KMP-equivalence for matching.
15.5 Tries — prefix dictionaries; the xor-trie named for the 1900 route.
15.6 Applications — matching (KMP or Z+needle), borders (Finding Borders), periods (Finding Periods: \(n - \pi_n\)), LCP via hashing + binary search.

Worked examples:
- WE 15.1 CSES *String Matching* — solved twice (KMP automaton, then Z-concatenation) to show the equivalence.
- WE 15.2 CSES *Finding Borders* + *Finding Periods* — prefix-function outputs repurposed (the \(n-\pi_n\) period trick with proof).
- WE 15.3 Rolling hash for substring equality — a worked collision discussion: where 1-in-\(10^9\) fails and double-hash saves it.
- WE 15.4 CSES *Word Combinations* — trie + DP over the string.

Figures:
- F 15.1 Failure-link automaton walk on `ABABAC` (the drawn KMP machine).
- F 15.2 Z-box window: \(l,r\) maintained as the scan proceeds.
- F 15.3 Rolling-hash sliding window: drop \(s_{i-1}B^{k-1}\), add \(s_i\).
- F 15.4 Trie with terminal counts, built from a 6-word dictionary.
- F 15.5 Border chain: \(\pi\), \(\pi(\pi)\), … drawn as nested equal blocks.

Code listings:
- L 15.1 Prefix function (KMP table) — the 15-line core.
- L 15.2 Z-function.
- L 15.3 Rolling hash (prefix hashes + substring hash + LCP via binary search).
- L 15.4 Trie node + insert + query.

Exercises: 3 inline (compute π by hand; the period identity; where collisions live). Additional (12): [easy] CSES Finding Borders, Finding Periods, USACO-OB Censoring, CF Check Transcription; [medium] CSES String Matching, Minimal Rotation, Longest Palindrome, Repeating Substring, USACO-G Lights Out; [hard] CSES Required Substring, Distinct Substrings, String Functions.
Named archive problems: + CSES Word Combinations, All Palindromes, Finding Patterns, Counting Patterns, Pattern Positions, Palindrome Queries, Substring Order I/II, Inverse Suffix Array [route], String Transform [route]; CEOI 2017 Palindromic Partitions; COCI 2017 Osmosmjerka; JOI Mergers [route].
Band: CF 1300–1900 — USACO Gold (hashing-flagged rare but high-yield).
Lib: `kmp.h`, `zfunc.h`, `rhash.h`, `trie.h`.

## Chapter 16 — Geometry basics [optional] (≈10 pp, outside the core page budget)

*Prerequisites:* Ch 1; vectors from school maths (review given).

Sections:
16.1 The integer-only discipline — why contests use cross products, not slopes or angles.
16.2 Points, vectors, cross product — the oriented area; `cross(a,b)` as the one primitive.
16.3 Orientation tests — left turn/right turn/collinear; CSES *Point Location Test*.
16.4 Segment intersection — straddling + the boundary cases (endpoint touches, collinear overlap).
16.5 Polygons — signed area (shoelace), point-in-polygon by ray casting, Pick's theorem.
16.6 Convex hull — Andrew's monotone chain; where hulls hide in problems.
16.7 Named for the route — sweep lines, closest pair, rotating calipers (signposts only).

Worked examples:
- WE 16.1 CSES *Point Location Test* — the cross-product sign table.
- WE 16.2 CSES *Line Segment Intersection* — the four orientation checks + the touch cases enumerated honestly.
- WE 16.3 CSES *Polygon Area* + *Polygon Lattice Points* — shoelace and Pick's theorem (Pick derived, not just cited).
- WE 16.4 CSES *Convex Hull* — monotone chain with the pop-while-turn rule.

Figures:
- F 16.1 Cross product = oriented parallelogram area; sign → turn direction.
- F 16.2 Segment-intersection case table (4 pictures: proper, touch, collinear-overlap, miss).
- F 16.3 Shoelace as trapezoid decomposition.
- F 16.4 Ray casting parity (inside/outside by crossing count).
- F 16.5 Monotone-chain hull: lower pass then upper pass (small multiple).
- F 16.6 Pick's theorem on a sample polygon (interior + boundary dots).

Code listings:
- L 16.1 `pt` struct + `cross`/`dot` (the 10-line geometry header).
- L 16.2 Segment intersection.
- L 16.3 Shoelace + Pick.
- L 16.4 Monotone chain hull.

Exercises: 3 inline (sign vs orientation convention; which touch cases; hull pop condition). Additional (10): [easy] CSES Point Location Test, Polygon Area, Polygon Lattice Points; [medium] CSES Line Segment Intersection, Point in Polygon, Convex Hull; [hard] CSES Minimum Euclidean Distance, Intersection Points, Maximum Manhattan Distances, Area of Rectangles.
Band: CF 1600–2200 — flagged: rare below 1600, standard at 1800+; skim level sufficient for the 1600 target, full mastery for the 1900 route.
Lib: `geometry.h` (pt, cross, seg-int, hull).

## Chapter 17 — Probability, expectation, and games [optional] (≈10 pp, outside the core page budget)

*Prerequisites:* Ch 11 (DP), Ch 14 (modular arithmetic; modular fractions).

Sections:
17.1 Probability as counting — uniform sample spaces, when combinatorics *is* the answer.
17.2 Linearity of expectation — the workhorse: expected sums without independence.
17.3 States with expectation — DP where the value is an expectation; Markov chains as recurrences.
17.4 Order statistics — E[max]/E[min] patterns (Candy Lottery).
17.5 Modular fractions — answers mod \(10^9+7\): \(p/q\) as \(p \cdot q^{-1}\).
17.6 Games — Nim and the xor rule (with the winning-strategy sketch), mex/Grundy computed for small states; Sprague–Grundy named for the 1900 route.

Worked examples:
- WE 17.1 CSES *Dice Probability* — counting outcomes to a probability mod p.
- WE 17.2 CSES *Moving Robots* — expectation-per-cell DP (each robot walks independently; linearity does the join).
- WE 17.3 CSES *Candy Lottery* — E[max] via P(max ≤ k) decomposition.
- WE 17.4 CSES *Nim Game I* — the xor rule with the strategy-stealing argument in outline.
- WE 17.5 CSES *Grundy's Game* — mex table computed bottom-up; the split move.

Figures:
- F 17.1 Linearity picture: indicators summing without independence.
- F 17.2 Expectation-DP transition graph for Moving Robots.
- F 17.3 E[max] as a staircase decomposition of P(max ≤ k).
- F 17.4 Nim-heap xor table; the winning move highlighted.
- F 17.5 mex computation walk for Grundy's Game (small multiple).

Code listings:
- L 17.1 Expectation DP skeleton.
- L 17.2 mex/grundy table for a take-and-split game.
- L 17.3 Nim solver (xor + first winning move).
- L 17.4 `modfrac` — probabilities mod p done right.

Exercises: 3 inline (linearity without independence; which state; what's losing in Nim). Additional (10): [easy] CSES Dice Probability, Throwing Dice, Nim Game I, Another Game; [medium] CSES Moving Robots, Candy Lottery, Nim Game II, Stair Game; [hard] CSES Inversion Probability, Grundy's Game.
Band: CF 1500–2100 — flagged rare below 1600 (CF `probabilities` p25 ≈ 2100); game-theory tags appear ~800+ but the real band is Gold+.
Lib: `mex.h`, `modfrac.h`.

# Part VII — Contest craft

## Chapter 18 — The contest playbook: strategy, stress testing, upsolving (≈11 pp)

*Prerequisites:* the whole book (this is the meta-chapter; readable any time after Ch 5).

Sections:
18.1 Before the contest — the template file, the checklist, sleep.
18.2 The first ten minutes — read everything, triage by solvability not by order.
18.3 The wrong-answer loop — constraints again, edge cases, the brute-force comparison.
18.4 Stress testing — the three-file harness (generator, brute force, fast solution); *the single most leveraged skill in this book*.
18.5 Debugging under time pressure — asserts, minimal counterexamples, when to rewrite.
18.6 After the contest — the upsolving protocol: editorial etiquette (read after real attempts; implement every editorial you read), the honest note that experts disagree on timing (with attributed positions), tracking rating by topic.
18.7 The long game — a season plan, the plateau, when to move up a band.
18.8 The rating-by-topic map — the big table (below); where each chapter lands.

Worked examples:
- WE 18.1 A stress-test debugging session — a buggy greedy vs its brute force on random small cases; finding the minimal failing input and the fix.
- WE 18.2 Triaging a 3-problem set — a mock scoreboard walk (which problem first and why).
- WE 18.3 An upsolve walkthrough — post-contest: read editorial for one problem, implement, verify, record what was missing.
- WE 18.4 Partial credit as a strategy — subtask-harvesting on an IOI-style problem.

Figures:
- F 18.1 Contest timeline swimlane: read → plan → code → test → submit → next.
- F 18.2 The stress-test pipeline diagram (gen → brute & fast → diff → shrink).
- F 18.3 The upsolving loop (attempt → editorial → implement → log → revisit).
- F 18.4 The rating-by-topic map as a stacked table (see below).
- F 18.5 A study-week template calendar (practice blocks vs review blocks).

Code listings:
- L 18.1 `stress.sh` — the harness loop with seeds.
- L 18.2 `gen.py` — a random-case generator with tunable knobs.
- L 18.3 `brute.cpp` + `sol.cpp` pair for WE 18.1 with the diff output shown.
- L 18.4 A minimal `Makefile` for the harness.

Exercises: 4 inline (triage a given set; write the brute; what's the smallest failing case; which chapter covers the missed topic). Additional (10 — process exercises): [easy] build the harness and stress 3 solved problems; write a brute for CSES Apartments; [medium] upsolve a real Div 2 C you missed, with a written post-mortem; virtual-participate one old contest with the triage rule; [hard] reproduce one USACO Gold problem's full solve+stress+writeup; design a 4-week plan against the rating-by-topic map.
Band: all.
Lib: `stress/` harness (gen, brute template, runner, shrinker).

## The rating-by-topic map (in Ch 18 + Appendix B)

Bands are CF ratings; `Div 2` letters the typical problem slot; the USACO column gives the division where the technique is assumed. Derived from the USACO Guide division structure + CF problemset tag quartiles computed 2026-10-10 (see `docs/sources.md`); tagged ratings skew high, so entry bands are stated conservatively. Date-stamped.

| Band | CF slot | Topics (chapters) | USACO |
|---|---|---|---|
| 800–1200 | Div 2 A–B | Implementation, simulation, ad hoc, basic complete search, sorting (Ch 1–3) | Bronze |
| 1200–1500 | Div 2 B–C | Binary search, two pointers, prefix sums, greedy with sorting, casework, basic sets/maps (Ch 4–6) | Silver |
| 1400–1700 | Div 2 C | Graph traversal, flood fill, flood of BFS apps, topo sort, basic DP, coordinate compression, monotonic stack (Ch 6–7, 11) | Silver→Gold |
| 1600–1900 | Div 2 C–D | Weighted shortest paths, DSU, MST, tree basics + LCA, knapsack/bitmask/standard DP, Fenwick/segtree, string hashing/KMP, modular arithmetic + nCr (Ch 8–15) | Gold |
| 1900–2200 | Div 2 D–E | DP reroot + optimisation (CHT, D&C DP, Knuth), lazy segtree variants, digit/range DP, Z/suffix structures, sweep-line geometry, expectation DP, Grundy (Ch 10, 12–17 horizon) | Gold→Platinum |
| 2200+ | Div 2 E–F | Flows, suffix automata, half-planes, FFT, heavy data structures — *out of this book's scope; pointers to cp-algorithms/CPH Part III* | Platinum |

# Back matter (~19 pp)

- Appendix A — The template library: the `code/lib/` catalogue (one-line description + complexity per routine; the checklist of what belongs and why ~30 routines, listed below).
- Appendix B — The route to 1900: the horizon topics (CHT, D&C DP, Knuth, SOS DP, reroot practice set, sweep line, suffix arrays/automata intro, Mo's algorithm, small-to-large, interactive problems) each with the single best free resource pointer; the "when to read what" sequence.
- Hints for all `[hard]` exercises; full solutions for ≥ half of all exercises (every `[easy]` has a full solution by policy).
- Bibliography (numbered `thebibliography`): PAPS, CPH, USACO Guide, CSES, cp-algorithms, MIT 6.006 OCW, KACTL, Codeforces EDU, USACO contest rules page — all as accessed in `docs/sources.md`.
- Index (makeindex): every defined term via `\index{}`.

# The capstone: `code/lib/` (≥20 tested routines; assigned to chapters)

Every routine is a header/single-file C++17 template the reader writes or adapts, **each paired with a stress test** (`code/stress/<name>_stress.cpp` + `gen.py` + brute) run by `make test`. The KACTL model: short, typed-in, header-annotated (author/date/description/complexity/tested-on). Assignment by chapter:

| Ch | Routines |
|---|---|
| 1 | `template.cpp` (starter file + fast I/O) |
| 2 | `subsets.h` (recursive + bitmask enumeration), `backtrack.h` skeleton |
| 3 | `compress.h` (coordinate compression) |
| 4 | `bsearch.h` (`first_true`) |
| 5 | `prefix.h` (1D + 2D), `diff.h`, `twoptr.h` pattern |
| 6 | `monostack.h`, `monodeque.h`, `sparse.h`, `sqrtdec.h` |
| 7 | `bfs.h` (+path reconstruction), `dfs.h` (iterative), `floodfill.h`, `toposort.h` (Kahn + 3-colour cycle) |
| 8 | `dijkstra.h`, `bellmanford.h` (+neg cycle), `floyd.h` |
| 9 | `dsu.h` (path halving + union by size + sizes), `kruskal.h`, `prim.h` |
| 10 | `lca.h` (binary lifting), `tree_diameter.h`, `reroot.h`, `euler.h` |
| 11 | `lis.h` (n log n), `knapsack.h` (+reconstruction), `coin.h` |
| 12 | `bitmask_dp.h`, `digitdp.h`, `rangedp.h`, `treedp.h`, `bitset_knapsack.h` |
| 13 | `fenwick.h`, `segtree.h`, `lazyseg.h`, `orderstat.h` |
| 14 | `binpow.h`, `sieve.h` (+SPF), `gcdext.h`, `modint.h`, `ncr.h`, `matpow.h` |
| 15 | `kmp.h`, `zfunc.h`, `rhash.h` (single + double), `trie.h` |
| 16 | `geometry.h` (pt, cross, seg-intersect, shoelace, Pick, hull) |
| 17 | `mex.h`, `modfrac.h` |
| 18 | `stress/` harness (gen.py, brute.cpp template, stress.sh, Makefile) |

Count: ~35 routines > the 20 minimum. Capstone completion check: the reader stress-tests every routine against a brute force in `make test`; the library finishes as an Appendix A reference sheet.

# Sources for this outline

Per `docs/sources.md`: PAPS (structure/register model), CPH (topic granularity + which advanced topics to signpost), USACO Guide Bronze/Silver/Gold module lists and per-module problem lists (chapter ordering + the entire problem bank), CSES problem list (exercise pool), cp-algorithms navigation (taxonomy check for NT/strings), MIT 6.006 OCW (rigorous ordering for graphs/DP), KACTL (capstone library + stress-test method), Codeforces EDU (second-treatment pointers), usaco.guide/practicing (upsolving protocol), usaco.org contests page (2025–26 season facts, date-stamped), Codeforces problemset API (rating-by-topic quartiles).
