#!/usr/bin/env python3
"""
This script illustrates the usage of the SiteSampler class.
You can run this script multiple times and it will generate
a different random walk trajectory every time.
"""

__author__="Igor Volobouev (i.volobouev@ttu.edu)"
__version__="0.4"
__date__ ="Mar 22 2018"

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import dla
import numpy as np

# Example array of transition probabilities (not normalized)
p = ((0, 0, 1, 2, 1, 0, 0),
     (0, 1, 2, 3, 2, 1, 0),
     (1, 2, 3, 4, 3, 2, 1),
     (2, 3, 4, 0, 4, 3, 2),
     (1, 2, 3, 4, 3, 2, 1),
     (0, 1, 2, 3, 2, 1, 0),
     (0, 0, 1, 2, 1, 0, 0))
a = np.array(p, 'float')

# ny is the number of rows and nx is the number of columns
ny, nx = a.shape

# Create the sampler
Walker = dla.Walker(a)

# Starting point for the random walk
x, y = 0, 0
xcoords = [x,]
ycoords = [y,]

# Create generator of random numbers
gen = dla.CPP11Random()

nsteps = np.arange(100,1100,100)
mean_dist = []
mean_vecx = []
mean_vecy = []
plot_dist = []
plot_vecx = []
plot_vecy = []

# Perform a random walk. Operator "//" is used to perform integer division.

for n in nsteps:
    mean_dist = []
    mean_vecx = []
    mean_vecy = []
   
    for i in range(10):
        dist_list = []
        dis_x = []
        dis_y = []

        for i in range(n):
            Walker.step(gen())
            xcoords.append(Walker.getI())
            ycoords.append(Walker.getJ())
    
        for i in range(len(xcoords)-1):
            dis_x.append(xcoords[i+1]-xcoords[i])
            dis_y.append(ycoords[i+1]-ycoords[i])

        for i in range(len(xcoords)):
            dist = np.sqrt(xcoords[i]**2+ycoords[i]**2)
            dist_list.append(dist)
    
        mean_dist.append(sum(dist_list)/len(dist_list))

        mean_vecx.append(sum(dis_x)/len(dis_x))
        mean_vecy.append(sum(dis_y)/len(dis_y))

    plot_dist.append(sum(mean_dist)/len(mean_dist))
    plot_vecx.append(sum(mean_vecx)/len(mean_vecx))
    plot_vecy.append(sum(mean_vecy)/len(mean_vecy))

plt.figure()
plt.plot(nsteps,plot_dist)
ax = plt.gca()
ax.grid()
ax.set_title('mean distance')
ax.set_xlabel('number of steps')
ax.set_ylabel('distance')
plt.savefig('distance_plot.pdf')
plt.close()

plt.figure()
plt.plot(plot_vecx, plot_vecy, 'bo')
ax = plt.gca()
ax.grid()
ax.set_title('mean displacement vectors (endpoints)')
ax.set_xlabel('mean x component')
ax.set_ylabel('mean y component')
plt.savefig('vector_plot.pdf')
plt.close() 
'''
# Display the trajectory
plot(xcoords, ycoords)
title("Random Walk Trajectory")
xlabel("X")
ylabel("Y")
show()
'''
