from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('GBPUSD=X.csv')

j = df[['Low', 'High', 'Close']]
print(j)

l = df['Open']

x = np.array(j)
print(x)

y = np.array(l)
print(y)

x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=0)


mle = LinearRegression()

mle.fit(x_train,y_train)

y_pred = mle.predict(x_test)

print('predicted value is',y_pred)
print('coefficients:',mle.coef_)

print('intercepts:', mle.intercept_)

dframe = {
           'actual':y_test,
           'predicted':y_pred,
           'difference':y_test - y_pred

           }

Mdata=pd.DataFrame(dframe)
print(Mdata)

