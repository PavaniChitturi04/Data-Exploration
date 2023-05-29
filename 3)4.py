import pandas as pd

# Creating a sample dataset
data = {'name': ['John', 'Mike', 'John', 'Sarah', 'Mike'], 'age': [25, 30, 25, 28, 30]}
df = pd.DataFrame(data)
print(df)
# Counting duplicates
duplicates = df.duplicated()
print('\n',duplicates)
# Dropping duplicates
df = df.drop_duplicates()
print('\n',df)


#df = df.drop_duplicates(subset=['name', 'age'])
print('\n',df)
