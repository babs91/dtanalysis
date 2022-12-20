from matplotlib import pyplot as plt
print(plt.style.available)
# plt.style.use('fivethirtyeight')

plt.xkcd()

dev_x = [25,26,27,28,29, 30, 31, 32, 33, 34, 35]

dev_y = [10000,25500,35000,45000, 50000, 30000, 55000, 65000, 70000, 45000, 67000]

plt.plot(dev_x, dev_y, label='all devs', color='b', linewidth='2', marker='o')

dev_y1 = [15000,24000,35700,55000, 75000, 35000, 95000, 75000, 80000, 95000, 90000]

plt.plot(dev_x, dev_y1, label='py devs', color='r', linewidth='2', marker='.')

plt.title('TEST PLOT')

plt.xlabel('Ages')
plt.ylabel('salary')

plt.legend()

plt.grid(True)

plt.show()