import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

# 1. real vs indep vs AR sample grids (3x8 panels each? -> 3 rows x 8)
fig,axes=plt.subplots(3,8,figsize=(8,3.2))
for r,(f,t) in enumerate([('sample_real','real'),('sample_indep','independent'),('sample_ar','AR prev-px')]):
    A=np.load(f'../code/ch12/{f}.npy')
    for c in range(8):
        axes[r,c].imshow(A[c],cmap='gray_r',vmin=0,vmax=1);axes[r,c].axis('off')
    axes[r,0].set_ylabel(t,fontsize=8,rotation=0,labelpad=34,va='center')
fig.suptitle('24 samples: held-out reals vs two generative baselines',fontsize=8)
fig.tight_layout();fig.savefig('ch12/samples.pdf');plt.close(fig)

# 2. VAE latent traversal grid (real 8x8 grid of 8x8 digits)
fig,ax=plt.subplots(figsize=(4.4,4.4))
ax.imshow(np.load('../code/ch12/vae_grid.npy'),cmap='gray_r',vmin=0,vmax=1)
ax.set_xticks([]);ax.set_yticks([])
ax.set_xlabel('z[0]: -2 .. +2');ax.set_ylabel('z[1]: -2 .. +2')
ax.set_title('VAE latent traversal (real decoder outputs)',fontsize=8)
fig.tight_layout();fig.savefig('ch12/vae_grid.pdf');plt.close(fig)

# 3. VAE fresh samples strip
A=np.load('../code/ch12/vae_samples.npy')
fig,axes=plt.subplots(2,8,figsize=(8,2.2))
for i in range(16):
    axes.flat[i].imshow(A[i],cmap='gray_r',vmin=0,vmax=1);axes.flat[i].axis('off')
fig.suptitle('VAE ancestral samples (z ~ N(0,I))',fontsize=8)
fig.tight_layout();fig.savefig('ch12/vae_samples.pdf');plt.close(fig)

# 4. diffusion denoising trajectory (real)
T=np.load('../code/ch12/diff_traj.npy')
fig,axes=plt.subplots(1,len(T),figsize=(8.4,1.6))
labels=['T=50 (noise)','40','30','20','10','1']
for ax,a,l in zip(axes,T,labels):
    ax.scatter(a[:,0],a[:,1],s=2,alpha=.5,c='#2166ac');ax.set_title(l,fontsize=7)
    ax.set_xticks([]);ax.set_yticks([]);ax.set_xlim(-2.5,2.5);ax.set_ylim(-2.5,2.5)
fig.suptitle('DDPM denoising a 2-D spiral (real trajectory)',fontsize=8)
fig.tight_layout();fig.savefig('ch12/diff_traj.pdf');plt.close(fig)
print('done')
