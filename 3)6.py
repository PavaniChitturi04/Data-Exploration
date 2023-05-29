import pandas as pd

# Creating a sample dataset
data = {'name': [' John', 'Mike ', ' John ', 'Sarah ', 'Mike '], 'age': [25, 30, 25, 28, 30]}
df = pd.DataFrame(data)
print(df)
# Removing whitespace from the 'name' column
df['name'] = df['name'].str.strip()
print('\n',df)

# Converting the 'name' column to lowercase
df['name'] = df['name'].str.lower()
print('\n',df)

# Replacing 'sarah' with 'sara'
df['name'] = df['name'].replace('sarah', 'sara')
print('\n',df)
