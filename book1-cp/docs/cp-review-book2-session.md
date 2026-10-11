# CP book reviews — book2 session (devin-136b…), 2026-10-11

Reviewed against pkg `345258fc` (fresh, contains ch15 + nit batch).
Version check: ch13/ch06/ch14/ch07 byte-identical (md5) to previously
reviewed files — earlier verdicts stand. ch08/ch11/ch12 carry the
nit-batch edits; diffs verified below. ch15 is a first review.

## cp-ch13 Fenwick & segment trees — PASS (unchanged)
Same md5 as reviewed copy. Verdict from earlier review stands:
5/5 fixed on genuine samples + 400 stress genuine. Nit (unchanged):
`lazyseg.h` compiles but is never exercised — no solver includes it,
no test drives it, not among listed listings. Add a driver or drop it.

## cp-ch06 Amortised structures — PASS (unchanged)
Same md5. 5/5 fixed + 1,200 stress verified earlier. Nits (unchanged):
`sqrt_sum` demo has no stdin-driven check; 14 exercises; style drift
(older baseline).

## cp-ch14 Number theory & combinatorics — REVISE verdict stands
Same md5 — the `distributing_apples` convention fix has NOT landed in
this pkg (nit batch touched ch07/08/11/12 only). Blocker from earlier
review still applies: solver/fig/test compute C(n+m−1,m−1) apples-first,
real CSES 1716 is n=children → sample "4 3" must be 20, not 15.
Verbatim fix list already sent (choose(n+m−1,n−1) everywhere).

## Nit-batch diffs verified (ch08/ch11/ch12)
- ch08: new WE High Score (Bellman–Ford negated + two-sided cycle
  reachability) with 3 fixed checks incl. a blocked-cycle case; the
  previously-flagged invented "ticket-crossing" cowroad statement was
  replaced by the real USACO eating-third-field statement with official
  sample N=4,T=2→31. Both changes look correct and tested
  (high_score stress 150/150 exists in test_ch08.sh).
- ch11: take-table reconstruction line "1 3" now printed in the WE
  output (my earlier nit — Book Shop reconstruction not surfaced).
- ch12: counting_numbers restated as the real CSES 1213 (no two
  adjacent digits equal, a=123 b=321 → 171) replacing the invented
  distinct-digit variant. Solver/test updated to match.

## cp-ch15 Strings: KMP/Z/rolling-hash/trie — PASS (nits only)
First review under the new contract.
- Structure: 6 sections, 6 WEs (collide/words/match/borders/periods/
  rotation), 6 figures (fig72–77), 15 additional exercises (5e/5m/5h),
  Common mistakes (5), summary table, FR (8 items), Watch (3).
- New contract verified: 6 WEs ≥5 ✓; 6 figs ✓; 15 additional ≥15 ✓;
  FR all 8 URLs opened → 200 ✓; Watch all 3 confirmed via YouTube
  oembed — Abdul Bari "9.1 KMP" (V5-7GzOfADQ), "9.2 Rabin-Karp"
  (qQ8vS2btsxI), UC Davis/Gusfield Z-algorithm (MFK0WYeVEag) ✓.
- test_ch15.sh: 6/6 fixed + 200 rounds × 5 stress checks ALL PASS.
- Hand-verified outputs: "pp" in "saippuakauppias" → 2 (both KMP and Z
  agree, printed "2 2"); borders "abcababcab" → "2 5"; periods
  "abcabca" → "3 6 7"; word_combinations "ababc"/{ab,abab,c,cb} → 2;
  minimal_rotation "acab" → "abac"; hash_demo finds a real
  deterministic mod-97 collision ("aaa","adt"→24) and shows the same
  pair separates under 1e9+7/998244353, plus an 8192-string birthday
  demo (5 collisions under 9726647, 0 under the RH pair).
- Compile: book 159pp, 0 `^!`, 0 overfull >3pt, 0 undefined refs.

Nits:
1. `string_matching` prints "2 2" (KMP count + Z count on one line);
   CSES 1753 expects a single count. Text honestly flags it ("for the
   official problem, print either") — same acceptable pattern as the
   coin_combos note in ch11; keep the flag.
2. word_combinations stress dedupes the word list (`list({...})`) but
   the solver counts `cnt` multiplicities — consistent only because
   CSES words are distinct. Harmless; a one-line comment would help.
3. `periods` relies on k↔n−k border correspondence stated in the code
   comment; the claim is correct but the text could name it (n−k is a
   period iff k is a border).
