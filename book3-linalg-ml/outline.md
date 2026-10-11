# Outline — Book 3: Linear algebra and mathematics for machine learning (`textbook-linalg-ml`)

To be approved by the user before any chapter is written.

**Reader:** Calculus I; vectors from precalculus. Strong at maths and programming; self-studying.
**Promised outcomes:** reads and derives the mathematics in ML papers; implements SVD-based methods
without library calls. **Book-level rule (from the brief):** every theorem used in ML is tied to a
short numerical experiment in Python (NumPy); every chapter ends with a derivation the reader
completes by hand.

## Overall architecture

Five parts, 16 chapters, capstone distributed then consolidated:

- **Part I — Linear systems and vector spaces (ch.1–4).** Concrete computation first (Strang),
  abstraction second (Axler). The reader manipulates real matrices before meeting the axioms.
- **Part II — Geometry, eigenvalues and least squares (ch.5–8).** Orthogonality, determinants,
  eigen-decomposition, and the book's first ML payoff: least squares / linear regression.
- **Part III — Symmetric structure and data (ch.9–10).** Spectral theorem → SVD → PCA. Second
  ML payoff and the headline "SVD without library calls" skill.
- **Part IV — Calculus and probability (ch.11–13).** Gradients/Jacobians, probability, statistics
  (MLE/Bayes). The paper-reading toolkit.
- **Part V — Optimization, information, synthesis (ch.14–16).** Convexity and gradient descent,
  information theory, and the capstone chapter that assembles `mlscratch`.

**Ordering deviations from sources (deliberate):**

- Determinants sit mid-book (ch.6, after elimination/orthogonality, before eigenvalues) —
  Strang/VMLS order — *not* banished to the end as in Axler. Reason: the characteristic polynomial
  is the most concrete route to eigenvalues for a first course, and det-as-volume pays off
  geometrically before eigen pictures. Axler's abstract-first ordering is borrowed for ch.3–4
  rigor only.
- Vector spaces and linear maps come *after* matrices are already familiar (Strang-first,
  Axler-second), unlike both Axler (spaces first) and MML (algebraic structures first).
- Orthogonality precedes determinants (as in 18.06SC unit II and ILA): projections and QR are
  too useful to wait for, and determinants flow better just before the characteristic polynomial.
- MML's Part II (regression, PCA, GMM, SVM) is folded into the theory chapters rather than a
  separate applications part — the brief requires every ML-relevant theorem to get an experiment
  inline. Ch.16 then consolidates the four capstone artifacts.

**Chapter standard applied everywhere:** opening paragraph (purpose + outcome); motivation before
definitions; ≥3 worked examples (strategy before solution); ≥4 captioned, referenced,
regenerable figures; ≥3 Python listings with real printed output; inline numbered exercises where
the text assumes them solved; ≥10 additional graded exercises; a Common Mistakes section
(compulsory); a one-page cheat-sheet table; a Notes section citing sources by number; each
chapter ends with a named hand-derivation. At least one exercise per chapter asks the reader to
implement or derive something.

**Page budget:** front matter ~9 pp + chapters ~208 pp + back matter ~26 pp ≈ **243 pp**
(within the 150–250 bound; ch.12/15/16 carry trim margin if it runs long).

---

## Front matter (~9 pp)

- How to use this book (figure-first reading order, code alongside text, exercise discipline).
- Prerequisites and self-test: single-variable calculus; vector basics; a Python 3 + NumPy +
  matplotlib setup note pinned in `code/README.md`.
- Notation summary table (one page; full table in `docs/notation.md` and appendix A).

---

## Part I — Linear systems and vector spaces

### Chapter 1 — Linear systems and Gaussian elimination (~14 pp)

**Prerequisites:** front matter only (high-school simultaneous equations).
**Sections:** 1.1 Two ways to see Ax = b (row picture, column picture) · 1.2 Elimination to
echelon form · 1.3 Pivots, free variables, and the shape of a solution set · 1.4 LU
factorization (and PA = LU with row exchanges) · 1.5 Cost and stability: why elimination is
$O(n^3)$ and why we pivot.
**Worked examples (3):** (a) a 3×3 system eliminated step-by-step; (b) a singular system read for
its null space; (c) LU factorization of a 3×3 with one row swap.
**Figures (5):** row-vs-column picture of a 2×2 system; elimination as small multiples (3 states);
solution-set geometry (point/line/plane/none in $\mathbb{R}^3$); failure-without-pivoting diagram;
log-log cost plot of elimination time vs $n$.
**Code listings (3):** hand-rolled forward elimination + `np.linalg.solve` check; LU by hand vs
`scipy.linalg.lu`; timing loop producing the $n^3$ cost figure.
**Hand derivation:** prove the solution set of $Ax=b$ is a particular solution plus the null space.
**Inline exercises:** 4 (one per section 1.2–1.5; §1.2's asks for an elimination by hand).
**Additional exercises (12):** 4 [easy], 5 [medium], 3 [hard]; [hard] set includes implementing
partial pivoting and a structured (tridiagonal) system.
**Common mistakes:** sign errors in elimination bookkeeping; assuming every square system has a
unique solution; confusing pivot and free variables; solving without pivoting and trusting
garbage.
**Sources:** 18.06SC unit I; ILA ch.5; VMLS ch.8; MML §2.3.

### Chapter 2 — Matrices and matrix algebra (~12 pp)

**Prerequisites:** ch.1.
**Sections:** 2.1 A matrix is a box of coefficients — and a recipe · 2.2 $A\mathbf{x}$ as a column
combination · 2.3 Matrix multiplication as composition · 2.4 Transpose, inverses, and when they
exist · 2.5 Special matrices: diagonal, triangular, permutation, block.
**Worked examples (3):** (a) matrix-vector product as column combination on a 3×3; (b) verify
$(AB)^T = B^TA^T$ numerically then prove it; (c) Gauss–Jordan inverse of a 3×3.
**Figures (4):** $A\mathbf{x}$ as weighted column picture; $AB$ as a grid of inner products;
inverse as "undo" map; gallery of the special matrices acting on a shape.
**Code listings (3):** triple-loop `matmul` vs `np.matmul` (with timing); Gauss–Jordan inverse vs
`np.linalg.inv`; permutation matrices reordering a dataset.
**Hand derivation:** prove $(AB)^{-1}=B^{-1}A^{-1}$ and that matrix multiplication is associative
via composition.
**Inline exercises:** 3.
**Additional exercises (11):** 4 [easy], 4 [medium], 3 [hard]; [medium] includes deriving the
commutator $[A,B]=AB-BA$ for given pairs; [hard] includes a block-matrix product proof.
**Common mistakes:** assuming $AB=BA$; wrong order in $(AB)^T$; dimension mismatches read as
"almost right"; believing every nonzero matrix is invertible.
**Sources:** 18.06SC unit I; VMLS ch.6, 10; MML §2.2; ILA ch.6.

### Chapter 3 — Vector spaces, subspaces, and the four fundamental subspaces (~14 pp)

**Prerequisites:** ch.1–2.
**Sections:** 3.1 Vector spaces: axioms with motivation, not ceremony · 3.2 Subspaces · 3.3 Span,
linear independence · 3.4 Basis and dimension · 3.5 The four fundamental subspaces of $A$
(column, null, row, left-null) · 3.6 Rank and the rank–nullity theorem · 3.7 Coordinates.
**Worked examples (4):** (a) subspace test on a subset of $\mathbb{R}^3$; (b) null-space basis via
RREF; (c) dimension counting for $\mathbb{R}^{m\times n}$-valued spaces; (d) all four subspaces of
a 3×4 matrix.
**Figures (5):** subspace vs. not-a-subspace pictures; the four-subspaces diagram (domain and
codomain each split into two orthogonal pieces — the book's signature figure); basis and
coordinates in $\mathbb{R}^2$; rank–nullity counting diagram; spanning vs. independent vs. basis
Venn-style.
**Code listings (3):** RREF → null-space basis, checked against `scipy.linalg.null_space`;
rank = column rank = row rank verified on random matrices; dimension check of the four
subspaces on a small matrix.
**Hand derivation:** derive $\dim \operatorname{col}(A) + \dim \ker(A) = n$ by counting pivots and
free variables in RREF.
**Inline exercises:** 4.
**Additional exercises (12):** 4 [easy], 5 [medium], 3 [hard]; [hard] includes proving the row
space is preserved by row operations while the column space is not.
**Common mistakes:** treating "spanning" as "independent" (a basis needs both); assuming row
operations preserve the column space; dimension of a space vs. dimension of its ambient space;
declaring a set a subspace without checking all three properties.
**Sources:** 18.06SC unit I (signature content); Axler ch.1–2 (rigor register); VMLS ch.5;
MML §2.4–2.6.

### Chapter 4 — Linear maps and change of basis (~12 pp)

**Prerequisites:** ch.3.
**Sections:** 4.1 Linear maps: definition and examples · 4.2 Kernel and image · 4.3 Every linear
map is a matrix (representation of $T$) · 4.4 Change of basis and similarity · 4.5 A geometric
catalog: rotations, reflections, projections, shears.
**Worked examples (3):** (a) verify a given $T$ is linear and find its matrix; (b) matrices of
rotation, reflection, projection in $\mathbb{R}^2$; (c) change of basis: same map, new matrix,
verify by similarity.
**Figures (5):** linear map as grid deformation (unit square with a marker letter) —
rotation/reflection/shear/projection small multiples; kernel–image schematic; the same linear map
in two bases; composition = matrix product diagram; non-examples (affine vs. linear).
**Code listings (3):** transform a point cloud / simple image with each catalog map; build a
projection matrix from its formula and apply; change-of-basis check that two matrices represent
the same map.
**Hand derivation:** derive the 2×2 rotation matrix $R_\theta$ from trigonometry.
**Inline exercises:** 3.
**Additional exercises (11):** 4 [easy], 4 [medium], 3 [hard]; [hard] includes proving
$[S\circ T] = [S][T]$ and similarity as same-map-different-basis.
**Common mistakes:** confusing an abstract vector with its coordinate vector; forgetting basis
order matters; applying $[T]_{\mathcal B}$ to coordinates in the wrong basis; treating similar
matrices as identical.
**Sources:** Axler ch.3 (definition rigor); ILA ch.9; MML §2.7; 3b1b series (figure pedagogy).

---

## Part II — Geometry, eigenvalues and least squares

### Chapter 5 — Orthogonality, projections, and QR (~12 pp)

**Prerequisites:** ch.1–3.
**Sections:** 5.1 Inner product, norm, angle · 5.2 Orthogonal and orthonormal sets; orthogonal
matrices · 5.3 Projection onto a line and onto a subspace · 5.4 Gram–Schmidt and the QR
factorization · 5.5 Orthogonal complements (the four subspaces pair up).
**Worked examples (3):** (a) project $\mathbf b$ onto a line and a plane; (b) Gram–Schmidt on
three vectors by hand; (c) QR of a 3×3 and solving $Ax=b$ via it.
**Figures (5):** projection onto a line (with residual vector); projection onto a plane;
Gram–Schmidt step-by-step small multiples; orthogonal vs. skew bases spanning the same plane;
complementarity of the four subspaces.
**Code listings (3):** classical vs. modified Gram–Schmidt stability test (orthogonality drift);
$P = A(A^TA)^{-1}A^T$ projection verified to be idempotent; `np.linalg.qr` comparison.
**Hand derivation:** derive the projection formula $\mathbf p = \frac{\mathbf a^T\mathbf b}{\mathbf a^T\mathbf a}\,\mathbf a$
and the general projection matrix.
**Inline exercises:** 4.
**Additional exercises (12):** 4 [easy], 5 [medium], 3 [hard]; [hard] includes proving $P^2=P$,
$P^T=P$ characterize projections.
**Common mistakes:** projecting onto the wrong subspace; forgetting to normalize before
projecting onto a *direction*; numerical loss of orthogonality in classical Gram–Schmidt (real —
MML issue #815 showed context confusion); believing $A^TA$ is invertible unconditionally.
**Sources:** 18.06SC unit II; VMLS ch.5, 11; MML ch.3; ILA ch.3.

### Chapter 6 — Determinants (~10 pp)

**Prerequisites:** ch.1–2, 5.
**Sections:** 6.1 Three definitions that agree: cofactors, pivots, volume · 6.2 Properties:
product, transpose, effect of row operations · 6.3 Determinant as signed volume · 6.4 $\det A=0$
means collapse — invertibility again · 6.5 Cramer's rule as a theoretical curiosity.
**Worked examples (3):** (a) 3×3 by cofactors and by elimination, same answer; (b)
$\det(AB)=\det A\det B$ numeric check then proof sketch; (c) signed volume of a parallelepiped.
**Figures (4):** determinant as area/volume scaling under a linear map (3b1b-style); orientation
and sign flip; collapse picture for $\det A = 0$; cofactor checkerboard pattern.
**Code listings (3):** det via pivot product (with swap counting) vs `np.linalg.det`; volume
scaling experiment with random matrices; near-singular determinant vs. actual singularity.
**Hand derivation:** derive the 2×2 formula from elimination and show a row swap flips the sign.
**Inline exercises:** 3.
**Additional exercises (10):** 4 [easy], 4 [medium], 2 [hard]; [hard] includes proving
$\det(AB)=\det A\det B$ via elimination.
**Common mistakes:** $\det(A+B)\neq\det A+\det B$; sign bookkeeping on swaps (MML issue #826 is a
real learner stall here); using Cramer's rule for actual computation; reading "small det" as
"singular".
**Sources:** 18.06SC unit II; ILA ch.7; Axler ch.10 (contrast — determinants via multilinear
forms, mentioned in Notes); 3b1b volume pedagogy.

### Chapter 7 — Eigenvalues and diagonalisation (~14 pp)

**Prerequisites:** ch.3, 5, 6.
**Sections:** 7.1 The eigen equation $A\mathbf v=\lambda\mathbf v$ · 7.2 Characteristic polynomial
and how to find them by hand · 7.3 Eigenspaces and algebraic/geometric multiplicity · 7.4
Diagonalisation $A=V\Lambda V^{-1}$ and powers of $A$ · 7.5 Defective matrices · 7.6
Applications: linear recurrences, Markov chains, a taste of PageRank.
**Worked examples (4):** (a) full 2×2 eigen computation by hand; (b) diagonalise and compute
$A^{10}$ cheaply; (c) Fibonacci closed form via matrix powers; (d) Markov chain steady state.
**Figures (6):** eigenvectors as directions unchanged by the map (before/after panels);
complex eigenvalues as rotation; defective (shear) matrix with collapsed eigendirections;
power-iteration convergence sequence; Markov transition graph; dominant-eigenvalue geometry.
**Code listings (4):** eigen by hand vs `np.linalg.eig`; power iteration to the dominant
eigenpair; Markov chain simulated and compared to the steady state; Fibonacci via diagonalisation
vs. recursion timing.
**Hand derivation:** derive the closed form of the Fibonacci recurrence via diagonalising
$\begin{pmatrix}1&1\\1&0\end{pmatrix}$.
**Inline exercises:** 4.
**Additional exercises (13):** 4 [easy], 5 [medium], 4 [hard]; [hard] includes diagonalisability
criteria and a defective-matrix analysis.
**Common mistakes:** expecting real matrices to have real eigenvalues; sign errors in
$\det(A-\lambda I)$; assuming every matrix diagonalises; eigenvectors defined only up to scale
(and sign); confusing eigenvalues of $A$ and $A^2$.
**Sources:** 18.06SC unit II; Axler ch.5 (contrast — determinant-free eigen theory, in Notes);
ILA ch.10; MML §4.4; VMLS ch.9 (linear dynamics as the application framing).

### Chapter 8 — Least squares and linear regression (~14 pp) — *capstone piece 1*

**Prerequisites:** ch.5 (projections, QR); helpful: ch.7.
**Sections:** 8.1 Overdetermined systems and the best we can do · 8.2 Normal equations
$A^TA\hat{\mathbf x}=A^T\mathbf b$ via the projection argument · 8.3 Linear regression:
one feature, many features, intercept · 8.4 Feature maps and polynomial fitting; overfitting
preview · 8.5 Solving least squares in practice: QR, and why $A^TA$ squares the condition
number · 8.6 Residuals, $R^2$, and honest evaluation.
**Worked examples (4):** (a) line fit to four points through the normal equations by hand; (b)
regression with a quadratic feature map; (c) the same system solved via QR instead of $A^TA$;
(d) reading a residual plot.
**Figures (6):** least squares as projection of $\mathbf b$ onto $\operatorname{col}(A)$
(signature figure); fitted line with residual segments; underfit–good–overfit polynomial panel;
geometry of the normal equations; residual-vs-fitted diagnostic plot; train/test split diagram.
**Code listings (4):** normal equations solved from scratch; the same fit via `np.linalg.lstsq`
(QR/SVD internals) vs. the explicit $A^TA$ route on an ill-conditioned problem; polynomial
regression overfit demo; **capstone:** `mlscratch.LinearRegression` checked against
`sklearn.linear_model.LinearRegression` on a real-ish dataset.
**Hand derivation:** derive the normal equations from residual-orthogonality
$A^T(\mathbf b - A\hat{\mathbf x}) = \mathbf 0$ (calculus derivation deferred to ch.14 where it
belongs).
**Inline exercises:** 4.
**Additional exercises (13):** 4 [easy], 5 [medium], 4 [hard]; [hard] includes proving the
minimizer's uniqueness when $A$ has full column rank and a weighted-least-squares derivation.
**Common mistakes:** forgetting the intercept column; forming $A^TA$ when QR is cheaper and
stabler (condition number squaring — a real numerical pitfall); unscaled features wrecking
conditioning; evaluating on training data and calling it performance (first leak lesson);
$R^2$ as a certificate of causality.
**Sources:** VMLS part III (the primary model — least squares as the book's application spine);
18.06SC unit II; MML ch.9; ILA ch.5.

---

## Part III — Symmetric structure and data

### Chapter 9 — Symmetric matrices and the spectral theorem (~12 pp)

**Prerequisites:** ch.5, 7.
**Sections:** 9.1 Symmetric matrices and why they are special · 9.2 The spectral theorem
$A=Q\Lambda Q^T$ · 9.3 Quadratic forms and definiteness · 9.4 Positive (semi)definite matrices;
$A^TA$ is always PSD · 9.5 Rayleigh quotient · 9.6 Covariance matrices as the data-motivating
PSD.
**Worked examples (3):** (a) spectral decomposition of a 2×2 symmetric matrix; (b) definiteness
classification via eigenvalues and via pivots; (c) eigendecomposition of a small covariance
matrix.
**Figures (5):** quadratic-form level sets for positive-definite/indefinite/semidefinite cases;
spectral decomposition as rotate–stretch–rotate–back; ellipsoid axes = eigenvectors with
eigenvalue lengths; Rayleigh quotient landscape; covariance ellipse on real 2-D data.
**Code listings (3):** verify $A=Q\Lambda Q^T$ numerically on random symmetric matrices;
definiteness tests (eigenvalues vs. pivot signs); covariance-matrix eigendecomposition previewing
PCA directions.
**Hand derivation:** prove symmetric matrices have real eigenvalues and orthonormal
eigenvectors (the two short classic proofs).
**Inline exercises:** 4.
**Additional exercises (12):** 4 [easy], 5 [medium], 3 [hard]; [hard] includes the Rayleigh-quotient
min–max characterization.
**Common mistakes:** "real matrix ⇒ real eigenvalues" false generalization; PSD vs. PD vs.
indefinite confusion (MML issue #805 flagged this exact clarity gap); assuming $A^TA$ can be
negative definite; mixing up similarity with orthogonal similarity.
**Sources:** 18.06SC unit III; Axler ch.7; MML §3.5, ch.4; Strang LALD site (application framing).

### Chapter 10 — The SVD and PCA (~14 pp) — *capstone piece 2*

**Prerequisites:** ch.7, 9.
**Sections:** 10.1 Statement of the SVD, $A=U\Sigma V^T$ · 10.2 Geometry: unit sphere to
ellipsoid · 10.3 Rank, condition number, pseudoinverse $A^+$ via SVD · 10.4 Low-rank
approximation and Eckart–Young · 10.5 PCA: eigendecomposition of the covariance matrix = SVD of
centered data · 10.6 Uses: compression, denoising, a first look at embeddings.
**Worked examples (4):** (a) full SVD of a 2×2 by hand via $A^TA$; (b) truncated-SVD image
compression at several ranks; (c) PCA on a 2-D dataset end-to-end; (d) least-squares solution via
the pseudoinverse.
**Figures (6):** unit sphere → ellipsoid with $\sigma_i$ axes (signature); the four subspaces
revisited through $U$ and $V$; scree plot of singular values; image reconstruction at
$k=1,5,20,50$ small multiples; PCA projection of correlated 2-D data; explained-variance curve.
**Code listings (4):** SVD assembled from an eigendecomposition of $A^TA$ — with the numerical
caveat — vs. `np.linalg.svd`; image compressor script; **capstone:** `mlscratch.PCA` (centering,
SVD, projection, variance report) checked against `sklearn.decomposition.PCA` including
explained-variance ratios; pseudoinverse vs. `np.linalg.pinv`.
**Hand derivation:** derive that the singular values of $A$ are $\sqrt{\lambda_i(A^TA)}$ and
compute the SVD of a given 2×2.
**Inline exercises:** 4.
**Additional exercises (13):** 4 [easy], 5 [medium], 4 [hard]; [hard] includes proving
Eckart–Young for the spectral norm case and connecting PCA to total least squares.
**Common mistakes:** skipping the centering step in PCA (universally done wrong once);
computing SVD through $A^TA$ on ill-conditioned data (condition squaring, again); sign ambiguity
of singular vectors read as a bug; conflating SVD with eigendecomposition for non-square
matrices; over-reading explained variance as feature importance.
**Sources:** 18.06SC unit III; MML ch.4 + ch.10; Strang LALD site; Axler ch.7 (SVD via operators,
in Notes).

---

## Part IV — Calculus and probability

### Chapter 11 — Multivariable calculus: gradients, Jacobians, Hessians (~14 pp)

**Prerequisites:** Calculus I; ch.2 (matrix algebra), ch.5 (norms).
**Sections:** 11.1 Partial derivatives · 11.2 The gradient and the steepest direction · 11.3
Directional derivatives and level sets · 11.4 The Jacobian: local linear approximation · 11.5 The
Hessian and second-order information · 11.6 The chain rule in matrix form (the backprop engine) ·
11.7 Worked library: gradients of $\mathbf w^T\mathbf x$, $\|A\mathbf x-\mathbf b\|^2$,
$\mathbf x^TA\mathbf x$, logits.
**Worked examples (4):** (a) gradient of a quadratic form derived fully; (b) Jacobian of a
vector-valued function; (c) two-step chain rule in matrix form; (d) finite-difference check of a
hand-computed gradient.
**Figures (5):** gradient field over contour lines (signature); directional derivative as slope
along a direction; Jacobian as local grid warp; finite-difference error vs. step size (log-log);
Rosenbrock banana contours.
**Code listings (4):** finite-difference gradient checker (the professional habit); SymPy
cross-check of $\nabla\|Ax-b\|^2$; gradient-field plotting script; a wrong-layout Jacobian
producing a transposed result — shown as the instructive bug.
**Hand derivation:** derive $\nabla_{\mathbf x}(\mathbf x^TA\mathbf x) = (A+A^T)\mathbf x$ and
the symmetric case $2A\mathbf x$ — the single most reused gradient in the book.
**Inline exercises:** 4.
**Additional exercises (13):** 4 [easy], 5 [medium], 4 [hard]; [hard] includes a Hessian
derivation and a two-layer chain-rule computation by hand.
**Common mistakes:** row-vector vs. column-vector gradient layout (the MML issue #822/#819 stall
cluster); chain-rule multiplication order in matrix form; finite-difference step too large or too
small; derivative ≠ gradient ≠ "direction of steepest ascent" wording trap (MML issue #808);
treating $\partial f/\partial \mathbf x$ of a scalar as a matrix.
**Sources:** MML ch.5 (topic mirror — including their matrix-gradient tables); CS229 prerequisite
evidence (what real ML courses assume); Kochenderfer ch.2; 18.02-style contour pedagogy.

### Chapter 12 — Probability and random variables (~16 pp)

**Prerequisites:** ch.1 (systems); no calculus beyond Calc I needed for most of the chapter.
**Sections:** 12.1 Sample spaces and the axioms · 12.2 Conditional probability and Bayes · 12.3
Independence · 12.4 Discrete random variables: Bernoulli, binomial, geometric, Poisson · 12.5
Continuous random variables, pdf and cdf: uniform, exponential, Gaussian · 12.6 Expectation,
variance, moments · 12.7 Joint, marginal and conditional distributions; covariance and
correlation · 12.8 The multivariate Gaussian · 12.9 LLN and CLT, stated and simulated.
**Worked examples (4):** (a) Bayes on a medical-test setup with real arithmetic; (b) expectation
and variance of a die and a binomial; (c) covariance/correlation on a small joint table; (d)
reading multivariate-Gaussian contours from a given $\Sigma$.
**Figures (6):** colah-style square-area diagrams for joint/conditional probability (signature);
pdf/cdf pairs for the named distributions; multivariate Gaussian contours as $\Sigma$ varies;
CLT histograms converging; correlation strength gallery (scatter plots at several $\rho$);
independence vs. dependence area diagram.
**Code listings (4):** simulation vs. theory for dice/binomial means and variances; Bayes'
theorem computed and sanity-checked; sampling a multivariate Gaussian through the
eigendecomposition of $\Sigma$ (ch.9 pays off); CLT simulation producing the figure.
**Hand derivation:** derive mean and variance of Bernoulli and binomial, and Bayes' theorem from
the definitions.
**Inline exercises:** 5.
**Additional exercises (14):** 5 [easy], 5 [medium], 4 [hard]; [hard] includes a proof that
uncorrelated does not imply independent (counterexample construction) and Poisson-as-limit work.
**Common mistakes:** swapping $\Pr[A\mid B]$ and $\Pr[B\mid A]$ (prosecutor's fallacy);
independent vs. uncorrelated; density $>1$ "can't be a probability" (it can — it is not one);
$\mathbb E[g(X)] = g(\mathbb E[X])$ fallacy; covariance sign misread as causation.
**Sources:** MIT 18.05 topic order; Blitzstein & Hwang via stat110.net (story-first register);
Pishro-Nik (coverage + simulate-the-theorem habit); MML ch.6; colah (figure vocabulary).

### Chapter 13 — Statistics, estimation, and Bayesian inference (~14 pp)

**Prerequisites:** ch.12; ch.8 for the regression revisiting; ch.11 for likelihood gradients.
**Sections:** 13.1 Samples, statistics, estimators · 13.2 Bias, variance, and the estimator
trade-off · 13.3 Maximum likelihood: principle and log-likelihood · 13.4 MLE worked set:
Bernoulli, Gaussian mean/variance · 13.5 Bayesian inference: prior, likelihood, posterior · 13.6
MAP vs. MLE · 13.7 Regression revisited: least squares = MLE under Gaussian noise; logistic
regression's objective as an MLE (implementation deferred to ch.14).
**Worked examples (4):** (a) MLE for a coin (closed form, plus numeric landscape); (b) MLE for
Gaussian $\mu,\sigma^2$; (c) Beta-prior coin updating to a posterior; (d) deriving the logistic
regression negative log-likelihood.
**Figures (6):** likelihood curve vs. $\theta$; prior→posterior updating small multiples;
bias–variance dartboard; sampling distribution of an estimator across simulated datasets;
sigmoid and decision boundary; likelihood vs. posterior shapes for different data sizes.
**Code listings (4):** MLE computed and plotted for the coin case; Bayesian updating simulation
(Beta–binomial); sampling-distribution experiment showing estimator variance; logistic NLL
surface and its convexity checked numerically (sets up ch.14).
**Hand derivation:** derive the Gaussian MLE for $\hat\mu$ and $\hat\sigma^2$ in full — the
canonical hand-derivation.
**Inline exercises:** 4.
**Additional exercises (13):** 4 [easy], 5 [medium], 4 [hard]; [hard] includes bias of
$\hat\sigma^2$ (the $n$ vs. $n-1$ story) and a conjugate-prior derivation.
**Common mistakes:** maximizing raw likelihood numerically (underflow — always take logs);
MLE vs. MAP conflated; dividing by $n$ vs. $n-1$ without knowing why; treating a point estimate
as the posterior; likelihood is not a probability over $\theta$.
**Sources:** MML §6.4–6.5 + ch.9; MIT 18.05 (Bayesian inference and regression ordering);
Blitzstein & Hwang (estimation chapters); Pishro-Nik (Bayesian + classical split).

---

## Part V — Optimization, information, synthesis

### Chapter 14 — Convexity, optimization, and Lagrange multipliers (~16 pp) — *capstone pieces 3a–b*

**Prerequisites:** ch.8, 9, 11, 13.
**Sections:** 14.1 Optimization problems in ML · 14.2 Convex sets and functions; why convexity
makes life easy · 14.3 Gradient descent: the update, step size, failure modes · 14.4 Momentum and
friends, briefly · 14.5 Constrained optimization and Lagrange multipliers; KKT sketched · 14.6 A
calculus-based derivation of the normal equations (kept promise from ch.8) · 14.7 Newton's method
in one section · 14.8 Backpropagation as the chain rule (from ch.11) — training a small network.
**Worked examples (4):** (a) gradient descent on a quadratic, tracking iterates; (b) Lagrange
multipliers solving $\max f$ s.t. $g=c$ by hand; (c) GD diverging/stalling at wrong step sizes;
(d) logistic regression's NLL minimized by GD.
**Figures (6):** convex vs. nonconvex function geometry; GD trajectories on contours for several
$\eta$ (small multiples); Lagrange condition geometry — constraint tangent to a level set;
saddle-point picture; sigmoid + logistic loss curve; training/validation loss curves of the small
NN.
**Code listings (4):** gradient descent from scratch on a quadratic then Rosenbrock;
**capstone:** `mlscratch.LogisticRegression` trained by GD on the ch.13 objective, checked
against `sklearn.linear_model.LogisticRegression`; **capstone:** `mlscratch.TinyNet` — a
two-layer NN with hand-derived backprop (forward pass, loss, manual gradients, gradient-checked
by ch.11's finite-difference tool) checked against an equivalent library MLP; stable-sigmoid vs.
naive-sigmoid overflow demo (the instructive bug).
**Hand derivation:** derive the Lagrange condition $\nabla f = \lambda \nabla g$ geometrically,
then the GD update rule for least squares and its convergence to the normal equations' solution.
**Inline exercises:** 5.
**Additional exercises (14):** 5 [easy], 5 [medium], 4 [hard]; [hard] includes a convergence-rate
estimate for quadratics and a KKT worked problem.
**Common mistakes:** step size too large (divergence) or microscopic (no progress); expecting a
global minimum on nonconvex objectives; confusing constraint and objective in Lagrange setups;
non-PSD Hessians and saddle points; sigmoid overflow in `exp` — the numerically stable form.
**Sources:** Boyd & Vandenberghe *Convex Optimization* (scope: early chapters only); Kochenderfer
ch.2–6 (algorithm-listing model); MML ch.7; CS229 evidence of assumed level.

### Chapter 15 — Information theory (~10 pp)

**Prerequisites:** ch.12–13.
**Sections:** 15.1 Surprise and information · 15.2 Entropy and its properties · 15.3
Cross-entropy · 15.4 KL divergence · 15.5 Mutual information · 15.6 Entropy of the Gaussian ·
15.7 Why cross-entropy loss is MLE (the ML connection).
**Worked examples (3):** (a) entropy of coins and dice; (b) KL divergence between two discrete
distributions both directions; (c) cross-entropy loss on a toy classifier — connected back to the
logistic NLL of ch.13–14.
**Figures (5):** Bernoulli entropy curve $h(p)$ (signature); colah-style codeword-length vs.
probability diagram; forward vs. reverse KL illustrated on a bimodal target; cross-entropy =
entropy + KL decomposition; mutual information as an area diagram.
**Code listings (3):** entropy/KL/cross-entropy computed and Gibbs' inequality verified
numerically; Huffman-style code-length experiment on letter frequencies; cross-entropy loss vs.
accuracy trade on a trained toy classifier.
**Hand derivation:** prove Gibbs' inequality $D_{\mathrm{KL}}(p\|q)\ge 0$ (via $\ln x\le x-1$ or
Jensen).
**Inline exercises:** 3.
**Additional exercises (10):** 4 [easy], 4 [medium], 2 [hard]; [hard] includes the Gaussian
differential-entropy derivation.
**Common mistakes:** KL is not symmetric (not a distance); bits vs. nats ($\log_2$ vs. $\ln$)
mix-ups; cross-entropy = entropy only when $p=q$; $\log 0$ blowups in naive implementations.
**Sources:** colah *Visual Information Theory* (figure model); MacKay ITILA (framing);
Cover & Thomas via identifiable ISBN 978-0-471-24195-9 (further reading, Notes only — not opened).

### Chapter 16 — Capstone: a small machine-learning library from scratch (~10 pp)

**Prerequisites:** ch.8, 10, 13, 14.
**Sections:** 16.1 The pieces and how they fit: `mlscratch` package tour · 16.2 Pipeline:
synthetic data → PCA preprocessing → regressors and a classifier · 16.3 Checking against
scikit-learn: comparison protocol · 16.4 Failure modes and the verification habit · 16.5 What to
read next (pointers into the Book 4 material).
**Worked examples (3):** (a) end-to-end pipeline on a synthetic dataset — center, reduce with
PCA, fit `mlscratch` models; (b) side-by-side metrics vs. sklearn in a table; (c) a deliberately
injected bug caught by the test suite.
**Figures (4):** `mlscratch` architecture block diagram; pipeline data-flow figure;
comparison-results table figure; test-harness flow diagram.
**Code listings (4):** package walkthrough listing; the pytest suite excerpt; comparison-driver
script printing the metrics table; the seeded-bug test failing, then passing (verification
culture in action).
**Hand derivation:** assemble and derive by hand the complete forward + backprop gradient set
for the two-layer network (the book's final derivation).
**Inline exercises:** 2.
**Additional exercises (10):** 3 [easy], 4 [medium], 3 [hard]; [hard] includes extending
`mlscratch` with a new component and writing its verification test.
**Common mistakes:** uncentered PCA; test leakage into training; unfair comparison protocols;
trusting any implementation without a numerical check.
**Sources:** MML part II structure (notebook-per-application model); sklearn API conventions
(cited via official docs at chapter time); brief's capstone spec.

---

## Back matter (~26 pp)

- **Appendix A — Mathematical notation** (the notation table, like PAPS's notation appendix).
- **Appendix B — Python environment** (pinned versions; how `make test` runs every listing).
- **Hints** for every [hard] exercise (~6 pp).
- **Solutions** to at least half of all exercises (~12 pp).
- **Bibliography** (numbered; every source in `docs/sources.md` that ships content, plus
  identifiable ISBNs clearly marked).
- **Index** (every defined term, via `\index{}`).

## Seed-topic coverage map (mandatory list → chapter)

| Seed topic | Chapter(s) |
|---|---|
| linear systems and elimination | 1 |
| matrices | 2 (and everywhere) |
| vector spaces | 3 |
| linear maps | 4 |
| determinants | 6 |
| eigenvalues and diagonalisation | 7 |
| orthogonality and least squares | 5, 8 |
| symmetric matrices and the spectral theorem | 9 |
| SVD and PCA | 10 |
| multivariable calculus, gradients, Jacobians | 11 |
| probability and random variables | 12 |
| statistics, MLE and Bayesian inference | 13 |
| optimisation, convexity, Lagrange multipliers | 14 |
| information theory | 15 |

**Capstone placement:** linear regression → ch.8; PCA → ch.10; MLE/MAP theory → ch.13;
logistic regression + small neural network → ch.14; package assembly, library checks and
verification harness → ch.16. All live in `code/mlscratch/` and are checked against scikit-learn.

## Page-count summary

| Part | Chapters | Pages |
|---|---|---|
| Front matter | — | ~9 |
| I. Linear systems and vector spaces | 1–4 | ~52 |
| II. Geometry, eigenvalues and least squares | 5–8 | ~50 |
| III. Symmetric structure and data | 9–10 | ~26 |
| IV. Calculus and probability | 11–13 | ~44 |
| V. Optimization, information, synthesis | 14–16 | ~36 |
| Back matter | — | ~26 |
| **Total** | 16 | **~243** |

If the build runs long, the negotiated trims are: ch.15 (−2), ch.16 (−2), ch.12 (−2), back
matter (−4).
