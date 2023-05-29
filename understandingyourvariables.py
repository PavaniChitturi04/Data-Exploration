import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['foo', 'bar', 'baz'],
                   'C': [True, False, True]})

# Print the summary
#df.info()
print(df.info())
# Print the statistics
#df.describe()
#print(df.describe())
# Print the value counts
df['B'].value_counts()
print(df['B'].value_counts())

# Create a sample DataFrame with numerical variables
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

# Print the correlation matrix
print(df.corr())
