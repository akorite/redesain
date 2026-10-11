# Shared notation — binding for Books 3 (linalg-ml), 4 (ml), 6 (quant)

**Status:** awaiting user approval (§5.2). Once approved, this file is copied verbatim into
`docs/notation-shared.md` of `textbook-linalg-ml`, `textbook-ml`, `textbook-quant`, and every
chapter of those books must conform. Books 1, 2, 5, 7, 8 are asked to adopt any non-conflicting
piece so the eight books read as one library.

Assembled by the coordinator from Book 3's notation-leader proposal plus Book 2's and Book 5's
cross-book asks. Spine = Book 3; additions marked.

## Foundations (coordinator addition, from Book 2's proposals)

- Number sets $\mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R},\mathbb{C}$ in blackboard bold.
  **Convention: $\mathbb{N}=\{1,2,\dots\}$** (matches dataset indexing $i=1..n$ and Book 2's
  olympiad convention); write $\mathbb{Z}_{\ge 0}$ when zero is needed.
- $[n]=\{1,\dots,n\}$. $|A|$ cardinality; $\#A$ avoided (Book 2 agrees: $|x|$/context splits).
- $\binom{n}{k}$, $[x^n]F(x)$ coefficient extraction.
- Sums always carry explicit bounds ($\sum_{k=1}^{n}$, $\sum_{d\mid n}$), never a bare $\sum$.
- Functions $f:A\to B$ with named domain/codomain; injective/surjective/bijective as words.
- **Log convention (decision needed, see review memo):** $\log$ = natural logarithm
  throughout books 3/4/6; $\log_2$ flagged explicitly for bits. $\ln$ is not used.
  (Book 2 currently uses $\ln$ — harmonization question for the user.)
- "i.i.d." spelled out at first use. $\square$ ends proofs (style file provides).

## Vectors, matrices, data

- Vectors: bold lowercase Roman, column vectors — $\mathbf{x},\mathbf{w},\boldsymbol\theta$;
  row vectors as $\mathbf{x}^T$. Components $x_i$.
- Matrices: plain uppercase Roman — $A,X,\Sigma$. Zero vector $\mathbf 0$; identity $I_n$.
- Transpose $A^T$, inverse $A^{-1}$, pseudoinverse $A^{+}$, $\det A$, $\operatorname{tr}A$,
  $\operatorname{rank}A$, $\operatorname{diag}(a_1,\dots)$.
- Inner product $\langle\mathbf x,\mathbf y\rangle$ (=$\mathbf x^T\mathbf y$ in $\mathbb R^n$);
  norm $\|\mathbf x\|$, $\|\mathbf x\|_p$.
- Dataset: $\mathcal D=\{(\mathbf x_i,y_i)\}_{i=1}^{n}$. Design matrix
  $X\in\mathbb{R}^{n\times d}$ with **one row per sample** (row $i$ is $\mathbf x_i^T$).
  Targets $\mathbf y$, predictions $\hat{\mathbf y}$, residual $e=y-\hat y$, noise
  $\varepsilon$.
- Parameters $\boldsymbol\theta$ (or $\mathbf w$ for linear weights); estimates $\hat\theta$;
  feature map $\phi(\mathbf x)$.
- Decompositions: $A=QR$, $A=V\Lambda V^{-1}$, $A=Q\Lambda Q^T$ (spectral),
  $A=U\Sigma V^T$ (SVD, $\sigma_i$ descending), $\kappa(A)$ condition number.

## Calculus

- $\nabla f$ gradient = column vector; Jacobian $J_{\mathbf f}=[\partial f_i/\partial x_j]$
  ($m\times n$, numerator layout, one row per output); Hessian $H_f=\nabla^2f$.
  Chain rule $J_{\mathbf g\circ\mathbf f}=J_{\mathbf g}J_{\mathbf f}$ in natural order.
- Iterates $\theta^{(t)}$; learning rate $\eta$; $\arg\min$, $\arg\max$; $\coloneqq$,
  $\approx$, $\propto$.

## Losses and likelihoods

- Per-sample loss $\ell(\hat y,y)$; empirical loss
  $\mathcal{L}(\theta)=\frac1n\sum_i\ell(\hat y_i,y_i)$ — calligraphic $\mathcal L$ is loss only.
- Likelihood $L(\theta)$ (plain $L$), log-likelihood $\ell(\theta)$ — deliberate
  case contrast $\mathcal L$ (loss) vs. $L$ (likelihood) vs. $\ell$ (log-likelihood and
  per-sample loss; role always clear from arguments).
- $\mathrm{NLL}(\theta)$ negative log-likelihood; sigmoid $\sigma(z)$; softmax written
  $\operatorname{softmax}(\mathbf z)_i$ in full.
- Regularization: penalty $\lambda\|\boldsymbol\theta\|_2^2$ or $\lambda\|\boldsymbol\theta\|_1$;
  $\lambda$ flagged vs. eigenvalues by context.

## Probability and statistics

- $\Pr[A]$, $\Pr[A\mid B]$; $\mathbb E[X]$, $\mathbb E_{X\sim p}[\cdot]$;
  $\operatorname{Var}[X]$; $\operatorname{Cov}[X,Y]$; $\operatorname{corr}(X,Y)$;
  indicator $\mathbb 1\{\cdot\}$ — **square brackets throughout this family**
  (Book 2 agrees; Book 2's own `Var(X)` is amended to `Var[X]` for consistency).
- Random variables lightface uppercase $X,Y$; values lowercase.
- Distributions: $\mathrm{Bernoulli}(p)$, $\mathrm{Binomial}(n,p)$, $\mathrm{Poisson}(\lambda)$,
  $\mathrm{Uniform}(a,b)$, $\mathrm{Exponential}(\lambda)$, $\mathcal N(\mu,\sigma^2)$,
  multivariate $\mathcal N(\boldsymbol\mu,\Sigma)$; $X\sim\mathcal D$.
- pdf/pmf $p(x)$ or $p_X(x)$; cdf $F_X$; standard normal CDF $\Phi$ (standard normal density
  always written out, never named $\phi$ — $\phi$ stays free for feature maps).
- Sample statistics: $\bar x$, $s^2$, $\hat\theta$.
- Information: $H(X)$ entropy (nats; $H_2$ in bits), $H(p,q)$ cross-entropy,
  $D_{\mathrm{KL}}(p\|q)$, $I(X;Y)$ mutual information.

## Accepted collisions (disambiguated by index/context)

- $\sigma_i$ singular values / $\sigma(\cdot)$ sigmoid / (Book 6) $\sigma$ volatility.
- $\lambda_i$ eigenvalues / $\lambda$ regularization, Lagrange multiplier / (Book 6, prob.)
  Poisson/Exponential rate.
- $\Sigma$ covariance vs. SVD diagonal matrix — always named explicitly (e.g. $\Sigma_V$)
  when a chapter needs both.
- $\phi$ feature map / $\Phi$ normal CDF.

## Per-book additions (on top, never contradicting)

- **Book 4 (ml):** layer index superscript $\mathbf h^{(\ell)}$, weight matrices $W^{(\ell)}$,
  activations named per function ($\operatorname{softmax}$, $\operatorname{ReLU}$ written out).
- **Book 6 (quant):** time index $t$ as subscript ($r_t$, $P_t$), portfolio weights
  $\mathbf w$, returns $r_t=\log(P_t/P_{t-1})$.

## Non-negotiables

Column-vector gradients; numerator-layout Jacobians; rows-are-samples design matrix;
$\mathcal L$=loss / $L$=likelihood split; square-bracket probability family
$\Pr[\cdot],\mathbb E[\cdot],\operatorname{Var}[\cdot]$; $\mathbb N=\{1,2,\dots\}$.

## Open flags for the user (see review memo)

1. $\log$ vs $\ln$ — harmonize all 8 books on $\log$ = natural, or keep per-field conventions?
2. Accepted $\sigma$/$\lambda$ collisions — confirm.
3. Book 5's electronics notation (SI units, $v,i,R,C,L$ lowercase time-varying / uppercase
   DC, $\omega$, $\mathrm{j}=\sqrt{-1}$ chosen over $i$ to avoid current-clash) is book-local;
   Book 7 inherits it where applicable. Noted for the record, no conflict with this file.
