# Review log
| Chapter | Author | Reviewer | Findings | Resolution |
|---|---|---|---|---|
| ch05-07 | author A | integrator (build+tests rerun, spot grep of fixes) | bne decoded from wrong bit; combinational loop in regfile bypass; ch06 naive pipe printed x; ch07 f30 never assigned; several wrong solutions | RESOLVED in code; tests PASS; independent content review PENDING |
| ch08-11 | author B | integrator (as above) | ch10 cache sim used addr/log2(B) so all old miss counts wrong; unfair timing harness; ch08 UART claims; ch11 PTE address | RESOLVED; numbers replaced with recomputed ones; independent review PENDING |
| ch12-15 | author C | integrator (as above) | ch12 pipeline fork count; ch13 lr.d in RV32; ch13 partition counter optimised away; ch14 random-read explanation wrong; ch15 page fault 0.7ms vs 744ns | RESOLVED; independent review PENDING |
| ch16-18 | author D | integrator (as above) | ch18 '14 operations' underived; stray-zero is final OUT not JNZ; ch16_soa.c uninitialised; ch17 linear-probe solution | RESOLVED; independent review PENDING |
| ch14 | coordinator | integrator | fsync ~60x -> ~115x (6722 MB/s vs 4KB/0.07ms = 58 MB/s) | RESOLVED, recomputed |

Note: the above 'integrator' entries are NOT the independent re-review the handoff requires before tagging book7-systems-v0.1. All new numbers are Linux x86_64 container measurements, noisy (10-30%); Mac numbers kept and labelled. Videos untouched by this branch.
