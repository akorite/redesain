# Review log
| Chapter | Author | Reviewer | Findings | Resolution |
|---|---|---|---|---|
# Review log — textbook-quant ch01–15 (depth-passed state, r3 pkg)

Independent reviewer: Devin (book-8 author session). Method: fresh make of whole book
(149pp), per-chapter contract counts, all 15 `code/test_NN.sh` suites executed under
pinned deps (numpy 2.0.2/pandas 2.3.3/statsmodels 0.14.6), all 55 non-YouTube FR URLs
fetched live, all 13 unique Watch videos verified via oEmbed + 4 duration spot-checks
(exact match), math spot-derivations (Kelly ladder, telescoping returns, funding
arithmetic, IL formula, Bonferroni bar). Reviewed as new work — no comparison to prior
reviews.

| chapter | verdict | blockers | nits | date |
|---|---|---|---|---|
| ch01 prices/returns/risk | REVISE | `test_01.sh` FAILS at step [6]: greps `excess kurtosis = +4.555`, chapter prints `+4.556`, live run today returns `+4.557` — three-way mismatch; `kraken_daily.py` ignores the pinned `data/btc_daily.csv` (README promises offline reproduction) and its fetch window (first 720 bars after 2024-01-01) is a different period than the pinned csv (2024-10→2026-10, kurtosis +1.974) so the pinned file cannot reproduce the printed number anyway | — | 2026-10-11 |
| ch02 time series/stationarity | ACCEPTED | — | none found (en-dash %-encoded Wikipedia URL verified 200) | 2026-10-11 |
| ch03 market structure/LOB | REVISE | — | verbatim overfull 89.8pt at ch03-quant.tex:329 (`faster fills are not free: they arrive exactly when informed flow is trading through you`) | 2026-10-11 |
| ch04 perps/funding | REVISE | — | verbatim overfulls at ch04:333 (5.8pt) and ch04:334 (191.8pt, ~24 chars too long) | 2026-10-11 |
| ch05 prediction markets | REVISE | — | verbatim overfull 41.8pt at ch05:284 (`vs orderbook: LMSR always quotes …`) | 2026-10-11 |
| ch06 AMMs/IL | REVISE | arithmetic error in exercise solution: `IL at r=1.3: 2√1.3/2.3−1 = −0.98%` — actual value −0.854%; conclusion net `+0.4%` should be `+0.5%` (direction unchanged) | verbatim overfull 173.8pt at ch06:253 | 2026-10-11 |
| ch07 data engineering | REVISE | — | verbatim overfull 185.8pt at ch07:278 (`bar calendars must be built from venue time …`) | 2026-10-11 |
| ch08 backtest harness | ACCEPTED | — | none found | 2026-10-11 |
| ch09 backtest lies | REVISE | Bonferroni example (ex:bonf): printed formula is two-sided `Φ⁻¹(1−α/(2N))` (→3.48 at N=100) but quoted bar is 3.29, the one-sided value — formula and number disagree | dead links ×2: alo.mit.edu Sharpe-Ratios PDF (line 445), cambridge.org HFT book URL (line 448) both 404 | 2026-10-11 |
| ch10 execution | REVISE | — | verbatim overfull 11.8pt at ch10:213; dead link: alo.mit.edu Sharpe PDF (line 349) | 2026-10-11 |
| ch11 walk-forward | ACCEPTED | — | none found | 2026-10-11 |
| ch12 evaluating a strategy | REVISE | — | dead link: wiley.com Hull product page (line 363) 404 | 2026-10-11 |
| ch13 Kelly sizing | ACCEPTED | — | none found (fraction-ladder growth rates verify exactly vs analytic G=p ln(1+f)+q ln(1−f)) | 2026-10-11 |
| ch14 risk | REVISE | — | dead link: wiley.com Hull product page (line 363) 404 | 2026-10-11 |
| ch15 writing it up | ACCEPTED | — | none found | 2026-10-11 |

## Verbatim fixes for every REVISE item

**ch01** — `code/kraken_daily.py`: add pinned-snapshot path consistent with README
promise. Write `data/kraken_daily_2024.csv` (the 2024-01-01→2024-10-23 window as the
API returns it today), then at top of `fetch()`:
```python
PINNED = os.path.join(os.path.dirname(__file__), "data", "kraken_daily_2024.csv")
if os.path.exists(PINNED):
    df = pd.read_csv(PINNED, parse_dates=["time"]); return df
```
Re-run once, capture the printed kurtosis (today: `+4.557`), set the chapter's printed
line to that value (ch01-quant.tex line ~297), and update `test_01.sh` line 26 grep to
match. Add one unverified.md row noting Kraken can revise historical prints (~±0.002).

**ch03** — ch03-quant.tex:329, shorten the verbatim line (verbatim cannot wrap):
`faster fills are not free: they land when informed flow trades through you` (75 chars)

**ch04** — two verbatim lines:
- :333 → `cross buys 15000 more room -- ALL collateral at risk, not just 2000`
- :334 → split into two lines:
  `cross risk: 2nd losing pos drains same pool -> both liq together`
  `          isolation caps loss at IM each`

**ch05** — ch05-quant.tex:284 → `vs orderbook: LMSR always quotes (depth=b); book depth vanishes when needed`

**ch06** — two fixes:
- exercise solution ~line 340: `IL at $r=1.3$: $2\sqrt{1.3}/2.3-1=-0.85\%$; net $+0.5\%$---yes, marginally.`
- verbatim line 253 → split:
  `uptime falls with width but each inside day earns a multiple:`
  `width = uptime x concentration`

**ch07** — verbatim line 278 → split:
`bar calendars must be built from venue time:`
`a 'daily' bar crossing DST is 23h or 25h twice a year`

**ch09** — two fixes:
- ex:bonf: make formula one-sided to match the quoted 3.29 (Sharpe bars are one-sided):
  `$\bar t_N=\Phi^{-1}(1-\alpha/N)$`
- dead links: line 445 replace with verified archive
  `\url{https://web.archive.org/web/2024/https://alo.mit.edu/wp-content/uploads/2017/06/The-Statistics-of-Sharpe-Ratios.pdf}`
  line 448 replace with ISBN-canonical `\url{https://www.cambridge.org/9781107091146}`

**ch10** — verbatim line 213 → `VWAP tracks volume; when vol and price spike together, it buys the top`
and dead link line 349: same archive.org replacement as ch09:445.

**ch12, ch14** — Hull FR item: product page is dead; cite the book without a URL
(`J.~Hull, \emph{Risk Management and Financial Institutions}, Wiley, 5th ed., ISBN 978-1-118-95594-9`)

## Checks that passed (record)

- Whole-book make: 149pp, 0 `!` errors, 0 undefined refs.
- Contract floors all 15 chapters: WEs 5–8, figures 6–8, exercises 18 each, FR items 6–8,
  Watch rulebox 1 (2 videos each).
- test_02–test_15: ALL PASS (14 suites; every chapter-printed number re-greps clean).
- Watch: all 13 unique video IDs resolve via oEmbed with correct title+channel;
  4 duration spot-checks exact (3630s, 628s, 1136s, 871s).
- Venue claims properly date-stamped (`accessed 2026-10-10/11`, `[unverified]` tags used
  honestly); unverified.md carries real rows.
- URLs: 47/55 verified 200/202 live; 4 dead (listed above); ~5 publisher pages return
  403-to-curl (bot-guards, e.g. princeton, tandfonline, wiley DOI) — recommend logging
  them in unverified.md rather than deleting.
