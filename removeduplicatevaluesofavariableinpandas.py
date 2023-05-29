import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob'],
                   'Age': [25, 32, 28, 31, 25, 32],
                   'City': ['New York', 'Chicago', 'Los Angeles', 'Houston', 'New York', 'Chicago']})

# Print original dataframe
print("Original DataFrame:")
print(df)

# Remove duplicate values based on a single column
df_no_duplicates = df.drop_duplicates(subset='Name')

# Print dataframe with duplicate values removed
print("\n","DataFrame with duplicate values removed based on 'Name' column:")
print(df_no_duplicates)

# Remove duplicate values based on multiple columns
df_no_duplicates2 = df.drop_duplicates(subset=['Name', 'Age'])

# Print dataframe with duplicate values removed
print("\n","DataFrame with duplicate values removed based on 'Name' and 'Age' columns:")
print(df_no_duplicates2)
