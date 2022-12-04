import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 1)
y = np.arange(0, 11, 1)
print(x)
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_eer = x.std() * np.sqrt(1 / len(x) +
                          (x - x.mean()) ** 2 / np.sum((x - x.mean()) ** 2))
fig, axes = plt.subplots()
axes.plot(x, y_est, '-')
axes.fill_between(x, y_est - y_eer, y_est + y_eer, alpha=0.2)
axes.plot(x, y, 'o', color='red')
plt.show()
