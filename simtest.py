#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run "python simtest.py" in terminal to see the animation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulation_calculations import *

num_electrons = 10

fig, ax = plt.subplots()

ax = plt.axis([-1,1,-1,1])

#generate charges here
c = [Charge([0,0],v,0.005,1) for v in np.random.normal(0,1,size=(num_electrons,2))]

#define fields here
field_position = [-0.75,0.5]
wire_direction = [1,0]
f = [InfiniteWire(field_position,wire_direction,10000000000)]

h = 0.01

time_limit = 3

animation_frames = np.arange(0.0, time_limit, h)


poses = np.zeros((len(animation_frames),2,num_electrons))

for i in range(len(animation_frames)-1):
	time_step(c,f,h)
	for j in range(num_electrons):
		poses[i+1,0,j] = c[j].position[0]
		poses[i+1,1,j] = c[j].position[1]

plt.plot([field_position[0]-2*wire_direction[0],field_position[0]+2*wire_direction[0]], [field_position[1]-2*wire_direction[1],field_position[1]+2*wire_direction[1]], "r-")
redDot, = plt.plot(poses[0,0,:], poses[0,1,:], 'go')

def run(pos):
    def animate(i):
        redDot.set_data(pos[i,0,:], pos[i,1,:])
        return redDot,
    return animate

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, run(poses), frames=list(range(len(animation_frames))), \
                                      interval=10, blit=True, repeat=True)

    
plt.show()

#myAnimation.save("animation.gif", writer='imagemagick')
