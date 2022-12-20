from matplotlib import pyplot as plt
import random

plt.style.use('bmh')


dev_y = []
dev_x = [0,4,3,5,6,7,8,9,10, 11,12]


for x in range(0,11):
 print(x)
 j= random.randint(0,1000)
 dev_y.append(j)


plt.grid(True)

plt.plot(dev_x,dev_y, color='red', marker='o')
plt.tight_layout()
plt.show()

