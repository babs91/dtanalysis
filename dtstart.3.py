from matplotlib import pyplot as plt
import statistics as st

plt.style.use('seaborn')



dev_x = [24500, 45000, 55000, 45000, 25000, 25000, 75000, 65000, 45000,
         45000, 24500, 55000, 25000, 25000, 75000, 65000, 50000, 40000,
         35000, 35000, 35000,  24500, 25000, 65000, 40000, 25000, 60000]


plt.hist(dev_x, histtype="bar", bins = [20000, 30000, 40000, 50000, 60000, 70000, 80000], edgecolor="white", color="cyan"
)

print(st.median(dev_x))

plt.xlabel('Salaries')
plt.ylabel('frequencies')
plt.tight_layout()
plt.axvline(st.mode(dev_x))

plt.show()


