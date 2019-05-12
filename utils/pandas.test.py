import pandas as pd

df = pd.DataFrame([[0, 5, 3], [0, 4, 1], ['Datum', 20, 30],  [30, 40, 50]], columns=['A', 'B', 'C'])

i =df.iloc[:, 0] == 'Datum'
print(i)
head2 = df.loc[i,:]

print(head2.iat[0,0])
print(i.index)

#df[df['model'].str.match('Mac')]

#df.loc[df['LastName']=='Smith'].index
