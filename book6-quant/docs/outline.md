# Outline (to be approved by the user before any chapter is written)

**Book 6 — Quantitative research and markets** (`textbook-quant`). Reader: Grade-12 student, fluent
Python, probability/statistics at Book 3 level. Length target ≈ **228 pages** (range 150–250).
Every method is demonstrated first on **synthetic data where the true answer is known**; real venue
mechanics are taught second, from public documentation, every venue-rule statement **date-stamped and
marked `\textbf{[unverified]}`** with a re-check date. Nothing in the book is investment advice.

**Book 3 dependencies** are cited by chapter *title* (numbering fixed once Book 3's approved outline
lands): "probability and random variables", "statistics, MLE and Bayesian inference", "optimisation,
convexity and Lagrange multipliers", "SVD and PCA".

**Disclaimer convention:** the preface carries a standing box "This book teaches research methods and
market mechanics; nothing here is investment, legal or tax advice. Venue rules change — every such
claim is date-stamped and must be re-verified before use." A short form of the same box reappears at
the start of ch4, ch13 and ch14. No chapter recommends or discourages any real trade.

**Notation:** per `docs/notation.md`; the shared Books-3/4/6 file is reused verbatim.

---

## Part I — The objects of study (chapters 1–2, ~28 pp)

### Ch1 — Prices, returns and risk (~14 pp)
*Prerequisites:* Python; Book 3 "probability and random variables", "statistics, MLE and Bayesian
inference". *Outcome:* compute and reason about returns, volatility and tail shape; know the
simple-vs-log distinction cold.

- §1.1 What a price series is (ticks, bars, sampling; what a candle hides)
- §1.2 Simple returns \(R_t\) and log returns \(r_t\) — the telescoping identity
- §1.3 Volatility and its estimators (close-to-close, range-based, EWMA)
- §1.4 The shape of returns: moments, heavy tails, QQ plots
- §1.5 Dependence: autocorrelation of returns vs. of \(|r_t|\)
- §1.6 Risk as a number (drawdown; a preview of VaR/ES, formal in ch14)
- Summary sheet · Common mistakes · Notes

*Worked examples:* **WE1** synthetic GBM — simple vs log returns, telescoping check;
**WE2** regime-switching volatility (known \(\sigma\) path) — compare three estimators;
**WE3** real BTC daily series (Kraken public endpoint) — QQ plot vs normal.
*Figures (5):* level→returns panel; simple-vs-log difference curve; QQ plot synthetic fat tail vs
normal; ACF of \(r_t\) vs \(|r_t|\) on synthetic GARCH; annotated equity drawdown.
*Listings (4):* `kraken_daily.py` fetch to DataFrame; `returns.py` simple/log + annualisation;
`vol_estimators.py`; `acf_panel.py`.
*Synthetic experiment:* planted \(\sigma\)-switching path — which estimator recovers truth fastest?
*Exercises:* inline checkpoints ×3 (predict the output) + ≥10 graded: telescoping proof [easy];
annualisation factors for hourly/minute bars [easy]; \(E[\log]\ne\log E\) [medium]; Parkinson
estimator implementation [medium]; simulation of EWMA lag bias [hard].
*Unverified marks:* endpoint availability table (verified 2026-10-10, re-check before writing).
*Sources:* FPP3 §9.1; McKinney; Hull ch23 (TOC); Cartea ch3 (TOC).

### Ch2 — Time series and stationarity (~14 pp)
*Prerequisites:* ch1; Book 3 "statistics, MLE and Bayesian inference". *Outcome:* recognise stationary
vs non-stationary series, run and read an ADF test, know why tests on prices are usually meaningless.

- §2.1 Stationarity, weak and strong — why tests need it
- §2.2 ACF, PACF and the Ljung–Box check
- §2.3 Deterministic trend vs unit root (the two ways to be non-stationary)
- §2.4 Differencing and logs — the price→returns fix
- §2.5 The ADF test: what it says, what it cannot say
- §2.6 Mean reversion vs random walk — where a testable edge could live
- Summary sheet · Common mistakes · Notes

*WE1* three synthetic paths (white noise, AR(1), random walk) — identify stationarity by eye, ACF,
test; **WE2** Ornstein–Uhlenbeck spread — half-life estimation on synthetic data, recovery of truth;
**WE3** real series: is BTC log-price stationary? does its differenced series pass?
*Figures (5):* "which are stationary?" 3×3 panel (own synthetic + real series); ACF bars
RW/AR(1)/OU; OU path with mean line and half-life annotation; ADF rejection-region sketch;
synthetic cointegrated pair spread.
*Listings (4):* `simulate_ts.py` (RW/AR(1)/OU generators); `adf_demo.py` (statsmodels `adfuller`);
`ljung_box.py`; `ou_halflife.py`.
*Synthetic experiment:* plant OU spread with known half-life — ADF + regression recover it within
tolerance; a random walk correctly fails.
*Exercises:* inline ×3 + ≥10 graded: OU autocorrelation decay [medium]; \(\operatorname{Var}[\text{RW}_t]=t\sigma^2\) consequence [medium]; build a synthetic cointegrated pair
[medium]; interpret a borderline ADF output [easy]; show differencing a trend-stationary series
over-differences [hard].
*Unverified marks:* statsmodels version pinned in `code/README.md` (verify at writing).
*Sources:* FPP3 §9.1 (pedagogy modelled, not copied); Cartea ch3 TOC; Hull ch23 TOC.

---

## Part II — How markets are organised (chapters 3–6, ~54 pp)

### Ch3 — Market structure and the limit order book (~14 pp)
*Prerequisites:* ch1. *Outcome:* read an order book, compute effective spread and walk-the-book cost,
explain maker/taker incentives, know what data a venue emits.

- §3.1 Who trades and why (liquidity traders, informed traders, market makers)
- §3.2 Orders and the LOB: bid, ask, mid, spread, depth, microprice
- §3.3 Matching: price–time priority; walking the book = slippage
- §3.4 Makers, takers, fees and rebates (venue docs, date-stamped)
- §3.5 What the tape looks like: trades, book deltas, candles
- §3.6 A 60-line exchange simulator (preview of the harness event loop)
- Summary sheet · Common mistakes · Notes

*WE1* market order through a toy LOB — average fill vs mid, explicit slippage; **WE2** synthetic
market-making game — quote around mid vs informed flow, adverse selection shown; **WE3** real trade
prints (public endpoint) resampled into candles and compared with venue candles.
*Figures (6):* LOB ladder diagram; book state machine (add/cancel/fill); small-multiple of a market
order eating three levels; bid–ask bounce vs mid path; depth→slippage curve; maker/taker fee table
figure.
*Listings (4):* `lob.py` price-level book with match; `walk_book.py` fill simulator;
`trades_to_candles.py`; `microprice.py`.
*Synthetic experiment:* random-cancel book + informed-order bursts — measure effective vs posted
spread (truth = injected flow).
*Exercises:* inline ×3 + ≥10 graded: time-priority matching by hand [easy]; effective spread
computation [easy]; why mid moves after fills [medium]; queue-position intuition [medium]; adverse
selection toy profit [hard].
*Unverified marks:* named-venue fee tiers (Hyperliquid perp base 0.045%/0.015%, volume tiers — docs
2026-10-10); Polymarket midpoint-display rule (docs 2026-10-10); order-type names differ per venue.
*Sources:* Cartea ch1–2 TOC (section order); Polymarket docs (CLOB, price-as-probability, midpoint);
Hyperliquid fees page.

### Ch4 — Perpetual futures and funding (~12 pp)
*Prerequisites:* ch1, ch3. *Outcome:* explain why a perp never expires, decompose funding payments,
and account for funding inside a PnL.

- §4.1 Forwards, futures, perpetuals — expiry convergence vs the funding tether
- §4.2 Mark price, index/oracle price, margin and liquidation (mechanics, not advice)
- §4.3 The funding mechanism: formula, interval, who pays whom
- §4.4 Funding in PnL: carry, basis, and why funding is not a fee to the venue
- §4.5 Perps inside a backtest: funding as a payment stream; mark-to-market
- Summary sheet · Common mistakes · Notes

*WE1* recompute a documented funding example with new numbers (premium → clamp → rate → payment);
**WE2** synthetic perp: OU premium process — funding's pull-to-oracle vs a no-funding counterfactual;
**WE3** basis decomposition: long perp + short spot, PnL split into basis/funding/fees (synthetic).
*Figures (5):* funding-formula block diagram; mark/index/last price series with funding stamps;
liquidation boundary diagram; basis-vs-funding scatter (synthetic); PnL decomposition stacked bars.
*Listings (4):* `funding.py` documented formula; `perp_sim.py` OU premium + funding pull;
`liquidation_price.py`; `funding_history.py` (public endpoint fetch).
*Synthetic experiment:* planted OU premium — simulated funding distribution matches the formula;
harness funding accrual equals hand computation.
*Exercises:* inline ×2 + ≥10 graded: sign of funding payment [easy]; funding cost over n intervals
[easy]; liquidation price under simplified margin [medium]; show funding is zero-sum [medium];
derive sensitivity of carry PnL to interval [hard].
*Unverified marks:* Hyperliquid formula parameters (hourly payment, 0.01%/8h interest, ±5 bp clamp,
4%/h cap — docs 2026-10-10); Binance rules explicitly unverifiable (docs unreachable 2026-10-10) —
taught as "venue varies, verify"; venue availability from Indonesia `[unverified]`.
*Sources:* Hyperliquid funding/fees docs (canonical formula + worked example); Hull ch1–2,5 TOC;
Bybit V5 intro; Cartea ch1 TOC.

### Ch5 — Prediction markets and scoring rules (~14 pp)
*Prerequisites:* ch1; Book 3 "probability and random variables". *Outcome:* read a prediction-market
price as a belief statement, score forecasts honestly, and know how resolution really works on a
documented venue.

- §5.1 Contracts that pay on events (winner-take-all / index / spread types)
- §5.2 Price as probability — and when it isn't (mean-belief conditions)
- §5.3 Proper scoring rules: Brier, log — honesty as a design constraint
- §5.4 Market scoring rules: the LMSR as an automated market maker
- §5.5 A documented venue: CLOB trading and oracle resolution (Polymarket + UMA)
- §5.6 Calibration: reliability diagrams, comparing forecasters
- Summary sheet · Common mistakes · Notes

*WE1* scoring rules on synthetic forecasters — proper rules reward the truth-teller, a linear
"score" rewards lying; **WE2** LMSR mechanics — cost \(C(\mathbf q)=b\log\sum_i e^{q_i/b}\), prices
from softmax, a full trade sequence; **WE3** calibration duel — calibrated vs overconfident
forecaster on synthetic draws; **WE4** fetch a real market's price history and read it as beliefs.
*Figures (6):* payoff diagrams for the three contract types; score functions (Brier/log/linear);
LMSR price and cost curves; reliability (calibration) diagram; resolution-timeline diagram
(proposal → challenge → DVM); real market price path vs outcome.
*Listings (4):* `scores.py` (Brier/log/linear); `lmsr.py` cost/price/trade; `calibration.py`;
`polymarket_fetch.py` (public market data).
*Synthetic experiment:* known-\(p\) binary event — proper scores rank the honest forecaster first;
LMSR worst-case operator loss confirmed \(\le b\log n\) numerically.
*Exercises:* inline ×3 + ≥10 graded: read price as implied probability [easy]; show linear score is
improper [medium]; derive LMSR price from cost [medium]; binary log-score propriety proof [hard];
bond/dispute outcome computation [medium].
*Unverified marks:* Polymarket fee formula `C·feeRate·p(1−p)` + category rates, ~$750 proposal bond,
2 h challenge, DVM escalation, $1.00/$0.50 redemption, "geopolitical markets fee-free" (docs
2026-10-10); venue legal availability `[unverified]`.
*Sources:* W&Z w10504 (contract types, information aggregation); w12200 (mean-belief conditions);
Gneiting–Raftery (propriety); Hanson (LMSR); Polymarket docs (resolution, prices, fees).

### Ch6 — Automated market makers and impermanent loss (~14 pp)
*Prerequisites:* ch1, ch3. *Outcome:* derive constant-product mechanics, quantify LP economics and
impermanent loss, explain why AMM prices track the market.

- §6.1 Market making without a book: constant-function market makers
- §6.2 \(x\cdot y=k\): marginal price, execution price, slippage vs size, fee reinvestment
- §6.3 LP economics: pool shares, fee income, impermanent loss (and when it's permanent)
- §6.4 Concentrated liquidity: ranged positions and virtual reserves
- §6.5 Why the pool price tracks the market (the arbitrage argument)
- §6.6 AMMs as data and inside a backtest (TWAP oracles)
- Summary sheet · Common mistakes · Notes

*WE1* swap mechanics by hand — execution price vs spot, slippage curve for two pool sizes;
**WE2** IL on a synthetic price path — LP vs HODL payoff with fee toggle; **WE3** v3 range position —
virtual reserves, what happens as price leaves the range; **WE4** arbitrage simulation — external
price jumps; compute the trade that restores the pool to market.
*Figures (6):* constant-product curve with trade vector; slippage-vs-size for two \(k\); IL curve vs
price ratio + fee breakeven; real vs virtual reserves diagram (v3); arbitrage price-tracking small
multiple; LP-vs-HODL payoff on a synthetic path.
*Listings (4):* `cpmm.py` swap + reserves; `imperm_loss.py`; `v3_virtual.py`; `arb_sim.py`.
*Synthetic experiment:* deterministic price jump — after one optimal arb trade the pool price equals
external price up to fee (numerical reproduction of the tracking result); IL formula verified
against simulation.
*Exercises:* inline ×3 + ≥10 graded: derive IL formula [medium]; effective price with fee [easy];
when does LP beat HODL [medium]; range position effective leverage intuition [hard]; TWAP
manipulation cost reasoning [hard].
*Unverified marks:* Uniswap fee tiers and dormant protocol-fee switch (whitepapers; current pool
state verify at writing); "IL" terminology vs official docs.
*Sources:* Uniswap v2 + v3 whitepapers; Angeris et al. (arbitrage tracking, agent-based stability);
Polymarket docs (CLOB-vs-AMM contrast).

---

## Part III — Backtesting honestly (chapters 7–12, ~76 pp)

### Ch7 — Data engineering for market data (~12 pp)
*Prerequisites:* ch1–3. *Outcome:* fetch, validate, store and serve market data with
point-in-time-correct semantics.

- §7.1 The data that exists: trades, book deltas/snapshots, candles, funding — and where to get it
  without a key (verified table, 2026-10-10)
- §7.2 Schemas and units: ms vs µs timestamps, timezones, precision, symbol mappings
- §7.3 Cleaning: gaps, duplicates, bad prints, calendar alignment across venues
- §7.4 Storage: CSV → Parquet, partitioning by symbol/date
- §7.5 Point-in-time correctness: survivorship, delisting, "today's universe" vs then
- §7.6 `harness/data.py`: an as-of loader that cannot serve the future
- Summary sheet · Common mistakes · Notes

*WE1* fetch the same market from two public venues, normalise, cross-check closes (planted errors
detected); **WE2** corrupted-file surgery — find planted duplicates/gaps/µs-vs-ms bug;
**WE3** survivorship demo on a synthetic universe (a dead market vanishes from "today's" listing).
*Figures (5):* fetch→validate→store→serve pipeline; timestamp-unit anatomy; defect diagnostics
panel; universe-membership heatmap (synthetic); directory layout tree.
*Listings (4):* `fetch_kraken.py`; `validate_feed.py` (monotonic ts, unit sniff, gap report);
`to_parquet.py`; `asof_loader.py` (returns only rows ≤ t).
*Synthetic experiment:* synthetic venue feed with 12 planted defects — validator catches all 12.
*Exercises:* inline ×2 + ≥10 graded: timestamp-unit bug [easy]; join two feeds on time [easy];
dedup-vs-bad-print judgement [medium]; calendar alignment across venues [medium]; design an as-of
API that makes leakage impossible by construction [hard].
*Unverified marks:* entire endpoint table date-stamped 2026-10-10; `api.binance.com` geo-451 and
Indonesia reachability `[unverified]`; Stooq JS-challenge and Yahoo 429 status at test date.
*Sources:* McKinney (pandas patterns); Jansen ML4T repo (code-tree precedent); live endpoint tests;
Hyperliquid/Polymarket/Bybit docs (endpoint shapes).

### Ch8 — A backtest harness that cannot leak (~14 pp)
*Prerequisites:* ch7. *Outcome:* own a correct-by-construction event-driven harness skeleton and a
test suite that deliberately fails on injected look-ahead — the capstone's core.

- §8.1 What a backtest must prove: decision at \(t\) sees only data \(\le t\)
- §8.2 Architecture: feed → strategy → broker/fills → ledger → metrics
- §8.3 The no-peek API: strategies receive a window, the harness enforces it
- §8.4 Fills and the ledger: positions, cash, equity marking conventions
- §8.5 The fail-on-purpose suite: tests that must fail when the future leaks
- §8.6 Vectorised speed vs event-loop correctness (and when each is safe)
- Summary sheet · Common mistakes · Notes

*WE1* the canonical leak — "buy if tomorrow's close is higher" sails through a naive vectorised test
and is caught by the harness; **WE2** honest MA-crossover on synthetic OU (planted drift, expected
sign known); **WE3** same-bar fill semantics — decide at close, fill next open: three conventions,
different answers, one chosen.
*Figures (5):* architecture block diagram; event-visibility timeline; ledger state diagram; leaky vs
honest equity pair; fail-on-purpose test tree.
*Listings (4):* `event_loop.py`; `window_view.py` (no-peek API); `ledger.py` apply-fill;
`test_leakage.py` (peek-injection that must fail).
*Synthetic experiment:* inject leaks of varying subtlety (shift-1, forward-fill, scale-on-full) —
detectors catch each; an honest strategy produces no flag (false-positive check).
*Exercises:* inline ×3 + ≥10 graded: spot the leak in three snippets [easy→medium]; write a no-peek
decorator [medium]; prove fill-at-next-open removes same-bar ambiguity [hard]; classify
vectorised-trap patterns [medium].
*Unverified marks:* none (own code; version pins in `code/README.md`).
*Sources:* QuantStart Part I (event-driven rationale, bias list); LdP lecture order (Backtesting
I/II); Bailey–Borwein–LdP–Zhu SSRN abstract (PBO framing); ML4T repo precedent.

### Ch9 — The ways backtests lie (~14 pp)
*Prerequisites:* ch8. *Outcome:* name, recognise and build detectors for each classic bias.

- §9.1 Look-ahead in disguise: same-bar fills, forward-filled features, full-sample scaling
- §9.2 Survivorship and universe bias
- §9.3 Selection bias and multiple testing (best-of-N inflation; PBO idea)
- §9.4 Data snooping and the garden of forking paths
- §9.5 Regime change: the past is a sample, not a promise
- §9.6 The bias audit checklist — every bias becomes a harness test
- Summary sheet · Common mistakes · Notes

*WE1* scale-on-full-sample leak: an otherwise-trivial signal looks tradable until scaling is made
causal; **WE2** survivorship on a synthetic universe — survivors-only vs full-universe results
diverge; **WE3** 200 random strategies — the best one's Sharpe distribution under the null.
*Figures (5):* leak taxonomy diagram; survivor-vs-universe equity curves; max-Sharpe null
distribution vs N; forking-paths tree; audit checklist table-figure.
*Listings (4):* `causal_scaler.py`; `universe_with_delisting.py`; `multi_test_sim.py`;
`n_trials_log.py` (trial-count bookkeeping).
*Synthetic experiment:* three planted biases above, truth always = construction; detectors emit the
expected warnings.
*Exercises:* inline ×3 + ≥10 graded: classify eight described leaks [easy]; write a forward-fill
detector [medium]; explain selection-bias inflation \(E[\mathrm{SR}\mid\text{selected}]\) [medium];
PBO interpretation [hard].
*Unverified marks:* "most published findings are false" cited as a claim from LdP's FDR seminar
abstract (not independently verified).
*Sources:* QuantStart Part I (bias taxonomy); Bailey–Borwein–LdP–Zhu (PBO/CSCV); LdP lectures
("7 reasons", FDR seminar); epchan (overfitting cautions).

### Ch10 — Execution: fees, spreads and slippage (~12 pp)
*Prerequisites:* ch3, ch8. *Outcome:* model the whole cost stack in the harness and measure its drag.

- §10.1 The cost stack: explicit (commission, funding) and implicit (spread, impact, delay)
- §10.2 Fill models: at-quote, walk-the-book, and a square-root impact sketch (model, not law)
- §10.3 Latency and stale decisions
- §10.4 Maker/taker fee schedules as documented (date-stamped)
- §10.5 `harness/fills.py` + `harness/fees.py`: cost models with unit tests
- Summary sheet · Common mistakes · Notes

*WE1* fee drag: same signals with/without realistic taker fees on synthetic — drag =
rate × turnover recovered; **WE2** spread vs adverse selection: market fills vs resting limits on
synthetic flow; **WE3** slippage model check: walk-the-book on the ch3 simulator vs a
square-root sketch.
*Figures (5):* cost-stack diagram; fee-drag vs turnover chart; slippage-vs-size (book vs model);
maker-vs-taker outcome split; latency/stale-decision timing diagram.
*Listings (4):* `fee_schedule.py` (tiered taker/maker); `book_fill.py`; `sqrt_impact.py`;
`cost_report.py`.
*Synthetic experiment:* known cost rates injected — harness cost attribution recovers them;
marketable-limit and partial-fill unit tests pass/fail correctly.
*Exercises:* inline ×3 + ≥10 graded: breakeven turnover [easy]; why rebates change quoting
incentives [medium]; fee at 30¢ = fee at 70¢ under the Polymarket formula — verify [medium]; value
of queue position for a limit order [hard].
*Unverified marks:* Hyperliquid tier table and rebate schedule; Polymarket `C·feeRate·p(1−p)` and
category rates (docs 2026-10-10).
*Sources:* Hyperliquid fees; Polymarket fees; Cartea Part III TOC (execution topics); QuantStart
cost discussion.

### Ch11 — Walk-forward and hold-out testing (~12 pp)
*Prerequisites:* ch9; Book 3 "statistics, MLE and Bayesian inference". *Outcome:* design split
schemes that respect time, with purging/embargo, and know when the untouched hold-out may be opened.

- §11.1 Train/validation/test for time series (no shuffling — ever)
- §11.2 Anchored vs rolling walk-forward
- §11.3 Purging and embargo at the split boundary
- §11.4 Combinatorially symmetric CV: the PBO sketch
- §11.5 The hold-out: lock it, and what looking costs you
- §11.6 `harness/splits.py` + boundary tests
- Summary sheet · Common mistakes · Notes

*WE1* shuffle-CV disaster on autocorrelated synthetic data vs walk-forward truth; **WE2**
walk-forward across a planted regime change — parameter-stability table; **WE3** embargo demo — a
label built from the next \(k\) bars leaks across the split until embargoed.
*Figures (5):* three split designs diagram; boundary-leak zoom; CSCV partition schematic;
parameter-stability heat table; per-window metric small multiples.
*Listings (4):* `walk_forward.py` generator; `embargo.py`; `cpcv_sketch.py`; `test_boundaries.py`.
*Synthetic experiment:* edge planted only in regime 1 — walk-forward exposes instability that a
single split hides.
*Exercises:* inline ×3 + ≥10 graded: embargo size ≥ feature+label reach [easy→medium]; compute the
WF window count for given lengths [easy]; write a purge rule [medium]; show why purging length ≥
reach [hard].
*Unverified marks:* none (methods, not venue rules).
*Sources:* LdP lecture order (Backtesting I/II → purging/embargo as AFML presents it); Bailey–LdP
PBO abstract (CSCV); FPP3 (time-series evaluation order); QuantStart.

### Ch12 — Evaluating a strategy (~12 pp)
*Prerequisites:* ch11; Book 3 "statistics, MLE and Bayesian inference". *Outcome:* report the right
metrics with honest uncertainty, including selection-adjusted significance.

- §12.1 The metric set: mean/vol/Sharpe, max drawdown, hit rate, expectancy, tail metrics
- §12.2 Uncertainty in a Sharpe estimate (standard error; Sharpe inference)
- §12.3 Selection-adjusted significance: deflated Sharpe, expected max under N trials
- §12.4 Benchmarks, capacity, and "net of what?"
- §12.5 `harness/metrics.py` and the standard results sheet
- §12.6 Sanity checks before believing any backtest
- Summary sheet · Common mistakes · Notes

*WE1* Sharpe CI on synthetic strategy (planted SR — coverage check of the interval); **WE2**
best-of-200 honestly evaluated — deflation changes the verdict; **WE3** metric traps dissected:
high-SR/deep-MDD and high-hit-rate/negative-expectancy strategies (synthetic).
*Figures (5):* equity + underwater paired plot; SR sampling distribution; deflated-SR vs trials
curve; metric dashboard; capacity curve (PnL vs size).
*Listings (4):* `metrics.py` (Sharpe/MDD/hit/expectancy); `sr_inference.py` (SE, CI);
`deflated_sr.py`; `results_sheet.py`.
*Synthetic experiment:* planted Sharpe 0.8 with a planted crash — evaluation recovers SR and flags
the tail.
*Exercises:* inline ×3 + ≥10 graded: annualise SR correctly [easy]; SE(SR) derivation [medium];
hit-rate vs expectancy [medium]; read a deflated-SR output [medium]; interpret a PBO estimate
[hard].
*Unverified marks:* none (statistics; LdP seminar claims cited as claims).
*Sources:* LdP seminars (*Sharpe Ratio Inference*; *7 reasons*); Bailey–LdP deflated-SR (via SSRN
listing); QuantStart performance section.

---

## Part IV — Strategy craft and research hygiene (chapters 13–15, ~38 pp)

### Ch13 — Position sizing and Kelly (~14 pp)
*Prerequisites:* ch1, ch12; Book 3 "optimisation, convexity and Lagrange multipliers". *Outcome:*
derive and simulate Kelly sizing, know why fractional Kelly exists, implement capped sizing.

- §13.1 Sizing is a decision separate from signal
- §13.2 Kelly for bets: coin toss → general odds → continuous approx \(f^*=\mu/\sigma^2\)
- §13.3 Growth \(g(f)\), and the probability of ruin or of reaching a goal
- §13.4 Fractional Kelly and estimation error (why practitioners halve it)
- §13.5 Kelly for a strategy: estimated edge, capped fractions
- §13.6 `harness/sizing.py`: fixed-fraction vs Kelly-capped callbacks
- Summary sheet · Common mistakes · Notes

*WE1* coin-toss Kelly by simulation (planted \(p\)) — \(g(f)\) curve, ruin past \(2f^*\); **WE2**
continuous Kelly on a GBM signal (synthetic, truth known); **WE3** noisy-\(\hat\mu\) plug-in —
distribution of \(\hat f^*\), and why half-Kelly is standard.
*Figures (5):* \(g(f)\) curve with \(f^*\) and the overbetting cliff; equity paths at
\(f/2, f, 2f\) on one bet stream; ruin probability vs \(f\); \(\hat f^*\) distribution under noisy
edge; sizing-rule comparison curves.
*Listings (4):* `growth_sim.py`; `kelly_fraction.py`; `ruin_prob.py`; `sizing_capped.py`.
*Synthetic experiment:* planted edge \(p{=}0.55\) — empirical \(f^*\to 0.10\); measured ruin
probability matches Thorp's formula.
*Exercises:* inline ×3 + ≥10 graded: derive binary-bet \(f^*\) [medium]; concavity of \(g\) [easy];
\(P(\text{halving})\) under full Kelly [medium]; multi-outcome Kelly setup [hard]; when \(f^*<0\)
interpretation [easy].
*Unverified marks:* none (pure mathematics + own simulations).
*Sources:* Thorp paper (section order mirrored); shared-notation growth/log conventions.

### Ch14 — Risk management (~12 pp)
*Prerequisites:* ch13. *Outcome:* express risk as constraints, estimate VaR/ES honestly on fat tails,
and implement kill-switch logic.

- §14.1 Risk as constraints: position, drawdown, daily-loss limits
- §14.2 VaR and expected shortfall — and how to backtest a risk model
- §14.3 Leverage, margin and forced liquidation (mechanics; perp tie-in)
- §14.4 Kill switches and circuit breakers in the harness
- §14.5 Portfolio-level risk: correlation and concentration (light touch)
- §14.6 A personal risk policy document (a checklist, not advice)
- Summary sheet · Common mistakes · Notes

*WE1* VaR/ES on synthetic fat tails — normal-model VaR vs empirical, model risk quantified;
**WE2** kill switch: planted crash — drawdown limit truncates losses vs free run; **WE3** margin
cascade: perp position near liquidation on a synthetic shock path.
*Figures (5):* VaR/ES tail diagram; normal-vs-empirical tail-risk understatement; drawdown control
loop; liquidation cascade; correlation → portfolio-vol illustration.
*Listings (4):* `var_es.py` + coverage backtest; `kill_switch.py`; `margin_monitor.py`;
`corr_stress.py`.
*Synthetic experiment:* \(t\)-distributed returns — nominal 99% VaR breached far beyond 1% under a
normal model.
*Exercises:* inline ×2 + ≥10 graded: VaR/ES from samples [easy]; expected breach count [easy]; when
ES = VaR [medium]; sizing a limit from a loss budget [medium]; multi-asset correlation stress
[hard].
*Unverified marks:* venue margin/liquidation parameters as documented (Hyperliquid mechanics,
2026-10-10).
*Sources:* Hull ch22 TOC (VaR/ES topic order); Hyperliquid docs (liquidation mechanics reference);
Thorp (ruin probabilities); Cartea Part III TOC.

### Ch15 — Writing it up: results, failures and negative results (~12 pp)
*Prerequisites:* all previous. *Outcome:* produce a complete, honest research write-up — including
when the answer is "the edge isn't there".

- §15.1 What a write-up must contain: provenance, split design, costs, trial count, unverified claims
- §15.2 The standard results sheet (`harness/report.py`)
- §15.3 Negative results are results — how to present a clean rejection
- §15.4 The honesty checklist: `[unverified]` marks, date-stamps, the no-advice line
- §15.5 Two case studies: one positive, one negative — full reports dissected
- Summary sheet · Common mistakes · Notes

*WE1* a planted-true strategy written up — every number recomputable from `code/`; **WE2** a
planted-false strategy that looked good naively — the negative report that saves the reader months;
**WE3** review exercise: find six planted sins in a flawed supplied report.
*Figures (4):* annotated results-sheet template; decision tree "what would change my mind";
audit-trail diagram; honesty checklist table.
*Listings (3):* `report.py` generator; `claims_table.py` (claim → status/date); `writeup_template.py`.
*Synthetic experiment:* both case studies run on planted-truth data — reported numbers reproduce.
*Exercises:* inline ×2 + ≥10 graded: fill a results sheet [easy]; find the leak in a supplied report
[medium]; preregister a test before running it [hard]; draft your own negative-result section
[medium].
*Unverified marks:* none — the chapter institutionalises the marking convention itself.
*Sources:* LdP FDR-seminar claim (cited as claim); Bailey et al. charlatanism (title/provenance via
SSRN listing); this book's own `docs/unverified.md` method.

---

## Capstone map — `code/harness/` (built chapter by chapter, tested throughout)

| Piece | Built in | Contents |
|---|---|---|
| `data.py` | ch7 | as-of loaders, validation, Parquet layout |
| `core.py`, `ledger.py`, `window_view.py` | ch8 | event loop, no-peek API, positions/cash/equity |
| `tests/test_leakage.py` | ch8–ch9 | fail-on-purpose look-ahead injections (must fail); survivorship and snooping fixtures |
| `fees.py`, `fills.py` | ch10 | tiered maker/taker fees, funding payments, book/sqrt slippage |
| `splits.py` | ch11 | walk-forward, anchored/rolling, purge+embargo |
| `metrics.py`, `results_sheet.py` | ch12 | Sharpe family, MDD, hit rate, deflated SR, report |
| `sizing.py` | ch13 | fixed-fraction, Kelly-capped callbacks |
| `risk.py` | ch14 | DD kill-switch, loss limits, margin monitor |
| `report.py`, `claims_table.py` | ch15 | standard write-up + claims/verification log |

Deliberately-failing tests (`test_leakage.py`) inject: shift-by-one look-ahead, same-bar close fills,
forward-filled feature, full-sample scaler, and a survivor-only universe — each must make the harness
fail loudly. That is the capstone's acceptance test, and it is exercised from ch8 onward.

## Page budget

Front matter ≈ 10 pp (preface, how-to-use, notation guide, disclaimer). Chapters: 14+14+14+12+14+14+
12+14+14+12+12+12+14+12+12 = 196 pp. Back matter ≈ 22 pp (Appendix A — Book-3 dependency map ~4 pp;
Appendix B — `harness` API reference ~6 pp; Appendix C — verified data-source table ~3 pp; hints +
solutions ≥ half of exercises ~9 pp; bibliography; index). **Total ≈ 228 pp.**
Compression order if over budget: merge ch14 into ch13's back half → compress ch7 → drop WE4s.
Never cut figures, listings, worked examples, or Common-mistakes sections (per approved process).

## Seed-topic coverage and deviations

Every seed topic is covered: returns/risk ch1; time series/stationarity ch2; market structure/order
books ch3; perpetual futures/funding ch4; prediction markets/scoring rules ch5; AMMs/impermanent
loss ch6; biases ch9; walk-forward/hold-out ch11; execution/fees/slippage ch10; sizing/Kelly ch13;
risk management ch14; evaluating ch12; data engineering ch7; negative results ch15.
Deviations from the seed order, all pedagogical: (a) **data engineering moved before backtesting**
(the harness needs its loader); (b) **"backtesting and its biases" split** into architecture (ch8)
and the bias zoo (ch9) — each is a full chapter's worth; (c) **execution split** between book/slippage
basics (ch3) and harness cost modelling (ch10); (d) **evaluation placed after walk-forward** —
deflated significance needs the split-design machinery first.

## Sources (full log: `docs/sources.md`)

Anchors: Wolfers–Zitzewitz w10504 + w12200; Thorp Kelly; López de Prado lecture library; Hull 11e
TOC; Cartea–Jaimungal–Penalva TOC. Supplements actually read: Gneiting–Raftery; Hanson LMSR;
Polymarket docs; Hyperliquid docs (funding + fees); Bybit V5 docs; Uniswap v2/v3 whitepapers;
Angeris et al.; McKinney; QuantStart; FPP3; epchan; Quantopian `research_public`; Jansen ML4T repo;
Bailey–LdP PBO (SSRN abstract). Plus live endpoint verification (2026-10-10) and a failed-fetch log.
