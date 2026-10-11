# Notation

Conventions for `textbook-cp`. Chapters must use these names for these concepts; anything else needs a local definition before use.

## Complexity and order of growth

| Symbol / macro | Meaning | First used |
|---|---|---|
| \(O(f)\), \(\Theta(f)\), \(\Omega(f)\) | asymptotic upper / tight / lower bounds, defined with limits and quantifiers in Ch 1 | Ch 1 |
| \(o(f)\), \(\omega(f)\) | strictly smaller / larger growth, named only | Ch 1 |
| \(\tilde{O}(f)\) | suppresses logarithmic factors (rare; flagged informal) | Ch 13 |
| \(n, m, q, k, T, C, N\) | problem sizes: array length / edges / queries / parameter / test cases / capacity / upper bound respectively | Ch 1 |
| \(10^9+7\), \(998244353\) | the two standard contest primes; written `MOD` in code | Ch 14 |

## Sets, sequences, functions

| Symbol / macro | Meaning | First used |
|---|---|---|
| \([l,r]\), \([l,r)\) | closed and half-open integer ranges; half-open is the convention inside code (matching C++ iterators) | Ch 4 |
| \(a_i\), \(a[l..r]\) | array element / subarray | Ch 5 |
| \(P[i] = \sum_{j\le i} a_j\) | prefix sum array; \(P[0] = 0\) by convention | Ch 5 |
| \(D[i] = a_i - a_{i-1}\) | difference array; \(a = \mathrm{prefix}(D)\) | Ch 5 |
| \(\binom{n}{k}\), \(n!\), \(\mathrm{C}(n,k)\) | binomial coefficient; code uses `ncr(n,k)` | Ch 14 |
| \(C_n\) | \(n\)-th Catalan number | Ch 14 |
| \(\gcd, \mathrm{lcm}\) | greatest common divisor / least common multiple | Ch 14 |
| \(a \bmod m\), \(a \equiv b \pmod m\) | remainder / congruence | Ch 14 |
| \(\varphi(n)\) | Euler's totient (named; not taught) | Ch 14 |
| \(\pi(s)\), \(z[i]\) | prefix-function values / Z-function values (bold-face convention: arrays named after the function) | Ch 15 |
| \(\operatorname{mex}(S)\) | smallest nonnegative integer absent from \(S\) | Ch 17 |
| \(\Pr[A]\), \(\mathbb{E}[X]\) | probability of event \(A\) / expectation of \(X\); indicators \(1_A\) | Ch 17 (shared with Books 3/4/6) |
| \(p\), \(q\) | generic primes / probabilities; context disambiguates | Ch 14, 17 |

## Graphs

| Symbol / macro | Meaning | First used |
|---|---|---|
| \(G = (V, E)\), \(n = |V|\), \(m = |E|\) | a graph, its vertex and edge counts | Ch 7 |
| \(u, v, w\) | vertices; \(s, t\) source and target | Ch 7 |
| `adj[v]`, `adj[u].push_back({v, w})` | adjacency list; weighted edges as pairs | Ch 7 |
| `dist[v]`, `parent[v]`, `visited[v]` | BFS/DFS state arrays, 1-indexed to match problems | Ch 7 |
| DAG | directed acyclic graph | Ch 7 |
| `tin[v]`, `tout[v]`, `timer` | Euler-tour entry/exit times | Ch 10 |
| `up[v][k]` | the \(2^k\)-th ancestor of \(v\) (binary lifting) | Ch 10 |
| \(\operatorname{lca}(u,v)\) | lowest common ancestor | Ch 10 |
| \(d(u,v)\) | graph distance; `dist()` in code | Ch 8 |

## Data structures

| Symbol / macro | Meaning | First used |
|---|---|---|
| `find(x)`, `unite(a,b)`, `same(a,b)` | DSU operations (never `union` in code — reserved word) | Ch 9 |
| `par[]`, `sz[]` | DSU parent and component-size arrays | Ch 9 |
| `lowbit(i) = i & -i` | Fenwick index step | Ch 13 |
| `bit[]` | Fenwick internal array | Ch 13 |
| `seg[]`, `lazy[]` | segment-tree value and deferred-tag arrays | Ch 13 |
| monoid \((S, \oplus, e)\) | associative operation + identity framing segment-tree generality | Ch 13 |
| `lg[x] = floor(log2 x)` | precomputed floor-log table (sparse table, LCA) | Ch 6, 10 |

## Dynamic programming

| Symbol / macro | Meaning | First used |
|---|---|---|
| `dp[...]` | the DP table; index order = evaluation order | Ch 11 |
| state | the tuple of parameters identifying a subproblem; always named and defined before the recurrence | Ch 11 |
| transition | the recurrence; written as min/max/sum over choices | Ch 11 |
| `mask`, `popcount(mask)` | subset bitmasks; `__builtin_popcount` in code | Ch 12 |
| `tight`, `lead` | digit-DP flags (still-bound-by-prefix / no-digit-yet) | Ch 12 |

## Problem and technique naming

| Convention | Meaning | First used |
|---|---|---|
| `CSES <name>` | problem from the CSES problem set, cited by exact list name (e.g. CSES *Array Division*) | Ch 1 |
| `USACO-<B\|S\|G\|P>` | USACO problem by division (Bronze/Silver/Gold/Platinum); `O` prefix = old division era (e.g. USACO-G *Closing the Farm*) | Ch 1 |
| `CF <name>` | Codeforces problem by common name; contest index added in bibliography where ambiguous | Ch 3 |
| `AC`, `Kattis`, `IOI`, `POI`, `Baltic OI`, `CEOI`, `JOI`, `APIO`, `IZhO`, `COCI`, `DMOPC`, `YS`, `LC`, `SPOJ`, `NOI`, `CF EDU` | other archives, cited the same way | Ch 2+ |
| `[easy]` `[medium]` `[hard]` | exercise difficulty tags; `[route]` marks problems above the book's 1600 target (they belong to the 1900 route) | Ch 1 |
| WE c.n | worked example n of chapter c | global |
| F c.n / L c.n | figure / code listing n of chapter c | global |

## Code conventions

| Convention | Meaning | First used |
|---|---|---|
| `C++17`, `-std=c++17 -O2 -Wall -Wextra` | language and compile flags; pinned in `code/README.md` | Ch 1 |
| `using ll = long long;` | 64-bit signed integer alias; used whenever overflow is possible | Ch 1 |
| `const int MOD = 1e9+7;` | modulus constant | Ch 14 |
| `rep(i,a,b)`, `all(x)` | the only two macros the book allows; defined and justified in Ch 1 | Ch 1 |
| `ios::sync_with_stdio(false); cin.tie(nullptr);` | fast-I/O preamble | Ch 1 |
| 1-indexed arrays | to match problem statements; arrays sized \(n+1\) | Ch 1 |
| `INF = 4e18` / `INT_MAX` guards | the overflow-safe infinity convention | Ch 8 |
| `modint` | modular-arithmetic value type (add/sub/mul/div/pow) | Ch 14 |
| `first_true(lo,hi,pred)` | the book's binary-search signature | Ch 4 |
| `find`, `unite` | DSU names (see above) | Ch 9 |
| recursive DFS only where depth is safe | recursion-depth tripwire at \(n \ge 10^5\): prefer explicit stack | Ch 7 |
| `#include <bits/stdc++.h>` | allowed; flagged as contest-only practice | Ch 1 |

## Shared with other books

The probability/expectation and combinatorics conventions above are offered to `notation-shared.md` (see structured output `shared_notation_proposals`): \(\Pr[\cdot]\), \(\mathbb{E}[\cdot]\), indicator \(1_A\), \(\binom{n}{k}\), factorial notation, \(O/\Theta/\Omega\) definitions, and the `dp`-style state-name convention.
