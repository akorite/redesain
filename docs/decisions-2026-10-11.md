
## Decisions — 2026-10-11 (supersedes earlier rules where they conflict)

1. Page limits: floor 180, target 220–320, ceiling 350 pages. Cut repetition only — never figures, code outputs, worked examples, or Common mistakes.
2. Chapter depth floor: ≥5 worked examples, ≥6 figures in visual topics, ≥15 additional exercises, code with real captured output. No filler.
3. Every chapter needs `\section*{Further reading}` (5–10 annotated items: author, title, URL or ISBN, level, one-line why) and a `rulebox` "Watch instead" (1–3 videos/playlist: title, channel, length, matching sections, access date, best first).
4. Video rule: only link videos actually opened and verified (title, channel, duration, content match). Prefer official university channels/course playlists/well-known educators (MIT OCW, Stanford, Harvard, 3Blue1Brown, Khan Academy, Computerphile, Ben Eater). Never invent a URL. Failures → [unverified] + docs/unverified.md. Note notation differences. Re-check all links at release (link-rot pass, date-stamped).
5. Per-book docs/watch.md + back-matter "Watch list" appendix ordered by chapter.
6. Wave-2 outlines (books 4, 6, 7, 8) approved pending reviewer compliance check; deviations recorded here.
7. Autonomy: no waiting between chapters/books. Stop and ask only for money/accounts/personal data, licence questions, irreversible actions, self-contradicting briefs, or 3 failed attempts on the same problem. Unanswered after 48h → recommended default applies, recorded.
8. GitHub: ONE private repo `akorite/study-textbooks` — `book1-cp/ … book8-physics/`, `shared/` (lifeos.sty, notation-shared.md, template), `docs/` (decisions.md, status.md), PROJECT.md, COMMUNICATION.md, README.md. PR per chapter (reviewer checklist + findings in description, merge after pass). Pinned "Status" issue. `needs-user` labelled issues w/ options + recommendation + 48h default. Tag vX.Y per book + main.pdf on releases. No secrets, no personal data, no private Life OS content.
9. The build is a portfolio/Substack project: PROJECT.md (pipeline, architecture, risks, AI-use statement), metrics.csv per chapter, case-study/lessons.md growing with each review, one-page retrospective per finished book.
10. Book 2 depth pass: 151pp → ~220pp across all 17 chapters (more WEs/figs/exercises + further reading + watch), re-review every changed chapter, tag v0.2.
- elec-ch11 merged to main BEFORE review logged (coordinator error vs standing order §3); review dispatched to book3 post-merge; fixes land as follow-up commits.
