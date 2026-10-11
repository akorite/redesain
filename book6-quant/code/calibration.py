"""Reliability calibration: bin forecast probs vs empirical hit rates."""
import numpy as np
rng=np.random.default_rng(3)
n=4000
fore=np.clip(rng.normal(0.5,0.22,n),0.02,0.98)
# miscalibrated generator: actual prob compressed toward 0.5
actual=0.5+(fore-0.5)*0.55
y=rng.random(n)<actual
edges=np.linspace(0,1,11); idx=np.digitize(fore,edges)-1
print("bin   mean_forecast  empirical   n")
ece=0
for b in range(10):
    m=idx==b
    if m.sum()>30:
        mf,er=fore[m].mean(),y[m].mean()
        ece+=m.sum()*abs(mf-er)/n
        print(f"{b/10:.1f}-{(b+1)/10:.1f}  {mf:.3f}          {er:.3f}      {m.sum()}")
print(f"ECE={ece:.4f}  (overconfident: forecasts more extreme than reality)")
# calibrated variant for contrast
fore2=0.5+(fore-0.5)*0.55  # forecaster = actual generator
y2=rng.random(n)<actual
idx2=np.digitize(fore2,edges)-1
ece2=sum(m2*0 for m2 in [0])
ece2=0
for b in range(10):
    m=idx2==b
    if m.sum()>30: ece2+=m.sum()*abs(fore2[m].mean()-y2[m].mean())/n
print(f"calibrated twin ECE={ece2:.4f}")
