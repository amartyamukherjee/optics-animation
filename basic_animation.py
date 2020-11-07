#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run "python basic_animation.py" in terminal to see the animation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)

ax = plt.axis([-1,1,-1,1])

pos = np.array([0.5,0.5])

velocity = np.random.normal(size=(2))

h = 0.01

animation_frames = np.arange(0.0, 100, 0.1)

poses = np.zeros((len(animation_frames),2))

poses[0,:] = pos

for i in range(len(animation_frames)-1):
    if poses[i,0] > 1 or poses[i,0] < -1:
        velocity[0] = -velocity[0]
    if poses[i,1] > 1 or poses[i,1] < -1:
        velocity[1] = -velocity[1]
    poses[i+1,:] = h*velocity + poses[i,:]
    
redDot, = plt.plot([pos[0]], [pos[1]], 'ro')

def run(pos):
    def animate(i):
        redDot.set_data([pos[i,0]], [pos[i,1]])
        return redDot,
    return animate

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, run(poses), frames=list(range(len(animation_frames))), \
                                      interval=10, blit=True, repeat=True)

plt.show()
