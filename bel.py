import pandas as pd

df1 = pd.read_csv('20232.csv',sep=';')

df2 = pd.read_csv('20231.csv',sep=';')

df3 = pd.read_csv('20222.csv',sep=';')

df4 = pd.read_csv('20221.csv',sep=';')

df5 = pd.read_csv('20212.csv',sep=';')

df6 = pd.read_csv('20211.csv',sep=';')

df6 = pd.concat([df6,df5], ignore_index=True)
df6 = pd.concat([df6,df4], ignore_index=True)
df6 = pd.concat([df6,df3], ignore_index=True)
df6 = pd.concat([df6,df2], ignore_index=True)
df6 = pd.concat([df6,df1], ignore_index=True)

df6.to_csv('belem.csv', sep=';',index=False)
