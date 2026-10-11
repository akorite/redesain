# Outline — Book 2: Discrete mathematics, proofs and olympiad (`textbook-discrete`)

**Status:** draft for approval. No chapter text written yet.
**Reader:** Grade-12, precalculus, no proof experience. **Outcomes:** writes clear proofs; AIME-level problems; basics for JMO-level work.
**Signature conventions (from the brief):** every worked example shows *strategy before the proof*; every chapter has a **Common mistakes** section; AMC/AIME problems are cited by year and number only (never reproduced); ≥1 Python/SymPy listing per chapter with a "predict before you run" checkpoint and its real output; every chapter ends its main text with a one-page summary table.

## Seed-topic coverage map (all mandatory topics are covered)

logic & quantifiers → Ch.1 · proof techniques → Ch.2 (+disproof) · induction → Ch.3 · sets, relations, functions → Ch.4 · divisibility & modular arithmetic → Ch.5, Ch.6 · CRT & Fermat–Euler → Ch.7 · counting & inclusion–exclusion → Ch.8, Ch.9 · generating functions → Ch.9 · recurrences → Ch.10 · graphs, trees, planarity → Ch.11 · probability on finite spaces → Ch.12 · inequalities (AM-GM, Cauchy–Schwarz, Muirhead) → Ch.13 · functional equations → Ch.14 · olympiad geometry (Ceva, Menelaus, power of a point, homothety, inversion) → Ch.15 (single merged chapter, approved 2026-10-10) · invariants & extremal arguments → Ch.16 · four-hour exam → Ch.17. Deliberate deviations from the seed order: (a) geometry is one merged chapter (Ch.15; the seed bundles four heavyweight topics and the approved merge keeps all five areas at reduced inversion depth — see the Chapter-15 note); (b) induction is taught *after* the general techniques chapter so induction appears as "just the template for ℕ", per Velleman and 6.042J; (c) sets/functions comes after the technique chapters, following Hammack (sets are needed as *material* for proofs, but the techniques themselves don't depend on relations); (d) pigeonhole is split — basic form inside counting (Ch.8), extremal/advanced inside invariants (Ch.16), matching Zeitz's three-tier pigeonhole.

## Page budget

Front matter (preface, how-to-use, notation) ~10 pp · Chapters 1–17 as listed · Back matter: hints ~8 pp, solutions (≥half of all exercises) ~10 pp, summary-of-proof-techniques table ~1 p, bibliography ~2 pp, index ~2 pp ≈ 23 pp. Chapter pages sum to ≈ 208 pp; **total ≈ 239 pp** (approved 2026-10-10 at ≤240 after the Ch.15+16 merge).

## Dependency order (teaching order; each chapter lists its own prerequisites)

Part I must precede everything; Part II and Part III are independent of each other (either order works); Part IV needs the chapter-level prereqs noted; Ch.17 is last. Within Part IV: light Ch.13→Ch.15 (Ptolemy’s inequality appears in §15.8), Ch.3+Ch.8→Ch.16.

---

# Part I — Proof craft (~48 pp)

## Chapter 1 — Logic and quantifiers (~11 pp)
**Prerequisites:** none (precalculus only).
**Sections:** 1.1 Statements and the connectives ∧, ∨, ¬ · 1.2 Truth tables · 1.3 Implication, converse, contrapositive, biconditional · 1.4 Quantifiers ∀, ∃ and order of quantifiers · 1.5 Negating statements mechanically · 1.6 Translating between English and symbols · 1.7 A first look at mathematical statements (parity, primes as running examples).
**Worked examples (strategy → solution):** (1) *Translating "every even integer >2 is a sum of two primes" into symbols and negating it* (strategy: outermost structure first, negate inward); (2) *Deciding truth of ∀x∃y vs ∃y∀x on a small relation table* (strategy: read ∃ as "produce a witness", ∀ as "be ready for anything"); (3) *Tarski-world style grid: evaluate four quantified claims on a 4×4 diagram* (strategy: small finite model before symbols).
**Figures:** (a) truth-table tree for (P∧Q)⇒R; (b) implication family portrait: converse/inverse/contrapositive diagram with truth arrows; (c) quantifier-order diagram: two axis interpretations of ∃y∀x vs ∀x∃y; (d) a 4×4 relation grid used in WE3.
**Code:** `verify_quantifiers.py` — brute-force check of ∀x∃y vs ∃y∀x over a finite relation; prints both verdicts. Checkpoint: predict the two verdicts first.
**Common mistakes:** asserting the converse; negating ∀∃ by flipping both quantifiers without moving ∃ after ∀; treating "or" as exclusive.
**Exercises:** inline ~4 ([easy] negate a quantified statement, [easy] truth table of a compound, [medium] find all n with a divisibility property, [medium] English→symbols for a contest-style sentence); additional 10: [easy]×4, [medium]×4, [hard]×2 (one: express "unique" ∃! purely with ∀∃ and prove the two readings agree).
**AMC/AIME cites:** 2024 AMC 12A P22 (constraint logic loop), 2024 AMC 12B P5 (sign-flip magnitude bounding).
**Sources:** Velleman ch.1–2 [4]; Hammack ch.2 [5]; 6.042J ch.3 [1]; Cut-the-Knot logic section [17].

## Chapter 2 — How to write a proof (~13 pp)
**Prerequisites:** Ch.1.
**Sections:** 2.1 What a proof is; axioms vs. proven tools · 2.2 Direct proof, with the proof-writing template (assume/show) · 2.3 Proof by cases · 2.4 Contrapositive · 2.5 Contradiction · 2.6 If and only if (two directions) · 2.7 Existence and uniqueness; constructive vs non-constructive · 2.8 Disproof and counterexamples · 2.9 Mathematical writing: sentences, displayed math, stating the claim first, naming objects · 2.10 Strategy before proof: how the book presents solutions.
**Worked examples:** (1) *Prove: if n² is even then n is even* — twice: direct attempt stalls, then contrapositive (strategy: the hypothesis has no handle on n — take the contrapositive to get one); (2) *Prove √2 is irrational* (strategy: contradiction — suppose the lowest-terms witness exists, then force a smaller one); (3) *Show that x²+x+41 is prime for x=0…39 — then find a counterexample* (strategy: disproof by counterexample; test the obvious boundary x=40,41); (4) *Prove: for integers a,b, a²−4b≠2* (strategy: work mod 4 — first "mod as a lens" example).
**Figures:** (a) proof-template box diagram (assume → derive → conclude); (b) decision flowchart "which technique fits the goal shape"; (c) the x²+x+41 counterexample timeline of near-misses; (d) annotated bad-vs-good solution paragraph (visual markup, our own example).
**Code:** `check_prime_run.py` — evaluate x²+x+41 for x=0…50, print first composite; predict-first checkpoint.
**Common mistakes:** proving the converse direction only in an iff; assuming what is to be proved (circular); a "proof" by examples; unfounded "clearly/obviously".
**Exercises:** inline ~5; additional 11: [easy]×4, [medium]×4, [hard]×3 (one: prove no integers x,y satisfy x²−4y=2 by two different methods and compare).
**AMC/AIME cites:** 2024 AMC 12B P14 (remainders), 2023 AMC 12A P3, 2010 AIME I P5, 2024 AMC 12A P6.
**Sources:** Velleman ch.3 + proof-technique summary [4]; Hammack ch.4–9 [5]; 6.042J ch.1–2 [1]; Chen *Remarks on English* [9]; OTIS Excerpts ch.1 [13]; Cut-the-Knot fallacies [17].

## Chapter 3 — Induction (~12 pp)
**Prerequisites:** Ch.1, Ch.2.
**Sections:** 3.1 The domino idea and the induction template · 3.2 Sums and formulas by induction · 3.3 Induction for inequalities · 3.4 Strong induction · 3.5 The well-ordering principle = induction in disguise (minimal counterexample) · 3.6 Structural examples: tilings, recurrences preview, "all horses the same color" fake proof · 3.7 Choosing what to induct on.
**Worked examples:** (1) *Σk= n(n+1)/2 by induction* (strategy: template first — write I.H. as a named claim); (2) *Every n≥12 is 3a+7b* by strong induction (strategy: a run of base cases because the step reaches back 3); (3) *L-shaped tromino tiling of a 2ⁿ×2ⁿ board missing one cell* (strategy: induct on n, cut the board in quarters and place one tromino at the center); (4) *Fake-proof autopsy: "all horses the same color"* (strategy: hunt the step where n=2 fails).
**Figures:** (a) domino/staircase schematic with labeled base and step; (b) tromino-tiling induction — the quartered board with the center tromino (step diagram, 4 panels); (c) induction vs strong-induction reach-back diagram; (d) fake-proof callout figure marking the failing link.
**Code:** `verify_tiling.py` — constructive tromino tiling for 8×8, prints ASCII tiling; predict-first.
**Common mistakes:** no base case / wrong base window; using the conclusion inside the inductive step; inducting on the wrong variable (dimension).
**Exercises:** inline ~4; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2024 AMC 12A P21 (recurrence evaluation), 2024 AMC 12B P18 (Fibonacci), 2021 AIME I P10 (rational recursion), 2025 AIME II P13 (rational sequence), 2023 AMC 12A P20 (array recurrence), 2023 AMC 12A P25.
**Sources:** 6.042J ch.5 (induction), ch.2 (WOP) [1]; Velleman ch.6 [4]; Hammack ch.10 [5]; Engel ch.8 [15]; Cut-the-Knot tromino puzzle [17].

## Chapter 4 — Sets, relations and functions (~12 pp)
**Prerequisites:** Ch.1–3.
**Sections:** 4.1 Sets, subsets, operations, Venn diagrams · 4.2 Power set and Cartesian product · 4.3 Functions: definition, domain, image · 4.4 Injective/surjective/bijective — with proof templates ("to prove f injective: suppose f(a)=f(b)…") · 4.5 Relations, equivalence relations, partitions · 4.6 Cardinality: finite counting by bijection; countability, Cantor's diagonal argument (light) · 4.7 The set [n] and indexing conventions used in this book.
**Worked examples:** (1) *Prove a composition of injections is injective* (strategy: chase the definitions one layer at a time); (2) *Show ℕ×ℕ is countable* (strategy: draw a snake through the grid — a picture argument made precise); (3) *Prove [0,1) is uncountable by diagonalization* (strategy: given any candidate list, manufacture the missing witness); (4) *Equivalence classes of "same parity" on ℤ* (strategy: verify reflexive/symmetric/transitive on the definition, then read the classes off the picture).
**Figures:** (a) injective/surjective/bijective arrow diagrams (3-panel small multiple); (b) ℕ×ℕ snake path; (c) diagonalization table with the constructed flip-digit row highlighted; (d) partition of ℤ into two equivalence classes; (e) Venn diagrams for identities (2- and 3-set).
**Code:** `diagonal_demo.py` — given a finite prefix list of decimals, produce a number absent from the list; predict-first.
**Common mistakes:** confusing ∈ with ⊆; proving f is a bijection by checking only one direction; "uncountable" confused with "infinite".
**Exercises:** inline ~5; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2024 AIME II P6, 2023 AIME II P11, 2022 AIME I P12, 2010 AIME I P7, 2023 AMC 12A P24.
**Sources:** Velleman ch.4–5,8 [4]; Hammack ch.1,11–12,14 [5]; 6.042J ch.4,8 [1]; Chen FuncEq-Intro (injective/surjective definitions) [11].

---

# Part II — Number theory (~35 pp)

## Chapter 5 — Divisibility and primes (~12 pp)
**Prerequisites:** Ch.2, Ch.3; notation from Ch.4.
**Sections:** 5.1 Divisibility a|b and the division algorithm · 5.2 gcd and the Euclidean algorithm · 5.3 Bezout's identity (and why the proof is an algorithm) · 5.4 Primes and the fundamental theorem of arithmetic · 5.5 Euclid's infinitude of primes · 5.6 Digit criteria and base representations · 5.7 Linear Diophantine equations.
**Worked examples:** (1) *Euclidean algorithm on (252, 198) then extended to Bezout* (strategy: run the algorithm forward, then read it backwards); (2) *Prove there are infinitely many primes* (strategy: contradiction — from any finite list build a number no listed prime divides); (3) *Find all solutions of 12x+18y=30* (strategy: gcd divides the constant ⇒ solutions exist; homogeneous part is periodic); (4) *Digit-sum criterion for 9 and 11 — prove both* (strategy: 10≡1 and 10≡−1; evaluates a polynomial at 10).
**Figures:** (a) Euclidean algorithm as repeated square/rectangle tiling of a 252×198 rectangle (the geometric proof of gcd); (b) divisibility poset diagram for 60; (c) base-b place-value diagram; (d) Sieve-of-Eratosthenes grid to 60 with primes struck in stages.
**Code:** `bezout.py` — extended Euclidean algorithm printing each step; verify 12x+18y=30 solutions. Predict-first.
**Common mistakes:** a|b read as a fraction; "prime" confused with "odd"; asserting gcd(a,b)=1 without checking it when a lemma needs it.
**Exercises:** inline ~5; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2025 AIME I P1, 2025 AIME I P5, 2024 AMC 12A P4, 2024 AMC 12A P9, 2024 AMC 12A P11, 2023 AMC 12A P3, 2021 AIME I P3, 2020 AIME I P4, 2021 AIME I P14, 2024 AIME II P7, 2018 AIME I P2, 2022 AIME I P2, 2020 AIME I P3, 2015 AIME I P8, 2015 AIME I P3, 2024 AMC 12B P21.
**Sources:** 6.042J ch.9 [1]; Velleman ch.7 [4]; Hammack (in proof chapters) [5]; Cut-the-Knot divisibility criteria [17]; Zhao modular-arithmetic handout listing [18].

## Chapter 6 — Modular arithmetic (~11 pp)
**Prerequisites:** Ch.5.
**Sections:** 6.1 Congruence a≡b (mod m) as an equivalence relation · 6.2 The residue system ℤ/mℤ; arithmetic rules · 6.3 Cancellation and multiplicative inverses · 6.4 Linear congruences · 6.5 Modular patterns: last digits, powers cycles, casting out nines · 6.6 Two moduli at once (preview of CRT).
**Worked examples:** (1) *Find the last two digits of 7^2026* (strategy: hunt the period of powers first, then reduce the exponent mod the period); (2) *Solve 14x≡6 (mod 20)* (strategy: gcd first — divide everything or declare no solutions); (3) *Prove n³−n is divisible by 6 for all n* (strategy: check the six residues — a finite case bash replacing induction); (4) *Calendar/day-of-week computation* (strategy: count in mod 7 with month offsets).
**Figures:** (a) clock-face residue circle mod 12 with step arrows; (b) power-cycle table for 7 mod 100 (spiral/cycle diagram); (c) multiplication table mod 5 vs mod 6 (units highlighted — why inverses exist only for gcd=1); (d) "same residue class" partition bar of ℤ mod 4.
**Code:** `powers_cycle.py` — print powers of a mod m until the cycle repeats; predict-first.
**Common mistakes:** dividing a congruence by a non-unit; confusing ≡ with = (writing x=3 (mod 5) inside algebra); forgetting that residues wrap (9 mod 4 = 1, so large-exponent shortcuts need the *period*, not the modulus).
**Exercises:** inline ~4; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2024 AMC 12B P14, 2020 AIME I P12, 2020 AIME I P11, 2020 AIME I P10, 2018 AIME I P11, 2010 AIME I P2, 2023 AIME II P15, 2024 AIME I P13, 2023 AIME I P7, 2025 AIME II P2.
**Sources:** 6.042J ch.9.6–9.9 [1]; Velleman ch.7.3–7.4 [4]; Hammack ch.5.2 [5]; CS70 note 5 [7]; Zhao modular arithmetic handout [18].

## Chapter 7 — CRT and Fermat–Euler (~12 pp)
**Prerequisites:** Ch.5, Ch.6; Ch.3 (induction for Fermat's little theorem); Ch.4 (function language for the totient).
**Sections:** 7.1 The Chinese remainder theorem — statement and the constructive proof · 7.2 Three ways to view CRT (construction, lifting, destruction — after Chen) · 7.3 Systems of congruences in practice · 7.4 Fermat's little theorem (two proofs: necklaces/cycles + induction) · 7.5 Euler's totient φ and Euler's theorem · 7.6 Orders mod p (gentle introduction) · 7.7 Wilson's theorem (enrichment) · 7.8 Applications: last digits again, check-digit schemes.
**Worked examples:** (1) *Solve x≡2 (3), x≡3 (5), x≡2 (7)* (strategy: satisfy one modulus, then "add multiples" to satisfy the next — construction view); (2) *Prove a^(p−1)≡1 mod p by the cycles-of-multiplication argument* (strategy: multiply the nonzero residues by a — a bijection — then match products); (3) *Find the last three digits of 3^400* (strategy: Euler reduces the exponent mod φ(1000)); (4) *USAMO-2008/1-style: show t²+t+1 has arbitrarily many prime divisors* (strategy: Euclid-style contradiction on a value-set, then CRT to assemble t).
**Figures:** (a) CRT alignment diagram — two rulers of lengths 3 and 5 sliding until residues line up; (b) multiplication-by-a permutation arrow diagram mod 7; (c) totient φ(n) chart for n≤36 (symmetry visible); (d) necklaces/beads picture for the FLT counting proof.
**Code:** `crt_solver.py` — brute-force and constructive CRT on small moduli, prints the unique solution mod M; predict-first.
**Common mistakes:** applying CRT when moduli aren't coprime (and not noticing the consistency check needed); using FLT as a^(p)≡1 (off-by-one exponent); computing φ by trial instead of the product formula.
**Exercises:** inline ~5; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2023 AIME I P7, 2025 AIME II P2, 2024 AIME I P13, 2020 AIME I P12, 2020 AIME I P11, 2010 AIME I P14, 2021 AIME I P7; olympiad-tier: 2024 USAJMO P3; USAMO 2008/1 (read in Chen's CRT handout — cite as "USAMO 2008 P1").
**Sources:** Chen CRT handout [10]; 6.042J ch.9.10 [1]; Velleman ch.7.4 [4]; CS70 note 6 [7]; Zhao modular arithmetic + aⁿ±1 handouts [18]; OTIS Excerpts [13].

---

# Part III — Counting, probability and graphs (~61 pp)

## Chapter 8 — Counting principles (~13 pp)
**Prerequisites:** Ch.1, Ch.4 (function/bijection language).
**Sections:** 8.1 Sum and product rules · 8.2 Permutations and factorials · 8.3 Binomial coefficients and Pascal's triangle · 8.4 The binomial theorem (proved two ways) · 8.5 Bijection = counting: counting in two ways · 8.6 Stars and bars (multisets) · 8.7 Basic pigeonhole principle · 8.8 Committee/identity proofs (combinatorial proof).
**Worked examples:** (1) *Prove Σ_k C(n,k)=2ⁿ by committee argument* (strategy: count the same object two ways — pick a subset by size vs by element decisions); (2) *Lattice paths on an m×n grid = C(m+n,m)* (strategy: bijection to words over {R,U}); (3) *Stars-and-bars: solutions of x₁+…+x₄=12 in nonnegative integers* (strategy: picture the bar positions, then count); (4) *Pigeonhole: among any 51 numbers from 1..100 two differ by a factor of 2* (strategy: partition into "largest odd divisor" classes).
**Figures:** (a) decision tree for the product rule; (b) Pascal triangle with the hockey-stick path highlighted; (c) lattice-path bijection picture; (d) stars-and-bars diagram; (e) pigeonhole partition diagram for the 51-numbers example.
**Code:** `count_check.py` — brute-force enumeration vs closed forms (paths, subsets, stars-bars); predict-first.
**Common mistakes:** multiplying where cases should be added (and vice versa); counting ordered when unordered is wanted (and fixing by "dividing by k!" wrongly); ignoring the "indistinguishable" clause.
**Exercises:** inline ~5; additional 12: [easy]×4, [medium]×5, [hard]×3.
**AMC/AIME cites:** 2025 AIME I P3, 2025 AIME I P10, 2025 AIME II P10, 2025 AIME II P11, 2024 AIME I P6, 2024 AIME II P3, 2024 AIME II P9, 2023 AIME I P11, 2023 AIME II P10, 2022 AIME I P6, 2021 AIME I P4, 2020 AIME I P5, 2020 AIME I P7, 2018 AIME I P9, 2018 AIME I P10, 2010 AIME I P10, 2024 AMC 12B P16, 2023 AMC 12A P13.
**Sources:** Hammack ch.3 [5]; 6.042J ch.15 (counting via bijection) [1]; CS70 counting notes [7]; Zhao bijections/counting-in-two-ways handouts [18]; Engel ch.5 [15].

## Chapter 9 — Inclusion–exclusion and generating functions (~12 pp)
**Prerequisites:** Ch.8; Ch.3 (induction for the PIE formula).
**Sections:** 9.1 Two and three sets, then the general PIE formula (proof by indicator functions) · 9.2 Derangements · 9.3 Surjections counted · 9.4 Euler's totient by PIE (bridge back to Ch.7) · 9.5 Ordinary generating functions: definition, coefficient extraction [xⁿ] · 9.6 The catalog of standard GFs and the convolution rule · 9.7 GF for counting (integer solutions with constraints) · 9.8 GF meets recurrences (bridge to Ch.10).
**Worked examples:** (1) *Derangement number D₄ by PIE* (strategy: count the complement — permutations fixing at least one specified set of points); (2) *φ(360) by PIE over prime divisors* (strategy: count coprimes by excluding each prime's multiples — same machinery as derangements, different pigeonholes); (3) *Number of ways to make 30 with coins of 5,10,25 via GF coefficients* (strategy: model each coin type as a geometric factor, then extract [x³⁰]); (4) *Indicator-function proof of PIE* (strategy: write membership as 0/1 functions and expand the product — "algebra as bookkeeping").
**Figures:** (a) 3-set Venn with ± labels showing the alternating correction; (b) PIE bar-stack diagram for derangements; (c) GF coefficient-extraction flowchart (factor → expand → read [xⁿ]); (d) coin-GF partial-product table.
**Code:** `gf_coin.py` — SymPy expands ∏1/(1−x^{c}) and prints [x³⁰]; also brute-forces the count for verification. Predict-first.
**Common mistakes:** stopping PIE at single sets (sign error); treating [xⁿ] notation as evaluation at xⁿ; multiplying GFs but reading the wrong coefficient index.
**Exercises:** inline ~4; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2024 AIME II P1, 2010 AIME I P7, 2022 AIME I P12, 2022 AIME I P13, 2015 AIME I P12, 2018 AIME I P12, 2023 AIME II P7, 2023 AIME II P11, 2023 AMC 12A P24, 2025 AIME II P8.
**Sources:** Hammack ch.3.7 [5]; Chen Summation handout (GF section, swap-of-order) [12]; 6.042J ch.15–16 [1]; Engel ch.5 [15]; CS70 combinatorial-proofs note [7].

## Chapter 10 — Recurrences (~10 pp)
**Prerequisites:** Ch.3, Ch.8, Ch.9 (GF for the GF-solution method).
**Sections:** 10.1 Recurrence vs closed form · 10.2 Guessing + induction · 10.3 Characteristic equations for linear homogeneous recurrences (order 1, 2) · 10.4 Fibonacci and friends; tilings counted by recurrence · 10.5 Solving by generating functions · 10.6 A feel for growth orders (divide-and-conquer preview, informal).
**Worked examples:** (1) *Tiling a 2×n strip with dominoes: set up and solve aₙ=aₙ₋₁+aₙ₋₂* (strategy: split on the last tile's shape, not the first); (2) *Towers of Hanoi Hₙ=2Hₙ₋₁+1 by "unwrap" then by induction* (strategy: compute four values, conjecture, then prove); (3) *Characteristic equation on aₙ=5aₙ₋₁−6aₙ₋₂* (strategy: try geometric ansatz — derive why rⁿ works); (4) *Derangement recurrence Dₙ=(n−1)(Dₙ₋₁+Dₙ₋₂) — proof of the recurrence* (strategy: classify by where element 1 lands).
**Figures:** (a) recursion tree for Hanoi (depth 4, call-count labels); (b) domino-tiling recurrence split diagram; (c) Fibonacci spiral-aside: growth-rate plot of consecutive ratios → golden ratio; (d) characteristic-equation decision diagram.
**Code:** `fib_closed.py` — iterate the recurrence vs evaluate Binet's formula with round-off warning; predict-first.
**Common mistakes:** off-by-one base cases; proving the closed form by plugging into itself (circularity); using the formula where the recurrence itself was the answer (e.g., "number of ways" asked, formula given — check integer-ness).
**Exercises:** inline ~4; additional 10: [easy]×4, [medium]×4, [hard]×2.
**AMC/AIME cites:** 2024 AMC 12A P21, 2024 AMC 12B P18, 2021 AIME I P10, 2025 AIME II P13, 2023 AMC 12A P20, 2023 AMC 12A P25, 2015 AIME I P9, 2023 AIME I P10.
**Sources:** 6.042J ch.22 [1]; Chen Summation §5 (GF for linear recurrences) [12]; Engel ch.9 [15]; Velleman ch.6.3 (recursion) [4].

## Chapter 11 — Graphs, trees and planarity (~12 pp)
**Prerequisites:** Ch.4 (relations), Ch.2.
**Sections:** 11.1 Graphs as relations; degrees and the handshake lemma · 11.2 Walks, paths, cycles, connectivity · 11.3 Bipartite graphs (odd-cycle characterization) · 11.4 Trees: n vertices ⇒ n−1 edges; spanning trees · 11.5 Eulerian trails and the Königsberg problem · 11.6 Planar graphs: Euler's formula V−E+F=2 and its corollaries (e≤3v−6; K₅, K₃,₃ nonplanar) · 11.7 Graph coloring basics.
**Worked examples:** (1) *Handshake lemma: in any party, an even number of people shook an odd number of hands* (strategy: count edge-ends two ways — the double-counting habit); (2) *Every tree on n vertices has n−1 edges by leaf-removal induction* (strategy: find the leaf first — the extremal object); (3) *K₃,₃ is nonplanar via Euler's formula + girth bound* (strategy: bound edges using shortest-cycle length, then contradict); (4) *Königsberg walk classification* (strategy: every intermediate visit consumes two edges — degree parity decides everything).
**Figures:** (a) handshake double-counting diagram (edge with two marked ends); (b) leaf-removal induction on a tree (3-step small multiple); (c) Königsberg schematic map → multigraph; (d) V−E+F worked on two planar embeddings; (e) K₅ and K₃,₃ with crossings marked.
**Code:** `euler_check.py` — networkx-free DFS connectivity + degree parity check on a random small graph; prints whether an Eulerian trail exists. Predict-first.
**Common mistakes:** confusing walk/path/cycle terms; using e≤3v−6 backwards (it's necessary, not sufficient — K₅ shows nonplanarity only via contradiction); assuming a graph is bipartite because it "looks" so.
**Exercises:** inline ~4; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2023 AMC 12A P21 (polyhedron distance = graph distance), 2024 AMC 12A P22 (loop constraints), 2018 AIME I P10 (bug on a wheel), 2018 AIME I P14 (frog sequences on a cycle graph), 2021 AIME I P12 (random walk on a polygon), 2024 AIME I P3 (game = path in state graph), 2023 AIME I P3 (arrangement constraints).
**Sources:** 6.042J ch.10–13 (walks, simple graphs, planar) [1]; CS70 graphs notes [7]; Engel ch.4 [15]; Cut-the-Knot games section [17].

## Chapter 12 — Probability on finite spaces (~12 pp)
**Prerequisites:** Ch.8; Ch.4 (functions = random variables).
**Sections:** 12.1 Sample spaces and uniform models · 12.2 Events, complement, "at least one" · 12.3 Conditional probability and tree diagrams · 12.4 Independence (and when it fails) · 12.5 Random variables and expectation · 12.6 Linearity of expectation — the flagship tool · 12.7 Geometric probability preview (areas instead of counts).
**Worked examples:** (1) *AIME-style conditional probability: prize given a prize-tier was hit* (strategy: define the event algebra first, then the four-step method — tree, compute, divide); (2) *Expected number of fixed points in a random permutation = 1* (strategy: linearity — indicator variables on each position, no independence needed); (3) *Birthday-paradox threshold via complement* (strategy: compute "all distinct" — the complement is a product); (4) *Simpson's-paradox table: two groups where each drug wins per-stratum but loses overall* (strategy: weighted sums on a 2×2×2 table — arithmetic, not opinion).
**Figures:** (a) probability tree for the two-stage draw; (b) fixed-points indicator table for n=4 (the 24-row table idea from Chen's Summation, drawn compactly); (c) Venn for "at least one" complement; (d) geometric-probability region plot (dartboard-style square with quarter-circle).
**Code:** `fixed_points.py` — Monte Carlo vs theory for E[fixed points], prints 10000-trial estimate and the exact 1; predict-first.
**Common mistakes:** assuming independence ("the events look unrelated"); adding probabilities where complements/multiplication apply; confusing P(A|B) with P(B|A) (the prosecutor's fallacy on a small table).
**Exercises:** inline ~5; additional 12: [easy]×4, [medium]×5, [hard]×3.
**AMC/AIME cites:** 2024 AIME I P4, 2024 AIME I P11, 2023 AIME I P1, 2023 AIME I P6, 2023 AIME II P6, 2021 AIME I P1, 2021 AIME I P12, 2020 AIME I P9, 2018 AIME I P3, 2018 AIME I P12, 2015 AIME I P2, 2015 AIME I P5, 2010 AIME I P1, 2010 AIME I P4, 2025 AIME II P7, 2023 AMC 12A P5, 2023 AMC 12A P17, 2024 AMC 12A P16, 2024 AMC 12A P20, 2024 AMC 12B P9, 2024 AMC 12B P17.
**Sources:** 6.042J ch.18–19 (four-step method, tree diagrams, linearity of expectation, Simpson's paradox) [1]; CS70 probability note sequence [7]; Chen *Expected Uses of Probability* (listing) [8]; Zhao probability-adjacent counting handouts [18].

---

# Part IV — Olympiad toolkit (~49 pp)

## Chapter 13 — Inequalities (~12 pp)
**Prerequisites:** Ch.2; algebra fluency.
**Sections:** 13.1 What's allowed: multiplying, flipping, transitivity — the algebra of < · 13.2 x²≥0 and (a−b)²≥0 as the root of everything · 13.3 AM-GM (proof by Cauchy's forward-backward induction) · 13.4 The power-mean chain · 13.5 Cauchy–Schwarz (proof + the Engel/Titu's-lemma form) · 13.6 Equality conditions — the part everyone skips · 13.7 Muirhead and Schur (statement, symmetric-sum notation, when to use) · 13.8 Strategy selection: homogenize, normalize, tangent line.
**Worked examples:** (1) *AM-GM for n=4 via (a−b)² algebra, then the n=2^k induction skeleton* (strategy: build the inequality from the only "free" fact, squares ≥0); (2) *Nesbitt's inequality (a/(b+c) cyclic ≥3/2) by Cauchy* (strategy: match denominators — the Engel form makes it a one-line application); (3) *Minimize x+1/x on x>0 with equality case* (strategy: guess equality x=1 first, then prove — equality case *guides* the proof); (4) *Schur's inequality derived, not stated* (strategy: expand Σ_sym x^3 and compare with the target).
**Figures:** (a) semicircle picture of AM-GM for n=2 (geometric mean vs arithmetic mean radii); (b) equality-case "touch" diagram for the tangent-line method; (c) power-mean ladder diagram QM≥AM≥GM≥HM; (d) Muirhead majorization diagram ([3,0,0] vs [2,1,0] bars).
**Code:** `ineq_scan.py` — Monte-Carlo check of Nesbitt and AM-GM on random triples + print the minimizer; predict-first.
**Common mistakes:** flipping < when multiplying by a possibly-negative quantity; asserting "the minimum is X" without exhibiting the equality case (the second half of every optimization proof); applying AM-GM where the equality case is unattainable.
**Exercises:** inline ~4; additional 11: [easy]×4, [medium]×4, [hard]×3.
**AMC/AIME cites:** 2024 AIME II P4, 2022 AIME I P15, 2022 AIME I P7, 2024 AMC 12B P13, 2010 AIME I P9, 2025 AIME II P15, 2024 AMC 12B P3, 2025 AIME I P14, 2023 AIME I P2.
**Sources:** OTIS Excerpts ch.2 (AM-GM, Muirhead, Schur, Ravi, Cauchy/Hölder, tangent-line, sharpness-vs-tractability) [13]; Chen Olympiad Inequalities + SOS handouts (listings) [8]; Engel ch.7 [15]; Velleman proof structure [4].

## Chapter 14 — Functional equations (~11 pp)
**Prerequisites:** Ch.2, Ch.4 (injectivity etc.), Ch.3 (induction over ℕ→ℤ→ℚ).
**Sections:** 14.1 What "solve over K" means; the two-directions discipline · 14.2 Guessing candidates (x, 0, kx, x+c, kx+c, polynomials) · 14.3 Substitution tactics: zeros, swapping, making terms collide · 14.4 Injectivity/surjectivity/involutions as milestones · 14.5 Cauchy's equation over ℚ (ℕ→ℤ→ℚ pipeline) and Jensen by shifting · 14.6 The pointwise trap and other named pitfalls · 14.7 Feeding back: verifying your answer is actually a solution.
**Worked examples:** (1) *Solve f(x+y)=f(x)+f(y) over ℚ* (strategy: candidate kx first; free parameter k=f(1); induction to ℤ then ℚ); (2) *Kyrgyzstan-2012-style equation with an involution* (strategy: plug x=u to expose f(f(y))=y → bijection → substitute x=f(t)); (3) *Jensen's equation by the shift g=f−f(0)* (strategy: normalize to kill the constant family); (4) *Pointwise-trap autopsy: if f(t)=±t for each t, why isn't the proof done* (strategy: exhibit the gap — sign may vary by point; kill it by plugging mixed a,b).
**Figures:** (a) substitution-tactics decision flowchart; (b) ℕ→ℤ→ℚ→ℝ domain-expansion staircase for Cauchy; (c) pointwise-trap counterexample sketch (piecewise ±x); (d) involution-as-bijection arrow diagram.
**Code:** `fe_search.py` — brute-force verify f(x)=kx is the only degree-≤2 polynomial solution of a toy FE on a grid; predict-first.
**Common mistakes:** solving "find all" but never verifying the candidates; proving f(t)=±t pointwise and claiming a global sign; plugging in values that generate only tautologies (0=0) and concluding nothing.
**Exercises:** inline ~4; additional 10: [easy]×4, [medium]×4, [hard]×2.
**AMC/AIME cites:** 2023 AMC 12A P22, 2023 AMC 12A P25, 2015 AIME I P10, 2010 AIME I P6, 2024 AIME I P12; olympiad-tier: 2024 USAJMO P5, JMO 2015 P4, USAMO 2002 (last two read inside Chen's FuncEq-Intro), IMO 2026 P5.
**Sources:** Chen FuncEq-Intro (the backbone: candidates → substitutions → involution → Cauchy) [11]; OTIS Excerpts ch.3 [13]; Engel ch.11 [15].

## Chapter 15 — Olympiad geometry (~22 pp)
**Prerequisites:** Ch.2; school geometry (angles, similarity) — the chapter rebuilds what it needs as lemmas. Complex-number basics stated where used.
**Sections:** 15.1 Angle chasing systematically (with directed angles as the upgrade) · 15.2 Cyclic quadrilaterals — the 50% lemma of olympiad geometry · 15.3 The incenter/excenter lemma (first "configuration" taught) · 15.4 Power of a point, radical axis and radical center · 15.5 Ceva and Menelaus (with directed lengths); the extended law of sines · 15.6 Homothety and spiral similarity (the nine-point circle as homothety image) · 15.7 Inversion in a circle: definition, image table, one worked transformation · 15.8 Analytic backup plans: coordinates, areas, trigonometry, Ptolemy's inequality; choosing synthetic vs analytic.
**Worked examples:** (1) *Angle-chase: show a constructed line is tangent* (strategy: chase backwards from the tangent criterion — reverse angle chase); (2) *Incenter/excenter lemma: midpoint-of-arc equidistant from B, I, C, I_A* (strategy: every relevant angle equals half the base angle — coincidences are configurations); (3) *Power of a point: AIME-style length computation with two secants* (strategy: pick the circle first, then the point); (4) *Ceva: prove medians concurrent, then a nontrivial Ceva ratio chase* (strategy: write the product in directed form and identify each factor); (5) *Nine-point circle exists: homothety at H with ratio ½ maps the circumcircle to it* (strategy: find the dilation — existence becomes a corollary); (6) *An AIME-style problem solved both synthetically and by coordinates, side by side* (strategy: compare costs — when does the algebra win?).
**Figures:** (a) directed-angle notation diagram (mod-180° convention); (b) cyclic-quadrilateral angle-equality picture; (c) incenter/excenter configuration (labeled arc-midpoint); (d) power-of-a-point three-case figure (interior/exterior/tangent); (e) Ceva and Menelaus side-by-side with directed-segment arrows; (f) radical-axis construction for two disjoint circles; (g) nine-point circle homothety figure with H, O, G marked; (h) inversion image table diagram.
**Code:** `power_check.py` — coordinates: place a triangle + cevian, compute PA·PB and PT² numerically to verify equality; `invert.py` — numeric inversion of a point set about a circle, plots pre/post images (matplotlib); predict-first for both.
**Common mistakes:** angle-chasing with unsigned angles and landing on the supplementary case (the EGMO-errata mistake); applying Ceva/Menelaus to unsigned ratios; assuming three points define the needed circle without checking concyclicity; inverting about the wrong center (the circle of inversion is a choice — usually a concurrency or tangency point); forgetting inversion reverses orientation; writing analytic coordinates without fixing scale/orientation first.
**Exercises:** inline ~6; additional 12: [easy]×4, [medium]×5, [hard]×3 (inversion problems skew hard; a full inversion problem set lives in the Notes for readers who want more).
**AMC/AIME cites:** 2024 AIME I P10, 2020 AIME I P15, 2024 AIME I P5, 2023 AIME I P5, 2023 AIME II P12, 2023 AIME II P9, 2021 AIME I P11, 2020 AIME I P1, 2018 AIME I P4, 2024 AIME I P8, 2022 AIME I P8, 2021 AIME I P13, 2018 AIME I P15, 2023 AIME I P8, 2025 AIME II P5/P6, 2025 AIME II P1, 2018 AIME I P13, 2015 AIME I P11, 2024 AMC 12A P19; JMO: 2024 USAJMO P1, 2023 USAJMO P2, 2024 USAJMO P6, 2023 USAJMO P6.
**Sources:** EGMO TOC + errata (order of topics; the "configurations" idea; directed angles early) [6]; Chen directed-angles + incenter/excenter + barycentric/complex handouts (listings) [8]; Zhao cyclic-quadrilaterals + power-of-a-point + big-picture handouts [18]; Yufei Zhao "Three Lemmas" (listing) [18]; Engel ch.12 [15].
**Chapter-15 note (approved merge):** formed by merging the former Ch.15+16 (user decision 4, 2026-10-10). Inversion is taught at depth ~1.5 sections — enough to recognise and deploy the standard transformation; a full second geometry chapter was traded for the ≤240 pp budget. The dropped depth is routed in the Notes to Zhao's and Chen's free geometry handouts.

## Chapter 16 — Invariants, monovariants and extremal arguments (~12 pp)
**Prerequisites:** Ch.3, Ch.8; light Ch.11 (game graphs).
**Sections:** 16.1 Invariants: quantities that don't change · 16.2 Monovariants: quantities that only move one way (termination) · 16.3 The extremal principle (take the minimal counterexample / largest element) · 16.4 Advanced pigeonhole (averages and the generalized form) · 16.5 Coloring and parity arguments · 16.6 Games: winning positions, strategy stealing, pairing.
**Worked examples:** (1) *Invariant: the chocolate-bar breaking problem (pieces always cost exactly n−1 breaks)* (strategy: find what each move preserves — count components, not cuts); (2) *Monovariant: numbers on a circle replaced by differences — termination* (strategy: exhibit a nonnegative integer measure that strictly drops); (3) *Extremal: every finite set of points has a closest pair* used inside a proof (strategy: the minimum exists because the set is finite — name the witness); (4) *Pairing strategy: second-player-symmetric games* (strategy: mirror across the center — strategy stealing turns the opponent's move into yours); (5) *Coloring: can a 10×10 board minus two opposite corners be tiled by dominoes?* (strategy: each domino covers one of each color — count colors).
**Figures:** (a) chocolate-bar component-count diagram (3-step small multiple); (b) monovariant descent plot; (c) extremal "take the minimum" diagram; (d) checkerboard coloring for the domino impossibility; (e) pairing-strategy symmetric board; (f) Nim-position game tree on the take-away game.
**Code:** `invariant_sim.py` — simulate the circle-difference process; prints the invariant/monovariant each step; predict-first.
**Common mistakes:** calling something an invariant without checking every legal move; using extremal principle on an infinite set ("take the least n" needs well-ordering); assuming a strategy exists from a draw argument (who moves first decides).
**Exercises:** inline ~4; additional 12: [easy]×4, [medium]×5, [hard]×3.
**AMC/AIME cites:** 2024 AIME I P3, 2023 AIME I P14, 2021 AIME I P10, 2024 AMC 12B P5, 2024 AMC 12A P22, 2010 AIME I P12, 2022 AIME I P9, 2025 AIME II P3, 2023 AIME II P11; JMO/IMO: 2024 USAJMO P2, 2024 USAJMO P4, 2023 USAJMO P3, 2023 USAJMO P4, 2023 USAJMO P5, IMO 2026 P1, IMO 2026 P3, IMO 2026 P4.
**Sources:** Engel ch.1–4,14 (invariance, coloring, extremal, box, games) [15]; 6.042J ch.6 (state machines/invariants) [1]; Cut-the-Knot games index [17]; Zeitz TOC (extreme principle, pigeonhole tiers, invariants) [16]; CS70 stable-matching note (invariant argument style) [7].

---

# Part V — Craft (~11 pp)

## Chapter 17 — Writing a four-hour exam + the proof portfolio (~11 pp)
**Prerequisites:** the whole book; placed last.
**Sections:** 17.1 What a timed contest tests vs what homework tests · 17.2 The four-hour budget: triage, first pass vs deep work, when to abandon · 17.3 Write-up standards: claim first, named lemmas, displayed math, diagrams, checking conventions · 17.4 Partial credit: what graders can and cannot reward; "fake-solving" and why it loses · 17.5 Checking your work in the last 30 minutes · 17.6 The 20-proof portfolio: how to build it, rubric for self-assessment, revision loop.
**Worked examples:** (1) *A worked write-up: one JMO-level problem shown as (a) scratch reasoning, (b) final submission text* (strategy: the artifact on paper is a different document from the thinking); (2) *A bad write-up autopsy with margin commentary* (strategy: grade a deliberately flawed solution — find the fake-solve); (3) *A timed-plan table: 15 problems/3 hours vs 6 proofs/4.5 hours — two budgets compared* (strategy: allocate by point value × probability of completion).
**Figures:** (a) time-budget Gantt-style strip for a 4-hour olympiad; (b) annotated side-by-side bad/good write-up page images (our own text, marked up); (c) portfolio rubric table; (d) the "strategy → skeleton → details" write-up pipeline diagram.
**Code:** `portfolio_check.py` — checklist validator that scans the reader's proof .tex files for required elements (claim statement, lemma names, QED); predict-first (toy script, honest about being a linter not a grader).
**Common mistakes:** writing the solution in the order it was discovered (discovery order ≠ proof order); omitting the "verify candidates" half of find-all problems; spending 90 minutes polishing problem 1 while problems 4–6 are blank.
**Exercises:** inline ~3; additional 10: [easy]×3, [medium]×4, [hard]×3 (timed rewrites of earlier chapter solutions).
**Cites:** write-up case studies on problems already cited (2024 AIME I P10 geometry; 2021 AIME I P10 invariant; 2024 USAJMO P1).
**Sources:** Chen *Remarks on English* (the core reference — grading, fake-solve, checking, detail level) [9]; OTIS Excerpts ch.1 + walkthrough format [13]; USAMO 2003 rubric (listed on olympiad.html) [8]; Hammack §5.3 mathematical writing [5]; Velleman proof-technique summary [4].

## The capstone (built across the book, assembled at the end)

**Where it lives:** each chapter's worked examples and hard exercises are written in the final proof style; the *portfolio itself* is a `portfolio/` directory in this repository (approved decision 4): a `portfolio/template.tex` plus `portfolio/proof-01.tex`…`proof-20.tex` stubs the reader completes himself, LaTeX-typeset and self-graded on the rubric; Ch.17 explains how to build it.

**The 20 proofs (working list — the reader writes all 20):** (1) √2 irrational (Ch.2) · (2) n³−n divisible by 6 (Ch.6) · (3) Σk formula by induction (Ch.3) · (4) tromino tiling exists (Ch.3) · (5) Euclid's infinitude of primes (Ch.5) · (6) Bezout/extended-Euclidean correctness (Ch.5) · (7) FTA uniqueness (Ch.5) · (8) Fermat's little theorem by residue-multiplication (Ch.7) · (9) CRT existence+uniqueness (Ch.7) · (10) ΣC(n,k)=2ⁿ two ways (Ch.8) · (11) hockey-stick identity (Ch.8) · (12) PIE general formula by indicator functions (Ch.9) · (13) derangement formula (Ch.9) · (14) Binet form for Fibonacci by induction or GF (Ch.10) · (15) handshake lemma (Ch.11) · (16) tree has n−1 edges (Ch.11) · (17) Euler's V−E+F (Ch.11) · (18) linearity of expectation (Ch.12) · (19) AM-GM by Cauchy induction (Ch.13) · (20) Ceva's theorem (Ch.15).

The stubs ship in `portfolio/` with the template and rubric; the repository also carries `portfolio_check.py` in `code/`.

**≥5 original solutions to olympiad-style problems (the reader writes these from scratch; six assigned so any five count):** (a) 2024 USAJMO P1 (prove PQRS cyclic — accessible geometry) · (b) 2023 USAJMO P1 (find-all triples — two-directions discipline) · (c) 2024 USAJMO P2 (rectangle-tiling configurations — invariant/extremal) · (d) 2023 USAJMO P5 (board game — strategy/invariant) · (e) IMO 2026 P1 (gcd/lcm moves — invariant + termination) · (f) 2024 USAJMO P4 (grid game — extremal/strategy). All six verified against the real statements read this session.

## Exercise and figure totals

- Inline exercises ≈ 75 (avg ~4/chapter) + additional exercises 187 across 17 chapters (≥10 each, all [easy]/[medium]/[hard]-tagged) — exceeds the ≥10/chapter minimum.
- Planned figures ≈ 85 (avg ~4.7/chapter, most in geometry Ch.15) — all TikZ/pgfplots or Python-generated, each with a named source file.
- Code listings: 17 chapters × 1–2 named listings (Python 3 + SymPy/matplotlib for the inversion plot), each with a predict-first checkpoint and real output.
- "Common mistakes": 2–4 items × 17 chapters, seeded by EGMO errata, OTIS ch.1, Chen's English handout, and the classic beginner errors catalogued in sources.md.
- Named contest citations: ~250 AMC/AIME problems + ~15 JMO/IMO/USAMO ids distributed across chapters (full pool in sources.md).

## Sources (numbering matches docs/sources.md)

[1] MIT 6.042J mcs.pdf · [2] MIT OCW 6.042J course page · [3] — · [4] Velleman frontmatter/TOC · [5] Hammack Book of Proof · [6] EGMO AMS TOC + geombook page · [7] CS70 course/notes index · [8] Chen olympiad.html handout index (+ AGEST/errata where noted) · [9] Chen Remarks on English · [10] Chen CRT handout · [11] Chen FuncEq-Intro · [12] Chen Summation · [13] Chen OTIS Excerpts · [14] CS103 · [15] Engel Problem-Solving Strategies (Springer TOC) · [16] Zeitz Art and Craft of Problem Solving (Wiley TOC) · [17] Cut-the-Knot · [18] Yufei Zhao olympiad page + handout listings · [19] imo-official.org · [20] AoPS wiki archives (index + per-year pages read) · [21] CMU 15-251 page.
