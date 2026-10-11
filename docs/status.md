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

## Book 7 — Systems & CPU (`book7-systems`)
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
