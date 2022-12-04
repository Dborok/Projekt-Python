import matplotlib.pyplot as plt
import numpy as np

from numpy import *


def f(x, y):
    return np.cos(x) * x * (1 + (np.cos(y)) / 2)


x = np.linspace(-10, 10, 150)
y = np.linspace(-10, 10, 150)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='magma')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Alpine Function")
plt.savefig("Alpine Function.png")
