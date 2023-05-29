import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3],
                   'B': ['foo', 'bar', 'baz'],
                   'C': [True, False, True]})

# Select the first row
print('\n',df.loc[0])

# Select the rows where column 'C' is True
print('\n',df.loc[df['C'] == True])

# Select the first row
print('\n',df.iloc[0])

# Select the first two rows and the first two columns
print('\n',df.iloc[:2, :2])

# Select column 'A'
print('\n',df['A'])

# Select the rows where column 'A' is greater than 1
print('\n',df[df['A'] > 1])

# Select the value in row 0 and column 'B'
print('\n',df.at[0, 'B'])

# Select the value in row 0 and column 1
print('\n',df.iat[0, 1])


# Select rows where column A is greater than 1
print('\n',df[df['A'] > 1])

# Select rows where column B is equal to 5 or 6
print('\n',df[(df['B'] == 5) | (df['B'] == 6)])
