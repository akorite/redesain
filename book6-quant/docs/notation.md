# Notation

**Shared file:** `notation-shared.md` (Books 3/4/6) is binding and reused verbatim — all
probability/statistics, linear-algebra, calculus and loss conventions come from there. This file adds
only Book-6 market notation; nothing below contradicts the shared file.

Conventions carried over: \(\log\) = natural log; \(\Pr[\cdot],\mathbb E[\cdot],\operatorname{Var}[\cdot]\)
square-bracket family; time index \(t\) subscripted; shared Book-6 additions \(r_t=\log(P_t/P_{t-1})\),
\(\mathbf w\) portfolio weights.

## Market notation

| Symbol / macro | Meaning | First used |
|---|---|---|
| \(P_t\) | Price at time \(t\) (of the instrument in context) | ch1 |
| \(R_t\) | **Simple** net return, \(P_t/P_{t-1}-1\) | ch1 |
| \(r_t\) | **Log** return, \(\log(1+R_t)=\log(P_t/P_{t-1})\) (shared file) | ch1 |
| \(\sigma\), \(\hat\sigma\) | Volatility (of returns); its estimate | ch1 |
| \(\mu\) | Mean return / drift | ch1 |
| \(W_t\) | Wealth / account equity | ch1 |
| \(D_t\) | Drawdown, \(W_t^{\max}-W_t\); \(\mathrm{MDD}=\max_t D_t\) | ch1 |
| \(o_t,h_t,l_t,c_t\) | Open / high / low / close of bar \(t\) (lowercase letters) | ch1 |
| \(a_t,b_t\) | Best ask, best bid | ch3 |
| \(m_t\) | Mid price, \((a_t+b_t)/2\) | ch3 |
| \(S_t\) | Quoted spread, \(a_t-b_t\) | ch3 |
| \(p_i,q_i\) | Price and resting quantity at book level \(i\) | ch3 |
| \(x_t\) | Signed order/trade size (\(+{}\) buy, \(-{}\) sell) | ch3 |
| \(z_t\) | Position (inventory) held | ch3 |
| \(\Pi_t\) | Profit and loss (PnL) over interval \(t\) | ch3 |
| \(c_{\mathrm t},c_{\mathrm m}\) | Taker / maker fee rate | ch3 |
| \(M_t\) | Mark price (perpetual) | ch4 |
| \(O_t\) | Oracle / index reference price | ch4 |
| \(\mathrm{prem}_t\) | Premium index, \((M_t-O_t)/O_t\) | ch4 |
| \(f_t\) | Funding rate for interval ending at \(t\) | ch4 |
| \(p\in[0,1]\) | Binary-contract price = implied probability (local to ch5) | ch5 |
| \(\mathcal S(q,y)\) | Scoring rule for forecast \(q\), outcome \(y\) | ch5 |
| \(\mathrm{BS},\mathrm{LS}\) | Brier score, log score | ch5 |
| \(C(\mathbf q)=b\log\sum_i e^{q_i/b}\) | LMSR cost function; \(b\) liquidity parameter | ch5 |
| \(x,y,k\) | AMM pool reserves; invariant \(x\cdot y=k\) | ch6 |
| \(L_{\mathrm{v3}}\coloneqq\sqrt{xy}\) | v3 "virtual liquidity" (locally defined at point of use) | ch6 |
| \(\mathrm{IL}(r)\) | Impermanent-loss function of price ratio \(r\) | ch6 |
| \(r_t^{(s)},r_t^{(b)}\) | Strategy return, benchmark return | ch8 |
| \(W\) (window), \(k\) (horizon), \(e\) (embargo) | Look-back window length; label horizon; embargo length | ch8–11 |
| \(N_{\mathrm{trials}}\) | Number of strategies/variants tested | ch9 |
| \(\mathrm{SR}\) | Sharpe ratio \(\mu/\sigma\) (annualised as stated); \(\mathrm{DSR}\) deflated Sharpe | ch12 |
| \(\mathrm{VaR}_\alpha,\mathrm{ES}_\alpha\) | Value at risk, expected shortfall at level \(\alpha\) | ch14 |
| \(f^*\) | Kelly optimal fraction; \(g(f)\) growth rate of fraction \(f\) | ch13 |
| \(\beta\) | Market beta of a return stream | ch14 |
| \(\mathrm{slip}_t\) | Slippage (fill price minus decision price) | ch10 |

## Collisions and their local resolutions (per approved decision 2)

| Symbol | Collision | Resolution |
|---|---|---|
| \(\sigma\) | Volatility (this book) vs sigmoid (shared ML) | Never used as sigmoid in this book; "volatility \(\sigma\)" defined at ch1 first use. |
| \(\lambda\) | EWMA decay / Poisson rate vs eigenvalues, regularisation, Lagrange | This book avoids \(\lambda\) for decay — uses \(\alpha\) (smoothing weight); \(\lambda\) keeps shared roles. |
| \(\Sigma\) | Covariance matrix vs SVD diagonal | Write \(\Sigma\) only for covariance here; SVD not used in Book 6. |
| \(S_t\) | Spread vs sample sd \(s\)/\(s^2\) | Case contrast: uppercase \(S_t\) is spread; lowercase \(s\) stays sample sd. No chapter uses both bare. |
| \(f_t\) vs \(f^*\) | Funding rate vs Kelly fraction | Different parts (ch4 vs ch13); each redefined at point of use; never co-occur. |
| \(L_t\) | Not used — OHLC written lowercase \(o_t,h_t,l_t,c_t\), so \(L(\theta)\) likelihood keeps its meaning. Note: lowercase \(l_t\) (low) vs calligraphic \(\ell\) (loss/log-lik) — flagged in text once. | ch1 convention note. |
| \(L_{\mathrm{v3}}\) | v3 liquidity vs likelihood \(L\) | Always written \(L_{\mathrm{v3}}\) and defined at point of use (ch6 only). |
| \(p\) | Binary-contract price (ch5) vs book-level price \(p_i\) (ch3) vs pdf \(p(x)\) | Ch5 notes the local \(p\in[0,1]\); ch3 uses indexed \(p_i\); no mixing in one display. |
| \(O_t\) | Oracle/index price vs open \(o_t\) | Case contrast \(O_t\) oracle vs \(o_t\) open; defined once in ch4. |
| \(\alpha\) | Significance level vs EWMA smoothing weight vs VaR level | Role stated at point of use; \(\mathrm{VaR}_\alpha\) keeps subscript form. |
| \(\mathbf w\) | Portfolio weights (shared) vs nothing else | Consistent; no local reuse. |

## Conventions

- Discrete bar times \(t=1,\dots,T\); decision at \(t\) uses data \(\le t\) (the book's load-bearing
  convention, stated in ch1 and enforced by the harness).
- Annualisation always states its factor explicitly ("×\(\sqrt{365}\) for daily crypto bars") — never
  a bare annualised number.
- Costs quoted in basis points written `bp` in text, decimal in formulas.
- All venue-rule statements carry `(docs, accessed YYYY-MM-DD)`; unverifiable ones also get
  `\textbf{[unverified]}`.
