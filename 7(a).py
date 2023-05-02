import pandas as pd
data={'name':['John','Emma','Peter','Mary'],
      'age':[25,30,28,32],
      'gender':['M','F','M','F']}
df=pd.DataFrame(data)
sub_df=df.loc[0:1,['name','age']]
print(sub_df)
sub_df=df.iloc[0:2,0:2]
print('\n',sub_df)
