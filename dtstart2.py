from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

age_x = [25,26,27,28,29, 30, 31, 32, 33, 34, 35]
dev_y = [10000,25500,35000,45000, 50000, 30000, 55000, 65000, 70000, 45000, 67000]


plt.bar(age_x,dev_y, linewidth='5', color='blue', label='All devs')




dev_y2 = [20000, 35500,45000,49000, 55000, 35000, 59000, 69000, 79000, 75000, 77000]
plt.bar(age_x,dev_y2, linewidth='5', color='y', label='js devs', bottom=dev_y)

plt.xlabel('Developer ages')
plt.ylabel('Developer salary in GBP')

plt.grid(True)

plt.tight_layout()

plt.legend()

plt.show()



