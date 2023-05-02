import pandas as pd
data={'name':['John','Emma','Peter','Mary'],
      'age':[25,30,28,32],
      'gender':['M','F','M','F']}
df=pd.DataFrame(data)
filtered_df=df[df['age']>=30]
print(filtered_df)
filter_df=df[(df['age']>30)&(df['gender']=='F')]
print('\n',filter_df)
