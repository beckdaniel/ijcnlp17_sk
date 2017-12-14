import matplotlib.pyplot as plt
import numpy as np
import argparse
import os
from run import SLENS

parser = argparse.ArgumentParser()
parser.add_argument('results', type=str)
args = parser.parse_args()

sk_results = np.loadtxt(os.path.join(args.results, 'sk.tsv'))
vsk_results = np.loadtxt(os.path.join(args.results, 'vsk.tsv'))
maybe_gpu = os.path.join(args.results, 'vsk_gpu.tsv')
if os.path.exists(maybe_gpu):
    vsk_gpu_results = np.loadtxt(maybe_gpu)
else:
    vsk_gpu_results = None

fig, ax = plt.subplots(1,1, figsize=(5,3))

ax.plot(SLENS, sk_results, lw=2, label='Non-vectorised SK', linestyle='--')
ax.plot(SLENS, vsk_results, lw=2, label='Vectorised SK')
if vsk_gpu_results is not None:
    ax.plot(SLENS, vsk_gpu_results, lw=2, label='Vectorised SK (GPU)', linestyle='-.')
ax.set_xlabel('String length')
ax.set_ylabel('Wall-clock time (seconds)')
ax.legend(loc=0)

plt.tight_layout()
plt.show()

