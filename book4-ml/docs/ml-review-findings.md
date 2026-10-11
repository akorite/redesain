# textbook-ml ch01-11 review (reviewer: quant session, pkg 56bd8ef9, 158pp)

Method: live-ran every .py in each code/chNN dir (numpy/sklearn/torch-cpu installed), diffed stdout vs recorded .out.txt, verified FR URLs + Watch videos via oembed/HTTP, counted contract items, spot-checked math.

## Verified-by-run evidence
- Scratch-vs-library pairs: ch03 knn_scratch VERBATIM; ch04 linreg_scratch VERBATIM; ch05 tree_scratch + forest_lib VERBATIM; ch06 kmeans_scratch VERBATIM, cluster_lib output present (ARI 0.665/0.794, silhouette 0.182/0.178 — content matches, minor print-order diff vs .out.txt); ch11 attention_scratch leak-detection real (leaked mask err 0.0709 vs causal 0.0000) and attn_vs_lib "max|scratch − nn.MultiheadAttention|=0.0, allclose True".
- ch01/02 scripts need data/{iris.csv,...} + ch10 needs data/tiny_shakespeare.txt — both files absent from pkg (KNOWN-MISSING delivered-state nit per coordinator note, not a content defect; scripts are written repo-root-relative and correct).
- ch07/09 torch scripts run under CPU torch 2.8 (mlp_torch trains to ~0.95 test acc; gradcheck catches a planted b1 bug at diff 3.0e-2 as designed). transformers not installed — hf_pipeline untested (code reads correct).
- FR: sampled 7 URLs all 200; Watch: all sampled videos oembed-verified w/ title+channel+duration+access date 2026-10-11 in-text.

## Verdicts
| chapter | verdict | notes |
|---|---|---|
| ch01 data loading | REVISE (contract) | 5 WEs OK, 16 ex OK, but only **1 figure** in text (<6; timing.dat exists under figures/ch01 but no figure uses it). ch01 dats missing = delivered-state nit. |
| ch02 wrangling | REVISE (contract) | 5 WEs OK, figs 4<6. |
| ch03 evaluation | REVISE (contract) | 5 WEs OK, figs 4<6. knn_scratch+leak_demo VERBATIM. |
| ch04 linear models | REVISE | **3 WEs <5**, figs 4<6, ex 15 OK. Content strong (WE 4.1 singular XTX correct) but WE count is a hard miss. |
| ch05 trees/ensembles | REVISE | **3 WEs <5**, figs 4<6. tree_scratch/forest_lib VERBATIM. |
| ch06 unsupervised | REVISE | **3 WEs <5**, figs 6 OK (met), ex 14<15 borderline nit. |
| ch07 backprop/MLP | REVISE | **4 WEs <5**, figs 5<6. gradcheck real. |
| ch08 optimization | REVISE | **3 WEs <5**, figs 6 OK. |
| ch09 CNNs | REVISE | **3 WEs <5**, figs 3<6. cnn_torch needs torch (present now; script correct). |
| ch10 sequence models | REVISE | **4 WEs <5**, figs 4 all MISSING (delivered-state nit), needs tiny_shakespeare.txt (missing nit). |
| ch11 transformers | REVISE | **4 WEs <5**, figs 3 all MISSING (delivered-state nit). attn scratch-vs-lib verified. |

## Verbatim-specified fixes (for a REVISE pass)
1. WE count: chapters 04,05,06,07,08,09,10,11 are below the ≥5 WE contract (3-4 each). Add 1-2 WEs per chapter (e.g. ch04: softmax-from-logreg generalization WE exists implicitly in §softmax — promote to an example env; ch09: a filter-as-feature-detector WE on the printed misclassified.pdf).
2. Figure count: ch01 (1 fig) add e.g. a data-layout figure (X matrix schema, train/val/test split bar) — sources exist in code outputs; ch02-05 add 2 each (book has 31 fig_*.py generators — run more of them); ch09 add 3 (CNN chapter is maximally visual).
3. Exercises: ch06 at 14 — add one graded item.
4. Known-delivered-state (NOT author defects): figures/ch10/*.pdf + figures/ch11/*.pdf + ch01 .dat data files are missing from this pkg; author's resend is in flight per coordinator.
