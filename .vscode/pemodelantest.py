import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np

fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.arange(-2, 15.5, 0.32)
Y = np.arange(3.27, 8.75, 0.1)
X, Y = np.meshgrid(X, Y)
Z = 10.4 + X * np.sin(3*np.pi*X) + Y * np.sin(13*np.pi*Y)
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2,
cmap=cm.winter,
linewidth=0, antialiased=True)
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()