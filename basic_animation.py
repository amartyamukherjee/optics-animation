#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run "python basic_animation.py" in terminal to see the animation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_electrons = 2

fig, ax = plt.subplots()

ax = plt.axis([-1,1,-1,1])

velocity = np.random.normal(size=(2,num_electrons))

h = 0.01

animation_frames = np.arange(0.0, 100, 0.1)

poses = np.zeros((len(animation_frames),2,num_electrons))

for i in range(len(animation_frames)-1):
    velocity = velocity * (-2*(np.logical_or(poses[i,:,:] > 1, poses[i,:,:] < -1)-0.5))
    poses[i+1,:,:] = h*velocity + poses[i,:,:]
    
redDot, = plt.plot(poses[0,0,:], poses[0,1,:], 'ro')

def run(pos):
    def animate(i):
        redDot.set_data(pos[i,0,:], pos[i,1,:])
        return redDot,
    return animate

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, run(poses), frames=list(range(len(animation_frames))), \
                                      interval=10, blit=True, repeat=True)

plt.show()
