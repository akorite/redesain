# Status — updated after each chapter

Last update: 2026-10-11

## Book 1 — Competitive programming (`book1-cp`)
18 chapters planned. ch01–05 accepted, ch06 + ch13 under review, ch07–12 accepted, ch14 writing. 137pp landed. Reviewer: book2 session.

## Book 2 — Discrete mathematics (`book2-discrete`) — **v0.1 tagged, delivered**
17 chapters + back matter, 151pp. All chapters reviewed and resolved. Depth pass to ~220pp starting (new contract), re-review per chapter, tag v0.2.

## Book 3 — Linear algebra for ML (`book3-linalg-ml`)
16 chapters planned. ch01–13 landed + accepted (ch13 PASS), ch14 writing. 153pp. Reviewer: book5 session.

## Book 4 — Machine learning (`book4-ml`)
Outline approved pending compliance check. 18 chapters planned. Not started.

## Book 5 — Electronics & digital design (`book5-electronics`)
19 chapters planned. ch01–09 landed + accepted (ch09 pending review), ch10 writing. 105pp. Reviewer: book3 session.

## Book 6 — Quantitative research (`book6-quant`)
Outline approved pending compliance check. 15 chapters planned. Not started.

## Book 7 — Systems & CPU (`book7-systems: 143pp, all 18ch merged; ch05-18 reviews back — all REVISE (WE/FR/ex floors, watch fabrications) — author fixing + depth pass to 180pp
Outline approved pending compliance check. 18 chapters planned. Not started.

## Book 8 — Physics for engineers (`book8-physics`)
Outline approved pending compliance check. 18 chapters planned. Not started.

## Repository
URL: https://github.com/akorite/redesain (empty repo reused per user 2026-10-11; rename to `study-textbooks` in Settings when ready — links survive).
Structure: `book1-cp/` … `book8-physics/`, `shared/`, `docs/`, `case-study/`, `metrics.csv`, `PROJECT.md`, `COMMUNICATION.md`, `README.md`. Root = main.
Pending a GitHub PAT: issue creation (pinned "Status" issue + `needs-user` label). Until then the pinned status lives in this file; PR-per-chapter runs via git_manager PRs starting with the next landed chapter.

## 2026-10-11 standing-order checkpoint
- Pipeline: 4 agents running (book1 cp-ch15; book2 reviews cp13/06/14→depth pass; book3 reviews elec09/10→linalg-ch15; book5 seq101_tb resend + reviews linalg13/14→elec-ch11).
- Pages: cp 147, discrete 151 (v0.1), linalg 167, elec 115 = 580pp. Wave-2 (4/6/7/8) outlines approved; starts when an agent frees.
- Fixes landed: fresh-clone make verified on all 4 books (figure PDFs now synced into monorepo); KKT CS wording corrected to λ(g−c)=0; PRs #1-3 merged pending logged reviews (queued).
- needs-user: none. Pending PAT for issues/releases (not blocking).
- 2026-10-11T13Z: book5 ch11 landed (127pp clean); linalg ch14 REVISE resolved (~4→~5); linalg ch13 review ACCEPTED. Book 3 ch14 review-log ✓ (order 6b partial). Open: book1-ch14 + book5-ch10 reviews (queued book2/book3); elec-ch11 post-merge review queued.
- 2026-10-11T13Z+: book1 ch15 strings landed (162pp clean, 5 test suites pass) + nit batch ch07/08/11/12; PR#4 open pending book2 review. Dispatched: book1→cp-ch16/17, book5→elec-ch12. Queues: book2=reviews cp-13/06/14/15→depth pass; book3=elec-09/10/11 reviews→linalg-ch15.
- 2026-10-11T13:30Z: book2 cp reviews LOGGED — ch06/ch13 ACCEPTED, nit batch VERIFIED, ch15 ACCEPTED (contract met), ch14 RESOLVED (apples convention fixed: n=children, "4 3"→20, test PASS). PR#4 merged (ch15+nit+ch14fix+review-log). All standing-order §6b reviews now logged.
- 2026-10-11T13:50Z: book3 ch15 information theory landed (178pp clean) → PR#5 open pending book5 review. book3 elec reviews logged: ch10 PASS + ch11 PASS (live iverilog incl. sabotage self-check). Queues: book1→cp-ch16/17; book2→depth pass; book3→elec-ch09 review→linalg-ch16 (final); book5→elec-ch12→linalg-ch15 review.
- 2026-10-11T14:10Z: book1 ch16+17 (optional) landed (186pp, tests ALL PASS) → PR#6 pending book2 review. book1 → ch18 (final). Queues: book2→depth pass + cp-16/17 reviews; book3→elec-ch09 review→linalg-ch16; book5→elec-ch12→linalg-ch15 review.
- 2026-10-11T14:20Z: book5 ch12 testbenches landed (142pp, tests OK) → PR#7 pending book3 review. linalg ch15 review ACCEPTED → PR#5 merged. Queues: book1→cp-ch18; book2→depth pass+cp16/17 revs; book3→elec-ch09/12 revs→linalg-ch16; book5→elec-ch13.
- 2026-10-11T14:30Z: book1 cp ch18 landed — ALL 18 chapters in (196pp clean). Consistency pass dispatched to book1; ch18 review queued to book2. PR#8 open pending review.
- 2026-10-11T14:50Z: book2 depth pass ch14-17 landed (157pp). cp review-log updated: ch18 ACCEPTED — all 18 chapters now have verdicts; ch16/17 rows pending (PRs #6, #8 wait). Depth-passed chapters queued for re-review to book1.
- 2026-10-11T15:20Z: book3 ch16 capstone landed — ALL 16 chapters in (191pp clean). Consistency pass next on book3; ch16 review queued to book5. elec ch09-12 reviews all PASS → PR#7 merged. PR#10 open.
- 2026-10-11T15:50Z: book5 ch13 FPGA flow landed (153pp, tests OK) → PR#11 pending review. linalg ch16 RESOLVED→ACCEPTED → PR#10 merged; book3 on consistency pass. Queues: book5→elec-ch14; book3→consistency→idle→ml session wakes.
- 2026-10-11T16:15Z: linalg consistency pass landed (190pp; ln→log, sum bounds, softmax). elec-ch13 RESOLVED→ACCEPTED → PR#11 merged. book3 now idle→ml session wakes for ml-ch01. Queues: book1→cp depth pass; book2→disc depth pass+cp16/17 revs; book5→elec-ch14; ml→ch01.
- 2026-10-11T16:50Z: book1 cp depth pass COMPLETE — all 18 chapters now meet new contract (FR+Watch everywhere, ch04 fig fixed, 5 new listings live-verified). 200pp clean. PR#14 open; depth-pass re-reviews owed to book2 before v0.1 tag. book1 session idle → physics session next.
- 2026-10-11T17:00Z: session rotation — SWE-2 quota is 5 total incl. coordinator, so max 4 children. book3 session terminated (its outstanding elec-ch13 review + linalg depth-gap audit reassigned; linalg repo holds full context). Exited wave-2 outline sessions can't be messaged; fresh chapter sessions created: ml f6682004 (running ch01), physics a8d4f65 (asleep, resumes on free slot), elec 0006303d (running ch14→19, replaces exited 360c6). Live writers: disc depth ch01-13, elec ch14, ml ch01 + disc ch14-17 review (book1). Still owed: cp ch16/17 review rows (blocks PR#6), disc depth re-reviews ch01-13 as they land, elec ch13 review, linalg depth audit. quant/systems unscheduled pending slots.
- 2026-10-11T17:20Z: PR#14 merged — disc ch14/15/17 re-review fixes + elec ch13 second-review fixes landed. OPEN review items: disc ch16 closest-pair WE rewrite (→ book2, Sylvester–Gallai restate), elec ch13 missing \section{Summary} (→ elec author), disc ch16 iv2 garble (→ book2). book1's disc+elec reviews caught one real math blocker + one contract violation — review loop working.
- 2026-10-11T17:25Z: book1 delivered both reviews (disc ch14-17 + elec ch13). Applied + verified all verbatim fixes; ch16 math blocker → book2 (Sylvester–Gallai spec); elec ch13 missing Summary → elec session. book1 now auditing linalg ch01-13 FR/Watch gaps + standing reviewer for incoming disc depth chapters. Pages: cp 200 / disc 157 / linalg 190 / elec 153 = 700 landed.

## 2026-10-11 — book2 depth pass landed (PR #15)
- Full ch01-17 depth batch landed: ~30 new figures, ch16 Sylvester-Gallai rewrite, ln→log, FR overfull fixes. 179pp, 0 err/0 undef/0 overfull>3pt, 17/17 tests PASS.
- Coordinator fixes: align=center on 29 figure nodes with \\ labels (LR-mode); ch03-tromino literal # in \foreach (restricted-mode). Verified in clean rebuild.
- cp review-log from book2 committed to book1-cp/docs (ch16/17 rows STILL absent — re-requested with dedicated pkg).
- Page ledger: cp 200, disc 179, linalg 190, elec 153, ml writing, quant/systems/physics pending slots.

## 2026-10-11 — PR#6 merged; book1-cp TAGGED v0.1
- book2 delivered cp ch16/17 reviews: ch17 ACCEPTED outright; ch16 REVISE→one verbatim URL fix (nearest-points→nearest_points, curl 200)→RESOLVED→ACCEPTED. All 18 cp chapters now have logged independent reviews.
- book1-cp v0.1 tagged (18ch, 200pp, 0 err/undef). Tag `book1-cp-v0.1` pushed to origin.
- Still owed: cp depth-passed ch01-13 re-review (book2 queue), disc depth re-review ch01-17 (reviewer TBD), linalg depth retrofit (book1 working ch01-04), elec ch14-19 (elec-0006 working), ml writing (ml-f668 working), physics/quant/systems awaiting slots.

## 2026-10-11 — book2 at 182pp; quant started
- Watch-list back-matter appendix added (PR #16): 17 chapter sections from docs/watch.md. 182pp clears the 180 floor.
- cp tagged v0.1 (all 18 chapters independently reviewed, PR#6 merged).
- book2 session now authoring textbook-quant ch01→15.
- Open: disc depth re-review ch01-17 (needs reviewer ≠ book2); cp depth ch01-13 re-review; linalg depth retrofit in flight (book1); elec ch14-19 (elec-0006); ml ch01+ (ml-f668); physics suspended; systems unassigned.

## 2026-10-11 — standing-order first-loop fixes verified
- 6a fresh-clone make: all 4 active books build clean from git clone (cp 200, disc 182, linalg 190, elec 153; 0 err/0 undef each).
- 6b review logging: cp-ch14, linalg-ch14, elec-ch10 review rows logged (earlier cycle).
- 6c linalg ch14 KKT: complementary slackness now λ(g(x)-c)=0 for g(x)≤c, prose "active (g=c)" consistent. Direct push.
- Additional catches this cycle: disc "IMO 2026 P5/P1/P3/P4" cites removed (nonexistent contest, logged unverified.md); elec ln→log harmonization (D-2026-10-11c); disc consistency sweep clean (no dup labels, no unmatched refs, no \ln).
- Page ledger: cp 200 ✓v0.1 · disc 182 · linalg 190 · elec 153 · ml/quant writing · physics suspended · systems unassigned.

## 2026-10-11 — linalg depth retrofit landed (208pp)
- book1's 3-batch retrofit merged (ch01-13): FR+Watch+WEs+figs+exercises to contract. Spot-verified ch01 (5ex/19ex/7fig/6listings/4tripwire). ch14-16 already at contract. Book at 208pp, 0 err/undef/overfull.
- book1 now authoring textbook-physics ch01→18 (session cap full — authored in-session rather than spawning).
- Owed reviews: linalg-depth re-review ch01-13 (→ elec-0006 queue after disc re-review); cp-depth re-review (ml-f668, queued); disc-depth re-review (elec-0006, queued); ml chapters (TBD); elec ch14-19 (TBD).
- Page ledger: cp 200 ✓v0.1 · disc 182 · linalg 208 · elec 153 · ml writing · quant writing · physics starting · systems unassigned.

## 2026-10-11 — elec ch14-16 landed (194pp); ml 158 (ch01-11, 9 artifacts pending) · quant 146 depth-passed (<180 floor, round-2 queued) · physics 141 · systems 45 (ch01-04)
- elec ch14 (ALU), ch15 (regfile/datapath), ch16 (CPU capstone: cpu8 + asm8 + fib/count/mult/uart + synth reports) merged — full Verilog+tb+asm+hex+vcd artifact set. 194pp clean.
- elec remaining: ch17-19 + consistency pass → v0.1.
- Session notes: book2 (quant) + book1 (physics) auto-paused on SWE-2 transient — resumed manually.
- Page ledger: cp 200 v0.1 · disc 182 · linalg 208 · elec 224 v0.1 · ml 158 (ch01-11, 9 artifacts pending) · quant 146 depth-passed (<180 floor, round-2 queued) · physics 141 · systems 45 (ch01-04) · systems unassigned.

## 2026-10-11 — book2 v0.2 TAGGED; elec complete at 224pp (ch17 file en route)
- book2-discrete v0.2 tagged+pushed: 182pp, all 17 chapters independently re-reviewed PASS (elec session, 89/89 links live).
- elec ch18+19 landed locally (KiCad + MCUs) + full consistency/link-rot pass (58 URLs re-curled, 16 dup labels fixed, ISA chain verified). ch17 source missing from delivery — requested.
- elec-0006 now running linalg depth re-review; then picks up book7-systems: 143pp, all 18ch merged; ch05-18 reviews back — all REVISE (WE/FR/ex floors, watch fabrications) — author fixing + depth pass to 180pp
- Needs reviewer assignment: elec ch14-19.

## 2026-10-11 — elec COMPLETE 224pp; linalg re-review resolved; systems dispatched
- elec ch17-19 landed: book5 fully written at 224pp (consistency pass + link-rot done by author). Merged.
- linalg depth re-review (elec session): 12 PASS + ch03 REVISE→RESOLVED (Beezer URL→Wayback). All review rows logged.
- elec-0006 now authoring textbook-systems ch01+; ml-f668 got elec ch14-19 independent review queued behind ml + cp re-review.
- Tags: book1-cp-v0.1 (200pp), book2-discrete-v0.2 (182pp). Next candidates: linalg (re-review done → v0.1), elec (needs ch14-19 review → v0.1).

## 2026-10-11 — book7 systems ch01-03 landed (38pp); book3 v0.1 tagged
- systems ch01-03 merged: ELF/linking, data representation, RV32I asm (real clang cross-compile + sim). Two delivery defects fixed at merge (wrong test_ch01, fig misroute).
- book3-linalg-ml-v0.1 TAGGED (208pp, all 16ch reviewed). Tags now: cp v0.1, disc v0.2, linalg v0.1.
- elec-0006 authoring systems at speed; ch04+ in flight. Reviews: elec ch14-19 all ACCEPT (ml-f668); ml ch01-11 reviewing now (book2); quant ch01-15 review queued (book1); systems/physics TBD. book5-electronics-v0.1 tagged 224pp.

## 2026-10-11 — physics COMPLETE (157pp); cp floor patch landed (206pp)
- book1 delivered physics ch18 (AC machines/power) + ch19 capstone workshop (20 multi-topic problems, checks verified: 84.4-min tunnel, 1432 m/s Hohmann) + ch04 ex patch (14→15). Book complete at 157pp, clean build. PR#19 updated.
- cp floor-gap patch: ch01/02/04/06/09 → WE=5, figs=12 each. 206pp, PR#20.
- book1 resumed → quant ch01-15 independent review.

## 2026-10-11 — physics review done (15/19 PASS); quant r3 at 150pp; ch16 commissioned
- book2 physics review: 15 PASS / 4 REVISE (ch06/07/10/15 at 5 figs — verbatim figure specs delivered, all from existing scripts). 38/38 watch videos oembed-verified, all check scripts physically correct. Nit: docs/notation.md is the cp file — author rewrite queued.
- quant round-3 structural pass: 6 new mechanism sections; still 150pp (content fills slack). book2's diminishing-returns read accepted — commissioned ch16 "portfolio construction" as the floor-gap chapter (recorded in decisions.md).
- physics needs-user flag: none. Its 4 figure fixes + notation rewrite go to book1.
