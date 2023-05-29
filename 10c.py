import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                   'Age': [25, 32, 28, 31],
                   'City': ['New York', 'Chicago', 'Los Angeles', 'Houston']})

# Print original dataframe
print("Original DataFrame:")
print(df)

# Sort dataframe by a single column
sorted_df = df.sort_values(by='Age')

# Print sorted dataframe
print("\n","Sorted DataFrame by 'Age':")
print(sorted_df)

# Sort dataframe by multiple columns
sorted_df2 = df.sort_values(by=['City', 'Age'], ascending=[True, False])

# Print sorted dataframe
print("\n","Sorted DataFrame by 'City' ascending and 'Age' descending:")
print(sorted_df2)
