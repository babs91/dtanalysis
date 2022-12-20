from matplotlib import pyplot as plt
import numpy as np

plt.style.use('seaborn')

import random


spc = np.arange(5)

m_eng = [70, 60, 80, 90, 50]

plt.bar(spc, m_eng, label='Male population', width=0.45)

f_eng = [30, 40, 20, 10, 50]

plt.bar(spc + 0.45, f_eng, label='Male population', width=0.45, color='g')

plt.xticks(spc + 0.45/2,('Mechanical', 'Electrical', 'Chemical', 'Civil', 'Aeronautic'))

plt.legend()

plt.xlabel('Gender Types')
plt.ylabel('% domination')
plt.grid(True)
plt.tight_layout()
plt.show()
