from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('seaborn')
df = pd.read_csv('GBPUSD=X.csv')

j = df['High'][0:100]
k = df['Open'][0:100]
x = np.array(j)
print(np.mean(x))
y = np.array(k)
print(np.mean(y))

# plt.xlabel('high')
# plt.ylabel('low')
#
#
# plt.scatter(x, y, label='plots1',  color='g', linewidth=0.9)
# plt.show()

num = 0
dnum = 0

for i in range(len(x)):

    num +=(x[i] - (np.mean(x)))*(y[i] - (np.mean(y)))

    dnum += (x[i] -(np.mean(x)))**2

ceR = num/dnum

print('coefficient reg is:{:.4f}'.format(ceR))

"The regression equation"

# y = ceR*x + c

cINT = np.mean(y) - (ceR*np.mean(x))
print('cINT:{:.4f}'.format(cINT))

y_pred = ceR*x + cINT

print(y_pred)


"R-square prediction"

r_num = 0
r_dnum = 0

for j in range(len(y)):

    r_num +=(y[j] - y_pred[j])**2

    r_dnum +=(y[j] - (np.mean(y)))**2

r_square = 1 - (r_num/r_dnum)
print('R-Squared:{:.4f}'.format(r_square))