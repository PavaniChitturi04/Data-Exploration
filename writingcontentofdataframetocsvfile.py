import pandas as pd

# create a sample DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'city': ['New York', 'San Francisco', 'London']}
df = pd.DataFrame(data)

# write DataFrame to CSV file
df.to_csv('data.csv', index=False)
print(df)
