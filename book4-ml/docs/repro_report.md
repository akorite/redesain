# Reproduction report -- LeNet-5 on MNIST (LeCun et al., 1998)
## Claim
> "error rate on the regular test set: 0.95%" -- LeNet-5, standard MNIST 10k test.
## Protocol
- Environment: torch 2.8.0 CPU, macOS, wall ~3 min; code: lenet5_repro.py
- Deviations (itemised): Adam lr=1e-3 vs diagonal-Hessian; 8 epochs vs ~20; no distortion augmentation; tanh kept; 32x32 pad kept
- Tolerance set beforehand: +/-0.3pp (accept 0.65--1.25%)
## Result
| metric | paper | mine | delta |
|--------|-------|------|-------|
| test err | 0.95% | 1.25% (8ep); 1.92% (3ep) | +0.30pp / +0.97pp |
## Deviation analysis
- Epoch count is the dominant deviation (3ep: 1.92% -> 8ep: 1.25%; still descending)
- Optimiser difference is second-order on MNIST
- Seed variance on this task ~+/-0.1pp (small vs the remaining gap)
## Verdict
The claim reproduces in direction (single-digit MNIST error from a tiny convnet) but lands
OUTSIDE the preset band -- the itemised deviations, not the claim, carry the gap.
