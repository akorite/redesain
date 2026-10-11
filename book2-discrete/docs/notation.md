# Notation — Book 2 (discrete mathematics, proofs and olympiad)

| Symbol / macro | Meaning | First used |
|---|---|---|
| $P \Rightarrow Q$ / $P \Leftarrow Q$ | implication / is implied by | Ch.1 |
| $P \iff Q$ | if and only if | Ch.1 |
| $\land, \lor, \lnot$ | and, or, not (logic connectives) | Ch.1 |
| $\forall, \exists, \exists!$ | for all, there exists, there exists a unique | Ch.1 |
| $\square$ | end-of-proof marker (environment `proof` supplies it) | Ch.2 |
| "assume / want to show" | proof-template phrases: *Assume* hypothesis, *want to show* goal | Ch.2 |
| WLOG | without loss of generality — always justified inline | Ch.2 |
| $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}$ | number sets; $\mathbb{N}=\{1,2,3,\dots\}$ (positive integers, olympiad convention; stated explicitly at first use) | Ch.1 |
| $\mathbb{Z}^{+}, \mathbb{R}^{+}$ | positive integers / positive reals (when emphasis needed) | Ch.5, Ch.14 |
| $\in, \notin$ | set membership | Ch.4 |
| $\subseteq, \subsetneq$ | subset (possibly equal) / proper subset | Ch.4 |
| $\cup, \cap, \setminus, \overline{A}$ | union, intersection, difference, complement | Ch.4 |
| $\emptyset$ | empty set | Ch.4 |
| $A \times B$, $A^n$ | Cartesian product, n-fold product | Ch.4 |
| $\mathcal{P}(A)$ | power set | Ch.4 |
| $|A|$ | cardinality of a finite set | Ch.4 |
| $\aleph_0$ | cardinality of $\mathbb{N}$ (informal use only) | Ch.4 |
| $f : A \to B$ | function with domain $A$, codomain $B$ | Ch.4 |
| $f(A')$, $f^{-1}(B')$ | image of a subset / preimage of a subset | Ch.4 |
| $x \sim y$, $[x]$ | equivalence relation, equivalence class | Ch.4 |
| $a \mid b$, $a \nmid b$ | $a$ divides $b$ / does not (vertical bar, never a fraction) | Ch.5 |
| $\gcd(a,b)$, $\operatorname{lcm}(a,b)$ | greatest common divisor, least common multiple | Ch.5 |
| $v_p(n)$ | $p$-adic valuation (largest $k$ with $p^k \mid n$) | Ch.5 |
| $a \equiv b \pmod{m}$ | congruence modulo $m$ | Ch.6 |
| $\mathbb{Z}/m\mathbb{Z}$, $\mathbb{Z}_m$ | the residue system mod $m$ | Ch.6 |
| $a^{-1} \pmod{m}$ | multiplicative inverse mod $m$ | Ch.6 |
| $\varphi(n)$ | Euler's totient | Ch.7 |
| $\operatorname{ord}_m(a)$ | multiplicative order of $a$ mod $m$ | Ch.7 |
| $n!$, $n!!$ avoided | factorial; double factorial not used | Ch.8 |
| $P(n,k) = \frac{n!}{(n-k)!}$ | $k$-permutations of $n$ | Ch.8 |
| $\binom{n}{k}$ | binomial coefficient, "$n$ choose $k$" | Ch.8 |
| $[n]$ | the set $\{1,2,\dots,n\}$ | Ch.4 (used from Ch.8 on) |
| $D_n$ | derangement number | Ch.9 |
| $[x^n]\,F(x)$ | coefficient of $x^n$ in the generating function $F(x)$ | Ch.9 |
| $(a_0,a_1,\dots) \leftrightarrow A(x)$ | sequence ↔ its ordinary generating function | Ch.9 |
| $\Sigma_{\mathrm{sym}}$, $\Sigma_{\mathrm{cyc}}$ | symmetric / cyclic sums, written out in words at first use | Ch.13 |
| $[a_1,\dots,a_n] \succ [b_1,\dots,b_n]$ | majorization (Muirhead) | Ch.13 |
| $G=(V,E)$ | graph with vertex and edge sets | Ch.11 |
| $\deg(v)$ | degree of a vertex | Ch.11 |
| $K_n$, $K_{m,n}$, $C_n$, $P_n$ | complete, complete bipartite, cycle, path graphs | Ch.11 |
| $\chi(G)$ | chromatic number (basics only) | Ch.11 |
| $\Pr[E]$, $\Pr[E \mid F]$ | probability, conditional probability | Ch.12 |
| $\mathbb{E}[X]$, $\operatorname{Var}[X]$ | expectation, variance | Ch.12 |
| $\mathbf{1}_E$, $\mathbf{1}[P]$ | indicator random variable / Iverson-style indicator | Ch.12 |
| $\overline{E}$ | complement of an event (context disambiguates vs set complement) | Ch.12 |
| $\triangle ABC$ | triangle with vertices $A,B,C$ | Ch.15 |
| $\angle ABC$ | ordinary (undirected) angle | Ch.15 |
| $\measuredangle ABC$ | directed angle modulo $180^\circ$ (EGMO convention) | Ch.15 |
| $(ABC)$, $\omega$, $\Gamma$ | circle through $A,B,C$; generic circles | Ch.15 |
| $\operatorname{pow}(P,\omega)$ | power of point $P$ w.r.t. circle $\omega$ | Ch.15 |
| $\overline{XY}$, $|XY|$ or $XY$ | directed segment vs length — stated at first use | Ch.15 |
| $O, H, G, I, I_A$ | circumcenter, orthocenter, centroid, incenter, $A$-excenter | Ch.15 |
| $R, r$ | circumradius, inradius | Ch.15 |
| $[\,\cdot\,]$ area | $[ABC]$ = area of triangle $ABC$ | Ch.15 |
| $\mathcal{I}_{O,k}$ | inversion about center $O$ radius $k$ | Ch.16 |
| Contest cites | "AIME 2024 I P10", "AMC 12 2024 A P19", "USAJMO 2024 P1", "USAMO 2008 P1", "IMO 2026 P1" — year + paper + number; problems are *referenced*, never reproduced | Ch.1 onward |
| Exercise tags | `[easy]`, `[medium]`, `[hard]` printed in the margin of exercise environments | all chapters |
| Code checkpoints | "Predict before you run" boxes precede every printed output | all chapters |

## Macro conventions for LaTeX (used consistently across chapters)

- `\N,\Z,\Q,\R,\C` → $\mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ (define once in main.tex).
- `\divides`, `\ndivides` → $\mid$, $\nmid$.
- `\Mod{a}{m}` → $a \pmod{m}$; `\congruent{a}{b}{m}` → $a \equiv b \pmod{m}$.
- `\choosem{n}{k}` or plain `\binom{n}{k}`.
- `\coeff{n}{F}` → $[x^n]F(x)$.
- `\abs{S}` → $|S|$; `\floor{x}`, `\ceil{x}` (floor/ceiling: define on first use, Ch.3 exercises).
- `\dangle` → $\measuredangle$ (directed angle); `\pow{P}{\omega}`; `\area{ABC}` → $[ABC]$.
- Proof/technique names are written as plain words ("by induction", "by the extremal principle"), not symbols.
- Figures numbered per chapter; every figure has `\label` + one sentence caption stating what to notice.
