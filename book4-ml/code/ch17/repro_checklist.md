# Reproduction checklist -- candidate A: LeNet-5 on MNIST (LeCun et al., 1998)

## Claim (what, exactly)
- [ ] Headline number copied verbatim: "error rate on the regular test set: 0.95%"
- [ ] Conditions: full MNIST, LeNet-5 (not -1/-4/boosted), no distortions
- [ ] Metric = test-set error rate; dataset = standard MNIST test (10,000)

## Protocol (the plan before running)
- [x] Architecture transcribed: C1(6,5x5)-S2-C3(16,5x5)-S4-C5(120,5x5)-F6(84)-out(10)
- [x] Input: 28x28 padded to 32x32, normalised (mean 0.1307, std 0.3081)
- [x] Optimiser (paper: diagonal-approx Hessian; ours: Adam lr=1e-3, 3 epochs -- DEVIATION, logged)
- [x] Seed fixed (0); 60k/10k split untouched
- [x] Tolerance set *before* running: +/-0.3pp of 0.95% = accept 0.65--1.25%

## Run
- [x] Command + environment logged (lenet5_repro.py, torch 2.8.0 CPU, macOS)
- [x] Every metric in one JSON line (lenet5_log.json)

## Report
- [ ] Result vs claim in one table; deviations itemised, each labelled mine/theirs
- [ ] Honest verdict: reproduces within tolerance / outside -- and why I think so
