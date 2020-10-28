import pygame
from math import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.animation
from matplotlib import animation

t = np.linspace(0, 20, 1000)

u = float(input("x0 = "))%pi
print(u)
g = 9.8
L = 1
k = float(input("k = "))
v = ((k/2)*u)/(np.sqrt(-(k**2) + ((4*g)/L)))
e = 2.7182818284590452353602874713527

def a(x):
    A = (e**(-(k/2)*x))*(u*(np.cos((np.sqrt(-(k**2) + ((4*g)/L)))*x)) + v*(np.sin((np.sqrt(-k**2+ ((4*g)/L)))*x)))
    
    return(A)

def x(x):
    X = np.cos((e**(-(k/2)*x))*(u*(np.cos((np.sqrt(-(k**2) + ((4*g)/L)))*x)) + v*(np.sin((np.sqrt(-k**2+ ((4*g)/L)))*x))) - (pi/2))
    return(X)

def y(x):
    Y = np.sin((e**(-(k/2)*x))*(u*(np.cos((np.sqrt(-(k**2) + ((4*g)/L)))*x)) + v*(np.sin((np.sqrt(-k**2+ ((4*g)/L)))*x))) - (pi/2))
    return(Y)

a = a(t)
x = x(t)
y = y(t)

plt.plot(t, a)
plt.show()
plt.plot(x, y)
plt.show()

fig = plt.figure()
ax = plt.axes(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
d, = ax.plot([], [], 'ro')

point, = ax.plot([], [], ls="none", marker="o")

def animate(k):
    i = min(k, x.size)
    d.set_data(x[i], y[i])
    return d,

ani = animation.FuncAnimation(fig=fig, func=animate, frames=range(x.size), interval=50, blit=True)
