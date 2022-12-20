from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.style.use('seaborn')
df = pd.read_csv('GBPUSD=X.csv')

print(df)

m = df.corr()['High']
print(m)

o = df.corr()['Low']
print(o)


cor_values = {
                'h':m,
                'l':o
    }

new = pd.DataFrame(cor_values)
print(new)

i = df['Date'][0:100]
j = df['High'][0:100]
k = df['Open'][0:100]

x = np.array(i)
print(x)
y = np.array(j)
print(y)

plt.xlabel('Dates')
plt.ylabel('High')


plt.title('Dates and all time highs')

plt.plot(x, y, label='plots1',  color='g', linewidth=0.9)

y1 = np.array(k)
print(y1)

plt.plot(x, y1, label='plots2', color='r', linewidth=0.9)

plt.xticks(rotation=90)


plt.legend()

plt.grid(True)

plt.tight_layout()

plt.show()


