#import pandas as pd

# create a sample DataFrame
#data = {'name': ['John', 'Emma', 'Peter', 'Mary'],
     #   'age': [25, 30, 28, 32],
     #   'gender': ['M', 'F', 'M', 'F']}
#df = pd.DataFrame(data)

# rename the 'name' column to 'full_name'
#df = df.rename(columns={'name': 'full_name'})

# display the new column names
#print(df.columns)
#print(df)


import pandas as pd

# create a sample DataFrame
data = {'name': ['John', 'Emma', 'Peter', 'Mary'],
        'age': [25, 30, 28, 32],
        'gender': ['M', 'F', 'M', 'F']}
df = pd.DataFrame(data)

# rename the 'name' and 'gender' columns
df = df.rename(columns={'name': 'full_name', 'gender': 'sex'})

# display the new column names
print(df.columns)
print(df)
