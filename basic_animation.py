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

redDot, = plt.plot([np.cos(0)], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(np.cos(i), np.sin(i))
    return redDot,

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
                                      interval=10, blit=True, repeat=True)

plt.show()
