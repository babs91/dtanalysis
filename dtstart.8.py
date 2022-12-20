from matplotlib import pyplot as plt
import numpy as np
import random
plt.style.use('seaborn')

a_1 = np.random.randint(1,7,7000)
a_2 = np.random.randint(1,7,7000)

a_3 = a_1 + a_2


plt.hist(a_3, bins=12, rwidth=5, label='dice proba', stacked=True, density=True, edgecolor='y')

plt.legend()

plt.show()

