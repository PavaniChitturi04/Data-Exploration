import pandas as pd

# create a sample DataFrame
data = {'name': ['John', 'Emma', 'Peter', 'Mary'],
        'age': [25, 30, 28, 32],
        'gender': ['M', 'F', 'M', 'F']}
df = pd.DataFrame(data)
print(df.columns)
# rename the 'name' column to 'full_name' in place
df.rename(columns={'name': 'full_name'}, inplace=True)

# display the new column names
print(df.columns)
