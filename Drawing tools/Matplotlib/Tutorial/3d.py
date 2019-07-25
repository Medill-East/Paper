# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


def polygon_under_graph(xlist, ylist):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (xlist, ylist) line graph.  Assumes the xs are in ascending order.
    """
    return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make verts a list, verts[i] will be a list of (x,y) pairs defining polygon i
verts = []
# verts = [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]


# Set up the x sequence
xs = np.linspace(0., 10., 3)
# xs = [0,0,1,1,2,2,0,0,1,1,2,2]

# ys = [0,1,0,1,0,1,0,1,0,1,0,1]

# The ith polygon will appear on the plane y = zs[i]
zs = range(4)
# zs = [0,1,2,3,4]
# zs = [-93.15,-38.33,-22.63,-62.07,-104.93,7.43,-94.64,-127.38,-77.09,-92.33,-123.23,-80.00]

for i in zs:
    ys = np.random.rand(len(xs))
    verts.append(polygon_under_graph(xs, ys))

print(xs)    
print(ys)    
print(zs)    
print(verts)    

poly = PolyCollection(verts, facecolors=['r', 'g', 'b', 'y'], alpha=.6)
ax.add_collection3d(poly, zs=zs, zdir='y')

ax.set_xlabel('Zeitgebers')
ax.set_ylabel('Cognitive Load')
ax.set_zlabel('Time Estimation Deviation')
ax.set_xlim(0, 10)
ax.set_ylim(-1, 4)
ax.set_zlim(0, 1)

# ax.set_xlim(0, 4)
# ax.set_ylim(-1, 2)
# ax.set_zlim(-150, 50)

plt.show()