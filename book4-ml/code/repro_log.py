# repro_log.py -- the lab-notebook harness: every run logs config -> seed -> metrics.
# Used to rehearse the reproduction protocol before pointing it at a paper claim.
import json, time, random
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def run(cfg, log='repro_log.jsonl'):
    """one logged run: seed in, metric out, everything appended as a JSON line"""
    random.seed(cfg['seed']); np.random.seed(cfg['seed'])
    X, y = load_breast_cancer(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2,
                                        random_state=cfg['seed'])
    m = LogisticRegression(max_iter=cfg['max_iter'], C=cfg['C'])
    m.fit(Xtr, ytr)
    rec = dict(t=time.strftime('%H:%M:%S'), **cfg,
               train_acc=round(m.score(Xtr, ytr), 4),
               test_acc=round(m.score(Xte, yte), 4))
    open(log, 'a').write(json.dumps(rec) + '\n')
    print(rec)
    return rec

base = dict(max_iter=5000, C=1.0)
print('--- variance across seeds (same config) ---')
accs = [run(dict(base, seed=s))['test_acc'] for s in range(5)]
print(f'test accs {accs}  mean {np.mean(accs):.4f} sd {np.std(accs):.4f}')
print('--- one knob turned (C=100) ---')
run(dict(base, seed=0, C=100))
print('log written: repro_log.jsonl -- diff two lines to see what changed')
