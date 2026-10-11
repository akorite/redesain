# Sources

Research log for `textbook-cp`. Every row below is a resource actually opened during Wave 1 (2026-10-10). What was "taken" is an idea, a topic order, an exercise style, or a problem name — never text, figures, or code.

| URL / ISBN | Accessed (2026-10-10) | Licence | What was taken (idea / topic order / exercise type; never text) |
|---|---|---|---|
| https://usaco.guide/PAPS1.pdf — Johan Sannemo, *Principles of Algorithmic Problem Solving* (2025), 455 pp | 2026-10-10 | © Johan Sannemo 2025; selected content marked CC BY-SA 3.0 / CC BY 3.0 inside the book | Anchor. Book shape: Part I preliminaries (algorithms/problems, C++, STL, implementation, complexity, basic DS, recursion, graphs) → Part II common techniques (brute force, greedy, DP, divide and conquer, union-find/range queries/sliding windows) → Part III topics (graph algorithms, flows, game theory, number theory, combinatorics, strings) → appendices (competition strategy for IOI/ICPC, math notation, hints, solutions, index). Register: exercises inline where the text assumes them solved, a short "Additional Exercises" section, worked examples that show the thought process before the solution, solutions-first-explain-later avoided. Adopted wholesale as the book's structural model (with chapter merging; see outline). |
| https://cses.fi/book/book.pdf — Antti Laaksonen, *Competitive Programmer's Handbook* (2018 draft), 296 pp | 2026-10-10 | Free PDF; no explicit licence statement found in the preface | Anchor. Checklist of the "standard" CP curriculum and its granularity: amortized analysis as its own topic (two pointers, nearest smaller elements, sliding window minimum); range queries (static → BIT → segment tree → lazy/dynamic/2D revisited); square-root algorithms and Mo's algorithm; strings (trie, hashing, Z); sweep-line geometry; matrices; game theory; probability. Confirmed which advanced topics exist *beyond* a 1600–1900 target (suffix automata, flows, Burnside, Sprague–Grundy proof) so the outline can flag them as "route to 1900". |
| https://usaco.guide/ (home) + /bronze/ + /silver/ + /gold/ | 2026-10-10 | Free; open-source project (GitHub repo linked from site) | Anchor. Division→module structure and the Guide's own frequency labels (Very Frequent / Somewhat Frequent / Not Frequent / Rare / Has Not Appeared): Bronze = simulation, complete search, sorting/sets, casework, intro greedy/graphs/rectangle geometry, ad hoc; Silver = prefix sums, two pointers, binary search, custom comparators + coordinate compression, greedy with sorting, priority queues, graph traversal, flood fill, trees, functional graphs, bitwise; Gold = divisibility/modular/combinatorics, DP (intro, knapsack, grid paths, LIS, bitmask, range, digit), shortest paths, DSU, toposort, MST, sorted sets, stacks, sliding window, point-update-range-sum, Euler tour + tree DP + all-roots, hashing, meet-in-middle, ternary search. Used to assign each chapter a division ceiling and to order modules within parts. |
| https://cses.fi/problemset/list/ | 2026-10-10 | Free | Anchor. Full problem list harvested verbatim for the exercise plans: 300+ named problems grouped in CSES's own categories (Introductory, Sorting and Searching, Dynamic Programming, Graph Algorithms, Range Queries, Tree Algorithms, Mathematics, String Algorithms, Geometry, Advanced Techniques, Sliding Window, Interactive, Bitwise Operations, Construction). Names reused below in the problem bank; problems are *cited by name*, never copied (per master prompt §3). |
| http://www.usaco.org/index.php?page=contests | 2026-10-10 | Free public information | Format facts for the strategy chapter, date-stamped: 2025–26 season = three online contests (Jan 9–12, Jan 30–Feb 2, Feb 20–23) plus a proctored invitational US Open (Mar 28); "certified" gold/platinum scores require starting within 15 min of Saturday noon ET release; platinum membership was reset for the season and promotion requires a certified score; division structure retained this year but may change. Must be re-verified before the book ships. |
| https://cp-algorithms.com/ + https://cp-algorithms.com/navigation.html | 2026-10-10 | Free; volunteer-run translation+extension of e-maxx.ru (per-article licences vary) | Topic-taxonomy cross-check and ordering for two chapters: strings (hashing → Rabin–Karp → prefix function/KMP → Z-function → suffix array, with suffix automaton/lyndon flagged advanced) and number theory (sieve → primality → factorization → modular inverse → linear congruence → CRT → discrete log). Also confirmed which structures are *out of scope* at this level (treap, sqrt tree, suffix automaton, half-plane intersection, flows beyond named references). |
| https://codeforces.com/edu/courses | 2026-10-10 | Free (Codeforces EDU, β) | EDU exists as a free structured course (ITMO Academy pilot + community course). The USACO Guide repeatedly cites EDU lessons as canonical references (DSU course, Segment Tree Pt 1 steps 1/3/4) — logged so chapter "Notes" sections can point readers to a second free treatment of DSU and segment tree. |
| https://github.com/kth-competitive-programming/kactl | 2026-10-10 | Mixed; project aims for CC0 on own code, unmarked files under good-will assumption; stress-tests implicitly CC0 | Model for the capstone `code/lib/`: short typed-in routines (~63-char lines) each carrying author/date/description/time-complexity headers; correctness maintained by a `stress-tests/` directory that diffs every routine against a naive implementation on random cases in CI. Our stress harness (generator + brute + fast + diff loop) copies this *method*, not the code. Also took the "library grows chapter by chapter" idea. |
| https://cpbook.net/ + https://cpbook.net/methodstosolve | 2026-10-10 | Companion site free; the CP4 book itself is paywalled | Anchor (partially accessible). The site's "Methods to Solve" index exposes CP4/CP5's problem classification scheme: per-chapter numbered categories (e.g. "1.4a One-Liner I/O"), DP-related and CS-related groupings, starred problems, and a DACU (distinct accepted users) count used as a difficulty proxy. The detailed book TOC is *not* freely visible — do not cite chapter contents beyond these categories. The book itself was NOT opened. |
| https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/lecture-notes/ | 2026-10-10 | MIT OpenCourseWare, CC BY-NC-SA 4.0 | Rigorous ordering sanity check: BFS → DFS → weighted shortest paths (Bellman–Ford before Dijkstra, then Johnson), DP as a four-lecture arc (SRTBOT → LCS/LIS/coins → rods/subset-sum/pseudopolynomial). Supports the outline's decision to teach Bellman–Ford *before* Dijkstra (relaxed correctness argument) and DP as state-first design. |
| https://usaco.guide/general/practicing | 2026-10-10 | Free; open-source project | Contest-craft material: named top contestants' answers to "when do you read the editorial" (Darren Yao: bronze 15–20 min, silver 30–40 min; Benjamin Qi's checklist; Siyong Huang's "implement every editorial you read"; William Lin's three guidelines). Used to write the upsolving protocol *with attribution and with the honest note that experts disagree*. |
| https://codeforces.com/api/problemset.problems | 2026-10-10 | Free public API | Quantitative grounding for the rating-by-topic map: 11,433 rated problems fetched and grouped by tag; per-tag rating quartiles computed locally (table below). Prevents invented difficulty claims. |
| https://codeforces.com/problemset?order=BY_RATING_ASC&tags=dp | 2026-10-10 | Free | Partial: page chrome retrieved but the problem table is JS-rendered and did not materialize. Replaced by the API pull above. |
| https://train.usaco.org/usacogate | 2026-10-10 | Login-gated | Inaccessible without a USACO training account — the legacy training-pages curriculum could not be read. Logged as attempted; not used. |
| ~35 USACO Guide module pages (usaco.guide/bronze/*, /silver/*, /gold/*) — simulation, intro-complete, complete-rec, intro-sorting, intro-greedy, intro-graphs, prefix-sums, more-prefix-sums, two-pointers, binary-search, custom-cmp-and-coord-compress, greedy-sorting, priority-queues, graph-traversal, flood-fill, intro-tree, func-graphs, intro-dp, knapsack, paths-grids, lis, dp-bitmasks, dp-trees, all-roots, unweighted-shortest-paths, shortest-paths, dsu, toposort, mst, sliding-window, PURS, hashing, meet-in-the-middle, lca-euler, modular, divisibility, combo | 2026-10-10 | Free; open-source project | Problem lists per module: the actual USACO/CSES/CF/Kattis/OI problem names the Guide assigns to each technique, with its own difficulty tier (Easy/Medium/Hard/Very Hard/Insane). Harvested into the problem bank below — this is how each chapter's "problems to point to" list was built. Also each module's "Resources" rows (which texts top contestants are pointed at for that topic) inform the per-chapter Notes. |

## Honesty notes

- The CP4/CP5 book (Halim) was not opened (paywalled); only its companion site and classification scheme were read. Nothing from inside the book is used.
- `train.usaco.org` requires a login; its curriculum is unknown to this project and is not cited.
- The Codeforces problemset HTML view could not be rendered; the public API was used instead (11,433 problems — the full rated set at fetch time).
- CSES solve counts (the "x / y" numbers next to each problem) were observed but are not reproduced; they change daily.

## Problem bank harvested for the exercise plans

Problem names below are used in `docs/outline.md` as citation targets. "USACO X" = USACO problem at division X (Bronze/Silver/Gold/Platinum, incl. "Old" divisions); CF = Codeforces; AC = AtCoder; YS = Library Checker; CSES per the official list above.

### Workflow / simulation / ad hoc (Ch 1)
- CSES: Weird Algorithm, Missing Number, Repetitions, Increasing Array, Permutations, Number Spiral, Two Knights, Two Sets, Bit Strings, Trailing Zeros, Coin Piles, Palindrome Reorder
- USACO Bronze: The Cow-Signal, Speeding Ticket, The Lost Cow, The Bovine Shuffle, The Bucket List, Shell Game, Mixing Milk, Measuring Traffic, Circular Barn, Block Game, Team Tic Tac Toe, Mowing the Field, Reflection, Milk Measurement, Stuck in a Rut

### Complete search (Ch 2)
- CSES: Apple Division, Creating Strings, Chessboard and Queens, Tower of Hanoi, Gray Code, Raab Game I, Mex Grid Construction, Digit Queries, Grid Path Description, Knight Moves Grid, String Reorder, Grid Coloring I
- USACO Bronze: Milk Pails, Diamond Collector, Daisy Chains, Counting Liars, Cow Gymnastics, Bovine Genomics, Triangles, Lifeguards, Why Did the Cow Cross the Road II, Guess the Animal, Load Balancing, Sleeping in Class, Cow Checkups, Contaminated Milk, Cowntact Tracing, Bull in a China Shop

### Sorting, sets, greedy (Ch 3)
- CSES: Distinct Numbers, Apartments, Ferris Wheel, Concert Tickets, Restaurant Customers, Movie Festival, Sum of Two Values, Stick Lengths, Missing Coin Sum, Collecting Numbers, Collecting Numbers II, Playlist, Towers, Tasks and Deadlines, Movie Festival II, Josephus Problem I, Josephus Problem II, Sum of Three Values, Sum of Four Values
- USACO Bronze/Silver: Why Did the Cow Cross the Road III (B), Cow College (B), Angry Cows (B), Watching Mooloo (B), Cow Tipping (B), Even More Odd Photos (B), Out of Place (B), Astral Superposition (B), Purchasing Milk (B), Milking Order (B), Photoshoot (B), FEB (B), Race (B), Lemonade Line (S), High Card Wins (S), Rest Stops (S), Bovine Acrobatics (S), Berry Picking (S), Closest Cow Wins (S); USACO Gold: High Card Low Card
- CF: Kayaking, Playing in a Casino, USB vs. PS/2, The Party and Sweets, Ciel and Duel, Yet Another Tournament, Permutator

### Binary search (Ch 4)
- CSES: Factory Machines, Array Division, Multiplication Table, Reading Books, Sum of Three Values, Sum of Four Values, Nearest Smaller Values, Subarray Sums II, Movie Festival II, Maximum Subarray Sum II, Nested Ranges Check, Nested Ranges Count, Room Allocation, Traffic Lights
- USACO Silver: Cow Dance Show, Convention, Angry Cows, Social Distancing, Loan Repayment, Bakery; USACO Gold: Talent Show
- CF/Other: Guess the K-th Zero (interactive), Edu C: Magic Ship, The Meeting Place Cannot Be Changed, Packmen, Max Median, Grouped Carriages, Level Generation; Baltic OI 2012 Mobile

### Prefix sums / two pointers / sliding windows (Ch 5)
- CSES: Static Range Sum Queries, Forest Queries, Subarray Sums I, Subarray Sums II, Subarray Divisibility, Maximum Subarray Sum, Maximum Subarray Sum II, Distinct Values Subarrays, Sliding Window Sum, Sliding Window Minimum, Sliding Window Median, Sliding Window Cost, Sliding Window Distinct Values, Sliding Window Xor, Sliding Window Mex
- USACO Silver: Breed Counting, Hoof, Paper, Scissors, Subsequences Summing to Sevens, Farmer John's Favorite Operation, Rectangular Pasture, Painting the Barn, Paired Up, Diamond Collector, Sleepy Cow Herding, Cow Checkups; USACO Gold: Haybale Feast; USACO Platinum: Modern Art, Fort Moo
- CF/Other: Good Subarrays, Karen and Coffee, Little Girl and Maximum Sum, Counting Rectangles, QED's Favorite Permutation, Queries for Number of Palindromes, They Are Everywhere, Quiz Master, Cellular Network, MEX vs MED; SPOJ: Haybale Stacking; Kattis: Map of Sweden

### Graphs, traversal, topo, functional graphs (Ch 6)
- CSES: Counting Rooms, Labyrinth, Building Roads, Message Route, Building Teams, Round Trip, Monsters, Course Schedule, Course Schedule II, Game Routes, Longest Flight Route, Round Trip II, Planets Cycles, Planets Queries I
- USACO Bronze: The Great Revegetation, Milk Factory, Hoofball, Swapity Swap, Cow Evolution, Family Tree; USACO Silver: Closing the Farm, Moocast, Fence Planning, Icy Perimeter, Cross Country Skiing, Switching on the Lights, Build Gates, Where's Bessie?, Mooyo Mooyo, Comfortable Cows, Snow Boots, 2D Conveyor Belt, Maze Tac Toe, Multiplayer Moo, The Bovine Shuffle, Visits, Cowntagion, Grass Planting; USACO Gold: Timeline
- CF/Kattis/Other: Solve The Maze, Connected Components?, PolandBall & Forest, Journey, Directing Edges, Fox and Names, Substring, Pattern Matching; Kattis: Birthday Party, Quantum Superposition; AC: Constrained Topological Sort, Exactly K Steps; IOI: Tropical Garden

### Shortest paths (Ch 7)
- CSES: Shortest Routes I, Shortest Routes II, High Score, Flight Discount, Cycle Finding, Flight Routes, Investigation, Graph Girth, Swap Game
- USACO Gold: Moortal Cowmbat, Milk Pumping, Why Did the Cow Cross the Road, Fine Dining, Shortcut, Telephone, Lasers and Mirrors, Cow at Large, Replication, A Pie for a Pie; USACO Silver: Milk Pails
- CF/Other: Not Escaping, D/D/D; Kattis: Robot Turtles; AC: Remainder Game, Construct a Palindrome, Small Multiple; IOI 2009 Mecho, IOI 2011 Crocodile, IOI Walls; JOI 2018 Commuter Pass, JOI 2021 Robot; APIO Find the Path; Balkan OI 2012 Shortest Paths, 2015 Circus

### DSU / MST (Ch 8)
- CSES: Road Construction, Road Reparation, New Roads Queries, Flight Routes Check, Necessary Roads, Necessary Cities, Dynamic Connectivity
- USACO: Closing the Farm (G), MooTube (G), Moocast (G/S), Wormhole Sort (S), Tractor (OS), Reachable Pairs (G), Strongest Friendship Group (G), Ski Course Rating (OG), Favorite Colors (G), Valleys (P), Superbull (OS), Fenced In (G), I Would Walk 500 Miles (G), Moo Network (G), Portals (G)
- CF/Other: Two Sets, Design Tutorial: Inverse the Problem, GCD and MST; CSA: Mountain Time; Kattis: Birthday Party; Baltic OI 2016 Park; JOI 2015 Inheritance; COCI Sirni; APIO 2013 Toll; AC: Choose Two and Eat One

### Trees / LCA (Ch 9)
- CSES: Subordinates, Tree Matching, Tree Diameter, Tree Distances I, Tree Distances II, Company Queries I, Company Queries II, Distance Queries, Counting Paths, Subtree Queries, Path Queries, Distinct Colors, Finding a Centroid, Fixed-Length Paths I, Fixed-Length Paths II, Even Outdegree Edges
- USACO: MooTube (S), Milk Visits (S/G), Ski Slope (S), Clock Tree (S), Family Tree (B), Cow Land (G), Directory Traversal (G), Cow at Large (G/P), Delegation (G), Bessie's Function (G), Promotion Counting (P), Bessie's Snow Cow (P)
- CF/AC/Other: Minimize the Diameter, Journey, Infected Tree, Distance in Tree, Tree Painting, Wizard's Tour; AC: Count Descendants, Distance Queries on a Tree, Subtree, Independent Set, Select Edges; DMOPC: Victor Takes Over Canada; POI 2014 Hotels; IOI 2009 Regions; APIO 2010 Patrol; CEOI 2020 Star Trek

### Dynamic programming (Ch 10–11)
- CSES: Dice Combinations, Minimizing Coins, Coin Combinations I, Coin Combinations II, Removing Digits, Grid Paths I, Book Shop, Array Description, Counting Towers, Edit Distance, Longest Common Subsequence, Rectangle Cutting, Minimal Grid Path, Money Sums, Removal Game, Two Sets II, Mountain Range, Increasing Subsequence, Increasing Subsequence II, Projects, Elevator Rides, Counting Tilings, Counting Numbers, Coding Company, Creating Offices
- USACO Gold: Hoof, Paper, Scissors, Time is Mooney, Teamwork, Snakes, Circular Barn Revisited, Taming the Herd, Drought, Moortal Cowmbat, Stamp Painting, Bovine Genetics, Interstellar Intervals, Fruit Feast, Talent Show, Bribing Friends, Cow Poetry, Exercise, Uddered but not Herd, Lights Off, Redistributing Gifts, Barn Painting, Delegation, Bessie's Function, Directory Traversal; USACO Platinum: Team Building, Moorio Kart, Cow at Large
- AC/Other: AtCoder DP Contest (Matching, Grouping, Independent Set, Subtree, Swap), IZhO 2014 Bank, Kattis Cat & Mice, CF Team Building, Mortal Kombat Tower, Increasing Frequency, Moving to the Capital, IOI Phidias, CEOI 2019 Amusement Park, IOI 2007 Training, POI 2004 Spies, POI 2008 Mafia, COI 2016 Torrent, APIO 2014 Beads and Wires

### Fenwick / segment tree / range structures (Ch 12)
- CSES: Static Range Sum Queries, Static Range Minimum Queries, Dynamic Range Sum Queries, Dynamic Range Minimum Queries, Range Xor Queries, Range Update Queries, Forest Queries II, Hotel Queries, List Removals, Salary Queries, Prefix Sum Queries, Pizzeria Queries, Range Interval Queries, Subarray Sum Queries, Subarray Sum Queries II, Distinct Values Queries, Distinct Values Queries II, Increasing Array Queries, Movie Festival Queries, Range Updates and Sums, Polynomial Queries, Range Queries and Copies, Missing Coin Sum Queries, Visible Buildings Queries
- USACO Gold: Haircut, Balanced Photo, Why Did the Cow Cross the Road III, Sleepy Cow Sorting; USACO Platinum: Why Did the Cow Cross the Road
- Kattis: Mega Inversions; CF: Irrigation; CSES Pyramid Array

### Amortized structures / static RMQ / sqrt (Ch 13)
- CSES: Nearest Smaller Values, Traffic Lights, Concert Tickets, Josephus Problem II, Subarray Squares, Sliding Window Median, Sliding Window Minimum, Sliding Window Cost, List Removals
- USACO: Convention II (S), Milk Measurement (S), Deforestation (S), Haybale Feast (G), Job Completion (G)
- CF/LC/Other: William and Robot, Survival of the Weakest (easy), Serval and Kaitenzushi Buffet, Bubble Sort Rounds II (CSES), Stick Division (CSES); LC: IPO; AC: Packing Under Range Regulations

### Number theory / combinatorics (Ch 14)
- CSES: Exponentiation, Exponentiation II, Counting Divisors, Common Divisors, Sum of Divisors, Divisor Analysis, Prime Multiples, Counting Coprime Pairs, Next Prime, Josephus Queries, Binomial Coefficients, Creating Strings II, Distributing Apples, Christmas Party, Permutation Order, Permutation Rounds, Bracket Sequences I, Bracket Sequences II, Counting Necklaces, Counting Grids, Fibonacci Numbers, Throwing Dice, Graph Paths I, Graph Paths II, System of Linear Equations, Sum of Four Squares, Triangle Number Sums
- USACO: (rare at this level) — CF used instead: Santa's Bot, Make it One, Round Subset; Gold: The Best Subsequence, Cow Poetry (counting)

### Strings (Ch 15)
- CSES: Word Combinations, String Matching, Finding Borders, Finding Periods, Minimal Rotation, Longest Palindrome, All Palindromes, Required Substring, Palindrome Queries, Finding Patterns, Counting Patterns, Pattern Positions, Distinct Substrings, Distinct Subsequences, Repeating Substring, String Functions, Inverse Suffix Array, String Transform, Substring Order I, Substring Order II, Substring Distribution
- USACO: Censoring (OB/S), Bovine Genomics (G), Lights Out (G)
- CF/Other: Check Transcription, Fullmetal Alchemist II, Three Occurrences, Liar, Hyperregular Bracket Strings; CEOI 2017 Palindromic Partitions; COCI 2017 Osmosmjerka, 2021 Sateliti, 2016 Zamjene; RMI 2017 Hangman 2; COI 2016 Palinilap; JOI Mergers

### Geometry (Ch 16)
- CSES: Point Location Test, Line Segment Intersection, Polygon Area, Point in Polygon, Polygon Lattice Points, Minimum Euclidean Distance, Convex Hull, Maximum Manhattan Distances, All Manhattan Distances, Intersection Points, Line Segments Trace I/II, Lines and Queries I/II, Area of Rectangles, Robot Path
- USACO: (geometry rare in USACO) — CF used instead per harvested lists

### Probability / games (Ch 17)
- CSES: Dice Probability, Moving Robots, Candy Lottery, Inversion Probability, Stick Game, Nim Game I, Nim Game II, Stair Game, Grundy's Game, Another Game, Raab Game I (intro), Josephus Queries (math)
- CF: tagged `probabilities` problems (n=268, median ≈2400 — flagged as 1900+ band)

### Strategy / capstone (Ch 18)
- CSES Interactive: Hidden Integer, Hidden Permutation, K-th Highest Score, Permuted Binary Strings, Colored Chairs, Inversion Sorting — used to discuss interactive problem types
- CSES Construction: Inverse Inversions, Monotone Subsequences, Third Permutation, Permutation Prime Sums, Chess Tournament, Distinct Sums Grid, Filling Trominos, Grid Path Construction — construction/ad-hoc appendix pool
- CSES Advanced (route-to-1900 pointers): Meet in the Middle, Hamming Distance, Reachable Nodes, Reachability Queries, Cut and Paste, Substring Reversals, Reversals and Sums, Eulerian Subgraphs, Monster Game I, Monster Game II, Houses and Schools, Knuth Division, Apples and Bananas, One Bit Positions, Signal Processing, Parcel Delivery, Task Assignment, Corner Subgrid Check/Count, Dynamic Connectivity
- Meet-in-middle specifically: CSES Meet in the Middle; CF Maximum Subsequence, Xor-Paths, Lizard Era: Beginning, Prime Gift; USACO Silver Robot Instructions; Kattis Playlist; YS Max Indep Set

## Codeforces rating bands per tag (computed 2026-10-10)

From `api/problemset.problems` (11,433 rated problems). For each tag: n = problems carrying the tag; p10/p25/p50/p75/p90 = rating percentiles. A tag's *typical entry band* for teaching purposes is its p10–p50 range — the ratings where problems actually tagged with the technique sit. Tags absent from the CF vocabulary (prefix sums, segment tree, fenwick tree) are noted.

| Tag | n | p10 | p25 | p50 | p75 | p90 |
|---|---|---|---|---|---|---|
| implementation | 3020 | 800 | 1000 | 1400 | 1900 | 2400 |
| math | 3483 | 800 | 1100 | 1700 | 2300 | 2800 |
| greedy | 3560 | 800 | 1200 | 1600 | 2100 | 2600 |
| brute force | 1987 | 800 | 1200 | 1700 | 2200 | 2700 |
| sortings | 1251 | 900 | 1200 | 1600 | 2100 | 2500 |
| strings | 809 | 800 | 1000 | 1600 | 2200 | 2700 |
| constructive algorithms | 2102 | 900 | 1200 | 1800 | 2300 | 2800 |
| number theory | 900 | 1000 | 1300 | 1900 | 2400 | 2900 |
| two pointers | 658 | 1200 | 1500 | 1900 | 2300 | 2600 |
| binary search | 1290 | 1300 | 1600 | 2000 | 2400 | 2900 |
| bitmasks | 711 | 1300 | 1700 | 2200 | 2600 | 2900 |
| dp | 2518 | 1400 | 1800 | 2200 | 2600 | 3000 |
| combinatorics | 839 | 1400 | 1900 | 2300 | 2700 | 3000 |
| ternary search | 69 | 1400 | 1800 | 2000 | 2200 | 2500 |
| games | 302 | 800 | 1300 | 1900 | 2500 | 3000 |
| geometry | 421 | 1100 | 1600 | 2200 | 2700 | 3100 |
| dfs and similar | 1071 | 1500 | 1800 | 2100 | 2500 | 2800 |
| dsu | 416 | 1500 | 1800 | 2200 | 2500 | 2800 |
| data structures | 2036 | 1500 | 1800 | 2300 | 2700 | 3100 |
| hashing | 237 | 1600 | 1900 | 2300 | 2600 | 3000 |
| graphs | 1208 | 1600 | 1900 | 2300 | 2600 | 3000 |
| shortest paths | 293 | 1600 | 1900 | 2200 | 2600 | 3000 |
| trees | 972 | 1700 | 2000 | 2400 | 2800 | 3200 |
| meet-in-the-middle | 51 | 1700 | 1900 | 2500 | 2900 | 3300 |
| probabilities | 268 | 1800 | 2100 | 2400 | 2800 | 3100 |
| divide and conquer | 364 | 1800 | 2200 | 2500 | 2800 | 3300 |
| flows | 160 | — | — | ≈2600 median | — | — |
| interactive | 311 | — | — | ≈2400 median | — | — |

Caveats recorded for the outline: (a) tags are community-applied — easy problems are frequently untagged even when the technique applies, so p25 reads high; (b) a Div2-B binary-search problem that is not tagged `binary search` is invisible in this table; (c) therefore the book's rating-by-topic map uses these quartiles *plus* the USACO Guide division structure, and is labelled as computed on 2026-10-10.
