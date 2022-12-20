from matplotlib import pyplot as plt

dev_x = []
dev_y = []

sum = 0
while sum <= 10000:
    sum += 1
    dev_x.append(sum)


j = 3
while j <= 10003:
    j += 1
    dev_y.append(j)


plt.xlabel('X Values')
plt.ylabel('y values')
plt.plot(dev_x, dev_y)
plt.grid(True)
plt.show()



