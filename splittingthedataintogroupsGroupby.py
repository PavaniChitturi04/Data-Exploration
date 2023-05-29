import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [1, 2, 3, 4, 5, 6]
})

# Group the DataFrame by 'Category'
grouped = df.groupby('Category')

# Calculate the sum of each group
sums = grouped.sum()

print(sums)
