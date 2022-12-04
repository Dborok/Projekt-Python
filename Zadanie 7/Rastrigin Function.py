import matplotlib.pyplot as plt
import numpy as np
import math


def f(x, y):
    return (pow(x, 2) - np.cos(18 * math.pi * x)) + (pow(y, 2) - np.cos(18 * math.pi * y))


x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z,cmap='magma')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Rastrigin Function")
plt.savefig("Rastrigin Function.png")
