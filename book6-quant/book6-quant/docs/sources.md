# Sources

Research log for `textbook-quant` (Book 6). Only sources actually opened are listed. Access date for
all rows: **2026-10-10**. "Licence" = status of what was opened (most are free public copies; we take
ideas/topic order/exercise types only, never text or figures).

| URL / ISBN | Accessed | Licence / access | What was taken (idea / topic order / exercise type; never text) |
|---|---|---|---|
| https://www.nber.org/system/files/working_papers/w10504/w10504.pdf — Wolfers & Zitzewitz, *Prediction Markets* (NBER WP 10504; JEP 18(2) 2004 version) | 2026-10-10 | Free working-paper PDF; © W&Z, short quoting allowed with credit | Ch5 spine: opening anecdote style (DARPA/Poindexter), the three contract types (winner-take-all / index / spread), "markets beat moderately sophisticated benchmarks" claim, market-design issue list. Note: paper does NOT formalise scoring rules — that gap is filled by Hanson + Gneiting–Raftery below. |
| https://www.nber.org/system/files/working_papers/w12200/w12200.pdf — Wolfers & Zitzewitz, *Interpreting Prediction Market Prices as Probabilities* (NBER WP 12200) | 2026-10-10 | Free working-paper PDF; © W&Z | Ch5 §"price as probability": Manski's challenge, sufficient conditions for price ≈ mean belief, deviations driven by risk aversion and belief dispersion → sets up the calibration exercise and the "price is not your probability" common mistake. |
| https://gwern.net/doc/statistics/decision/2006-thorp.pdf — Thorp, *The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market* (Elsevier, Handbook of ALM, 2006; mirror) | 2026-10-10 | Free PDF mirror of published paper (DOI 10.1016/S1872-0978(06)01009-X) | Ch13 order: coin tossing → practitioner formulas → ruin/goal probabilities → blackjack/sports → Wall Street → fractional Kelly → case study. Continuous approx \(f^*=\mu/\sigma^2\), growth function \(g(f)\), "fractional Kelly" §7.3 → sizing chapter arc and its synthetic simulations. |
| https://www.quantresearch.org/Lectures.htm — López de Prado lecture library (Cornell ORIE 5256 + seminars) | 2026-10-10 | Free slides index | Lecture-series order: pitfalls → financial applications → data → modelling → backtesting I/II → ML portfolio → features → HPC → "7 reasons ML funds fail"; seminar titles incl. *Sharpe Ratio Inference* (2026) and *False Discovery Rate in Finance* (2026, FDR > 80% claim — cite as claimed) → order for ch8, ch9, ch11, ch12 and the "most published findings are false" caution. |
| https://www.pearson.com/en-gb/subject-catalog/p/options-futures-and-other-derivatives-global-edition/P200000004519/9781292410654 + http://www-2.rotman.utoronto.ca/~hull/ofod/ — Hull, *Options, Futures and Other Derivatives* 11e official TOC | 2026-10-10 | Publisher TOC pages (book paywalled; TOC facts only) | Chapter map used for topic placement: ch2 futures mechanics/margin/CCPs, ch3 hedging, ch5 forward & futures price determination, ch14–15 Wiener/Itô/BSM, ch22 VaR & expected shortfall, ch23 estimating volatilities & correlations, ch37 derivatives mishaps → ch4 (margin/convergence contrast), ch14 (VaR/ES), ch1 (volatility estimators). |
| https://assets.cambridge.org/97811070/91146/frontmatter/9781107091146_frontmatter.pdf + https://www.cambridge.org/ae/universitypress/subjects/mathematics/mathematical-finance/algorithmic-and-high-frequency-trading — Cartea, Jaimungal & Penalva, *Algorithmic and High-Frequency Trading* frontmatter + TOC | 2026-10-10 | Publisher frontmatter PDF + product page (book paywalled; TOC facts only) | Part I order: electronic markets & the LOB → microstructure primer (market making, trading costs, liquidity measures) → empirical facts (prices/returns, activity/market quality); Part III: optimal execution, market making, pairs trading, order imbalance → ch3 and ch10 section order and which empirical facts to teach first. |
| https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf — Gneiting & Raftery, *Strictly Proper Scoring Rules* (JASA 2007, author copy) | 2026-10-10 | Author-hosted copy of JASA paper | Ch5 §scoring rules: definition of (strictly) proper rules, propriety ⇒ honest elicitation, log/spherical/quadratic scores, CRPS — the mathematical heart the W&Z papers leave out. Used for the honest-vs-strategic forecaster synthetic experiment. |
| https://mason.gmu.edu/~rhanson/mktscore.pdf — Hanson, *Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation* (2002) | 2026-10-10 | Author-hosted copy | Ch5 §LMSR: market scoring rule = scoring rule + betting market; only logarithmic versions preserve (conditional) probabilities; bounded operator loss \(b\log n\) → LMSR worked example and the "automated market maker before crypto AMMs" note. |
| https://docs.polymarket.com/ (+ /llms.txt, /concepts/resolution.md, /concepts/prices-orderbook.md, /trading/fees.md, /developers/CLOB/introduction) | 2026-10-10 | Public venue docs — all mechanics date-stamped & marked for re-verification | Venue mechanics: CLOB with prices in $0–$1 read as probabilities; midpoint display rule (last trade if spread > $0.10); taker fee `C·feeRate·p(1−p)` with per-category rates and maker rebates; UMA optimistic-oracle resolution (proposal bond ≈ $750 pUSD, 2 h challenge, DVM vote on double dispute, $1.00/$0.50 redemption) → ch3 and ch5. |
| https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding | 2026-10-10 | Public venue docs — date-stamped & marked for re-verification | Perp funding mechanics (the book's canonical documented formula): `F = prem + clamp(interest − prem, ±0.0005)`, hourly payment at 1/8 of the 8 h rate, impact-bid/ask premium, weighted-median CEX oracle, 4%/hour cap, worked numeric example → ch4 worked example + perp simulator. Chosen over Binance because Binance pages were unreachable (see failed fetches below). |
| https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees | 2026-10-10 | Public venue docs — date-stamped | Fee tables: 14-day rolling volume tiers, perp base taker 0.045% / maker 0.015%, maker-rebate tiers, spot 2× volume weighting → ch3/ch10 fee-tier table and "maker vs taker incentives" discussion. |
| https://bybit-exchange.github.io/docs/v5/intro — Bybit V5 API introduction | 2026-10-10 | Public API docs | V5 unified account covering linear/inverse/spot/options; endpoint list for ch7 data sources. (The dedicated funding-history page failed to fetch — noted; intro coverage table only.) |
| https://uniswap.org/whitepaper.pdf — Uniswap v2 Core whitepaper | 2026-10-10 | Public whitepaper | \(x\cdot y=k\) invariant, reserves-ratio price, 30 bp swap fee to LPs (with dormant 5 bp protocol-fee switch), TWAP cumulative-price oracle, flash swaps, first printed use of "impermanent loss" → ch6 sections 6.1–6.3 and oracle-as-data-source note. |
| https://uniswap.org/whitepaper-v3.pdf — Uniswap v3 Core whitepaper | 2026-10-10 | Public whitepaper | Concentrated liquidity: ranged positions act like constant-product pools with virtual reserves; fee tiers 0.05/0.30/1% at pool init; improved oracle/liquidity oracles → ch6 §v3 mechanics + "effective leverage of a range" exercise. |
| https://arxiv.org/abs/1911.03380 — Angeris, Kao, Chiang, Noyes, Chitra, *An analysis of Uniswap markets* | 2026-10-10 | arXiv open access | Arbitrage argument that constant-product prices track the reference market + agent-based stability simulation → ch6 §"why AMM prices are informative" and the arbitrage-restore synthetic experiment. |
| https://wesmckinney.com/book/ — McKinney, *Python for Data Analysis* 3e, open-access HTML | 2026-10-10 | Open-access text (do-not-copy terms; code MIT) | pandas/NumPy patterns and time-series handling order for ch7 (reader-side reference; also sets the code-style bar for listings). |
| https://www.quantstart.com/articles/Successful-Backtesting-of-Algorithmic-Trading-Strategies-Part-I/ — QuantStart backtesting series | 2026-10-10 | Free blog article | Bias taxonomy (optimisation/look-ahead/survivorship/psychological-tolerance) and the case for event-driven backtests → ch8 architecture rationale and ch9 bias checklist. |
| https://otexts.com/fpp3/stationarity.html — Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* 3e, §9.1 | 2026-10-10 | Free online textbook | Ch2 pedagogy: "which of these series is stationary?" multi-panel figure exercise, differencing to stabilise mean, ACF + Ljung-Box worked demonstration on a real series → figure plan and exercise style (we reproduce the pedagogy with our own synthetic + crypto series, not their text or R code). |
| https://epchan.blogspot.com/ — Ernest Chan, *Quantitative Trading* blog | 2026-10-10 | Free blog | Practitioner cautions: feature selection/overfitting, parameter-count discipline (PCA/SVD factor models of returns), GenAI-hype realism → common-mistakes seeds and Notes recommendations for ch9/ch12. |
| https://github.com/quantopian/research_public — Quantopian lecture-series notebooks | 2026-10-10 | CC BY 4.0 | Notebook-companion format precedent (lecture → runnable notebook) → `code/` organisation; nothing reused. |
| https://github.com/stefan-jansen/machine-learning-for-trading — Jansen, *Machine Learning for Trading* code repo | 2026-10-10 | MIT | Precedent for pairing a book with a runnable, versioned code tree → `code/harness/` layout; nothing reused. |
| https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253 — Bailey, Borwein, López de Prado & Zhu, *The Probability of Backtest Overfitting* (SSRN abstract) | 2026-10-10 | Abstract page only (paper behind SSRN) | PBO and combinatorially symmetric cross-validation (CSCV) framing, "hold-out is unreliable in backtests" thesis, deflated-Sharpe pointer → ch9 selection-bias section and ch11 CSCV sketch (presented as the paper's idea, cited). |

## Failed fetches (honesty log)

| URL | Result | Consequence |
|---|---|---|
| https://www.binance.com/en/support/faq/introduction-to-binance-futures-funding-rates-360033525031 | HTTP 202, 0 bytes — bot/geo block | Binance funding mechanics NOT verified from docs; any Binance-specific rule gets `\textbf{[unverified]}` or is dropped. Hyperliquid docs used as the canonical documented funding formula instead. |
| https://www.binance.com/en/fee/futureFeeRate | HTTP 202, 0 bytes | Same — Binance fee schedule unverified. |
| https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History | HTTP 202, 0 bytes | Same. |
| https://www.bybit.com/en/help-center/article/Funding-rate | No content retrieved | Bybit help-centre article unread; Bybit V5 developer docs used instead. |
| https://www.okx.com/help/section/announcements-announcements | No content retrieved | OKX help centre unread (API endpoint itself verified live below). |
| https://github.com/quantopian/lectures | No content returned | Superseded by `quantopian/research_public` (logged above). |
| https://bybit-exchange.github.io/docs/v5/market/funding-history | Not returned in batch | Bybit funding mechanics not independently verified → treated as unverified. |
| https://arxiv.org/abs/1401.0478 — Bailey et al., *Pseudo-mathematics and financial charlatanism* | Page reached but content not captured in the batch | Cited only via the SSRN listing row above (title + provenance), not as a read source. |

## Venue mechanics recorded for the book (all date-stamped 2026-10-10, all get `[unverified]` + "verify at use" marks in text)

- **Perpetual funding (canonical example — Hyperliquid docs):** peer-to-peer transfer, no fee to venue;
  `F = premium_index + clamp(interest − premium_index, −0.05%, +0.05%)` per 8 h basis, paid hourly at
  1/8; interest component fixed at 0.01% per 8 h; premium from impact bid/ask vs weighted-median CEX
  oracle; capped at 4%/hour; payment = position size × oracle price × rate.
- **Fee schedules:** Hyperliquid perps base 0.045% taker / 0.015% maker on 14-day volume tiers with
  maker rebates at high maker share; Polymarket taker fee `C·feeRate·p(1−p)` (parabolic, max at 50¢,
  makers never pay; category rates 0.04–0.07; geopolitical/world-events markets fee-free) funding a
  daily maker-rebate program.
- **Prediction-market resolution (Polymarket):** UMA optimistic oracle; proposer posts ≈$750 pUSD
  bond; 2 h challenge; dispute → second proposal round → second dispute → UMA DVM token-holder vote
  (24–48 h debate + ~48 h vote); winners redeem $1.00, losers $0.00, "unknown" resolves 50/50.
- **AMM mechanics:** Uniswap v2: `x·y = k`, 30 bp to LPs, block-start TWAP accumulators; v3: ranged
  positions with virtual reserves, fee tiers 0.05%/0.30%/1%.

## Prediction-market scoring rules — how W&Z actually treat them (task-required note)

- Wolfers & Zitzewitz (w10504, JEP 2004): explain *prices as probabilities* via contract design —
  three contract types for eliciting probabilities/means/medians — and survey market-design issues;
  they do **not** develop scoring-rule mathematics (no "scoring" in the paper).
- W&Z (w12200, 2006): give the microfoundation — when prices ≈ mean beliefs (risk aversion + belief
  dispersion drive the wedge).
- The scoring-rule machinery the brief names therefore comes from **Hanson (LMSR)** — a market maker
  that pays each trader the change in a log score and bounds operator loss — and **Gneiting–Raftery**
  for proper scoring rules generally. Outline cites all four together; nothing is attributed to W&Z
  that they did not write.

## Free market data without an API key — verified live 2026-10-10 (curl from this VM; Indonesia reachability needs reader-side check → `[unverified]`)

| Endpoint | Result (2026-10-10) | Usable without key? |
|---|---|---|
| `api.kraken.com/0/public/OHLC?pair=XBTUSD` | HTTP 200, real OHLC rows | Yes — primary recommended source. |
| `www.okx.com/api/v5/market/candles?instId=BTC-USDT` | HTTP 200, real candles | Yes. |
| `api.gateio.ws/api/v4/spot/candlesticks?currency_pair=BTC_USDT` | HTTP 200 | Yes. |
| `api.exchange.coinbase.com/products/BTC-USD/candles` | HTTP 200 | Yes. |
| `api.coingecko.com/api/v3/simple/price` | HTTP 200 `{"bitcoin":{"usd":82944}}` | Yes (rate-limited free tier). |
| `data.binance.vision/data/spot/daily/klines/...zip` | HTTP 200, CSV inside zip (timestamps in µs — 16 digits) | Yes — bulk history, no key. |
| `api.binance.com/api/v3/klines` | HTTP 451 "restricted location" | No — geo-blocked from this VM (US). Indonesia availability unknown → `[unverified]`; Binance is also not a locally licensed venue in Indonesia (regulatory claim needs verification at writing). |
| `query1.finance.yahoo.com/v8/finance/chart/AAPL` | HTTP 429 rate-limited | Unreliable — do not teach as a source. |
| `stooq.com/q/d/l/?s=spy.us` | HTTP 200 but JS proof-of-work challenge page | Not usable from scripts at test date (browser may work) → flagged. |
