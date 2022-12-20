import pandas as pd
import statistics

people = {

        'first':['Ade','Okon', 'Gbade'],
        'last':['John', 'Kosi', 'Effiong'],
         'Age':[30, 40, 50],
         'gender':['m', 'f', 'm'],
        'email':['john@gmail.ccom', 'Kosi@gmail.com', 'Effiong@rtt.com']
}


df = pd.DataFrame(people)
print(df)

print(df['email'])


print(df[['first', 'last', 'Age']])
print(df['Age'].sum(axis=0))
print(df.describe())
print(df.iloc[0:1])
print(df['gender'].value_counts())

filt = (df['first'] == 'Ade') & (df['Age']==55)
print(filt)

print(df.loc[filt])







