# textbook-ml ch12–18 — independent review findings (quant session, 2026-10-11)

Branch `book4-ml-ch12-18` @ 0ca0a82. Same rigor as the ch01–11 pass:
contract counts, every code artifact run and diffed vs committed
.out.txt, FR/Watch live-verified, math spot-checks.

## Verdicts: all 7 chapters REVISE on ONE shared build-blocking defect
Content is otherwise in far better shape than ch01–11 — every chapter
meets every count (5 WEs / ≥6 figure graphics / 15 graded exercises /
Common mistakes / Notes / Hints-and-answers / summary table), all math
spot-checks pass, and 19/20 runnable artifacts reproduce their printed
output verbatim.

---

## F1 [build-blocking, all chapters] code/chNN/ paths — artifacts at repo root
Every chapter references `code/chNN/<file>` but the artifacts landed at
`code/<file>` (convention from ch01–11 is per-chapter subdirs). Each
chapter fatals on its first listing:
`! Package Listings Error: File 'code/ch12/sample_compare(.py)' not found.`

**Verbatim fix** — 43 of 45 referenced files exist, just misplaced:
```
cd book4-ml/code
mkdir -p ch12 ch13 ch14 ch15 ch16 ch17 ch18
git mv sample_compare.py sample_compare.out.txt vae_torch.py vae_torch.out.txt gan_collapse.py gan_collapse.out.txt diffusion2d.py diffusion2d.out.txt ch12/
git mv bandits.py bandits.out.txt qlearn_grid.py qlearn_grid.out.txt cartpole_linear.py cartpole_linear.out.txt ch13/
git mv skew_demo.py skew_demo.out.txt canary_sim.py canary_sim.out.txt drift_detect.py drift_detect.out.txt ch14/
git mv rouge_bleu_scratch.py rouge_bleu_scratch.out.txt judge_bias_test.py judge_bias_test.out.txt golden_eval.py golden_eval.out.txt contam_demo.py contam_demo.out.txt ch15/
git mv prompt_chain.py prompt_chain.out.txt react_minimal.py react_minimal.out.txt agent_eval.py agent_eval.out.txt ch16/
git mv repro_log.py repro_log.out.txt ch17/
git mv ../docs/repro_checklist.md ch17/
git mv service.py service.out.txt eval_harness.py eval_harness.out.txt lenet5_repro.py lenet5_repro.out.txt lenet5_log.json ch18/
git mv ../docs/repro_report.md ch18/
```
(mockllm.py, lenet5_state.pt, *.npy intermediates: move mockllm.py to
ch16/ too — react_minimal.py imports it — and either commit
lenet5_state.pt into ch18/ or note in ch18 Notes that
`lenet5_repro.py` must run first to produce it.)

## F2 [ch14, content] `code/ch14/monitoring.yaml` does not exist anywhere
lst:monyaml (ch14 line ~215) inputs it as "the capstone dashboard as a
config — six panels, four alarms, runbook lines". No such file in the
tree. Fix: write the yaml the caption describes (six panels: request
rate/latency/prediction-dist/PSI/error-rate/uptime; four alarms w/
runbook lines), or drop the listing. Everything else in ch14 verified.

## F3 [delivered-state] main.tex still `\input`s only ch01–11
The 164pp build claim in the commit is ahead of main.tex; ch12–18 are
not yet in the book. Chapters compile individually once F1 is fixed.

## Code-run results (all executed on this box)
VERBATIM (byte-identical to committed .out.txt): sample_compare,
skew_demo, canary_sim, drift_detect, rouge_bleu_scratch,
judge_bias_test, golden_eval, contam_demo, prompt_chain, react_minimal,
agent_eval, bandits, qlearn_grid, cartpole_linear, vae_torch,
gan_collapse, diffusion2d — 18/20.
- repro_log: DIFF in 't' timestamps only; every metric identical → nit.
- service.py: runs clean; pred confidences differ (mine p=1.000 vs
  committed 0.999) — inherent retrain variance; lenet5_state.pt not
  committed (see F1 fix). Nit.
- eval_harness.py: golden acc 0.985 vs committed 0.965, broken_acc 0.1
  vs 0.07 — retrain variance; PSI identical 11.0862; all checks caught.
  Nit.
- lenet5_repro.py (8 epochs, real MNIST): reproduced committed
  .out.txt EXACTLY except wall-times — params 61706, final err 0.0125
  vs paper 0.0095. Fully deterministic. Strongest possible outcome.

## Links: 46/46 live (200). Watch: 14/14 verified to the SECOND
(oembed + lengthSeconds): CS231n L13 77:41; Arxiv Insights VAE 15:05;
M2L Salimans diffusion 69:24; Silver RL L1 88:12; Stanford Eng L14
64:01; Full Stack ML-test 15:48; GAIA Aukea 23:04; Schovia HELM 14:36;
onepagecode LLM-judge 129:15; AI Engineer Zhang 15:09; Anthropic
agents 18:19; Siraj read-paper 8:43(→8:44 measured, rounding nit);
Stuckler 9:42; EuroPython FastAPI 45:05.

## Math spot-checks (all pass)
ch12: ΔNLL 0.3943−0.3740=0.0203 nats/px → e^(0.0203·64)≈3.7× ✓;
log2−0.394=0.299 → e^19.1≈2e8 ✓. ch13: G0[1,1,1,1,−3] at γ=0/0.5/0.9/0.99
= 1.00/1.69/1.47/1.06 all recomputed ✓; Bellman eq correct form.
ch14: PSI 0.013–0.038 quiet → 0.601 at injection, zero rows late — text
matches out.txt. ch15: BLEU/ROUGE table matches out.txt (D 0.893/0.909,
E 0.002). ch16: success 5/8=0.62, mean steps 43/8≈5.4, cost/success
0.0131/5≈0.0026 all recomputed. ch17: seed spread mean 0.9351 sd 0.0131,
3.5pp — recomputed. ch18: 1.25% err vs 0.95% band — matches log.

## Nits (non-blocking)
- \index coverage thins out ch14→ch18 (4,4,1,1,1) vs ch01-13 (~10-15);
  book-wide pattern, same in ch11.
- Scripts save intermediates to /tmp/*.npy and cwd (untracked outputs);
  figure PDFs are committed so provenance is fine, but regeneration
  needs the .npy step documented.
- FR lists run 13–15 items (ceiling is "5–10"); consistent with
  ch01–11's landed style — book-wide call, not per-chapter.
- Siraj video measured 8:44 vs claimed 8:43 (rounding).
