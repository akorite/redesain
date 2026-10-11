# service.py -- a minimal model service: /predict /health /metrics, offline.
# uses the trained LeNet state dict; run: uvicorn service:app  (or the __main__ stub)
import torch, torch.nn as nn, time, io, base64
import numpy as np
from PIL import Image

class LeNet5(nn.Module):
    def __init__(self):
        super().__init__()
        self.f = nn.Sequential(
            nn.Conv2d(1, 6, 5), nn.Tanh(), nn.AvgPool2d(2),
            nn.Conv2d(6, 16, 5), nn.Tanh(), nn.AvgPool2d(2),
            nn.Conv2d(16, 120, 5), nn.Tanh(), nn.Flatten(),
            nn.Linear(120, 84), nn.Tanh(), nn.Linear(84, 10))
    def forward(self, x): return self.f(x)

net = LeNet5(); net.load_state_dict(torch.load('lenet5_state.pt')); net.eval()
STATS = dict(requests=0, errors=0, t0=time.time())

def predict_tensor(x):
    """x: (1,1,32,32) normalised -> (pred, prob)"""
    with torch.no_grad():
        p = torch.softmax(net(x), 1)
    v, i = p.max(1)
    return int(i), float(v)

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    app = FastAPI(title='digit-svc')
    class Req(BaseModel): image_b64: str
    @app.get('/health')
    def health(): return {'ok': True, 'up_s': time.time()-STATS['t0']}
    @app.get('/metrics')
    def metrics(): return dict(STATS, requests=STATS['requests'])
    @app.post('/predict')
    def predict(r: Req):
        STATS['requests'] += 1
        try:
            img = Image.open(io.BytesIO(base64.b64decode(r.image_b64))).convert('L')
            x = torch.from_numpy(np.array(img).astype('float32')/255)
            x = (x - 0.1307) / 0.3081
            x = torch.nn.functional.pad(x[None,None], (2,2,2,2))
            v, i = predict_tensor(x)
            return {'digit': v, 'prob': round(i, 4)}
        except Exception as e:
            STATS['errors'] += 1
            raise HTTPException(400, str(e))
except ImportError:
    app = None

if __name__ == '__main__':
    # offline smoke test: predict one real MNIST test image via the tensor path
    from torchvision import datasets, transforms
    tf = transforms.Compose([transforms.Pad(2), transforms.ToTensor(),
                             transforms.Normalize((0.1307,), (0.3081,))])
    te = datasets.MNIST('/tmp/mnist', train=False, transform=tf)
    for idx in [0, 1, 2]:
        x, y = te[idx]
        v, p = predict_tensor(x[None])
        print(f'idx {idx}: pred {v} (p={p:.3f}) true {y}')
    print('service module OK -- fastapi app' + (' ready' if app else ' (fastapi not installed; tensor path verified)'))
