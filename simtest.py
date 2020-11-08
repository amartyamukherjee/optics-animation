#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run "python basic_animation.py" in terminal to see the animation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulation_calculations import *

num_electrons = 10

fig, ax = plt.subplots()

ax = plt.axis([-1,1,-1,1])

#generate charges here
c = [Charge([0,0],v,0.005,1) for v in np.random.normal(size=(num_electrons,2))]

#define fields here
f = [InfiniteWire([0.5,-1],[1,0],10000000000)]

h = 0.01

animation_frames = np.arange(0.0, 100, h)

poses = np.zeros((len(animation_frames),2,num_electrons))

for i in range(len(animation_frames)-1):
	time_step(c,f,h)
	for j in range(num_electrons):
		poses[i+1,0,j] = c[j].position[0]
		poses[i+1,1,j] = c[j].position[1]

    #velocity = velocity * (-2*(np.logical_or(poses[i,:,:] > 1, poses[i,:,:] < -1)-0.5))
    #poses[i+1,:,:] = h*velocity + poses[i,:,:]
    
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
