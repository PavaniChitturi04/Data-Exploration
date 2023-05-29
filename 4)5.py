#import pandas as pd
#df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   #'B': [6, 7, 8, 9, 10],
                   #'C': [11, 12, 13, 14, 15]})

#mask = (df['A'] > 0) & (df['B'] < 10)
#df.loc[mask, ['A', 'B']]
#df.query('A > 0 and B < 10')
#df.loc[df['A'] > 0 & (df['B'] < 10), ['A', 'B']]


import pandas as pd

# create a sample dataframe
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 40, 45],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'City': ['New York', 'Boston', 'San Francisco', 'Chicago', 'Miami']
})

# select all rows where Age is greater than 30
print('\n',df[df['Age'] > 30])

# select all rows where Gender is 'Male'
print('\n',df.loc[df['Gender'] == 'Male'])

# select all rows where Age is greater than 30 and City is 'Boston'
print('\n',df.query('Age > 30 and City == "Boston"'))

# select all rows where City is either 'New York' or 'Boston'
print('\n',df[df['City'].isin(['New York', 'Boston'])])
