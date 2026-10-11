# hf_pipeline.py -- the library view: a real transformers pipeline,
# its model card, and what it costs to load one.
from transformers import pipeline
import time

t0 = time.time()
clf = pipeline("sentiment-analysis")
print(f"model loaded in {time.time()-t0:.0f}s:",
      clf.model.name_or_path)
for s in ["This chapter took longer than the LSTM chapter.",
          "The mask leak was subtle and I nearly shipped it.",
          "Perplexity 8.9 is honest but not impressive."]:
    r = clf(s)[0]
    print(f"  {r['label']:8s} {r['score']:.3f}  | {s[:52]}")

lm = pipeline("fill-mask")
print("fill-mask model:", lm.model.name_or_path)
mtok = lm.tokenizer.mask_token          # '<mask>' for RoBERTa, '[MASK]' for BERT
print("mask token for this model:", mtok)
for r in lm(f"Attention is all you {mtok}.")[:3]:
    print(f"  {r['token_str']:10s} {r['score']:.3f}")
