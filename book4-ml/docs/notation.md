# Notation — Book 4 (textbook-ml)

Cross-book notation for Books 3/4/6 is fixed in `docs/notation-shared.md` and is **binding**:
it is copied verbatim below for reference and may not be redefined. This file only *adds*
ML-specific symbols and names, and lists every accepted symbol collision with its local
resolution (per the 2026-10-10 approved decisions).

## 1. Shared notation (verbatim from `notation-shared.md` — binding)

- $\mathbb N=\{1,2,\dots\}$; $\mathbb{Z}_{\ge 0}$ when zero is needed; $[n]=\{1,\dots,n\}$; $|A|$ cardinality.
- $\log$ = natural log everywhere; other bases explicit ($\log_2$); $\ln$ never used except when contrasting bases.
- Vectors bold lowercase Roman, column vectors: $\mathbf x,\mathbf w,\boldsymbol\theta$; components $x_i$; row vectors $\mathbf x^T$.
- Matrices plain uppercase Roman: $A,X,\Sigma$; $\mathbf 0$; $I_n$; $A^T$, $A^{-1}$, $A^{+}$, $\det A$, $\operatorname{tr}A$, $\operatorname{rank}A$, $\operatorname{diag}(\cdot)$.
- Inner product $\langle\mathbf x,\mathbf y\rangle$; norms $\|\mathbf x\|,\|\mathbf x\|_p$.
- Dataset $\mathcal D=\{(\mathbf x_i,y_i)\}_{i=1}^{n}$; design matrix $X\in\mathbb R^{n\times d}$, one row per sample.
- Targets $\mathbf y$, predictions $\hat{\mathbf y}$, residual $e=y-\hat y$, noise $\varepsilon$.
- Parameters $\boldsymbol\theta$ (or $\mathbf w$ linear weights); estimates $\hat\theta$; feature map $\phi(\mathbf x)$.
- $A=QR$, $A=Q\Lambda Q^T$ (spectral), $A=U\Sigma V^T$ (SVD, $\sigma_i$ descending), $\kappa(A)$ condition number.
- $\nabla f$ column gradient; Jacobian $J_{\mathbf f}$ numerator layout; Hessian $H_f$; iterates $\theta^{(t)}$; learning rate $\eta$; $\arg\min/\arg\max$.
- Per-sample loss $\ell(\hat y,y)$; empirical loss $\mathcal L(\theta)=\tfrac1n\sum_i\ell(\hat y_i,y_i)$; likelihood $L(\theta)$; log-likelihood $\ell(\theta)$; $\mathrm{NLL}(\theta)$.
- Sigmoid $\sigma(z)$; softmax written $\operatorname{softmax}(\mathbf z)_i$.
- Regularisation $\lambda\|\boldsymbol\theta\|_2^2$ or $\lambda\|\boldsymbol\theta\|_1$.
- $\Pr[\cdot]$, $\mathbb E[\cdot]$, $\operatorname{Var}[\cdot]$, $\operatorname{Cov}[\cdot,\cdot]$, indicator $\mathbb 1\{\cdot\}$ — square brackets throughout.
- Distributions: $\mathrm{Bernoulli}(p)$, $\mathrm{Binomial}(n,p)$, $\mathrm{Poisson}(\lambda)$, $\mathrm{Uniform}(a,b)$, $\mathrm{Exponential}(\lambda)$, $\mathcal N(\mu,\sigma^2)$, $\mathcal N(\boldsymbol\mu,\Sigma)$; $X\sim\mathcal D$.
- pdf/pmf $p(x)$ or $p_X(x)$; cdf $F_X$; standard normal CDF $\Phi$ (standard normal density written out, never named $\phi$).
- $\bar x$, $s^2$, $\hat\theta$.
- Information: $H(X)$ entropy in nats ($H_2$ in bits), $H(p,q)$ cross-entropy, $D_{\mathrm{KL}}(p\|q)$, $I(X;Y)$.
- **Book-4 shared additions (already in the shared file):** layer index superscript $\mathbf h^{(\ell)}$, weight matrices $W^{(\ell)}$; activations named per function ($\operatorname{softmax}$, $\operatorname{ReLU}$ written out).

## 2. Book-4 additions (do not contradict the shared file)

| Symbol / macro | Meaning | First used |
|---|---|---|
| $\mathcal D_{\mathrm{train}},\mathcal D_{\mathrm{val}},\mathcal D_{\mathrm{test}}$ | Dataset splits (subscripts on shared $\mathcal D$) | ch3 |
| $\mathrm{TP},\mathrm{FP},\mathrm{TN},\mathrm{FN}$ | Confusion-matrix counts | ch3 |
| $\operatorname{precision},\operatorname{recall},\mathrm F_1,\operatorname{accuracy},\operatorname{AUC}$ | Metric names as operators (spelled, not single letters) | ch3 |
| $R^2$ | Coefficient of determination | ch3 |
| $\mathcal V$, $|\mathcal V|$ | Vocabulary (calligraphic, distinct from SVD matrix $V$) and its size | ch10 |
| $x_{1:T}$, $T$ | Sequence and its length | ch10 |
| $Q,K,V$ | Attention query/key/value matrices; $d_k,d_v$ their head widths | ch11 |
| $d_{\mathrm{model}}$ | Transformer residual-stream width | ch11 |
| $\mathbf P$, $\mathrm{PE}(\cdot)$ | Positional-encoding matrix / function | ch11 |
| $\tau$ | Sampling temperature (generative chapters only — see collision list) | ch10 |
| $\operatorname{PPL}=\exp(\mathrm{NLL}/T)$ | Perplexity of a language model | ch10 |
| $\mathbf z$ | Latent vector / pre-activation logits (context names it each time) | ch12 |
| $m_t,v_t$ | Adam's first/second moment estimates (subscript $t$) | ch8 |
| $B$, $|B|$ | Minibatch (a subset of indices) and batch size | ch7 |
| $a(\cdot)$ | Generic activation function; $\operatorname{ReLU},\tanh,\sigma$ named | ch7 |
| $\mathcal S,\mathcal A,P(\cdot\mid s,a),r(s,a,s'),\gamma$ | RL state set, action set, transition kernel, reward, discount | ch13 |
| $\pi(a\mid s)$ | Policy (always carries its argument) | ch13 |
| $V^\pi(s),Q^\pi(s,a)$ | Value functions (always superscripted $\pi$ or $*$) | ch13 |
| $G_t=\sum_{k\ge0}\gamma^k r_{t+k+1}$ | Discounted return | ch13 |
| $\varepsilon_{\mathrm{greedy}}$ written $\varepsilon$ locally | Exploration rate in ch13 only (see collisions) | ch13 |
| $\mathrm{PSI}$ | Population stability index (drift statistic, defined at use) | ch14 |
| $\mathrm{BLEU},\mathrm{ROUGE},\kappa_{\mathrm{Cohen}}$ | Text-eval metrics and inter-rater coefficient (spelled names) | ch15 |
| $\operatorname{ELBO}(\theta,\phi;\mathbf x)$ | Evidence lower bound | ch12 |

## 3. Accepted collisions and their local resolutions (per approved decision #2)

| Symbol | Meanings | Resolution in this book |
|---|---|---|
| $\sigma$ | sigmoid / singular values $\sigma_i$ | Shared file accepts this. Within any chapter it means one thing; in ch6 (SVD/PCA) $\sigma_i$ = singular values and the sigmoid is written $\operatorname{sigmoid}(z)$; everywhere else $\sigma(z)$ = sigmoid. |
| $\lambda$ | regularisation strength / eigenvalues $\lambda_i$ / Lagrange multipliers / Poisson rate | Accepted. Indexed $\lambda_i$ = eigenvalues; scalar $\lambda$ in loss context = regularisation; redefined at point of use otherwise. |
| $\Sigma$ | covariance matrix / SVD diagonal | Accepted. When a chapter needs both (ch6, ch12), the SVD diagonal is named $\Sigma_V$ explicitly. |
| $\phi$ vs $\Phi$ | feature map / standard normal CDF | Accepted (shared). |
| $\varepsilon$ | noise term / $\varepsilon$-greedy exploration rate | New, book-local. Noise $\varepsilon$ appears in ch3–4, ch12; exploration $\varepsilon$ appears only in ch13, where noise never occurs. If both ever meet, exploration is spelled $\varepsilon_{\mathrm{greedy}}$. |
| $V$ | SVD right-factor / value function / vocabulary | New, book-local. SVD's $V$ is confined to ch6 (and Book 3 references); value functions always carry a superscript ($V^\pi,V^*$) in ch13; vocabulary is calligraphic $\mathcal V$ (ch10+). |
| $K$ | attention key matrix / kernel / cluster count | New, book-local. Cluster count is lowercase $k$ (scalar, ch6); conv kernels are treated as weights $W$ (ch9 — a kernel *is* a weight); matrix $K$ = attention keys only in ch10–11. |
| $\pi$ | policy / circle constant | New, book-local. Policy always written $\pi(a\mid s)$ or $\pi_\theta$; the constant $3.14159\ldots$ is rare in this book and spelled out if it co-occurs. |
| $Q$ | QR factor / attention queries / action-value function $Q(s,a)$ | New, book-local. QR only in ch6 (decomposition recap); attention $Q$ only in ch10–11; $Q$-function only in ch13. |
| $\tau$ | sampling temperature / RL trajectory | New, book-local. $\tau$ = temperature only in ch10–12 sampling contexts; trajectories are written $(s_0,a_0,r_1,\dots)$ in words in ch13 — no $\tau$ there. |
| $\ell$ | per-sample loss / log-likelihood / layer index $\ell$ | Accepted (shared). Role is fixed by arguments vs superscripts: $\ell(\hat y,y)$ and $\ell(\theta)$ take parentheses; layer index is parenthesised superscript ${}^{(\ell)}$. |

## 4. Conventions beyond symbols

- Layer indexing: superscript $(\ell)$, $\ell=1..L$; input is $\mathbf h^{(0)}=\mathbf x$.
- Training iterates superscript $(t)$ on parameters: $\theta^{(t)}$ (shared). Epoch vs step stated in words at first use.
- Code-style identifiers stay in texttt/ascii: `train_test_split`, `predict`, `loss.item()` — never math-mode.
- Dataset names in text are code-quoted (`digits`, `titanic`); math dataset symbol is $\mathcal D$.
- Confusion matrix $C$ with $C_{ij}$ = count of true-$i$ predicted-$j$ (stated at first use, ch3).
- All probability square-bracket forms are non-negotiable (shared file).
