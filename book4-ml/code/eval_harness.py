# eval_harness.py -- golden set + drift check + canary mode over the service model.
# every run logs config/seed/metrics as one JSON line (ch17's protocol).
import json, time, numpy as np, torch
from torchvision import datasets, transforms
from service import net, predict_tensor

tf = transforms.Compose([transforms.Pad(2), transforms.ToTensor(),
                         transforms.Normalize((0.1307,), (0.3081,))])
te = datasets.MNIST('/tmp/mnist', train=False, transform=tf)

def score(model_predict, n=200, seed=0):
    g = torch.Generator().manual_seed(seed)
    idx = torch.randperm(len(te), generator=g)[:n]
    ok = sum(model_predict(te[int(i)][0][None])[0] == te[int(i)][1] for i in idx)
    return ok / n

def psi(ref, cur, bins=10):
    e = np.quantile(ref, np.linspace(0, 1, bins+1)); e[0], e[-1] = -np.inf, np.inf
    p = np.histogram(ref, e)[0]/len(ref); q = np.histogram(cur, e)[0]/len(cur)
    p = np.clip(p, 1e-4, None); q = np.clip(q, 1e-4, None)
    return float(np.sum((p-q)*np.log(p/q)))

log = open('harness_log.jsonl', 'a')
def emit(**kw):
    rec = dict(t=time.strftime('%H:%M:%S'), **kw)
    log.write(json.dumps(rec)+'\n'); print(rec)

print('== golden: 200-image fixed set ==')
g = score(predict_tensor)
emit(check='golden', acc=round(g, 4))
print('== drift: brightness-boosted batch vs train-mean reference ==')
ref = np.concatenate([te[int(i)][0].numpy().ravel() for i in range(500)])
drift_imgs = [te[int(i)][0].numpy().ravel()*1.6 for i in range(500)]
p = psi(ref, np.concatenate(drift_imgs))
emit(check='drift_psi', psi=round(p, 4), alarm=p > 0.25)
print('== canary: real model vs deliberately-broken (shuffled logits) ==')
def broken(x):
    with torch.no_grad(): p = torch.softmax(net(x), 1)
    return int(torch.randperm(10)[0]), 0.1
b = score(broken)
emit(check='canary', good_acc=round(g, 4), broken_acc=round(b, 4),
     caught=(g - b) > 0.10)
print('harness OK -- see harness_log.jsonl')
