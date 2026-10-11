import numpy as np, torch, os, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import torchvision as tv
from torch import nn

# --- 1. receptive field growth -----------------------------------------
fig,axes=plt.subplots(1,3,figsize=(9,2.6))
img=np.zeros((32,32));img[10:22,10:22]=1
axes[0].imshow(img,cmap='gray');axes[0].set_title('input (32x32)',fontsize=8)
for ax,(r,tt) in zip(axes[1:],[(5,'after conv1 5x5: rf=5'),(9,'after conv2 3x3+pool: rf=9')]):
    ax.imshow(img,cmap='gray')
    c=16;ax.add_patch(plt.Rectangle((c-r/2,c-r/2),r,r,fill=False,ec='r',lw=2))
    ax.set_title(tt,fontsize=8)
for ax in axes:ax.axis('off')
fig.tight_layout();fig.savefig('ch09/receptive.pdf');plt.close(fig)

# --- 2. misclassified gallery ------------------------------------------
cnn=nn.Sequential(nn.Conv2d(1,8,5),nn.ReLU(),nn.MaxPool2d(2),
    nn.Conv2d(8,16,3),nn.ReLU(),nn.MaxPool2d(2),nn.Flatten(),
    nn.Linear(16*5*5,64),nn.ReLU(),nn.Linear(64,10))
cnn.load_state_dict(torch.load('/Users/devin/textbook-ml/code/ch09/cnn_state.pt'))
cnn.eval()
te=tv.datasets.MNIST('/tmp/mnist',train=False,download=True)
X=te.data[:2000].float().unsqueeze(1)/255.;y=te.targets[:2000]
with torch.no_grad():pred=cnn(X).argmax(1)
wrong=(pred!=y).nonzero().flatten()[:12]
fig,axes=plt.subplots(2,6,figsize=(8,2.9))
for ax,i in zip(axes.ravel(),wrong):
    ax.imshow(te.data[i],cmap='gray')
    ax.set_title(f'{y[i]}→{pred[i]}',fontsize=7);ax.axis('off')
fig.suptitle('cnn misclassifications (true→pred)',fontsize=9)
fig.tight_layout();fig.savefig('ch09/misclassified.pdf');plt.close(fig)
print('n wrong:',len((pred!=y).nonzero().flatten()),'/2000')
