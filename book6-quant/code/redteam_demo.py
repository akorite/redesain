# attack list applied to a candidate result (the SMA chapter's numbers)
attacks = [
 ("lookahead?",   "signal uses close_i, fill open_i+1  PASS"),
 ("costs?",       "5bp fee + 2bp slip modeled          PASS"),
 ("n trials?",    "1 window pair, no search            PASS"),
 ("regime?",      "OOS fold -0.52 in quiet regime      FLAG: gate on vol"),
 ("capacity?",    "BTC liquid; footprint <<1% ADV      PASS"),
]
for a,r in attacks: print(f"  {a:14s} {r}")
print("4 pass / 1 flag -- the flag is the research, not the failure")
