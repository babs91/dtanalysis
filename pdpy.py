import pandas as pd
import numpy as np

df = pd.read_csv('GBPUSD=X.csv')


print(df.loc[[0,2]])

df1 = pd.set_option('display.max_rows', 262)
print(df1)



df['Average Region'] = (df['High'] + df['Low'])/2

j = np.array(df['Average Region'])
print(j)

print(df['Average Region'])

df = df.drop(columns=['Average Region'])

dp = df['Date'][0:5]
print(dp)


print(df.info())

dp2 = df.sort_values(['High'], ascending=True)
print(dp2)

l = np.array(dp2)
print(l)


dp3 = (df['High'] > 1.3).value_counts()
print(dp3)

dp4 = df['High'] > 1.32
print(dp4)


dp5 = df.loc[dp4,['Date','Low', 'High']]
print(dp5)





