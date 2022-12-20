from matplotlib import pyplot as plt
import numpy as np
import random

plt.style.use('seaborn')


x = np.linspace(0,5,10)
print(x.itemsize)
y = x**2

color=[]

for i in range(2):

    rgb = (random.uniform(0,0.7),random.uniform(0,0.7),random.uniform(0,0.7))

    color.append(rgb)

plt.subplot(1,2,1)
plt.plot(x,y, color=color[0])
plt.subplot(1,2,2)

x1 = np.linspace(0, 5, 25)
y1 = np.cos(x1)**3
plt.plot(x1,y1, color=color[1])

plt.grid(True)
plt.tight_layout()
plt.show()
