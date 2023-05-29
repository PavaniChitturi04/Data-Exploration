import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 32, 28],
                   'City': ['New York', 'Chicago', 'Los Angeles']})

# Print original dataframe
print("Original DataFrame:")
print(df)

transposed_df = df.T

# Print transposed dataframe
print("\n","Transposed DataFrame using T attribute:")
print(transposed_df)
transposed_df2 = df.transpose()

# Print transposed dataframe
print("\n","Transposed DataFrame using transpose() method:")
print(transposed_df2)
