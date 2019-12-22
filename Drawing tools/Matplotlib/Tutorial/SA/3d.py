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
# verts = []
verts = [ [(0,0.0),(0,-93.15),(1,-22.63),(2,-104.93),(2,0.0)],
		  [(0,0.0),(0,-38.33),(1,-62.07),(2,7.43),(2,0.0)], 
		  [(0,0.0),(0,-94.64),(1,-77.09),(2,-123.23),(2,0.0)], 
		  [(0,0.0),(0,-127.38),(1,-92.33),(2,-80.00),(2,0.0)] ]

verts1 = [ [(0,0.0),(0,-93.15),(1,-22.63),(2,-104.93),(2,0.0)] ]		  
verts2 = [ [(0,0.0),(0,-38.33),(1,-62.07),(2,7.43),(2,0.0)] ]
verts3 = [ [(0,0.0),(0,-94.64),(1,-77.09),(2,-123.23),(2,0.0)] ]
verts4 = [ [(0,0.0),(0,-127.38),(1,-92.33),(2,-80.00),(2,0.0)] ]

# Set up the x sequence
# xs = np.linspace(0., 10., 3)
# xs = [0,0,1,1,2,2,0,0,1,1,2,2]
# xs = [0,1,2]


# ys = [0,1,0,1,0,1,0,1,0,1,0,1]

# The ith polygon will appear on the plane y = zs[i]
# zs = range(4)
zs = [0,1,0,1]
# zs = [-93.15,-38.33,-22.63,-62.07,-104.93,7.43,-94.64,-127.38,-77.09,-92.33,-123.23,-80.00]

# for i in zs:
#     ys = np.random.rand(len(xs))
#     verts.append(polygon_under_graph(xs, ys))

# print(xs)    
# print(ys)    
print(zs)    
print(verts)    

poly = PolyCollection(verts, 
					  facecolors=['r', 'g', 'b', 'y'], 
					  alpha=.6
					  # , 
					  # label = ['Visual Zeitgebers Without Task',
							#    'Visual Zeitgebers With Task',
							#    'Auditory Zeitgebers Without Task',
							#    'Auditory Zeitgebers With Task']
							)
ax.add_collection3d(poly, zs=zs, zdir='y')


poly._facecolors2d = poly._facecolors3d
poly._edgecolors2d = poly._edgecolors3d

ax.legend([poly],['Visual Zeitgebers Without Task',
				  'Visual Zeitgebers With Task',
				  'Auditory Zeitgebers Without Task',
				  'Auditory Zeitgebers With Task'])


# poly1 = PolyCollection(verts1, facecolors='r', alpha=.6)

# poly1._facecolors2d = poly1._facecolors3d
# poly1._edgecolors2d = poly1._edgecolors3d

# ax.add_collection3d(poly1, zs=0, zdir='y')

# ax.legend([poly1],['poly1'])
# ax.legend(poly)


ax.set_xlabel('Zeitgebers')
ax.set_ylabel('Cognitive Load')
ax.set_zlabel('Time Estimation Deviation')
# ax.set_xlim(0, 10)
# ax.set_ylim(-1, 4)
# ax.set_zlim(0, 1)

ax.set_xticks([0,1,2])
ax.set_xticklabels(['0','1','2'])
ax.set_yticks([0, 1])
# ax.set_yticklabels(['Without Task','With Task'])
ax.set_yticklabels(['0','1'])
ax.set_zlim(-150, 50)

plt.legend(loc='best')

plt.show()