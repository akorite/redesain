# Outline — Book 4: Artificial intelligence and machine learning (`textbook-ml`)

**Status: draft for user approval — no chapter may be written before approval (§5.1).**

- Reader: Python-fluent; Book 3 (`textbook-linalg-ml`) in progress — linear algebra, gradients/Jacobians, probability, MLE, convex optimisation, information theory are assumed where stated.
- Outcomes: trains, evaluates and deploys models; builds and evaluates agent systems; reproduces a paper.
- Book rule (brief "special"): **every model is first implemented from scratch on a small dataset, then with a library, and the two are compared on the same split and seed.** Every chapter carries an explicit evaluation / failure-analysis item.
- Compute constraint (declared to the reader in ch1): everything runs on a laptop CPU; only ch9, ch11 and the ch18 stretch reproduction want a free-tier GPU (Colab/Kaggle, ~1–2 h). Nothing requires paid compute or API keys for the core path; chapters 15–16 offer a no-API-key path plus an optional keyed path.
- Chapter standard per §3/§3A: ≥3 worked examples, ≥4 figures, ≥3 code listings with real captured output, a common-mistakes/failure-analysis item, inline exercises + ≥10 additional exercises split `[easy]`/`[medium]`/`[hard]`, a one-page summary table ("cheat sheet") ending each chapter, a Notes section citing sources by number.
- Total: **≈238 pages** (front matter ~10, chapters ~206, back matter ~22). If trimming is required, the compression order is: (1) merge ch1–2 into one 12-page chapter, (2) cut ch12 to VAE + diffusion-concept only, (3) shorten appendices. Figures, code outputs, worked examples and failure-analysis sections are never cut (approved process rule).

## Book 3 dependency map (used in per-chapter prerequisites)

| Book 3 material | Needed by |
|---|---|
| Vectors, matrices, inner products, norms | ch1 onward |
| Least squares, orthogonality, projections | ch3–4, ch6 |
| Eigenvalues, SVD, PCA | ch6, ch9 |
| Gradients, Jacobians, chain rule | ch7–12 |
| Probability, MLE, Bayes | ch3–4, ch12–13 |
| Convexity, Lagrange multipliers | ch4, ch8 |
| Information theory (entropy, KL, cross-entropy) | ch3–4, ch11–12 |

## Coverage of the seed list (brief)

Python/NumPy for data → ch1; pandas/visualisation → ch2; supervised learning and evaluation → ch3; regularisation → ch4; trees and ensembles → ch5; clustering and dimension reduction → ch6; neural networks and backprop → ch7; optimisation → ch8; CNNs → ch9; sequence models and attention → ch10; transformers → ch11; generative models → ch12; reinforcement learning → ch13; MLOps and monitoring → ch14; evaluating LM systems → ch15; agent patterns → ch16; reading and reproducing papers → ch17 (+ capstone ch18).

**Deliberate deviations (flagged, not hidden):**
1. k-nearest neighbours and naïve Bayes are folded into ch3 — they are the cheapest possible classifiers and make evaluation concrete before parametric models (same didactic role as CS231n's kNN). This is *addition*, not omission.
2. SVM/kernels get one optional section inside ch4 (ISLP gives it a chapter; the seed does not). Noted so the reader can find it in Notes.
3. RL is compressed to a single 13-page chapter (bandits → MDP → tabular TD → approximation → policy-gradient sketch). S&B is the roadmap in Notes; depth is traded for a full systems part.
4. LM-evaluation and agent chapters sit at the *end* of the systems part, not next to transformers: they are systems topics, and the field moves fast — every framework/model/venue claim there is date-stamped `[checked 2026-10]` and carries an `[unverified]` path to `docs/unverified.md`.
5. Omitted entirely (named): survival analysis, multiple testing, recommender systems, graph networks, Gaussian processes, distributed training. Each gets a one-line pointer in the relevant chapter's Notes.
6. fast.ai's "train first, theory later" order is deliberately rejected — Book 3 exists, so we keep mechanism-first. Said out loud in ch1's Notes so the reader knows the alternative exists.

---

## Part I — Data foundations (≈34 pp)

### Chapter 1 — Data as matrices: NumPy and the dataset (10 pp)

- **Aim:** every dataset is a matrix $X\in\mathbb R^{n\times d}$ with row $i$ = sample $\mathbf x_i^T$; the reader loads, cleans, normalises and batch-slices real data in NumPy.
- **Prerequisites:** Python; Book 3 vectors/matrices.
- **Sections:** 1.1 Why datasets are matrices (and when they are not) · 1.2 NumPy arrays: shape, dtype, broadcasting — the three rules that carry the whole book · 1.3 Loading data: CSV → `ndarray`; missing values, encodings, leakage at the loading step · 1.4 Features and targets; numerical vs categorical; one-hot encoding from scratch · 1.5 Shuffling, batching, vectorised ops vs Python loops (timed) · 1.6 Data hygiene: duplicates, impossible values, units · 1.7 Common mistakes · 1.8 Summary table · Notes.
- **Worked examples:** (a) load `iris` into $X,\mathbf y$ and vectorise "distance to class mean" — a working classifier in 8 lines; (b) one-hot encode `penguins` sex/island and show the shape change $(n,d)\to(n,d+4)$; (c) benchmark loop vs vectorised Euclidean distances on 10⁴ rows (~100× speedup, real timing printed).
- **Figures:** (a) $X$ as $n\times d$ block diagram with rows/columns labelled (TikZ); (b) broadcasting illustrated: $(n,1)+(1,d)$ step-by-step; (c) loop-vs-vectorised timing bar chart from the real run; (d) missing/impossible-value scatter panel (penguins bill length vs depth with injected NaNs); (e) one-hot encoding before/after matrix sketch.
- **Code listings:** `load_iris_scratch.py` (CSV → ndarray, no pandas); `onehot_scratch.py`; `broadcast_benchmark.py` with printed timing table.
- **Evaluation/failure analysis:** "garbage in" — build a split where a duplicated row inflates apparent accuracy; show the fake win and the fix.
- **Exercises:** ~4 inline checkpoints; +10 (4 easy: shapes/broadcasts; 4 medium: write `zscore`, `train_val_split` with seed; 2 hard: implement `iter_batches` generator + prove a broadcasting identity).

### Chapter 2 — Tables, pandas and visualisation (10 pp)

- **Aim:** the reader explores a real tabular dataset with pandas and makes the three plots that survive peer review (labelled axes, legend, honest scales).
- **Prerequisites:** ch1; Book 3 (nothing new).
- **Sections:** 2.1 DataFrame as labelled matrix; index, columns, dtypes · 2.2 Filter/aggregate/groupby — the SQL-shaped verbs · 2.3 Joins and reshaping (long vs wide) · 2.4 Visualisation that does not lie: matplotlib mechanics, scales, baselines, colour-vs-style · 2.5 The exploration loop: question → slice → plot → question · 2.6 Common mistakes (aggregates hiding distributions, truncated axes, pie charts) · 2.7 Summary table · Notes.
- **Worked examples:** (a) `titanic`: survival rate by class×sex via groupby, then drawn as a grouped bar; (b) long→wide pivot of a time series and back; (c) same data, two plots — one misleading (truncated y), one honest — the reader spots the trick before the reveal.
- **Figures:** (a) groupby→aggregate dataflow diagram; (b) scatter matrix of `penguins` numeric features; (c) misleading-vs-honest bar chart pair; (d) long-vs-wide reshape diagram; (e) matplotlib anatomy figure (figure/axes/artists).
- **Code listings:** `titanic_groupby.py` + printed table; `pivot_longwide.py`; `two_plots_one_truth.py` producing the misleading/honest pair as output figures.
- **Evaluation/failure analysis:** Simpson's paradox on a two-group aggregate — pooled rate reverses a per-group trend; the chapter's failure item is "the aggregate lied because a covariate was dropped".
- **Exercises:** ~3 inline; +10 (4 easy reads of groupby output; 4 medium: reproduce a plot from a spec; 2 hard: construct a Simpson's-paradox table + a plot that reveals it).

### Chapter 3 — Supervised learning and honest evaluation (14 pp)

- **Aim:** the whole supervised frame in one chapter — task, model, loss, split, metric — plus the two simplest models (kNN, naïve Bayes) so evaluation is concrete. From here on, "did it work?" always has a protocol.
- **Prerequisites:** ch1–2; Book 3 probability (Bayes rule, expectation), least squares.
- **Sections:** 3.1 The supervised problem $\mathcal D=\{(\mathbf x_i,y_i)\}$ and the two questions (predict what? measure how?) · 3.2 kNN as non-parametric memory — distance, $k$, curse of dimensionality preview · 3.3 Naïve Bayes: conditional independence, likelihoods, log-space arithmetic · 3.4 The split: train/validation/test and why the test set is touched once · 3.5 Cross-validation: $k$-fold, stratified, grouped; when CV lies (groups, time) · 3.6 Metrics for regression: MAE/MSE/RMSE/$R^2$ · 3.7 Metrics for classification: confusion matrix, accuracy, precision/recall, $F_1$, ROC-AUC; class imbalance changes the question · 3.8 Bias and variance; the learning curve · 3.9 Leakage: the five ways it sneaks in · 3.10 Common mistakes · 3.11 Summary table · Notes.
- **Worked examples:** (a) kNN on `digits` — sweep $k$, plot train/test accuracy curve, read the bias–variance shape; (b) naïve Bayes on `titanic` (categorical+Gaussian NB), confusion matrix by hand-then-code; (c) the leak: "scale on the full data before splitting" — show +4% phantom accuracy and the corrected pipeline.
- **Figures:** (a) the supervised pipeline (raw data → split → fit → predict → score) as a block diagram; (b) decision boundaries of kNN at $k{=}1,5,25$ on 2-D synthetic data (small multiples); (c) bias–variance train/test error curves vs model complexity; (d) confusion-matrix schematic with TP/FP/FN/TN cells; (e) learning curve: accuracy vs training-set size for NB and kNN; (f) ROC curve construction step diagram.
- **Code listings:** `knn_scratch.py` (pairwise distances, majority vote); `nb_scratch.py` (Gaussian NB in log-space); `eval_protocol.py` — the book's canonical split+metric harness reused by every later chapter; `leak_demo.py` printing the phantom +4% then the honest number.
- **Evaluation/failure analysis:** the chapter's own worked example is failure analysis — the phantom-accuracy leak; plus an imbalanced-`breast_cancer` rerun where 96% accuracy is worse than 91% recall-aware F1.
- **Exercises:** ~5 inline; +12 (4 easy metric computations by hand; 5 medium: implement stratified k-fold, precision/recall, micro-vs-macro; 3 hard: prove NB decision boundary is linear under equal-variance Gaussians; design a leak-free grouped split; derive why accuracy fails at 99:1 imbalance). USAAIO-style MC drill of 5 concept questions ends the chapter.

---

## Part II — Classical machine learning (≈34 pp)

### Chapter 4 — Linear models and regularisation (12 pp)

- **Aim:** least squares → ridge/lasso → logistic regression, all derived, implemented, and compared; regularisation read as geometry, not incantation.
- **Prerequisites:** ch3; Book 3 least squares, gradients, MLE, convexity, Lagrange.
- **Sections:** 4.1 Linear regression: normal equations, $X^{+}$, and when $X^TX$ is singular · 4.2 Ridge: $\lambda\|\boldsymbol\theta\|_2^2$ as coefficient shrinkage; the constraint ball picture · 4.3 Lasso: $\lambda\|\boldsymbol\theta\|_1$ and why the corners give zeros · 4.4 Logistic regression: $\sigma(\mathbf w^T\mathbf x)$, cross-entropy from MLE, decision boundary · 4.5 Multiclass softmax · 4.6 Feature maps $\phi(\mathbf x)$: polynomials and the price of expressivity · 4.7 (optional) The kernel trick and SVM in one page · 4.8 Common mistakes · 4.9 Summary table · Notes.
- **Worked examples:** (a) `diabetes` regression: OLS vs ridge path — coefficients vs $\log\lambda$; (b) lasso on `california_housing`: which features die first and why; (c) logistic regression on 2-feature `breast_cancer`: the boundary, the sigmoid, the probability calibration.
- **Figures:** (a) ridge-vs-lasso constraint geometry (diamond vs ball, TikZ, step-by-step); (b) coefficient paths vs $\lambda$ (two panels: ridge smooth, lasso dropping to zero); (c) sigmoid + decision boundary on 2-D data; (d) train/test error vs $\lambda$ U-curves; (e) polynomial feature-map overfit strip (degrees 1, 3, 9, small multiples).
- **Code listings:** `linreg_scratch.py` (normal equations + ridge closed form); `logreg_scratch.py` (gradient descent on NLL); `reg_compare.py` — sklearn `Ridge/Lasso/LogisticRegression` vs the scratch versions, printed coefficient comparison.
- **Evaluation/failure analysis:** residual-plot autopsy on `california_housing` — heteroscedasticity and the log-target fix; plus the singular-$X^TX$ failure and the ridge rescue.
- **Exercises:** ~4 inline; +12 (4 easy: closed-form fills; 5 medium: implement ridge/lasso path, F1-vs-threshold sweep; 3 hard: derive logistic gradient $\nabla_\mathbf w \mathrm{NLL}$; prove ridge solution exists for $\lambda>0$; elastic-net from scratch). USAAIO-style drill: L1-vs-L2 sparsity.

### Chapter 5 — Trees and ensembles (11 pp)

- **Aim:** a decision tree built split-by-split, then the ensemble idea — bagging, random forests, gradient boosting — and why "average many flawed learners" works.
- **Prerequisites:** ch3–4; Book 3 entropy/information.
- **Sections:** 5.1 Trees as axis-aligned partitions · 5.2 Splitting criteria: entropy/information gain and Gini · 5.3 Growing and pruning; depth vs overfit · 5.4 Variance of a single tree → bootstrap and bagging · 5.5 Random forests: feature subsampling as decorrelation · 5.6 Gradient boosting: fitting residuals step by step · 5.7 Feature importance (and when it lies) · 5.8 Common mistakes · 5.9 Summary table · Notes.
- **Worked examples:** (a) grow a stump-then-tree on `wine` computing information gain by hand for the first split; (b) `digits`: single tree vs forest — test accuracy and per-depth variance measured over 20 bootstrap refits; (c) `california_housing` gradient boosting: residual shrinkage stage by stage.
- **Figures:** (a) tree ↔ partition correspondence diagram; (b) information-gain computation panel for one split; (c) bias–variance: 20 trees overlaid vs their bagged average (real output); (d) boosting residual-fit sequence (4-step small multiples); (e) feature-importance bar chart with a planted-mislead variant (correlated-feature importance dilution).
- **Code listings:** `tree_scratch.py` (recursive splits, Gini, depth cap); `forest_lib.py` (sklearn `RandomForest`); `boost_compare.py` — scratch tree → `HistGradientBoosting` comparison with timing and score table.
- **Evaluation/failure analysis:** importance-illusion failure — feature importance credited to a correlated redundant column; permutation importance as the honest alternative.
- **Exercises:** ~4 inline; +10 (3 easy: entropy/Gini arithmetic; 4 medium: split search, OOB scoring, depth sweep; 3 hard: derive Gini as an impurity bound; implement column subsampling; boosting-step residual proof for squared loss).

### Chapter 6 — Clustering and dimension reduction (11 pp)

- **Aim:** unlabelled data — $k$-means, hierarchical clustering, PCA, and honest reading of "structure" claims; every clustering output is interrogated, not trusted.
- **Prerequisites:** ch1–3; Book 3 SVD, eigenvalues, projections.
- **Sections:** 6.1 Unsupervised ≠ evaluation-free: internal vs external criteria · 6.2 $k$-means: Lloyd's iterations, init sensitivity, choosing $k$ · 6.3 Hierarchical clustering and linkage · 6.4 PCA via SVD: variance, projection, reconstruction error · 6.5 Beyond linear: t-SNE and UMAP — what they preserve and what they invent · 6.6 Common mistakes (scaling forgotten, cluster-count assumed, projection over-read) · 6.7 Summary table · Notes.
- **Worked examples:** (a) $k$-means on `iris`, silhouette score, and the $k{=}2$ vs $k{=}3$ disagreement; (b) PCA on `digits`: cumulative variance curve, reconstruct a digit from top-10 components; (c) same `digits` through t-SNE and UMAP — clusters that separate locally but not globally, discussed honestly.
- **Figures:** (a) Lloyd's algorithm in 4 steps (small multiples); (b) dendrogram of `wine` with two linkage cuts compared; (c) PCA scree/cumulative-variance curve; (d) digit reconstruction strip (10, 30, 60 components); (e) t-SNE/UMAP side-by-side with a "fabricated cluster" caution panel; (f) scaling-forgotten before/after.
- **Code listings:** `kmeans_scratch.py` (Lloyd + k-means++ init); `pca_svd.py` (NumPy SVD, projection+reconstruction); `cluster_lib.py` — sklearn `KMeans/Agglomerative/PCA/TSNE` vs scratch on `digits`, printed ARI/silhouette table.
- **Evaluation/failure analysis:** the "clusters in noise" trap — $k$-means on uniform random data returns clean-looking clusters; silhouette + a null baseline expose it.
- **Exercises:** ~4 inline; +10 (3 easy: distance/linkage reads; 4 medium: silhouette implementation, variance-explained computation, linkage comparison; 3 hard: derive PCA objective ↔ top eigenvectors; show k-means monotonic objective; why t-SNE distances are not quantitative). USAAIO-style drill: UMAP property MC.

---

## Part III — Deep learning (≈73 pp)

### Chapter 7 — Neural networks and backpropagation (14 pp)

- **Aim:** the MLP as composed maps; backpropagation derived once, implemented in raw NumPy, verified by finite differences, then re-derived by `torch.autograd`.
- **Prerequisites:** ch3–4; Book 3 Jacobians/chain rule, gradients.
- **Sections:** 7.1 From linear model to stacked map: $\mathbf h^{(\ell)}=a(W^{(\ell)}\mathbf h^{(\ell-1)}+\mathbf b^{(\ell)})$ · 7.2 Activation functions: $\operatorname{ReLU}$, $\sigma$, $\tanh$ — shapes and gradients · 7.3 The chain rule as local Jacobian products — computation-graph picture · 7.4 Backpropagation by hand on a 2-layer net (every number shown) · 7.5 Numerical gradient checking — the sanity ritual (CS231n's lesson) · 7.6 Losses matched to tasks: MSE / binary cross-entropy / multiclass cross-entropy + softmax · 7.7 autograd: same net, gradients for free · 7.8 Common mistakes (broadcasting silent bugs, activation/loss mismatch, dead ReLUs) · 7.9 Summary table · Notes.
- **Worked examples:** (a) forward + backward pass on a 2-3-2 net with explicit numbers; (b) `digits` MLP from scratch — loss curve vs epochs, compared to sklearn `MLPClassifier` on the same split/seed; (c) gradient-check deliberately broken (off-by-one bias) — the check catches it, teaching why we check.
- **Figures:** (a) network graph with weights/activations labelled (TikZ); (b) activation functions + their gradients (2-panel pgfplots); (c) computation graph annotated with local Jacobians and the backward pass arrows; (d) loss curves scratch-vs-library overlaid; (e) finite-difference illustration; (f) decision regions of a 2-D MLP vs depth (small multiples, real runs).
- **Code listings:** `mlp_scratch.py` (~60 lines: forward, backprop, SGD loop); `gradcheck.py` (finite differences); `mlp_torch.py` (`nn.Module` + manual loop) with printed agreement table scratch↔torch↔sklearn.
- **Evaluation/failure analysis:** silent-broadcast bug planted and diagnosed; saturation failure — sigmoid net stalls, ReLU variant trains (loss curves shown).
- **Exercises:** ~5 inline; +12 (4 easy: shapes/counts of parameters; 5 medium: implement activation + derivative, batch-ify backprop; 3 hard: full backprop derivation for 3 layers; prove softmax+CE gradient simplification; dead-ReLU diagnosis protocol). USAAIO-style drill on computation-graph complexity.

### Chapter 8 — Training and optimisation (11 pp)

- **Aim:** how deep nets actually get trained — SGD and its relatives, learning-rate regimes, initialisation, and the diagnostic checklist when training goes wrong.
- **Prerequisites:** ch7; Book 3 convexity.
- **Sections:** 8.1 GD → SGD → minibatch: noise as a feature · 8.2 Momentum and Nesterov · 8.3 Per-parameter rates: AdaGrad, RMSProp, Adam — one unifying template $\theta^{(t+1)}=\theta^{(t)}-\eta\,\hat m_t/(\sqrt{\hat v_t}+\epsilon)$ · 8.4 Learning-rate schedules and warmup · 8.5 Initialisation: symmetry-breaking, Xavier/Kaiming · 8.6 Batchnorm and dropout as practical regularisers · 8.7 Babysitting training: the CS231n checklist — sanity overfit, loss curve autopsies, gradient health · 8.8 Common mistakes · 8.9 Summary table · Notes.
- **Worked examples:** (a) same `digits` MLP trained with GD/SGD/SGD+momentum/Adam — four overlaid loss curves and final test scores; (b) learning-rate sweep: too-high divergence vs too-slow plateau vs just-right, all real runs; (c) dead-vs-alive: bad init killing a 4-layer sigmoid net, fixed by Kaiming+ReLU.
- **Figures:** (a) 2-D loss surface with GD/SGD/momentum trajectories; (b) four-optimiser loss-curve comparison; (c) LR regimes triptych (diverging/slow/good); (d) activation histograms before/after init fix; (e) schedule shapes (step/cosine/warmup); (f) gradient-norm dashboard from a real run.
- **Code listings:** `optim_scratch.py` (SGD/momentum/Adam on one small net, shared loop); `lr_sweep.py` output table; `train_diagnostic.py` — the chapter's reusable "babysit" checklist script.
- **Evaluation/failure analysis:** loss-curve autopsy gallery — diverging, plateau, noise-floor, val-train gap; the reader diagnoses each before the answer.
- **Exercises:** ~4 inline; +10 (3 easy: moment arithmetic, parameter counts; 4 medium: implement Adam step, cosine schedule; 3 hard: derive momentum as exponential moving average; analyse Adam's bias correction; design an LR-finder). 

### Chapter 9 — Convolutional networks (12 pp)

- **Aim:** images — why dense layers lose, what a convolution is (as a matrix operation and as a sliding window), and the classical architecture vocabulary up to residual connections.
- **Prerequisites:** ch7–8; Book 3 SVD (for parameter counting context).
- **Sections:** 9.1 Images as tensors $(C,H,W)$; why $\mathbf x_i$ flattening destroys structure · 9.2 Convolution = local linear map + weight sharing; stride, padding, output-size arithmetic · 9.3 Channels, pooling, receptive fields · 9.4 A first CNN on `digits`/MNIST · 9.5 Classic architectures as design history: LeNet → AlexNet → VGG — what each added · 9.6 Residual connections and why depth suddenly trains · 9.7 Transfer learning and pretrained features (library-side only) · 9.8 Common mistakes · 9.9 Summary table · Notes.
- **Worked examples:** (a) hand-convolve a $5\times5$ patch — output-size arithmetic $\lfloor(H+2p-k)/s\rfloor+1$; (b) MNIST CNN scratch vs `torch.nn` version — accuracy/time comparison; (c) visualise learned first-layer filters and a feature map through the net.
- **Figures:** (a) sliding-window convolution step diagram; (b) padding/stride output-size geometry; (c) LeNet block diagram (TikZ); (d) learned filters grid + one feature-map panel (real outputs); (e) receptive-field growth diagram; (f) residual block + why the gradient highway works.
- **Code listings:** `conv_scratch.py` (im2col or 4-loop conv on a single image, verified against `scipy`/`torch`); `cnn_torch.py` (LeNet-style on MNIST, real epoch log); `filters_viz.py` producing the filter/feature-map figures from the trained checkpoint.
- **Evaluation/failure analysis:** misclassified-digit gallery — the confusion pairs (4/9, 5/3) and what the features missed; plus a padding-off-by-one output-shape bug.
- **Exercises:** ~4 inline; +10 (3 easy: output-size arithmetic; 4 medium: parameter counting per layer, implement max-pool; 3 hard: derive conv-as-matrix (im2col); receptive-field recurrence; ResNet-vs-plain degradation argument). Compute note: the scratch conv stays on `digits`; the library run on MNIST takes ~5–15 min CPU.

### Chapter 10 — Sequence models (12 pp)

- **Aim:** data arrives ordered — text, sensors, prices. From n-grams and the Markov view to RNNs, their gradients (BPTT), LSTM's fix, and the first character-level language model.
- **Prerequisites:** ch7–8; probability (Book 3); softmax (ch4, ch7).
- **Sections:** 10.1 Sequences and the prediction task; tokens, vocabulary $\mathcal V$, encodings · 10.2 n-gram language models: the count-and-smooth baseline that still matters · 10.3 The RNN recurrence $\mathbf h_t=f(\mathbf h_{t-1},\mathbf x_t)$; BPTT; exploding/vanishing gradients · 10.4 LSTM/GRU: gates as learned memory access · 10.5 Character-level LM on Tiny Shakespeare — perplexity $\operatorname{PPL}=\exp(\mathrm{NLL}/T)$ · 10.6 Teacher forcing, sampling, temperature · 10.7 Common mistakes (state resets across batches, tokeniser leakage) · 10.8 Summary table · Notes.
- **Worked examples:** (a) train a trigram model on Tiny Shakespeare — sample text at $\tau\in\{0.5,1.0,1.5\}$, compute perplexity; (b) RNN from scratch (raw NumPy or tensor-level torch) on the same corpus — sample text compared to trigram; (c) BPTT gradient blow-up demonstrated numerically, then clipped.
- **Figures:** (a) n-gram count table → sampling illustration; (b) RNN unrolled diagram (TikZ); (c) gradient decay vs timestep plot (real or computed); (d) LSTM gate diagram; (e) perplexity-vs-epoch for trigram/RNN/library-LSTM; (f) temperature sampling quality panel (short real samples quoted).
- **Code listings:** `trigram_lm.py` (counts → sampling → perplexity); `rnn_scratch.py` (forward + truncated BPTT); `lstm_torch.py` (`nn.LSTM` on Tiny Shakespeare) with the three-way perplexity comparison table.
- **Evaluation/failure analysis:** vanishing-gradient autopsy — long-range dependency test (copy-task) where RNN fails and LSTM passes; tokenisation pitfall (train/test split mid-word leaking structure).
- **Exercises:** ~4 inline; +10 (3 easy: perplexity arithmetic, vocabulary counting; 4 medium: smoothing variants, teacher-forcing loss; 3 hard: derive BPTT for one recurrence; analyse gate gradients; design a long-range synthetic task).

### Chapter 11 — Attention and transformers (13 pp)

- **Aim:** attention as differentiable lookup; multi-head self-attention, positional encoding, and the transformer block — built from primitives, then used via the library.
- **Prerequisites:** ch7–10; Book 3 inner products, projections.
- **Sections:** 11.1 Why recurrence is a bottleneck: parallelism vs order · 11.2 Scaled dot-product attention: $\operatorname{softmax}(QK^T/\sqrt{d_k})V$ — what $Q,K,V$ mean · 11.3 Multi-head attention; masking (padding and causal) · 11.4 Positional encodings: sinusoidal, learned, relative (the USAAIO-style view) · 11.5 The transformer block: attention + FFN + residuals + layernorm · 11.6 A miniature character-level GPT on Tiny Shakespeare — trained and sampled · 11.7 The library view: `transformers` pipeline, model card, a small fine-tune · 11.8 Cost accounting: $O(T^2d)$ attention and why sequence length is money · 11.9 Common mistakes · 11.10 Summary table · Notes.
- **Worked examples:** (a) attention weights computed by hand on a 4-token example — who attends to whom; (b) mini-GPT on Tiny Shakespeare: loss curve + sampled text vs ch10's LSTM; (c) encoder-only classifier on a small text set (AG News subset): from-scratch attention block vs `nn.TransformerEncoder`, printed agreement.
- **Figures:** (a) $Q,K,V$ → scores → weights → output dataflow (TikZ); (b) attention-matrix heatmap from the trained mini-GPT (two heads compared); (c) multi-head split/concat diagram; (d) causal-mask triangle diagram; (e) transformer block anatomy; (f) $O(T^2)$ attention-cost plot; (g) sinusoidal positional-encoding heatmap.
- **Code listings:** `attention_scratch.py` (scaled dot-product + multi-head + causal mask, tensor-level torch, no `nn.MultiheadAttention` — USAAIO-style constraint); `minigpt_train.py`; `hf_pipeline.py` (`transformers` pipeline + tiny fine-tune log); printed comparison of scratch-vs-library attention outputs (allclose check).
- **Evaluation/failure analysis:** positional-information ablation — remove position encoding, watch the model's order-blindness on a permuted-token task; plus a mask-leak bug letting the model see the future (detected by anachronistically-low train loss).
- **Exercises:** ~5 inline; +12 (4 easy: dimension bookkeeping, complexity; 5 medium: implement mask, second head, parameter count; 3 hard: derive the $\sqrt{d_k}$ scaling argument; linear-attention feature-map analysis in USAAIO R2 style — derive $\exp(\mathbf q^T\mathbf k)=\phi(\mathbf q)^T\phi(\mathbf k)$ requires $\ell=\infty$; design a positional-encoding ablation). Compute note: mini-GPT trains on free-tier GPU (~30–60 min); a CPU-only nano config is provided.

### Chapter 12 — Generative models (11 pp)

- **Aim:** models that make data — the likelihood view, autoregressive sampling, VAEs, GANs and diffusion at concept-plus-one-lab depth.
- **Prerequisites:** ch7–11; Book 3 MLE, KL.
- **Sections:** 12.1 Generative vs discriminative: $p(\mathbf x)$ vs $p(y\mid\mathbf x)$ · 12.2 Autoregressive models: the chain factorisation $p(\mathbf x)=\prod_t p(x_t\mid \mathbf x_{<t})$ — ch10–11 were already generative · 12.3 Latent-variable models and the ELBO idea → VAE: encoder, reparameterisation, decoder · 12.4 GANs: minimax training and why it is fragile · 12.5 Diffusion: denoising as iterative refinement (concept; library-side sampling demo only) · 12.6 Evaluating generative models — likelihood, samples, and the honesty problem · 12.7 Common mistakes · 12.8 Summary table · Notes.
- **Worked examples:** (a) fit a pixel-independent generative baseline and an autoregressive one on `digits` — sampled grids compared; (b) VAE on `digits` scratch-in-torch: latent-space traversal figure; (c) diffusion sampling on a 2-D spiral — the denoising trajectory as the whole lesson.
- **Figures:** (a) generative-vs-discriminative decision-boundary/density panel; (b) chain-factorisation diagram; (c) VAE architecture (encoder→μ,σ→z→decoder); (d) latent-space traversal strip (real outputs); (e) GAN minimax diagram + a real mode-collapse gallery; (f) 2-D diffusion denoising trajectory (6-step small multiples).
- **Code listings:** `vae_torch.py` (ELBO loop on `digits`); `sample_compare.py` (real-vs-generated grid); `diffusion2d.py` (toy 2-D DDPM denoising, ~80 lines); printed loss/NLL-comparison table.
- **Evaluation/failure analysis:** the honesty problem as the failure item — a "good-looking" sample that is a memorised training digit, caught by nearest-neighbour distance histograms.
- **Exercises:** ~4 inline; +10 (3 easy: ELBO terms, sampling steps; 4 medium: implement reparameterisation, nearest-neighbour check; 3 hard: derive ELBO lower bound; analyse mode collapse; DDPM forward-process closed form).

---

## Part IV — Decisions and systems (≈45 pp)

### Chapter 13 — Reinforcement learning (13 pp)

- **Aim:** the sequential-decision frame — MDPs, value functions, Q-learning — compressed from S&B to what an engineer needs: tabular methods that work, approximation that breaks honestly, and policy gradients sketched.
- **Prerequisites:** ch3, ch7 (for function approximation); Book 3 expectation, Markov chains (as needed — supplied inline if Book 3 lacks it).
- **Sections:** 13.1 From prediction to action: agent, environment, reward · 13.2 The $k$-armed bandit: exploration vs exploitation, $\varepsilon$-greedy, UCB · 13.3 MDPs: $(\mathcal S,\mathcal A,P,r,\gamma)$, returns $G_t$, policies $\pi$ · 13.4 Value functions $V^\pi,Q^\pi$ and the Bellman equations · 13.5 Dynamic programming: policy and value iteration · 13.6 Model-free learning: Monte Carlo → TD(0) → Sarsa → Q-learning · 13.7 Function approximation: linear $Q$ on `CartPole`; where it diverges (the deadly triad, stated not proved) · 13.8 Policy gradient in one page: REINFORCE idea → why LLM post-training lives here · 13.9 Common mistakes · 13.10 Summary table · Notes.
- **Worked examples:** (a) 10-armed testbed: $\varepsilon$-greedy vs UCB, average-reward curves over 2000 runs; (b) Q-learning on a gridworld + on `FrozenLake`-style toy — learned policy drawn as arrows; (c) linear-approximation Q on `CartPole-v1` — trains, then the failure replay when the approximation lies.
- **Figures:** (a) agent–environment loop diagram; (b) bandit average-reward curves (real runs, ε-greedy vs UCB vs optimistic); (c) gridworld with $V(s)$ heatmap + greedy-policy arrows; (d) MC vs TD backup diagrams; (e) Q-learning reward-vs-episode curve on the toy env; (f) CartPole failure curve (approximation divergence).
- **Code listings:** `bandits.py` (ε-greedy/UCB testbed, S&B-style); `qlearn_grid.py`; `cartpole_linear.py` + the honest failure case; printed mean-reward comparison table.
- **Evaluation/failure analysis:** reward hacking + approximation divergence — the agent that maximises reward while solving nothing (exploiting a shaping bug), and the divergence replay.
- **Exercises:** ~4 inline; +12 (4 easy: Bellman arithmetic, return discounting; 5 medium: implement UCB, value iteration, ε-schedule; 3 hard: prove greedy-policy improvement; derive TD(0) update as bootstrapped sample; analyse maximisation bias → double learning).

### Chapter 14 — Machine learning systems in production (11 pp)

- **Aim:** a model is not a system — the pipeline around it (data → features → training → deployment → monitoring) and the failure modes that only appear after launch.
- **Prerequisites:** ch3–9.
- **Sections:** 14.1 The ML system ≠ the model: components and stakeholders · 14.2 Training/serving skew and feature pipelines · 14.3 Offline vs online evaluation; shadow and canary deployment · 14.4 Data distribution shifts: covariate, label, concept drift — detecting with PSI-style statistics · 14.5 Monitoring: what to log, what to alarm, feedback loops · 14.6 Retraining and continual learning — when it helps, when it poisons · 14.7 Versioning: data, code, model · 14.8 Common mistakes · 14.9 Summary table · Notes. *(All vendor/tool claims date-stamped `[checked 2026-10]`.)*
- **Worked examples:** (a) build a train/serve skew bug deliberately (normalisation fit on train but recomputed at serve) — the metrics diverge, the fix; (b) inject drift into a live-feature stream and detect it with PSI + a two-sample test; (c) design the monitoring dashboard for the capstone service — which panels, which alarms, drawn as a figure.
- **Figures:** (a) full-system block diagram (data → features → train → registry → serve → monitor → retrain); (b) train/serve skew illustration; (c) drift types panel (three small plots of shifting $p(\mathbf x),p(y),p(y\mid\mathbf x)$); (d) PSI histogram pair pre/post drift; (e) shadow/canary deploy diagram; (f) feedback-loop schematic.
- **Code listings:** `skew_demo.py` (the bug + fix, printed metrics); `drift_detect.py` (PSI + KS test on a shifted stream); `canary_sim.py` (traffic-split simulator scoring old-vs-new model); monitoring-config YAML snippet.
- **Evaluation/failure analysis:** the whole chapter is failure analysis; the capstone is "the model that scored well and failed silently" — silent skew + label-delay feedback loop.
- **Exercises:** ~3 inline; +10 (3 easy: drift-type identification; 4 medium: implement PSI, design an alarm policy; 3 hard: analyse a feedback loop mathematically; design retraining triggers; adversarial-skew case study).

### Chapter 15 — Evaluating language-model systems (10 pp)

- **Aim:** how to measure a system whose output is text — reference metrics, LLM-as-judge, golden sets, rubrics, and building an eval loop you trust.
- **Prerequisites:** ch3 (metrics), ch10–11; Book 3 statistics.
- **Sections:** 15.1 Why LM evaluation is hard: open outputs, no single truth · 15.2 Reference metrics: BLEU/ROUGE/exact-match — what they do and do not measure · 15.3 Human evaluation and inter-rater agreement · 15.4 LLM-as-judge: position bias, length bias, self-preference — measured, not asserted · 15.5 Golden sets and rubric grading; capability vs system evals · 15.6 The eval loop: prompt change → regression suite → decision · 15.7 Public benchmarks and their contamination problem · 15.8 Common mistakes · 15.9 Summary table · Notes. *(Every model/benchmark claim date-stamped.)*
- **Worked examples:** (a) compute BLEU/ROUGE by hand on two candidate summaries — where they disagree with human judgment; (b) a tiny LLM-as-judge experiment (two orderings of the same pair, judge bias measured); (c) build a 30-item golden set for a toy QA task and run a prompt-regression suite.
- **Figures:** (a) eval taxonomy map (reference/human/judge/task); (b) judge-bias experiment bars (position A vs B flip rate); (c) golden-set pipeline diagram; (d) prompt-regression dashboard mock (real eval output); (e) contamination cartoon→mechanism figure.
- **Code listings:** `rouge_bleu_scratch.py`; `judge_bias_test.py` (paired-ordering protocol, prints flip rate — works with a tiny open model or a stub); `golden_eval.py` (rubric scorer + regression diff table).
- **Evaluation/failure analysis:** judge-bias measurement IS the failure item; plus benchmark-contamination demo (a "95%" that collapses when the test items are paraphrased).
- **Exercises:** ~3 inline; +10 (3 easy: metric reads; 4 medium: implement ROUGE-L, design a rubric, paired-ordering protocol; 3 hard: inter-rater reliability (Cohen's $\kappa$) computation; design an eval for a task with no reference; contamination audit design). No-API-key path: all listings run against a tiny local model or canned responses.

### Chapter 16 — Agent patterns (11 pp)

- **Aim:** when an LLM is a component in a larger system — the workflow/agent distinction, the standard workflow patterns, tool use, and how agents fail.
- **Prerequisites:** ch11, ch15.
- **Sections:** 16.1 Workflows vs agents: who controls the path — code or model · 16.2 The augmented LLM: retrieval, tools, memory as the building block · 16.3 Workflow patterns: prompt chaining · routing · parallelisation · orchestrator–workers · evaluator–optimiser · 16.4 Agents: the plan–act–observe loop, ReAct-style traces · 16.5 Memory: short-term, retrieval, and what to store · 16.6 Tool use: schemas, errors, and the interface contract · 16.7 Evaluating agents: trajectories, success rates, cost · 16.8 When NOT to build an agent · 16.9 Common mistakes · 16.10 Summary table · Notes. *(Framework landscape date-stamped; the patterns are taught framework-free.)*
- **Worked examples:** (a) prompt-chaining a two-step task (extract → answer) vs a single monolithic prompt — quality/latency comparison; (b) an orchestrator–workers toy: decompose a research task into subtasks with a join; (c) a minimal ReAct agent with two tools (calculator, mock search) — a full trace shown, then a failure trace.
- **Figures:** (a) workflow-vs-agent control diagram; (b) the augmented-LLM building block; (c) the five workflow patterns as a taxonomy figure (routing/chaining/parallel/orchestrator/evaluator); (d) ReAct trace timeline; (e) memory-architecture diagram; (f) agent-failure gallery (loop, tool-misuse, context overflow).
- **Code listings:** `prompt_chain.py` (chain vs monolith, printed outputs); `react_minimal.py` (~60 lines: loop, two tools, trace dump); `agent_eval.py` (trajectory scorer + cost table). No-API-key path via a mock-LLM shim so every listing runs offline.
- **Evaluation/failure analysis:** the failure-trace autopsy — a real (recorded) agent run that loops on a tool error; the fix and the re-run.
- **Exercises:** ~3 inline; +10 (3 easy: pattern identification; 4 medium: add a tool, design an evaluator prompt, route by confidence; 3 hard: design agent eval for a multi-step task; analyse loop-termination guarantees; memory-retrieval design).

---

## Part V — Craft (≈20 pp)

### Chapter 17 — Reading and reproducing papers (8 pp)

- **Aim:** the meta-skill — deconstructing an ML paper, and the discipline of reproduction (what the claim is, what evidence would show it, what to vary).
- **Prerequisites:** all of the above (used, not assumed).
- **Sections:** 17.1 The anatomy of an ML paper: claim, method, evidence, ablations · 17.2 The three-pass read and the questions to ask at each pass · 17.3 Reproduction levels: re-run → re-implement → replicate on new data · 17.4 The reproduction lab notebook: what to log, seeds, variance, reporting honestly · 17.5 When reproductions fail: missing details, evaluation drift, compute gaps · 17.6 Summary table · Notes.
- **Worked examples:** (a) three-pass read of the LeNet-5 paper done on the page — marginalia shown; (b) the reproduction plan for candidate A built as a checklist; (c) a published "result" that failed to reproduce (a documented case, cited) — post-mortem.
- **Figures:** (a) paper-anatomy map; (b) reproduction-levels ladder; (c) lab-notebook template page; (d) reproduction funnel figure (paper → plan → code → run → report).
- **Code listings:** `repro_checklist.md`/`repro_log.py` (the notebook harness: config → seed → run → metric table); a filled reproduction-report skeleton.
- **Evaluation/failure analysis:** the post-mortem of a failed reproduction — is the claim wrong or the reproduction?
- **Exercises:** ~2 inline; +10 (4 easy: claim/evidence extraction; 4 medium: write reproduction plans for two named papers; 2 hard: reproduce a table row of the chosen paper as rehearsal).

### Chapter 18 — Capstone: a model service, an evaluation harness and a reproduction (12 pp)

- **Aim:** three artefacts that prove the outcomes: a deployed model service with an evaluation harness, and a written reproduction of one published result.
- **Prerequisites:** ch3–17.
- **Deliverable A — model service:** FastAPI service wrapping a Part-II/III model: `/predict`, `/health`, `/metrics`; input validation; model-card README; runs locally (Docker optional). 
- **Deliverable B — eval harness:** golden set + regression suite + drift check (reusing ch14's `drift_detect`) + a canary-comparison mode; every run logs config/seed/metrics.
- **Deliverable C — reproduction write-up:** one published result reproduced and reported (claim → protocol → result → deviation analysis), 2–3 pages using ch17's template.
- **Reproduction candidates (decided at writing time; all CPU/free-GPU feasible):**
  1. **LeNet-5 on MNIST** (LeCun et al. 1998): headline ~99% test accuracy; ~minutes–1 h CPU. *Primary pick* — cheapest fully-verifiable reproduction.
  2. **ResNet-20 on CIFAR-10** (He et al. 2016): ~8.75% reported test error; free-tier GPU ~1–2 h. *Stretch pick* — demonstrates residual learning, needs GPU.
  3. **Double-descent on MNIST-1D** (Belkin/Nakkiran et al.; UDL's variant): interpolation-peak curve; ~tens of minutes CPU. *Fallback* — teaches evaluation skepticism, no GPU.
- **Figures:** (a) capstone system diagram (data→train→service→harness→report); (b) service endpoint sequence diagram; (c) harness dashboard output; (d) reproduction result figure (our curve vs paper's number).
- **Code listings:** `service.py` (the FastAPI app); `eval_harness.py` (golden+drift+canary runner); `repro_report.md` skeleton + the result table.
- **Evaluation:** the harness IS the evaluation; success = service answers correctly, harness catches a deliberately-broken model, reproduction lands within a stated tolerance of the published number.
- **Exercises:** +10 (5 medium: extend service (batch endpoint, auth stub), add a harness check; 5 hard: deploy to a free tier (date-stamped, optional), reproduce a second table row, adversarial inputs).

---

## Back matter (≈22 pp)

- Hints for all `[hard]` exercises.
- Solutions to ≥half of all exercises (full solutions; the rest get hints).
- `docs/` set kept current: `sources.md`, `unverified.md`, `progress.md`, `review-log.md`.
- Bibliography (numbered): ISLP, D2L, S&B, DMLS, AI Engineering, UDL, CS231n notes, SLP3 draft, fast.ai course, Weng (2023), Anthropic (2024), CS329S notes, HF course, USAAIO problems (by year/round), LeCun et al. 1998, He et al. 2016, Vaswani et al. 2017, Kingma & Welling 2013, Goodfellow et al. 2014, Ho et al. 2020, Belkin/Nakkiran.
- Index via `makeindex`.

## Sources for this outline

See `docs/sources.md`. Ordering decisions follow D2L's two-level progression for Part III, ISLP's concept→lab rhythm adapted to per-section labs, S&B's tabular→approximation compression for ch13, CS329S/DMLS ordering for ch14, and Anthropic's workflow taxonomy + Weng's decomposition for ch16. Exercise style borrows USAAIO's derive→implement→apply pattern and Round-1 concept drills.
