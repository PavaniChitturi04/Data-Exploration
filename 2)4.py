import pandas as pd

# create a sample DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'London']}
df = pd.DataFrame(data)

# write DataFrame to Excel file
df.to_excel('data.xlsx', index=False)
print(df)
