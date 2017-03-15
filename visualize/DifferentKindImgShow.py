# -*- encoding: utf-8 -*-

__author__ = 'luopei'

import numpy as np
import matplotlib.pyplot as plt

#smoothing between pixels of imagesc\imshow in matlab like the matplotlib imshow

plt.rcParams['image.interpolation'] = 'none'

methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming', \
           'hermite', 'kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

grid = np.random.rand(4,4)

fig, ax = plt.subplots(3,6,figsize=(12,6), subplot_kw={'xticks': [], 'yticks': []})
fig.subplots_adjust(hspace=0.3, wspace=0.05)

ax = ax.ravel()

for n, interp in enumerate(methods):
    ax[n].imshow(grid, interpolation=interp)
    ax[n].set_title(interp)
    
plt.show()
