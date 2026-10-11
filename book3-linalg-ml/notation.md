# Notation — Book 3 (`textbook-linalg-ml`)

This book is the notation leader: Books 4 (ML) and 6 (quant) inherit the shared subset
(`docs/notation-shared.md` seeds it). Conventions are fixed once, stated early, and used
without exception. The table's "First used" column refers to chapters in `docs/outline.md`.

## Stated conventions (read before the table)

- **Vectors** are bold lowercase Roman: $\mathbf{x}$, $\mathbf{v}$, $\boldsymbol\theta$.
  Vectors are **column vectors**; row vectors are written $\mathbf{x}^T$.
- **Matrices** are plain uppercase Roman: $A$, $X$, $\Sigma$. A matrix is *not* bold —
  the bold/plain contrast separates matrices from vectors.
- **Scalars** are lightface italic: $x$, $\lambda$, $\alpha$.
- **Random variables** are lightface uppercase: $X$, $Y$; their values lowercase: $X=x$.
- **Estimators and predictions** wear hats: $\hat\theta$, $\hat{\mathbf x}$, $\hat y$.
- **Sets and spaces** are blackboard bold ($\mathbb{R}^n$) for named spaces and calligraphic
  ($\mathcal{B}$, $\mathcal{D}$, $\mathcal{N}$) for bases, datasets and families.
- **Layout convention for derivatives (the one everyone trips on):** the gradient $\nabla f$
  of a scalar field is a **column vector**; the Jacobian $J_{\mathbf f}(\mathbf x)$ of
  $\mathbf f:\mathbb{R}^n\to\mathbb{R}^m$ is the $m\times n$ matrix
  $[\,\partial f_i/\partial x_j\,]$ ("numerator layout": one row per output). The chain rule
  then reads $J_{\mathbf g\circ \mathbf f} = J_{\mathbf g}\,J_{\mathbf f}$ with matrices in
  the natural order. We say this once, loudly, in ch.11 and never deviate — it is the exact
  spot where MML readers filed confusion issues.
- **Logs:** $\log$ is natural logarithm throughout; information quantities in bits are written
  $H_2$ or "in bits" with $\log_2$ made explicit. Cross-entropy loss uses $\ln$.
- **Deliberate symbol collisions, kept and flagged** (each is the universal convention in its
  own field; context and index distinguish them): $\sigma_i$ singular values vs. $\sigma(\cdot)$
  the sigmoid; $\lambda_i$ eigenvalues vs. $\lambda$ regularization/Lagrange multiplier;
  $\Sigma$ covariance/singular-value matrix (context always explicit); $\phi(\mathbf x)$
  feature map vs. $\Phi$ the standard normal CDF (the standard normal *density* is always
  written out explicitly and never named $\phi$, to remove that ambiguity).

## Symbol table

| Symbol / macro | Meaning | First used |
|---|---|---|
| $\mathbb{R},\ \mathbb{N},\ \mathbb{Z},\ \mathbb{C}$ | real numbers, naturals, integers, complex numbers | ch.1 |
| $\mathbb{R}^n$ | Euclidean $n$-space, column vectors | ch.1 |
| $\mathbb{R}^{m\times n}$ | space of $m\times n$ real matrices | ch.2 |
| $\mathbf{x},\mathbf{v},\mathbf{w},\mathbf{b}$ | vectors (columns) | ch.1 |
| $x_i$ | $i$-th component of vector $\mathbf x$ | ch.1 |
| $\mathbf{e}_1,\dots,\mathbf{e}_n$ | standard basis vectors | ch.3 |
| $\mathbf{0}$ | zero vector | ch.1 |
| $A,B,X,\Sigma$ | matrices | ch.1–2 |
| $a_{ij}$ / $(A)_{ij}$ | entry of a matrix | ch.2 |
| $I_n$ | $n\times n$ identity matrix | ch.2 |
| $A^T$ | transpose | ch.2 |
| $A^{-1}$ | matrix inverse | ch.2 |
| $\overline{A}$ or $A^{*}$; $A^H$ | conjugate / conjugate-transpose (remark-level; book is real-valued) | ch.9 |
| $PA=LU$ | LU factorization with permutation | ch.1 |
| $A=QR$ | QR factorization, $Q$ orthogonal | ch.5 |
| $V,\Lambda$ | eigenvector matrix, diagonal eigenvalue matrix in $A=V\Lambda V^{-1}$ | ch.7 |
| $A=Q\Lambda Q^T$ | spectral decomposition (symmetric $A$) | ch.9 |
| $A=U\Sigma V^T$ | singular value decomposition | ch.10 |
| $\sigma_i(A)$ | $i$-th singular value of $A$, ordered $\sigma_1\ge\sigma_2\ge\cdots$ | ch.10 |
| $A_k=U_k\Sigma_kV_k^T$ | rank-$k$ truncated SVD | ch.10 |
| $A^{+}$ | Moore–Penrose pseudoinverse (NumPy `pinv`) | ch.10 |
| $\det A$, $\lvert A\rvert$ | determinant | ch.6 |
| $\operatorname{adj}(A)$ | adjugate (cofactor) matrix | ch.6 |
| $\operatorname{tr}(A)$ | trace | ch.6 |
| $\operatorname{rank}(A)$ | rank | ch.3 |
| $\operatorname{col}(A),\ \operatorname{row}(A)$ | column space, row space | ch.3 |
| $\ker(A)$ | null space / kernel of $A$ (never $\mathcal{N}(A)$ — see $\mathcal{N}$ below) | ch.3 |
| $\dim(V)$ | dimension of a space | ch.3 |
| $V,W,U$ | vector spaces | ch.3 |
| $\operatorname{span}\{\mathbf v_1,\dots,\mathbf v_k\}$ | span | ch.3 |
| $\mathcal{B},\mathcal{C}$ | ordered bases | ch.4 |
| $[\mathbf v]_{\mathcal B}$ | coordinate vector of $\mathbf v$ in basis $\mathcal B$ | ch.4 |
| $T:V\to W$ | linear map | ch.4 |
| $[T]_{\mathcal C\leftarrow\mathcal B}$ | matrix of $T$ sending $\mathcal B$-coordinates to $\mathcal C$-coordinates | ch.4 |
| $\ker T,\ \operatorname{im} T$ | kernel and image of a linear map | ch.4 |
| $\kappa(A)$ | condition number $\sigma_1/\sigma_n$ | ch.8 |
| $\langle \mathbf x,\mathbf y\rangle$ | inner product; in $\mathbb{R}^n$, $=\mathbf x^T\mathbf y$ (both forms taught, angle brackets primary) | ch.5 |
| $\|\mathbf x\|$ | norm; $\|\mathbf x\|_2$ Euclidean, $\|\mathbf x\|_p$ the $p$-norm | ch.5 |
| $\mathbf x\perp\mathbf y$ | orthogonality | ch.5 |
| $S^\perp$ | orthogonal complement | ch.5 |
| $P=A(A^TA)^{-1}A^T$ | projection matrix onto $\operatorname{col}(A)$ | ch.5 |
| $\partial f/\partial x_i$ | partial derivative | ch.11 |
| $\nabla f$ | gradient, **column vector** | ch.11 |
| $J_{\mathbf f}(\mathbf x)=\partial \mathbf f/\partial \mathbf x$ | Jacobian, $m\times n$, numerator layout | ch.11 |
| $H_f=\nabla^2 f$ | Hessian | ch.11 |
| $Df$ | total derivative (used sparingly, when emphasizing maps) | ch.11 |
| $f',\ \dot f$ | ordinary derivative notations | ch.11 |
| $f\circ g$ | composition | ch.4 |
| $\Pr[A]$ | probability of event $A$ | ch.12 |
| $\Pr[A\mid B]$ | conditional probability | ch.12 |
| $X\sim\mathrm{Bernoulli}(p),\ \mathrm{Binomial}(n,p),\ \mathrm{Poisson}(\lambda),\ \mathrm{Uniform}(a,b),\ \mathrm{Exponential}(\lambda),\ \mathcal{N}(\mu,\sigma^2)$ | named distributions; $X\sim$ reads "distributed as" | ch.12 |
| $\mathcal{N}(\boldsymbol\mu,\Sigma)$ | multivariate Gaussian | ch.12 |
| $p(x)$, $p_{X}(x)$ | pmf/pdf; subscript added when ambiguous | ch.12 |
| $F_X(x)=\Pr[X\le x]$ | cumulative distribution function | ch.12 |
| $\mathbb{E}[X]$ | expectation; $\mathbb{E}_{X\sim p}[\,\cdot\,]$ when the law matters | ch.12 |
| $\operatorname{Var}[X]$ | variance | ch.12 |
| $\operatorname{Cov}[X,Y]$ | covariance | ch.12 |
| $\operatorname{corr}(X,Y)$ | correlation | ch.12 |
| $\mathbb{1}\{\cdot\}$ | indicator function | ch.12 |
| $\Phi$ | standard normal CDF (density always written out) | ch.12 |
| $\bar x$ | sample mean | ch.13 |
| $s^2$ | sample variance | ch.13 |
| $\hat\theta,\ \hat{\boldsymbol\theta}$ | estimator / estimate | ch.13 |
| $L(\theta)$ | likelihood function (plain $L$ — never $\mathcal L$, which is loss) | ch.13 |
| $\ell(\theta)=\log L(\theta)$ | log-likelihood | ch.13 |
| $\mathrm{NLL}(\theta)$ | negative log-likelihood | ch.13 |
| $p(\theta)$, $p(\theta\mid\mathcal D)$ | prior, posterior densities | ch.13 |
| $\mathcal{D}=\{(\mathbf x_i,y_i)\}_{i=1}^{n}$ | dataset | ch.8 |
| $X\in\mathbb{R}^{n\times d}$ | design matrix, **one row per sample**, row $i$ is $\mathbf x_i^T$ | ch.8 |
| $\mathbf y$, $\hat{\mathbf y}$ | targets, predictions | ch.8 |
| $e_i=y_i-\hat y_i$ | residual | ch.8 |
| $\varepsilon_i$ | noise term in a generative model | ch.13 |
| $\phi(\mathbf x)$ | feature map / basis expansion | ch.8 |
| $R^2$ | coefficient of determination | ch.8 |
| $\ell(\hat y,y)$ | per-sample loss function | ch.13 |
| $\mathcal{L}(\theta)=\frac1n\sum_i\ell(\hat y_i,y_i)$ | empirical loss / cost (calligraphic $\mathcal L$ is loss only) | ch.13 |
| $J(\theta)$ | generic objective when a neutral letter is wanted | ch.14 |
| $\arg\min_x,\ \arg\max_x$ | optimizing argument | ch.8 |
| $\eta$ | learning rate / step size | ch.14 |
| $\theta^{(t)}$ | parameter iterate at step $t$ (parenthesized index, never a component) | ch.14 |
| $\lambda$ | Lagrange multiplier / regularization strength (context-flagged vs. eigenvalues) | ch.14 |
| $\sigma(z)=1/(1+e^{-z})$ | sigmoid (context-flagged vs. singular values) | ch.13 |
| $\propto$ | proportional to | ch.13 |
| $\coloneqq$ | "is defined as" | ch.1 |
| $\approx$ | approximately equal | ch.1 |
| $H(X)$, $H_2(X)$ | entropy (nats; bits when marked) | ch.15 |
| $H(p,q)$ | cross-entropy | ch.15 |
| $D_{\mathrm{KL}}(p\Vert q)$ | Kullback–Leibler divergence | ch.15 |
| $I(X;Y)$ | mutual information | ch.15 |
| $O(\cdot)$ | big-O complexity | ch.1 |
| $\sum,\prod$ | summation, product | ch.1 |
| $\implies,\ \iff$ | implication, equivalence | ch.3 |
| $\forall,\exists$ | quantifiers (used sparingly in prose) | ch.3 |
| $\{x\in S : \dots\}$ | set-builder notation | ch.3 |
| $\lfloor x\rfloor,\lceil x\rceil$ | floor, ceiling | ch.12 |
| $\lvert S\rvert$ vs. $\lvert x\rvert$ vs. $\lvert A\rvert$ | cardinality vs. absolute value vs. determinant — distinguished by operand type | ch.12 |
