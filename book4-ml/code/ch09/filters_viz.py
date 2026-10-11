# code/ch09/filters_viz.py -- render the learned conv1 filters and the
# feature maps they produce on a real digit. Requires cnn_state.pt,
# written by cnn_torch.py (run that first).
# Run from the repository root:  python3 code/ch09/filters_viz.py
import os, torch
import torchvision as tv
from torch import nn
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

cnn = nn.Sequential(
    nn.Conv2d(1, 8, 5), nn.ReLU(), nn.MaxPool2d(2),
    nn.Conv2d(8, 16, 3), nn.ReLU(), nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(16*5*5, 64), nn.ReLU(), nn.Linear(64, 10))
state = torch.load(os.path.join(os.path.dirname(__file__),
                                'cnn_state.pt'))
cnn.load_state_dict(state); cnn.eval()

te = tv.datasets.MNIST('/tmp/mnist', train=False, download=True,
                       transform=tv.transforms.ToTensor())
x, y = te.data[0].float().unsqueeze(0).unsqueeze(0)/255., te.targets[0].item()

fig = plt.figure(figsize=(10, 3))
W = cnn[0].weight.detach()            # (8, 1, 5, 5)
fm = cnn[1](cnn[0](x)).detach()       # conv1 + relu -> (1, 8, 24, 24)
for i in range(8):
    ax = fig.add_subplot(2, 8, i+1)
    ax.imshow(W[i,0], cmap='RdBu', vmin=-W.abs().max(),
              vmax=W.abs().max())
    ax.set_title(f'f{i}', fontsize=7); ax.axis('off')
    ax = fig.add_subplot(2, 8, i+9)
    ax.imshow(fm[0,i], cmap='viridis'); ax.axis('off')
fig.suptitle(f'top: learned 5x5 conv1 filters   '
             f'bottom: their feature maps on a "{y}"', fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__),
                         '../../figures/ch09/filters_maps.pdf'))
print(f"digit label {y}; conv1 filters {tuple(W.shape)};"
      f" feature maps {tuple(fm.shape)}")
print("wrote figures/ch09/filters_maps.pdf")
