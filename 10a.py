import pandas as pd

# Create sample dataframes
df1 = pd.DataFrame({'ID': [1, 2, 3, 4],
                    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'Age': [25, 32, 28, 31]})

df2 = pd.DataFrame({'ID': [3, 4, 5, 6],
                    'City': ['New York', 'Chicago', 'Los Angeles', 'Houston'],
                    'Salary': [5000, 6000, 5500, 7000]})

print("Merge dataframes on 'ID' column using an inner join")
merged_df = pd.merge(df1, df2, on='ID', how='inner')

#Print merged dataframe
print(merged_df)

print("\n","Merge dataframes on 'ID' column using an outer join")
merged_df = pd.merge(df1, df2, on='ID', how='outer')

#Print merged dataframe
print(merged_df)
print("\n","Merge dataframes on 'ID' column using a left join")
merged_df = pd.merge(df1, df2, on='ID', how='left')

# Print merged dataframe
print(merged_df)

print("\n","Merge dataframes on 'ID' column using a right join")
merged_df = pd.merge(df1, df2, on='ID', how='right')

# Print merged dataframe
print(merged_df)

print("\n","Concatenate dataframes along rows with outer join")
concatenated_df = pd.concat([df1, df2], ignore_index=True, sort=False)

# Print concatenated dataframe
print(concatenated_df)
