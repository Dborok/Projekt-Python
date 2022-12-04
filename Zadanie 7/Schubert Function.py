import matplotlib.pyplot as plt
import numpy as np

from numpy import *


def f(x, y):
    return ((np.cos(2 * x + 1)) + (2 * np.cos(3 * x + 2))
            + (3 * np.cos(4 * x + 3)) + (4 * np.cos(5 * x + 4))
            + (5 * np.cos(6 * x + 5))) * ((np.cos(2 * y + 1))
                                          + (2 * np.cos(3 * y + 2)) + (3 * np.cos(4 * y + 3))
                                          + (4 * np.cos(5 * y + 4)) + +(5 * np.cos(6 * y + 5)))


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
plt.title("Schubert Function")
plt.savefig("Schubert Function.png")





